<template>
  <div>
    <div id="provinceMapInfection"><province-map-infection :provinceMapInfectionData="data" :province="province"></province-map-infection></div>
  </div>
</template>

<script>
import ProvinceMapInfection from '../components/ProvinceMapInfection.vue'

export default {
  name: 'App',
  components: {
    ProvinceMapInfection
  },
  data() {
    return {
      country: '',
      data: {nowConfirm: [{name: '渝中区', value: 48}, {name: '涪陵区', value: 300}, {name: 'Quebec', value: 4000.3},  {name: '山东', value: 5010.3}], 
            totalConfirm: [{name: '涪陵区', value: 12}], 
            cured: [{name: '涪陵区', value: 32}],
            dead: [{name: '涪陵区', value: 100}]
        },
      refresh: true
    }
  },
  created() {
    this.province = this.$route.params.province
    // console.log(this.province)
  }
}
</script>

<style>
#provinceMapInfection {
  position: relative;
  margin-top: 10%;
  width: 80%;
  height: 60%;
  margin-left: 30%;
}
</style>
