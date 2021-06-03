<template>
  <div id="map"></div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/theme/sakura'
import {mixin} from '../../mixins'

export default {
  name: 'CountryMapVaccine',
  props: [
    'country',
    'countryMapVaccineData'
  ],
  mixins: [mixin],
  data() {
    return {
      countryFileName: '',
      countryEgName: ''
    }
  },
  watch: {
    country() {
      [this.countryFileName, this.countryEgName] = this.getCountryName(this.country)
      this.drawCountryMapVaccine()
    },
    countryMapVaccineData9() {
      this.drawCountryMapVaccine()
    }
  },
  mounted() {
    //   console.log(this.country)
    //   console.log(this.countryMapVaccineData)
    [this.countryFileName, this.countryEgName] = this.getCountryName(this.country)
    this.drawCountryMapVaccine()
  },
  methods: {
    drawCountryMapVaccine() {
      // console.log(this.countryEgName)
      if (this.countryFileName === '') {
        console.log("Name error!")
        return
      }
      var json = require('../../../static/json/map/world/geojson/' + this.countryFileName + '.json')
      if (json === null) {
        console.log('Load json error!')
        return
      }
      // console.log(json)
      echarts.registerMap(this.countryEgName, json)
      var countryMapVaccine = echarts.init(document.getElementById('map'), 'sakura');
      var countryMapVaccine_Option = {
        title: {
          text: '新冠疫苗接种' + this.country + '分布图',
          left: 'center',
          textStyle: {
            color: '#000',
            fontSize: 22
          }
        },
        tooltip: {
          formatter: function (params) {
            var value = parseFloat(params.value)
            if (!isNaN(params.value) && value >= 0) {
              if (params.seriesName === '覆盖率') {
                value = value + '/百人'
              }
              return params.seriesName + '：' + value
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
        color: ['#0099FF', '#7ae997'],
        legend: {
          data: ['已接种', '每百人接种剂量'],
          left: '2%',
          orient: 'horizontal',
          top: '2%',
          selected: {'已接种': true, '每百人接种剂量': false},
          selectedMode: 'single',
          textStyle: {
            color: '#000',
            fontSize: 14
          }
        },
        visualMap: [{
          seriesIndex: 0,
          show: true,
          showLabel: false,
          left: '5%',
          bottom: '1%',
          textStyle: {
            fontSize: 12,
          },
          min: 0,
          max: 5000,
          maxOpen: true,
          // text: ['接种人数/万'],
          textGap: 20,
          realtime: true,
          calculable: true,
          // precision: 2,
          inRange: {
            color: ['rgba(181,255,253,0.56)', '#a1d5ff', '#72a0ff',
              '#8885ff', '#7358ff']
          },
          outOfRange: {color: 'darkblue'}
        }, {
          seriesIndex: 1,
          show: false,
          left: '5%',
          bottom: '1%',
          // text: ['覆盖率'],
          textGap: 20,
          textStyle: {
            // fontStyle: 'italic',
            fontSize: 12,
          },
          min: 0,
          max: 100,
          realtime: true,
          calculable: true,
          inRange: {
            color: ['rgba(181,255,253,0.56)', '#a1d5ff', '#72a0ff',
              '#8885ff', '#7358ff']
          },
          outOfRange: {color: ['#EEEEEE']}
        }],
        series: [{
          name: '已接种',
          type: 'map',
          mapType: this.countryEgName,
          roam: true,
          zoom: 1.2,
          top: '15%',
          left: 'center',
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14,
            }
          },
          data: this.countryMapVaccineData.vaccined
        }, {
          name: '每百人接种剂量',
          type: 'map',
          mapType: this.countryEgName,
          zoom: 1.2,
          roam: true,
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14,
            }
          },
          data: this.countryMapVaccineData.coverage
        }]
      }
      // countryMapVaccine_Option.visualMap[0].show = countryMapVaccine_Option.legend.selected.已接种? true: false
      // countryMapVaccine_Option.visualMap[1].show = countryMapVaccine_Option.legend.selected.已接种? false: true
      countryMapVaccine.setOption(countryMapVaccine_Option)
      countryMapVaccine.on('legendselectchanged', function (params) {
        countryMapVaccine_Option.legend.selected = params.selected
        var keys = Object.keys(params.selected)
        for (let i = 0; i < keys.length; i++) {
          if (params.selected[keys[i]]) countryMapVaccine_Option.visualMap[i].show = true
          else countryMapVaccine_Option.visualMap[i].show = false
        }
        // console.log(countryMapVaccine_Option.visualMap)
        this.setOption(countryMapVaccine_Option)
      })
    },
  }
}
</script>

<style>
#map {
  position: relative;
  width: 100%;
  height: 600px;
  margin-top: 30px;
}
</style>
