<template>
  <div>
    <el-container>
      <el-header>
        <wbc-nav></wbc-nav>
      </el-header>
      <el-container>
        <el-aside width="400px">
          <vaccine-detail-sidebar v-bind:country="countryMsg"></vaccine-detail-sidebar>
        </el-aside>
        <el-main>
          <div style="float: right">
            <el-button type="primary" plain @click="back()">返回</el-button>
          </div>
          <div style="align: center; margin-top: 20px">
            <vaccine-detail-country-map v-bind:country="countryMsg"
                                        v-bind:countryMapVaccineData="countryMapVaccineDataMsg"></vaccine-detail-country-map>
          </div>
          <scroll-to-bottom
            v-bind:is-bottom="false"
            style="position: relative; float: right; bottom: 50px"
          ></scroll-to-bottom>
        </el-main>
      </el-container>
    </el-container>
    <div style="text-align: center; margin-top: 50px">
      <line-chart-vaccine></line-chart-vaccine>
    </div>
  </div>
</template>

<script>
import vueHeader from '../../components/pc/PageHeader.vue'
import vaccineDetailSidebar from '../../components/pc/VaccineDetailSidebar.vue'
import vaccineDetailCountryMap from '../../components/pc/CountryMapVaccine.vue'
import lineChartVaccine from '../../components/pc/CountryVaccine.vue'
import scrollToBottom from '../../components/pc/ScrollToBottom'
import {mixin} from '../../mixins'

export default {
  name: 'VaccineDetail',
  components: { // 定义组件
    'wbc-nav': vueHeader,
    'vaccine-detail-sidebar': vaccineDetailSidebar,
    'vaccine-detail-country-map': vaccineDetailCountryMap,
    'line-chart-vaccine': lineChartVaccine,
    'scroll-to-bottom': scrollToBottom
  },
  data () { // 选项 / 数据
    return {
      countryMsg: '',
      countryMapVaccineDataMsg: ''
    }
  },
  mixins: [mixin],
  methods: { // 事件处理器
    getCountryMsg () {
      var that = this
      that.countryMsg = this.$route.params.country
    },
    getCountryMapVaccineDataMsg () {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineDetail/countryMapVaccineDataMsg/' + this.$route.params.country).then(function (response) {
        response.json().then((data) => {
          that.judgeDataExistPC(data)
          // console.log(data)
          that.countryMapVaccineDataMsg = data
        })
      })
    },
    back () {
      this.$router.go(-1)
    }
  },
  created () {
    this.getCountryMsg()
    this.getCountryMapVaccineDataMsg()
  }
}
</script>

<style scoped>

</style>
