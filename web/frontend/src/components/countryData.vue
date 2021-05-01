<template>
  <div ref="countryDataCharts" style="width: 100%;height:600px"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'countryData',
  mounted () {
    this.chart = echarts.init(this.$refs.countryDataCharts)
    this.drawCountryData()
  },
  methods: {
    drawCountryData () {
      var that = this
      fetch('../static/json/charts/testData').then(function (response) {
        response.json().then(function (data) {
          that.chart.setOption({
            title: {
              text: data.name + '总体数据'
            },
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              data: ['接种人数', '确诊人数', '治愈人数', '死亡人数']
            },
            xAxis: [{
              name: '日期',
              type: 'category',
              data: data.time
            }],
            yAxis: [{
              type: 'value'
            }],
            dataZoom: {
              type: 'inside'
            },
            series: [{
              name: '接种人数',
              type: 'line',
              data: data.vaccined
            },
            {
              name: '确诊人数',
              type: 'line',
              data: data.confirmed
            },
            {
              name: '治愈人数',
              type: 'line',
              data: data.cured
            },
            {
              name: '死亡人数',
              type: 'line',
              data: data.deceased
            }]
          }, true)
        })
      }).catch(function (err) {
        alert(err.toString())
      })
    }
  }
}

</script>

<style scoped>

</style>
