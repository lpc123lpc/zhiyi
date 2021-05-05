<template>
    <div ref="deceasedChart" style="width: 800px;height: 600px"></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'CountryInfectionDeceased',
  props: {
    times: Array,
    names: Array,
    deceased: Array
  },
  watch: {
    deceased () {
      this.drawDeceased()
    }
  },
  mounted () {
    this.drawDeceased()
  },
  methods: {
    drawDeceased () {
      var chart = echarts.init(this.$refs.deceasedChart)
      chart.setOption({
        title: {
          text: '死亡人数',
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
        series: this.deceased
      }, true)
    }
  }
}
</script>

<style scoped>

</style>
