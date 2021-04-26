<template>
  <div><world-map-vaccine :worldMapVaccineData="data"></world-map-vaccine></div>
</template>

<script>
import WorldMapVaccine from '../components/WorldMapVaccine.vue'

export default {
  name: 'App',
  components: {
    WorldMapVaccine
  },
  data() {
    return {
      data : {vaccined: [{name: '中国', value: 4800000}, {name: '加拿大', value: 10000}], 
              coverage: [{name: '中国', value: 0.111}]}
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
