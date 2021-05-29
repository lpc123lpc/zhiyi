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
      fetch('http://81.70.134.96:5000/countryVaccine/' + this.$route.params.country).then(function (response) {
        response.json().then(function (data) {
          if (JSON.stringify(data) === '{}') {
            return
          }
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
          var legendItemSize = 15
          if (this.$route.params.country === '俄罗斯') {
            legendItemSize = 8
          }
          myChart.setOption({
            title: {
              text: data[0].name + '接种人数折线图',
              left: '65%',
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
              orient: 'vertical',
              right: '55%',
              itemGap: 15,
              data: names,
              selected: this.getSelected(names),
              textStyle: {
                color: '#000',
                fontSize: legendItemSize
              },
              selectedMode: 'multiple'
            },
            grid: {
              left: '50%',
              containLabel: true
            },
            xAxis: [{
              name: '日期',
              type: 'category',
              nameTextStyle: {
                fontSize: '14'
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
