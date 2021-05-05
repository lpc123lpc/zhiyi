<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
    <el-container>
      <el-aside width="450px">
        <infect-detail-province-sidebar v-bind:province="provinceMsg"></infect-detail-province-sidebar>
      </el-aside>
      <el-main>
        <div style="margin-left: 950px; position: absolute">
          <el-button type="primary" plain @click="back()">返回</el-button>
        </div>
        <div style="align: center; margin-top: 20px">
          <infect-detail-province-map v-bind:province="provinceMsg" v-bind:provinceMapInfectionData="provinceMapInfectionDataMsg"></infect-detail-province-map>
        </div>
        <div style="align: center; margin-top: 50px">
          <line-chart-infect-province></line-chart-infect-province>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import header from '../components/Header.vue'
import infectDetailProvinceSidebar from '../components/InfectDetailProvinceSidebar.vue'
import infectDetailProvinceMap from '../components/ProvinceMapInfection.vue'
import lineChartInfectProvince from '../components/ProvinceInfection.vue'
export default {
  name: 'InfectProvinceDetail',
  components: { // 定义组件
    'wbc-nav': header,
    'infect-detail-province-sidebar': infectDetailProvinceSidebar,
    'infect-detail-province-map': infectDetailProvinceMap,
    'line-chart-infect-province': lineChartInfectProvince
  },
  data () { // 选项 / 数据
    return {
      provinceMsg: '',
      provinceMapInfectionDataMsg: ''
    }
  },
  methods: { // 事件处理器
    getProvinceMsg () {
      var that = this
      that.provinceMsg = this.$route.params.province
    },
    getProvinceInfectionDataMsg () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetail/provinceMapInfectionDataMsg/' + this.$route.params.province).then(function (response) {
        response.json().then((data) => {
          that.provinceMapInfectionDataMsg = data
        })
      })
    },
    back() {
      this.$router.go(-1)
    }
  },
  mounted () {
    this.getProvinceMsg()
    this.getProvinceInfectionDataMsg()
  }
}
</script>

<style scoped>

</style>
