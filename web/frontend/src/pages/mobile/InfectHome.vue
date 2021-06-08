<template>
  <div>
    <page-header v-bind:header_title="'感染情况'"></page-header>
    <home-info></home-info>
    <van-cell style="align: center; margin-top: 10px">
      <world-map-infection v-bind:worldMapInfectionData="worldMapInfectionDataMsg"></world-map-infection>
    </van-cell>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import worldMapInfection from '../../components/mobile/WorldMapInfection'
import infectHomeHeadbar from '../../components/mobile/InfectHomeHeadbar'

export default {
  name: 'InfectHome',
  components: {
    'page-header': pageHeader,
    'home-info': infectHomeHeadbar,
    'world-map-infection': worldMapInfection
  },
  data () { // 选项 / 数据
    return {
      worldMapInfectionDataMsg: ''
    }
  },
  methods: { // 事件处理器
    getWorldMapInfectionDataMsg () {
      var that = this
      fetch('http://81.70.134.96:5000/infectHome/worldMapInfectionDataMsg').then(function (response) {
        response.json().then((data) => {
          // console.log(data)
          that.worldMapInfectionDataMsg = data
        })
      })
    }
  },
  created () { // 生命周期函数
    this.getWorldMapInfectionDataMsg()
  }
}
</script>

<style scoped>

</style>
