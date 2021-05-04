<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
    <el-container>
      <el-aside width="400px">
        <infect-detail-sidebar v-bind:country="'疫苗接种'"></infect-detail-sidebar>
      </el-aside>
      <el-main>
        <div style="align: center; margin-top: 20px">
          <infect-detail-country-map v-bind:country="countryMsg" v-bind:countryMapInfectionData="countryMapInfectionDataMsg"></infect-detail-country-map>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import header from '../components/Header.vue'
import infectDetailSidebar from '../components/InfectDetailSidebar.vue'
import infectDetailCountryMap from '../components/CountryMapInfection.vue'
export default {
  name: 'InfectDetail',
  components: { // 定义组件
    'wbc-nav': header,
    'infect-detail-sidebar': infectDetailSidebar,
    'infect-detail-country-map': infectDetailCountryMap
  },
  data () { // 选项 / 数据
    return {
      countryMsg: '',
      countryMapInfectionDataMsg: ''
    }
  },
  methods: { // 事件处理器
    getCountryMsg () {
      this.countryMsg = this.$route.params.country
    },
    getCountryInfectionDataMsg () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetail/countryMapInfectionDataMsg/' + this.$route.params.country).then(function (response) {
        response.json().then((data) => {
          that.countryMapInfectionDataMsg = data
        })
      })
    }
  },
  mounted () {
    this.getCountryMsg()
    this.getCountryInfectionDataMsg()
  }
}
</script>

<style scoped>

</style>
