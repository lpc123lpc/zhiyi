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
              text: data[0].name + '接种人数折线图',
              left: 'center',
              textStyle: {
                fontSize: '22',
                color: '#000',
                fontWeight: 'normal'
              }
            },
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              left: '10%',
              top: '5%',
              data: names,
              textStyle: {
                color: '#000',
                fontSize: 18
              }
            },
            grid: {
              top: '15%',
              containLabel: true
            },
            xAxis: [{
              name: '日期',
              type: 'category',
              nameTextStyle: {
                fontSize: '14',
              },
              axisTick: {
                alignWithLabel: 'true'
              },
              data: data[0].time
            }],
            yAxis: [
              {
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
