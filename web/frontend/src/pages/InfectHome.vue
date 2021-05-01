<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
    <el-main>
      <div style="align: center;">
        <home-info></home-info>
      </div>
      <div style="align: center; margin-top: 175px">
        <infect-home-world-map v-bind:worldMapInfectionData="worldMapInfectionDataMsg"></infect-home-world-map>
      </div>
    </el-main>
    <!--<div class="container">
        <el-row  :gutter="30">
            <el-col :sm="24" :md="16" style="transition:all .5s ease-out;margin-bottom:30px;">
                <wbc-sharelist></wbc-sharelist>
            </el-col>
            <el-col :sm="24"  :md="8" >
                <wbc-rightlist></wbc-rightlist>
            </el-col>
        </el-row>
    </div>
    <wbc-footer></wbc-footer>-->
  </el-container>
</template>

<script>
import header from '../components/Header.vue'
import infectHomeHeadbar from '../components/InfectHomeHeadbar.vue'
import infectHomeWorldMap from '../components/WorldMapInfection.vue'
export default {
  name: 'InfectHome',
  components: { // 定义组件
    'wbc-nav': header,
    'home-info': infectHomeHeadbar,
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
      fetch('/infectHome/worldMapInfectionDataMsg').then(function (response) {
        response.json().then((data) => {
          that.worldMapInfectionDataMsg = data
        })
      })
    }
  },
  mounted () {
    this.worldMapInfectionDataMsg = this.getWorldMapInfectionDataMsg()
  }
}
</script>

<style scoped>

</style>
