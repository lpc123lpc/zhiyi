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
        <vaccine-home-world-map v-bind:worldMapVaccineData="worldMapVaccineDataMsg"></vaccine-home-world-map>
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
import vaccineHomeHeadbar from '../components/VaccineHomeHeadbar.vue'
import vaccineHomeWorldMap from '../components/WorldMapVaccine.vue'
export default {
  name: 'VaccineHome',
  data () { // 选项 / 数据
    return {
      worldMapVaccineDataMsg: ''
    }
  },
  methods: { // 事件处理器
    getWorldMapVaccineDataMsg () {
      var that = this
      fetch('/vaccineHome/worldMapVaccineDataMsg').then(function (response) {
        response.json().then((data) => {
          that.worldMapVaccineDataMsg = data
        })
      })
    }
  },
  components: { // 定义组件
    'wbc-nav': header,
    'home-info': vaccineHomeHeadbar,
    'vaccine-home-world-map': vaccineHomeWorldMap
  },
  created () { // 生命周期函数

  },
  mounted () {
    this.worldMapVaccineDataMsg = this.getWorldMapVaccineDataMsg()
  }
}
</script>

<style scoped>

</style>
