<template>
  <div>
    <el-button @click="back()">返回</el-button>
    <div id="countryMapInfection"><country-map-infection :countryMapInfectionData="data" :country="country" v-if="refresh"></country-map-infection></div>
  </div>
</template>

<script>
import CountryMapInfection from '../components/CountryMapInfection.vue'

export default {
  name: 'App',
  components: {
    CountryMapInfection
  },
  data() {
    return {
      country: '',
      data: {nowConfirm: [{name: 'Alberta', value: 48}, {name: 'Northwest Territories', value: 300}, {name: 'Quebec', value: 4000.3},  {name: '山东', value: 5010.3}], 
            totalConfirm: [{name: 'Alberta', value: 12}], 
            cured: [{name: 'Alberta', value: 32}],
            dead: [{name: 'Alberta', value: 100}]
        },
      refresh: true
    }
  },
  created() {
    this.country = this.$route.params.country
    // console.log(this.country)
  },
  methods: {
    back() {
      this.refresh = false
      this.$nextTick(() => {
        this.refresh = true;
      });
    }
  }
}
</script>

<style>
#countryMapInfection {
  position: relative;
  margin-top: 10%;
  width: 80%;
  height: 60%;
  margin-left: 30%;
}
</style>
