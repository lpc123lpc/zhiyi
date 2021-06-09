<template>
  <div>
    <page-header></page-header>
    <search-page
      v-bind:region="this.region"
      v-bind:data="regionInfectDataMsg"
      v-bind:vaccine-data="regionVaccineDataMsg"
    ></search-page>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import searchPage from '../../components/mobile/SearchPage'

export default {
  name: 'Search',
  components: { // 定义组件
    'page-header': pageHeader,
    'search-page': searchPage
  },
  data () {
    return {
      region: '',
      regionInfectDataMsg: '',
      regionVaccineDataMsg: ''
    }
  },
  mounted () {
    this.region = this.$route.params.region
  },
  created () {
    this.getRegionInfectDataMsg()
    this.getRegionVaccineDataMsg()
  },
  methods: {
    getRegionInfectDataMsg () {
      var that = this
      fetch('http://81.70.134.96:5000/search/' + that.$route.params.region + '/regionInfectDataMsg').then(function (response) {
        response.json().then((data) => {
          // console.log(data)
          that.regionInfectDataMsg = data
        })
      })
    },
    getRegionVaccineDataMsg () {
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
