<template>
  <div id="worldMapVaccine"></div>
</template>

<script>
  import echarts from 'echarts'

  export default {
    name: 'WorldMapVaccine',
    props: [
      'worldMapVaccineData'
    ],
    mounted() {
      this.worldMapVaccineData = {'vaccined': [{'name': "中国", 'value': 1000}], 'coverage': [{'name': "China", 'value': 0.1}]}
      this.drawWorldMapVaccine()
    }, 
    methods: {
       drawWorldMapVaccine() {
        //  console.log(this.worldMapVaccineData.vaccined)
        //  console.log(this.worldMapVaccineData.coverage)
        var json = require('../static/json/map/world/geojson/world.json')
        echarts.registerMap('world', json)
        var worldMapVaccine = echarts.init(document.getElementById('worldMapVaccine'));
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
                return params.seriesName + '：' + params.value
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
            data: ['已接种', '覆盖率'],
            left: '2%',
            orient: 'horizontal',
            top: '2%',
            selected: {'已接种': true, '覆盖率': false},
            selectedMode: 'single',
            textStyle: {
                color: '#000',
                fontSize: 18
            }
          },
          visualMap: {
            show: true,
            left: '2%',
            bottom: '20%',
            textStyle: {
                fontSize: 18,
            },
            splitList: [{start: 0, end: 0},
                {start: 1, end: 99},
                {start: 100, end: 999},
                {start: 1000, end: 9999},
                {start: 10000, end: 99999},
                {start: 100000, end: 999999},
                {start: 1000000}],
            color: ['#30161D', '#70161D', '#CB2A2F', '#E55A4E',
                      '#F59E83', '#FDEBCF', '#DCE2EB']
          },
          series: [{
            name: '已接种',
            type: 'map',
            roam: true,
            mapType: 'world',
            zoom: 1.2,
            top: '15%',
            left: 'center',
            label: {
              normal: {
                  show: false,
                  fontSize: 5,
              },
              emphasis: {
                  show: true,
                  fontSize: 14,
              }
            },
            nameMap: this.getNameMap(),
            data: []
          },{
            name: '覆盖率',
            type: 'map',
            mapType: 'world',
            zoom: 1.2,
            roam: false,
            label: {
              normal: {
                  show: false,
                  fontSize: 14,
              },
              emphasis: {
                  show: false,
                  fontSize: 14,
              }
            },
            data: []
          }]
        }
        worldMapVaccine_Option.series[0].data = this.worldMapVaccineData.vaccined
        worldMapVaccine_Option.series[1].data = this.worldMapVaccineData.coverage
        worldMapVaccine.setOption(worldMapVaccine_Option)
        console.log(worldMapVaccine_Option)
      },
      getNameMap() {
        var json = require('../static/json/map/world/world-mapping.json')
        var nameMap = {}
        for (let i in json) {
          console.log(i)
          nameMap[i] = json[i].cn
        }
        console.log(nameMap)
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
