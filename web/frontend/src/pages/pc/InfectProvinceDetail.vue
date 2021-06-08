<template>
  <div>
    <el-container>
      <el-header>
        <wbc-nav></wbc-nav>
      </el-header>
      <el-container>
        <el-aside width="400px">
          <infect-detail-province-sidebar v-bind:province="provinceMsg"></infect-detail-province-sidebar>
        </el-aside>
        <el-main>
          <div style="margin-left: 950px; position: absolute">
            <el-button type="primary" plain @click="back()">返回</el-button>
          </div>
          <div style="align: center; margin-top: 20px">
            <infect-detail-province-map v-bind:province="provinceMsg"
                                        v-bind:provinceMapInfectionData="provinceMapInfectionDataMsg"></infect-detail-province-map>
          </div>
          <scroll-to-bottom
            v-bind:is-bottom="false"
            style="position: absolute; margin-left: 1050px; margin-top: -25px"
          ></scroll-to-bottom>
        </el-main>
      </el-container>
    </el-container>
    <div style="text-align: center; margin-top: 50px">
      <line-chart-infect-province></line-chart-infect-province>
    </div>
  </div>
</template>

<script>
import vueHeader from '../../components/pc/PageHeader.vue'
import infectDetailProvinceSidebar from '../../components/pc/InfectDetailProvinceSidebar.vue'
import infectDetailProvinceMap from '../../components/pc/ProvinceMapInfection.vue'
import lineChartInfectProvince from '../../components/pc/ProvinceInfection.vue'
import scrollToBottom from '../../components/pc/ScrollToBottom'
import {mixin} from '../../mixins'

export default {
  name: 'InfectProvinceDetail',
  components: { // 定义组件
    'wbc-nav': vueHeader,
    'infect-detail-province-sidebar': infectDetailProvinceSidebar,
    'infect-detail-province-map': infectDetailProvinceMap,
    'line-chart-infect-province': lineChartInfectProvince,
    'scroll-to-bottom': scrollToBottom
  },
  data () { // 选项 / 数据
    return {
      provinceMsg: '',
      provinceMapInfectionDataMsg: ''
    }
  },
  mixins: [mixin],
  methods: { // 事件处理器
    getProvinceMsg () {
      var that = this
      that.provinceMsg = this.$route.params.province
    },
    getProvinceInfectionDataMsg () {
      var that = this
      fetch('http://81.70.134.96:5000/infectDetail/provinceMapInfectionDataMsg/' + this.$route.params.province).then(function (response) {
        response.json().then((data) => {
          that.judgeDataExistPC(data)
          that.provinceMapInfectionDataMsg = data
        })
      })
    },
    back () {
      this.$router.go(-1)
    }
  },
  created () {
    this.getProvinceMsg()
    this.getProvinceInfectionDataMsg()
  }
}
</script>

<style scoped>

</style>
