<template>
  <div id="countryDataInfChart" ref="countryDataInfChartRef"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'CountryDataInf',
  mounted () {
    this.setEchartHeight()
    this.drawInf()
  },
  props: {
    country: String
  },
  watch: {
    country (newValue) {
      this.drawInf()
    }
  },
  methods: {
    setEchartHeight () {
      const echartItem = document.getElementById('countryDataInfChart')
      echartItem.style.setProperty('height', window.screen.width / 3 * 2 + 'px')
    },
    drawInf () {
      // const echartItem = document.getElementById('countryDataInfChart')
      let mychart = echarts.init(this.$refs.countryDataInfChartRef)
      fetch('http://81.70.134.96:5000/countryInfData/' + this.country).then(function (response) {
        response.json().then(function (data) {
          if (JSON.stringify(data) === '{}') {
            return
          }
          mychart.setOption({
            title: {
              text: data.name + '感染数据折线',
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
              data: ['确诊人数', '治愈人数', '死亡人数'],
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
#countryDataInfChart {
  position: relative;
  width: 100%;
  height: 100%;
  border-style: solid;
  border-color: #ffffff #ffffff #e6e6e6 #ffffff;
  border-bottom-width: 1px;
}
</style>
