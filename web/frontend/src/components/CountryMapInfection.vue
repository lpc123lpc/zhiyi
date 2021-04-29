<template>
  <div id="countryMapInfection"></div>
</template>

<script>
  import echarts from 'echarts'
  import 'echarts/theme/sakura'
  import { mixin } from '../mixins'

  export default {
    name: 'CountryMapInfection',
    props: [
      'country',
      'countryMapInfectionData'
    ],
    mixins: [mixin],
    data() {
        return {
            countryFileName: '',
            countryEgName: ''
        }
    },
    mounted() {
      [this.countryFileName, this.countryEgName] = this.getCountryName()
      this.drawCountryMapInfection()
    }, 
    methods: {
       drawCountryMapInfection() {
            if (this.countryFileName === '') {
                console.log("Name error!")
                return
            }
                // console.log(this.countryMapInfectionData)
            var json = require('../../static/json/map/world/geojson/' + this.countryFileName + '.json')
            if (json === null) {
                console.log('Load json error!')
                return
            }
            // console.log(json)
            echarts.registerMap(this.countryEgName, json)
            var countryMapInfection = echarts.init(document.getElementById('countryMapInfection'), 'sakura');
            var countryMapInfection_Option = {
                title: {
                    text: '新冠疫苗感染' + this.country + '分布图',
                    left: 'center',
                    textStyle: {
                        color: '#000',
                        fontSize: 22
                    }
                },
                tooltip: {
                    formatter: function (params) {
                        if (!isNaN(params.value)) {
                            return params.seriesName + '：' + params.value + '万'
                        }
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
                    data: ['当前确诊', '累计确诊', "累计治愈", "累计死亡"],
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
                    showLabel: false,
                    left: '5%',
                    bottom: '1%',
                    calculable: true,   
                    realtime: true,
                    textStyle: {
                        fontSize: 12,
                    },
                    min: 0,
                    max: 5000,
                    maxOpen: true, 
                    textGap: 20,
                    realtime: true,
                    calculable: true,
                    inRange: {
                        color: ['#FDEBCF', '#F59E83', '#E55A4E', '#CB2A2F', '#70161D', '#30161D']
                    },
                    outOfRange: { color: 'darkRed' }
                },
                series: [{
                    name: '当前确诊',
                    type: 'map',
                    roam: true,
                    mapType: this.countryEgName,
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
                    data: this.countryMapInfectionData.nowConfirm
                },{
                    name: '累计确诊',
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
                    data: this.countryMapInfectionData.totalConfirm
                },{
                    name: '累计治愈',
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
                    data: this.countryMapInfectionData.cured
                },{
                    name: '累计死亡',
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
                    data: this.countryMapInfectionData.dead
                }]
            }
            countryMapInfection.setOption(countryMapInfection_Option)
        },
    }
}
</script>

<style>
    #countryMapInfection {
        position: relative;
        width: 70%;
        height: 600px;
    }
</style>
