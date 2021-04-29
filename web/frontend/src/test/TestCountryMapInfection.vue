<template>
  <div id="countryMapInfection"><country-map-infection :countryMapInfectionData="data" :country="country"></country-map-infection></div>
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
      country: '加拿大',
      data: {nowConfirm: [{name: 'Alberta', value: 48}, {name: 'Northwest Territories', value: 300}, {name: 'Quebec', value: 4000.3},  {name: '山东', value: 5010.3}], 
            totalConfirm: [{name: 'Alberta', value: 12}], 
            cured: [{name: 'Alberta', value: 32}],
            dead: [{name: 'Alberta', value: 100}]
        }
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
