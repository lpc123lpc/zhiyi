<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
    <el-container>
      <el-aside width="400px">
        <vaccine-sidebar v-bind:vaccine_header_title="'疫苗接种'"></vaccine-sidebar>
        <infect-sidebar v-bind:infect_header_title="'感染情况'"></infect-sidebar>
      </el-aside>
      <el-main id="my-el-main">
        <search-page v-bind:region="this.region" v-bind:data="regionInfectDataMsg"
                     v-bind:vaccine-data="this.regionVaccineDataMsg"></search-page>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import vueHeader from '../../components/pc/PageHeader.vue'
import vaccineSidebar from '../../components/pc/VaccineSidebar.vue'
import infectSidebar from '../../components/pc/InfectSidebar.vue'
import searchPage from '../../components/pc/SearchPage.vue'

export default {
  name: 'Search',
  components: { // 定义组件
    'wbc-nav': vueHeader,
    'vaccine-sidebar': vaccineSidebar,
    'infect-sidebar': infectSidebar,
    'search-page': searchPage
  },
  data() {
    return {
      region: '',
      regionInfectDataMsg: {
        infect: {nowConfirm: '', totalConfirm: '', cured: '', dead: '', coverage: ''},
        vaccine: {vaccined: '', coverage: ''}
      },
      regionVaccineDataMsg: ''
    }
  },
  mounted() {
    this.region = this.$route.params.region
    this.set_left()
  },
  created() {
    this.getRegionInfectDataMsg()
    this.getRegionVaccineDataMsg()
  },
  watch: {
    region() {
      this.getRegionInfectDataMsg()
      this.getRegionVaccineDataMsg()
    }
  },
  methods: {
    set_left() {
      const elMain = document.getElementById('my-el-main')
      // console.log(elMain.offsetWidth)
      const searchPage = document.getElementById('search-page-id')
      searchPage.style.setProperty('margin-left', elMain.offsetWidth / 2 - 637 + 'px')
    },
    getRegionInfectDataMsg() {
      var that = this
      fetch('http://81.70.134.96:5000/search/' + that.$route.params.region + '/regionInfectDataMsg').then(function (response) {
        response.json().then((data) => {
          // console.log(data)
          that.regionInfectDataMsg = data
        })
      })
    },
    getRegionVaccineDataMsg() {
      var that = this
      fetch('http://81.70.134.96:5000/search/' + that.$route.params.region + '/regionVaccineDataMsg').then(function (response) {
        response.json().then((data) => {
          // console.log(data)
          that.regionVaccineDataMsg = data
        })
      })
    }
  }
}
</script>

<style scoped>

</style>
