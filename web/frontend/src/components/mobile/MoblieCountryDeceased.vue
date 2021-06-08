<template>
  <div ref="deceasedChart" style="width: 100%;height: 1200px"></div>
</template>

<script>
import {mixin} from '../../mixins'
import echarts from 'echarts'

export default {
  name: 'MoblieCountryDeceased',
  props: {
    times: Array,
    names: Array,
    deceased: Array
  },
  mixins: [mixin],
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
      if (this.deceased.length === 0) {
        return
      }
      var legendItemSize = 15
      if (this.$route.params.country === '俄罗斯') {
        legendItemSize = 8
      }
      var chart = echarts.init(this.$refs.deceasedChart)
      chart.setOption({
        title: {
          text: '死亡人数折线图',
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
          itemGap: 15,
          top: '500px',
          data: this.names,
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
        series: this.deceased
      }, true)
    }
  }
}
</script>

<style scoped>

</style>
