<template>
  <div style="width: 100%;height:500px">
    <div>
      <el-button type="danger" plain style="margin-left: 35%" @click="change('inf')">感染数据</el-button>
      <el-button type="success" plain style="margin-left: 10%" @click="change('vac')">接种数据</el-button>
    </div>
    <el-row>
      <el-main style="text-align:center">
        <CountryDataInf v-if="isShow==='inf'" v-bind:country="country"></CountryDataInf>
        <CountryDataVac v-if="isShow==='vac'" v-bind:country="country"></CountryDataVac>
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
  },
  props: {
    country: String
  },
  methods: {
    change (x) {
      this.isShow = x
    }
  }
}

</script>

<style scoped>

</style>
