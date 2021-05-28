<template>
  <div>
    <world-map-infection :worldMapInfectionData="data"></world-map-infection>
  </div>
</template>

<script>
import WorldMapInfection from '../components/WorldMapInfection.vue'

export default {
  name: 'TestWorldMapInfection',
  components: {
    WorldMapInfection
  },
  data() {
    return {
      data: {
        nowConfirm: [{name: '中国', value: 22030.9}, {name: '加拿大', value: 10}],
        totalConfirm: [{name: '中国', value: 322}],
        cured: [{name: '中国', value: 322}],
        dead: [{name: '中国', value: 322}],
      }
    }
  }
}
</script>
