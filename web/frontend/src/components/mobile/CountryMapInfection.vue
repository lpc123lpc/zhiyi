<template>
  <div id="countryMapInfection"></div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/theme/sakura'
import {mixin} from '../../mixins'

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
      var json = require('../../../static/json/map/world/geojson/' + this.countryFileName + '.json')
      if (json === null) {
        console.log('Load json error!')
        return
      }
      // console.log(json)
      echarts.registerMap(this.countryEgName, json)
      var countryMapInfection = echarts.init(document.getElementById('countryMapInfection'), 'sakura')
      var countryMapInfection_Option = {
        title: {
          text: '新冠疫情感染情况' + this.country + '分布图',
          left: 'center',
          textStyle: {
            color: '#000',
            fontSize: 18
          }
        },
        tooltip: {
          formatter: function (params) {
            if (!isNaN(params.value) && parseInt(params.value) >=0 ) {
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
          data: ['当前确诊', '累计确诊', "累计治愈", "累计死亡"],
          left: '2%',
          orient: 'horizontal',
          top: '7%',
          selected: {'当前确诊': true, '累计确诊': false, '累计治愈': false, '累计死亡': false},
          selectedMode: 'single',
          itemWidth: 14,
          itemHeight: 10,
          textStyle: {
            color: '#000',
            fontSize: 12
          },
        },
        visualMap: {
          show: true,
          left: '3%',
          top: 350,
          orient: 'horizontal',
          itemHeight: 10,
          itemWidth: 10,
          textStyle: {
            fontSize: 8,
          },
          splitList: [{start: 0, end: 999},
            {start: 1000, end: 9999},
            {start: 10000, end: 19999},
            {start: 20000, end: 49999},
            {start: 50000, end: 99999},
            {start: 100000, end: 199999},
            {start: 200000}],
          color: this.getMapColor(),
          outOfRange: {color: '#EEEEEE'}
        },
        series: [
          {
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
          },
          {
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
          },
          {
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
          },
          {
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
      var list0 = [{start: 0, end: 0, color: '#EEEEEE'},
        {start: 1, end: 5, color: '#FDEBCF'},
        {start: 6, end: 10, color: '#f5af96'},
        {start: 11, end: 20},
        {start: 21, end: 40},
        {start: 41, end: 60},
        {start: 61}]
      var list1 = [{start: 0, end: 99},
        {start: 100, end: 499},
        {start: 500, end: 999},
        {start: 1000, end: 9999},
        {start: 10000, end: 49999},
        {start: 50000, end: 99999},
        {start: 100000}]
      var list2 = [{start: 0, end: 99},
        {start: 100, end: 999},
        {start: 1000, end: 9999},
        {start: 10000, end: 99999},
        {start: 100000, end: 999999},
        {start: 1000000, end: 9999999},
        {start: 10000000}]
      var list3 = [{start: 0, end: 99},
        {start: 100, end: 999},
        {start: 1000, end: 9999},
        {start: 10000, end: 99999},
        {start: 100000, end: 499999},
        {start: 500000, end: 999999},
        {start: 1000000}]
      var list4 = [{start: 0, end: 99},
        {start: 100, end: 999},
        {start: 1000, end: 4999},
        {start: 5000, end: 9999},
        {start: 10000, end: 19999},
        {start: 20000, end: 49999},
        {start: 50000}]
      if (this.country === '中国') {
        // set the initial color mode
        countryMapInfection_Option.visualMap.splitList = list0
        // countryMapInfection_Option.visualMap.color[6] = '#EEEEEE'
        // set jump to province
        countryMapInfection.setOption(countryMapInfection_Option)
        const that = this
        countryMapInfection.on('click', function (param) {
          // console.log(param.name)
          if (param.name !== '') that.$router.push({path: `/InfectProvinceDetail/${param.name}`})
        })
      } else {
        countryMapInfection.setOption(countryMapInfection_Option)
      }
      var that = this
      countryMapInfection.on('legendselectchanged', function (params) {
        countryMapInfection_Option.legend.selected = params.selected
        var keys = Object.keys(params.selected)
        var chinaSplitList = [list0, list1, list1, list0]
        var splitList = [list2, list3, list3, list4]
        for (let i = 0; i < keys.length; i++) {
          if (params.selected[keys[i]]) { // show different color range in different legend
            if (that.country === '中国') {
              countryMapInfection_Option.visualMap.splitList = chinaSplitList[i]
            } else {
              countryMapInfection_Option.visualMap.splitList = splitList[i]
            }
            countryMapInfection_Option.visualMap.color = that.getMapColor(i)
          }
        }
        this.setOption(countryMapInfection_Option)
      })
    },
  }
}
</script>

<style>
#countryMapInfection {
  position: relative;
  height: 600px;
}
</style>
