<template>
  <div>
    <el-container>
      <el-header>
        <wbc-nav></wbc-nav>
      </el-header>
      <el-container>
        <el-aside width="400px">
          <infect-detail-sidebar v-bind:country="countryMsg"></infect-detail-sidebar>
        </el-aside>
        <el-main>
          <div style="align: center; margin-top: 20px">
            <infect-detail-country-map v-bind:country="countryMsg"
                                       v-bind:countryMapInfectionData="countryMapInfectionDataMsg"></infect-detail-country-map>
          </div>
          <scroll-to-bottom
            v-bind:is-bottom="false"
            style="position: absolute; margin-left: 1050px; margin-top: -25px"
          ></scroll-to-bottom>
        </el-main>
      </el-container>
    </el-container>
    <div style="margin-top: 50px; text-align: center">
      <line-chart-infect></line-chart-infect>
    </div>
  </div>
</template>

<script>
import vueHeader from '../components/PageHeader.vue'
import infectDetailSidebar from '../components/InfectDetailSidebar.vue'
import infectDetailCountryMap from '../components/CountryMapInfection.vue'
import lineChartInfect from '../components/CountryInfection.vue'
import scrollToBottom from "../components/ScrollToBottom";
import {mixin} from '../mixins'

export default {
  name: 'InfectDetail',
  components: { // 定义组件
    'wbc-nav': vueHeader,
    'infect-detail-sidebar': infectDetailSidebar,
    'infect-detail-country-map': infectDetailCountryMap,
    'line-chart-infect': lineChartInfect,
    'scroll-to-bottom': scrollToBottom
  },
  mixins: [mixin],
  data() { // 选项 / 数据
    return {
      countryMsg: '',
      countryMapInfectionDataMsg: '',
    }
  },
  methods: { // 事件处理器
    getCountryMsg() {
      var that = this
      that.countryMsg = this.$route.params.country
    },
    getCountryInfectionDataMsg() {
      var that = this
      fetch('http://81.70.134.96:5000/infectDetail/countryMapInfectionDataMsg/' + this.$route.params.country).then(function (response) {
        response.json().then((data) => {
          that.judgeDataExist(data)
          that.countryMapInfectionDataMsg = data
        })
      })
    }
  },
  created() {
    this.getCountryMsg()
    this.getCountryInfectionDataMsg()
  }
}
</script>

<style scoped>

</style>
