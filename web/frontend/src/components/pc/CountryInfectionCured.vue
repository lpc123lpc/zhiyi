<template>
    <div ref="curedChart" style="width: 100%;height: 600px"></div>
</template>

<script>
import echarts from 'echarts'
import {mixin} from '../../mixins'

export default {
  name: 'CountryInfectionCured',
  props: {
    times: Array,
    names: Array,
    cured: Array
  },
  mixins: [mixin],
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
      if (this.cured.length === 0) {
        return
      }
      var legendItemSize = 15
      if (this.$route.params.country === '俄罗斯') {
        legendItemSize = 8
      }
      var chart = echarts.init(this.$refs.curedChart)
      chart.setOption({
        title: {
          text: '治愈人数折线图',
          left: '65%',
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
          right: '55%',
          data: this.names,
          itemGap: 15,
          selected: this.getSelected(this.names),
          textStyle: {
            color: '#000',
            fontSize: legendItemSize
          },
          selectedMode: 'multiple'
        },
        grid: {
          left: '50%',
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
