<template>
  <div ref="curedChart" style="width: 100%;height: 1200px"></div>
</template>

<script>
import {mixin} from '../../mixins'
import echarts from 'echarts'

export default {
  name: 'MobileCountryCured',
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
          left: 'center',
          text: '治愈人数折线图',
          textStyle: {
            color: '#000',
            fontWeight: 'normal'
          }
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          top: '500px',
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
          height: '400px',
          containLabel: true
        },
        xAxis: [{
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
