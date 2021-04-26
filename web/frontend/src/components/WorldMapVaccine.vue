<template>
  <div id="worldMapVaccine"></div>
</template>

<script>
  import echarts from 'echarts'
  import 'echarts/theme/sakura'

  export default {
    name: 'WorldMapVaccine',
    props: [
      'worldMapVaccineData'
    ],
    mounted() {
      this.drawWorldMapVaccine()
    }, 
    methods: {
       drawWorldMapVaccine() {
        // console.log(this.worldMapVaccineData)
        var json = require('../../static/json/map/world/geojson/world.json')
        echarts.registerMap('world', json)
        var worldMapVaccine = echarts.init(document.getElementById('worldMapVaccine'), 'sakura');
        var worldMapVaccine_Option = {
          title: {
              text: '新冠疫苗接种全球分布图',
              left: 'center',
              textStyle: {
                  color: '#000',
                  fontSize: 22
              }
          },
          tooltip: {
              formatter: function (params) {
                var value = parseFloat(params.value)
                if (params.seriesName === '覆盖率') {
                  value =  value * 100 + '%'
                } else {
                    value = value + '万'
                }
                return params.seriesName + '：' + value
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
            data: ['已接种', '覆盖率'],
            left: '2%',
            orient: 'horizontal',
            top: '2%',
            selected: {'已接种': true, '覆盖率': false},
            selectedMode: 'single',
            textStyle: {
                color: '#000',
                fontSize: 14
            }
          },
          visualMap: [{
            seriesIndex: 0,
            // show: true,
            left: '1%',
            bottom: '10%',
            calculable: true,   
            realtime: true,
            textStyle: {
                fontSize: 12,
            },
            min: 0,
            max: 150000,
            maxOpen: true, 
            text: ['接种人数/万'],
            realtime: false,
            calculable: true,
            inRange: {
                color: ['#99CCFF', '#66CCFF', '#0099FF', '#0066CC', '#0033FF']
            }
          },{
            seriesIndex: 1,
            show: true,
            left: '10%',
            bottom: '10%',
            calculable: true,   
            calculable: true,   
            realtime: true,
            precision: 3,
            text: ['覆盖率'],
            textStyle: {
              // fontStyle: 'italic',
              fontSize: 12,
            },
            min: 0,
            max: 1,
            realtime: true,
            calculable: true,
            inRange: {
                color: ['#d6f6cf', '#acff9a', '#a6f6a3', '#7ae997', '#44d544', '#298518']
            }
          }],
          series: [{
            name: '已接种',
            type: 'map',
            roam: true,
            mapType: 'world',
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
            nameMap: this.getNameMap(),
            data: this.worldMapVaccineData.vaccined
          },{
            name: '覆盖率',
            type: 'map',
            mapType: 'world',
            zoom: 1.2,
            roam: true,
            showLegendSymbol: false,
            label: {
              emphasis: {
                  show: true,
                  fontSize: 14,
              }
            },
            data: this.worldMapVaccineData.coverage
          }]
        }
        worldMapVaccine.setOption(worldMapVaccine_Option)
        // console.log(worldMapVaccine_Option)
      },
      getNameMap() {
        var json = require('../../static/json/map/world/world-mapping.json')
        var nameMap = {}
        for (let i in json) {
          // console.log(i)
          nameMap[i] = json[i].cn
        }
        // console.log(nameMap)
        return nameMap
      }
    }
  }
</script>

<style>
  #worldMapVaccine {
    position: relative;
    width: 100%;
    height: 600px;
    margin-top: 30px;
  }
</style>
