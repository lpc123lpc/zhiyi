<template>
  <div ref="countryDataVacChart" style="width: 900px;height:500px"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'CountryDataVac',
  mounted () {
    this.drawVac()
  },
  props: {
    country: String
  },
  methods: {
    drawVac () {
      let mychart = echarts.init(this.$refs.countryDataVacChart)
      fetch('http://127.0.0.1:5000/countryVacData/' + this.country).then(function (response) {
        response.json().then(function (data) {
          mychart.setOption({
            title: {
              text: data.name + '接种数据',
              textStyle: {
                fontSize: '22',
                color: '#000',
                fontWeight: 'normal'
              },
              left: '20%'
            },
            backgroundColor: '',
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              left: '50%',
              data: ['接种人数'],
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
              name: '接种人数',
              type: 'line',
              data: data.vaccined
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
