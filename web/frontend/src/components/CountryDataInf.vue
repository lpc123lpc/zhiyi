<template>
    <div ref="countryDataInfChart" style="width: 900px;height:500px"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'CountryDataInf',
  mounted () {
    this.drawInf()
  },
  props: {
    country: String
  },
  methods: {
    drawInf () {
      let mychart = echarts.init(this.$refs.countryDataInfChart)
      fetch('http://81.70.134.96:5000/countryInfData/' + this.country).then(function (response) {
        response.json().then(function (data) {
          if (JSON.stringify(data) === '{}') {
            return
          }
          mychart.setOption({
            backgroundColor: '',
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              left: 'center',
              data: ['确诊人数', '治愈人数', '死亡人数'],
              textStyle: {
                color: '#000',
                fontSize: 14
              }
            },
            xAxis: [{
              name: '日期',
              type: 'category',
              nameTextStyle: {
                fontSize: '14',
                color: '#000'
              },
              axisTick: {
                alignWithLabel: 'true'
              },
              data: data.time
            }],
            yAxis: [{
              nameTextStyle: {
                fontSize: '14',
                color: '#000'
              },
              type: 'value'
            }],
            dataZoom: {
              type: 'inside'
            },
            grid: {
              containLabel: true
            },
            series: [{
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
