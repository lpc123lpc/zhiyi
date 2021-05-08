<template>
  <div style="width: 100%;height:500px">
    <el-row type="flex">
      <el-col span="4" offset="4">
        <el-button type="warning" @click="change('inf')">感染数据</el-button>
      </el-col>
      <el-col span="4" offset="2">
        <el-button type="danger"  @click="change('vac')">接种数据</el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-main style="text-align:center">
        <CountryDataInf v-show="isShow==='inf'" v-bind:country="country"></CountryDataInf>
        <CountryDataVac v-show="isShow==='vac'" v-bind:country="country"></CountryDataVac>
      </el-main>
    </el-row>
  </div>
</template>

<script>
import CountryDataInf from './CountryDataInf'
import CountryDataVac from './CountryDataVac'
export default {
  name: 'countryData',
  components: {CountryDataVac, CountryDataInf},
  data: function () {
    return {
      isShow: 'inf'
    }
  },
  mounted () {
    this.drawCountryData()
  },
  props: {
    country: String
  },
  methods: {
    change (x) {
      alert(this.$route.params.country)
      this.isShow = x
    }
  }
}

</script>

<style scoped>

</style>
