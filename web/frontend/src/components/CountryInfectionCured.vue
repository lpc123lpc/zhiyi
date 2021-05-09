<template>
    <div ref="curedChart" style="width: 1000px;height: 600px"></div>
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
          text: '治愈人数折线图',
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
          orient: 'vertical',
          left: '0%',
          data: this.names,
          textStyle: {
            color: '#000',
            fontSize: 18
          },
          selectedMode: 'single'
        },
        grid: {
          left: '20%',
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
        series: this.cured
      }, true)
    }
  }
}
</script>

<style scoped>

</style>
