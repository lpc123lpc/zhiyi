<template>
  <div><world-map-vaccine :worldMapVaccineData="data"></world-map-vaccine></div>
</template>

<script>
import WorldMapVaccine from '../components/WorldMapVaccine.vue'

export default {
  name: 'TestWorldMapVaccine',
  components: {
    WorldMapVaccine
  },
  data() {
    return {
      data : {vaccined: [{name: '中国', value: 22030.9}, {name: '加拿大', value: 10}], 
              coverage: [{name: '中国', value: 0.111}]}
    }
  }
}
</script>
