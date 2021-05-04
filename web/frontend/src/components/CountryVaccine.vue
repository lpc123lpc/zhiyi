<template>
    <div id="countryVaccine" style="width: 100%;height:600px;"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'CountryVaccine',
  mounted () {
    this.CountryVaccine()
  },
  methods: {
    CountryVaccine () {
      var myChart = echarts.init(document.getElementById('countryVaccine'))
      var series = []
      var names = []
      fetch('../static/json/charts/testVaccine').then(function (response) {
        response.json().then(function (data) {
          for (var i = 0; i < data.length; i++) {
            series.push(
              {
                name: data[i].name,
                type: 'line',
                data: data[i].vaccined
              }
            )
            names.push(data[i].name)
          }
          myChart.setOption({
            title: {
              text: data[0].name + '接种数据',
              textStyle: {
                color: '#333'
              }
            },
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              data: names
            },
            xAxis: [{
              name: '日期',
              type: 'category',
              data: data[0].time
            }],
            yAxis: [
              {
                name: '接种人数',
                type: 'value'
              }
            ],
            dataZoom: {
              type: 'inside'
            },
            series: series
          })
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
