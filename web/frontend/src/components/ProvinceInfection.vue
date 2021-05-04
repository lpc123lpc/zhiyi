<template>
  <div ref="ProvinceInfection" style="width: 100%;height:600px;"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'ProvinceInfection',
  mouted () {
    this.drawProvinceInfection()
  },
  methods: {
    drawProvinceInfection () {
      var mychart = echarts.init(this.$refs.ProvinceInfection)
      fetch('').then(function (response) {
        response.json().then(function (data) {
          mychart.setOption({
            title: {
              text: data.name + '感染数据',
              textStyle: {
                fontSize: '20',
                color: '#696969'
              },
              left: '10%'
            },
            backgroundColor: '',
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              left: '50%',
              data: ['确诊人数', '死亡人数', '治愈人数']
            },
            xAxis: [{
              name: '日期',
              type: 'category',
              nameTextStyle: {
                fontSize: '14',
                fontWeight: 'bold'
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

</style>
