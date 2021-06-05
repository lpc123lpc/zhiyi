<template>
  <div id="provinceMapInfection"></div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/theme/sakura'
import {mixin} from '../../mixins'

export default {
  name: 'ProvinceMapInfection',
  props: [
    'province',
    'provinceMapInfectionData'
  ],
  mixins: [mixin],
  watch: {
    province () {
      // console.log(this.province)
      this.drawProvinceMapInfection()
    },
    provinceMapInfectionData () {
      this.drawProvinceMapInfection()
    }
  },
  mounted () {
    this.drawProvinceMapInfection()
  },
  methods: {
    drawProvinceMapInfection () {
      var provinceFileName = this.getChinaProvinceFileName(this.province)
      // console.log(provinceFileName)
      var json = require('../../../static/json/map/china-province/geojson/' + provinceFileName + '.json')
      if (json === null) {
        console.log('Load json error!')
        return
      }
      // console.log(json)
      echarts.registerMap(this.province, json)
      var provinceMapInfection = echarts.init(document.getElementById('provinceMapInfection'), 'sakura')
      var provinceMapInfection_Option = {
        title: {
          text: '新冠疫苗感染中国' + this.province + '分布图',
          left: 'center',
          textStyle: {
            color: '#000',
            fontSize: 22
          }
        },
        tooltip: {
          formatter: function (params) {
            if (!isNaN(params.value) && parseInt(params.value) >= 0) {
              return params.seriesName + '：' + params.value
            }
          }
        },
        grid: {
          left: '6%',
          right: '6%',
          bottom: '8%',
          top: '10%',
          containLabel: true
        },
        legend: {
          data: ['当前确诊', '累计确诊', '累计治愈', '累计死亡'],
          left: '2%',
          orient: 'vertical',
          top: '10%',
          selected: {'当前确诊': true, '累计确诊': false, '累计治愈': false, '累计死亡': false},
          selectedMode: 'single',
          textStyle: {
            color: '#000',
            fontSize: 18
          }
        },
        visualMap: {
          show: true,
          left: '5%',
          bottom: '1%',
          textStyle: {
            fontSize: 12
          },
          splitList: [{start: 0, end: 0},
            {start: 1, end: 9},
            {start: 10, end: 99},
            {start: 100, end: 999},
            {start: 1000, end: 1999},
            {start: 2000}],
          color: this.getMapColor(0),
          outOfRange: {color: ['#EEEEEE']}
        },
        series: [{
          name: '当前确诊',
          type: 'map',
          roam: true,
          mapType: this.province,
          zoom: 1.2,
          top: '15%',
          left: 'center',
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14
            }
          },
          nameMap: this.getProvinceNameMap(this.province),
          data: this.provinceMapInfectionData.nowConfirm
        }, {
          name: '累计确诊',
          type: 'map',
          mapType: this.province,
          zoom: 1.2,
          roam: true,
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14
            }
          },
          data: this.provinceMapInfectionData.totalConfirm
        }, {
          name: '累计治愈',
          type: 'map',
          mapType: this.province,
          zoom: 1.2,
          roam: true,
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14
            }
          },
          data: this.provinceMapInfectionData.cured
        }, {
          name: '累计死亡',
          type: 'map',
          mapType: this.province,
          zoom: 1.2,
          roam: true,
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14
            }
          },
          data: this.provinceMapInfectionData.dead
        }]
      }
      provinceMapInfection.setOption(provinceMapInfection_Option)
      var that = this
      provinceMapInfection_Option.on('legendselectchanged', function (params) {
        provinceMapInfection_Option.legend.selected = params.selected
        var keys = Object.keys(params.selected)
        for (let i = 0; i < keys.length; i++) {
          if (params.selected[keys[i]]) { // show different color in cured
            provinceMapInfection_Option.visualMap.color = that.getMapColor(i)
          }
        }
        this.setOption(provinceMapInfection_Option)
      })
    }
  }
}
</script>

<style>
#provinceMapInfection {
  position: relative;
  /* margin-left: 5%; */
  height: 600px;
}
</style>
