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
    watch: {
        country() {
            [this.countryFileName, this.countryEgName] = this.getCountryName(this.country)
            this.drawCountryMapInfection()
        },
        countryMapInfectionData() {
            this.drawCountryMapInfection()
        }
    },
    mounted() {
        [this.countryFileName, this.countryEgName] = this.getCountryName(this.country)
        this.drawCountryMapInfection()
    },
    methods: {
       drawCountryMapInfection() {
            // console.log(this.countryFileName)
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
            var countryMapInfection = echarts.init(document.getElementById('countryMapInfection'), 'sakura')
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
                    left: '5%',
                    bottom: '1%',
                    textStyle: {
                        fontSize: 12,
                    },
                    splitList: [{start: 0, end: 100},
                                {start: 100, end: 499},
                                {start: 500, end: 1999},
                                {start: 2000, end: 9999},
                                {start: 10000, end: 99999},
                                {start: 100000}],
                    color: ['#70161D', '#CB2A2F', '#E55A4E', '#F59E83', '#FDEBCF', '#DCE2EB'],

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
            if (this.country == '中国') {
                const that = this
                countryMapInfection.on('click', function (param) {
                    // console.log(param.name)
                    that.$router.push({path: `/InfectProvinceDetail/${param.name}`})
                })
            }
        },
    }
}
</script>

<style>
    #countryMapInfection {
        position: relative;
        /* margin-left: 5%; */
        height: 600px;
    }
</style>
