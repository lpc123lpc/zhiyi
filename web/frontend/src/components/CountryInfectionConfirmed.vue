<template>
  <div ref="confirmedChart" style="width: 800px;height: 600px"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'CountryInfectionConfirmed',
  props: {
    times: Array,
    names: Array,
    confirmed: Array
  },
  watch: {
    confirmed () {
      this.drawConfirmed()
    }
  },
  mounted () {
    this.drawConfirmed()
  },
  methods: {
    drawConfirmed () {
      var chart = echarts.init(this.$refs.confirmedChart)
      chart.setOption({
        title: {
          text: '感染人数',
          textStyle: {
            fontSize: '20',
            color: '#696969'
          },
          left: '10%'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          left: '50%',
          data: this.names
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
          data: this.times
        }],
        yAxis: [{
          type: 'value'
        }],
        dataZoom: {
          type: 'inside'
        },
        series: this.confirmed
      }, true)
    }
  }
}
</script>

<style scoped>

</style>
