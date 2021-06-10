<template>
  <div id="ProvinceInfection"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'ProvinceInfection',
  mounted () {
    this.setEchartHeight()
    this.drawProvinceInfection()
  },
  methods: {
    setEchartHeight () {
      const echartItem = document.getElementById('ProvinceInfection')
      echartItem.style.setProperty('height', window.screen.width / 3 * 2 + 'px')
    },
    drawProvinceInfection () {
      const echartItem = document.getElementById('ProvinceInfection')
      var mychart = echarts.init(echartItem)
      fetch('http://81.70.134.96:5000/provinceInfection/country/' + this.$route.params.province).then(function (response) {
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
              data: ['确诊人数', '死亡人数', '治愈人数'],
              textStyle: {
                color: '#000',
                fontSize: 13
              }
            },
            xAxis: [{
              type: 'category',
              nameTextStyle: {
                fontSize: '14'
              },
              axisTick: {
                alignWithLabel: 'true'
              },
              data: data.time
            }],
            yAxis: [{
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
            series: [
              {
                name: '确诊人数',
                type: 'line',
                data: data.confirmed
              },
              {
                name: '死亡人数',
                type: 'line',
                data: data.deceased
              },
              {
                name: '治愈人数',
                type: 'line',
                data: data.cured
              }]
          })
        })
      })
    }
  }
}
</script>

<style scoped>
#ProvinceInfection {
  position: relative;
  width: 100%;
  height: 100%;
  border-style: solid;
  border-color: #ffffff #ffffff #e6e6e6 #ffffff;
  border-bottom-width: 1px;
}
</style>
