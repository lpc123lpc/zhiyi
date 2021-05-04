<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
    <el-container>
      <el-aside width="400px">
        <vaccine-detail-sidebar v-bind:country="countryMsg"></vaccine-detail-sidebar>
      </el-aside>
      <el-main>
        <div style="align: center; margin-top: 175px">
          <vaccine-detail-country-map v-bind:country="countryMsg" v-bind:countryMapVaccineData="countryMapVaccineDataMsg"></vaccine-detail-country-map>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import header from '../components/Header.vue'
import vaccineDetailSidebar from '../components/VaccineDetailSidebar.vue'
import vaccineDetailCountryMap from '../components/CountryMapVaccine.vue'
export default {
  name: 'VaccineDetail',
  components: { // 定义组件
    'wbc-nav': header,
    'vaccine-detail-sidebar': vaccineDetailSidebar,
    'vaccine-detail-country-map': vaccineDetailCountryMap
  },
  data () { // 选项 / 数据
    return {
      countryMsg: '',
      countryMapVaccineDataMsg: ''
    }
  },
  methods: { // 事件处理器
    getCountryMsg () {
      var that = this
      that.countryMsg = this.$route.params.country
    },
    getCountryMapVaccineDataMsg () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineDetail/countryMapVaccineDataMsg/' + this.$route.params.country).then(function (response) {
        response.json().then((data) => {
          that.countryMapVaccineDataMsg = data
        })
      })
    }
  },
  mounted () {
    this.countryMsg = this.getCountryMsg()
    this.countryMapVaccineDataMsg = this.getCountryMapVaccineDataMsg()
  }
}
</script>

<style scoped>

</style>
