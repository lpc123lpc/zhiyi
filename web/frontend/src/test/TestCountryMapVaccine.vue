<template>
  <div id="countryMapVaccine"><country-map-vaccine :countryMapVaccineData="data" :country="country"></country-map-vaccine></div>
</template>

<script>
import CountryMapVaccine from '../components/CountryMapVaccine.vue'

export default {
  name: 'App',
  components: {
    CountryMapVaccine
  },
  data() {
    return {
      country: '中国',
      data: {vaccined: [{name: '北京', value: 48}, {name: '上海', value: 300}, {name: '浙江', value: 4000.3},  {name: '山东', value: 5010.3}], 
            coverage: [{name: '北京', value: 0.730}]}
    }
  }
}
</script>

<style>
#countryMapVaccine {
  position: relative;
  margin-top: 10%;
  width: 80%;
  height: 60%;
  margin-left: 20%;
}
</style>
