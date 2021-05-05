<template>
    <div ref="curedChart" style="width: 800px;height: 600px"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'CountryInfectionCured',
  props: {
    times: Array,
    names: Array,
    cured: Array
  },
  watch: {
    cured () {
      this.drawCured()
    }
  },
  mounted () {
    this.drawCured()
  },
  methods: {
    drawCured () {
      var chart = echarts.init(this.$refs.curedChart)
      chart.setOption({
        title: {
          text: '治愈人数',
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
        series: this.cured
      }, true)
    }
  }
}
</script>

<style scoped>

</style>
