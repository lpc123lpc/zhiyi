<template>
  <div>
    <page-header v-bind:header_title="'国家列表'"></page-header>
    <div style="align: center">
      <!--<infect-home-world-map v-bind:worldMapInfectionData="worldMapInfectionDataMsg"></infect-home-world-map>-->
    </div>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import infectHomeWorldMap from '../../components/pc/WorldMapInfection.vue'
export default {
  name: 'Home',
  components: {
    'page-header': pageHeader,
    'infect-home-world-map': infectHomeWorldMap
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
  created () {
    this.getWorldMapInfectionDataMsg()
  }
}
</script>

<style scoped>

</style>
