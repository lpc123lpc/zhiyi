<template>
  <div>
    <page-header v-bind:header_title="'疫苗接种'"></page-header>
    <div style="align: center;">
      <home-info></home-info>
    </div>
    <div style="align: center; margin-top: 120px">
      <world-map-vaccine v-bind:worldMapVaccineData="worldMapVaccineDataMsg"></world-map-vaccine>
    </div>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import worldMapVaccine from '../../components/mobile/WorldMapVaccine'
import vaccineHomeHeadbar from "../../components/mobile/VaccineHomeHeadbar";

export default {
  name: 'VaccineHome',
  components: {
    'page-header': pageHeader,
    'home-info': vaccineHomeHeadbar,
    'world-map-vaccine': worldMapVaccine
  },
  data() { // 选项 / 数据
    return {
      worldMapVaccineDataMsg: ''
    }
  },
  methods: { // 事件处理器
    getWorldMapVaccineDataMsg() {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineHome/worldMapVaccineDataMsg').then(function (response) {
        response.json().then((data) => {
          that.worldMapVaccineDataMsg = data
        })
      })
    }
  },
  created() { // 生命周期函数
    this.getWorldMapVaccineDataMsg()
  },
}
</script>

<style scoped>

</style>
