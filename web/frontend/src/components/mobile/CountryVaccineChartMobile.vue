<template>
  <div id="countryDataVacChart" style="width: 100%;height:500px"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'CountryDataVac',
  mounted () {
    this.setEchartHeight()
    this.drawVac()
  },
  props: {
    country: String
  },
  watch: {
    country (newValue) {
      this.drawVac()
    }
  },
  methods: {
    setEchartHeight () {
      const echartItem = document.getElementById('countryDataInfChart')
      echartItem.style.setProperty('height', window.screen.width + 'px')
    },
    drawVac () {
      const echartItem = document.getElementById('countryDataVacChart')
      let mychart = echarts.init(echartItem)
      fetch('http://81.70.134.96:5000/countryVacData/' + this.country).then(function (response) {
        response.json().then(function (data) {
          if (JSON.stringify(data) === '{}') {
            return
          }
          mychart.setOption({
            title: {
              text: data.name + '接种数据折线',
              top: 0,
              left: 'center',
              textStyle: {
                fontSize: 16,
                color: '#000',
                fontWeight: 'normal'
              }
            },
            backgroundColor: '',
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              left: 'center',
              top: 40,
              data: ['接种人数'],
              textStyle: {
                color: '#000',
                fontSize: 13
              }
            },
            xAxis: [{
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
              left: '5%',
              top: 80,
              bottom: '6%',
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
#countryDataVacChart {
  position: relative;
  width: 100%;
  height: 100%;
  border-style: solid;
  border-color: #ffffff #ffffff #e6e6e6 #ffffff;
  border-bottom-width: 1px;
}
</style>
