<template>
  <div id="worldMapInfection"></div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/theme/sakura'
import {mixin} from '../../mixins'

export default {
  name: 'WorldMapInfection',
  props: [
    'worldMapInfectionData'
  ],
  mixins: [mixin],
  watch: {
    worldMapInfectionData () {
      this.drawWorldMapInfection()
    }
  },
  mounted () {
    this.setEchartHeight()
    this.drawWorldMapInfection()
  },
  methods: {
    setEchartHeight () {
      const echartItem = document.getElementById('worldMapInfection')
      echartItem.style.setProperty('height', window.screen.width + 'px')
    },
    drawWorldMapInfection () {
      // console.log(this.worldMapInfectionData)
      var json = require('../../../static/json/map/world/geojson/world.json')
      echarts.registerMap('world', json)
      var worldMapInfection = echarts.init(document.getElementById('worldMapInfection'), 'sakura')
      var worldMapInfection_Option = {
        title: {
          text: '新冠疫情感染情况全球分布图',
          left: 'center',
          top: 0,
          textStyle: {
            color: '#000',
            fontSize: 18
          }
        },
        tooltip: {
          formatter: function (params) {
            var value = parseInt(params.value)
            if (!isNaN(params.value)) {
              if (value < 0) return
              else {
                if (params.seriesName === '感染率') {
                  value = parseFloat(params.value) * 100 + '%'
                } else {
                  value = params.value + '万'
                }
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
        legend: {
          data: ['当前确诊', '累计确诊', '累计治愈', '累计死亡', '感染率'],
          left: '2%',
          orient: 'horizontal',
          top: 40,
          selected: {'当前确诊': true, '累计确诊': false, '累计治愈': false, '累计死亡': false, '感染率': false},
          selectedMode: 'single',
          itemWidth: 12,
          itemHeight: 8,
          textStyle: {
            color: '#000',
            fontSize: 10
          }
        },
        visualMap: {
          show: true,
          showLabel: false,
          left: '3%',
          top: 150,
          itemHeight: 60,
          itemWidth: 10,
          textStyle: {
            fontSize: 8
          },
          min: 0,
          max: 100,
          maxOpen: true,
          textGap: 20,
          precision: 0,
          realtime: true,
          calculable: true,
          color: this.getMapColor(0),
          outOfRange: {color: ['#EEEEEE']}
        },
        series: [{
          name: '当前确诊',
          type: 'map',
          roam: true,
          mapType: 'world',
          zoom: 1.2,
          top: 100,
          left: 'center',
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14
            }
          },
          nameMap: this.getWorldNameMap(),
          data: this.worldMapInfectionData.nowConfirm
        }, {
          name: '累计确诊',
          type: 'map',
          mapType: 'world',
          zoom: 1.2,
          roam: true,
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14
            }
          },
          data: this.worldMapInfectionData.totalConfirm
        }, {
          name: '累计治愈',
          type: 'map',
          mapType: 'world',
          zoom: 1.2,
          roam: true,
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14
            }
          },
          data: this.worldMapInfectionData.cured
        }, {
          name: '累计死亡',
          type: 'map',
          mapType: 'world',
          zoom: 1.2,
          roam: true,
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14
            }
          },
          data: this.worldMapInfectionData.dead
        }, {
          name: '感染率',
          type: 'map',
          mapType: 'world',
          zoom: 1.2,
          roam: true,
          showLegendSymbol: false,
          label: {
            emphasis: {
              show: true,
              fontSize: 14
            }
          },
          data: this.worldMapInfectionData.coverage
        }]
      }
      worldMapInfection.setOption(worldMapInfection_Option)
      const that = this
      worldMapInfection.on('click', function (param) {
        // console.log(param.name)
        if (param.name !== '') that.$router.push({path: `/InfectDetail/${param.name}`})
      })
      worldMapInfection.on('legendselectchanged', function (params) {
        worldMapInfection_Option.legend.selected = params.selected
        var keys = Object.keys(params.selected)
        var max = [100, 2000, 1000, 50, 1]
        for (let i = 0; i < keys.length; i++) {
          if (params.selected[keys[i]]) { // show different color range in different legend
            worldMapInfection_Option.visualMap.color = that.getMapColor(i)
            worldMapInfection_Option.visualMap.max = max[i]
            worldMapInfection_Option.visualMap.precision = i === 4 ? 3 : 0
            break
          }
        }
        this.setOption(worldMapInfection_Option)
      })
    }
  }
}
</script>

<style>
#worldMapInfection {
  position: relative;
  width: 100%;
  height: 100%;
  border-style: solid;
  border-color: #ffffff #ffffff #e6e6e6 #ffffff;
  border-bottom-width: 1px;
}
</style>
