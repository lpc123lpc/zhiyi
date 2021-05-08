<template>
  <div ref="confirmedChart" style="width: 1000px;height: 600px"></div>
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
          text: '感染人数折线图',
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
          data: this.names,
          textStyle: {
            color: '#000',
            fontSize: 18
          },
          selectedMode: 'single'
        },
        grid: {
          top: '15%',
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
