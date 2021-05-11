<template>
    <div>
      <div style="width: 100%">
        <el-button type="warning" plain style="margin-left: 20%" @click="change('confirmed')">确诊人数</el-button>
        <el-button type="danger" plain style="margin-left: 14%" @click="change('deceased')">死亡人数</el-button>
        <el-button type="success" plain style="margin-left: 15%" @click="change('cured')">治愈人数</el-button>
      </div>
      <el-row>
      <el-main style="text-align:center">
        <country-infection-confirmed v-if="isShow==='confirmed'" v-bind:names="names"
                                   v-bind:times="times" v-bind:confirmed="confirmed"></country-infection-confirmed>
      <country-infection-deceased v-if="isShow==='deceased'" v-bind:names="names"
      v-bind:times="times" v-bind:deceased="deceased"></country-infection-deceased>
      <country-infection-cured v-if="isShow==='cured'" v-bind:names="names"
      v-bind:times="times" v-bind:cured="cured"></country-infection-cured>
      </el-main>
        </el-row>
    </div>
</template>

<script>

import CountryInfectionConfirmed from './CountryInfectionConfirmed'
import CountryInfectionDeceased from './CountryInfectionDeceased'
import CountryInfectionCured from './CountryInfectionCured'
export default {
  name: 'CountryInfection',
  components: {CountryInfectionCured, CountryInfectionDeceased, CountryInfectionConfirmed},
  data: function () {
    return {
      names: [],
      times: [],
      confirmed: [],
      deceased: [],
      cured: [],
      isShow: 'confirmed'
    }
  },
  mounted () {
    this.getData()
  },
  methods: {
    getData () {
      var that = this
      fetch('http://81.70.134.96:5000/countryInfection/' + this.$route.params.country).then(function (response) {
        response.json().then(data => {
          that.times = data[0].time
          for (var i = 0; i < data.length; i++) {
            that.names.push(data[i].name)
            that.confirmed.push({
              name: data[i].name,
              type: 'line',
              data: data[i].confirmed
            })
            that.deceased.push({
              name: data[i].name,
              type: 'line',
              data: data[i].deceased
            })
            that.cured.push(({
              name: data[i].name,
              type: 'line',
              data: data[i].cured
            }))
          }
        })
      }).catch(function (err) {
        alert(err.toString)
      })
    },
    change (x) {
      this.isShow = x
    }
  }
}
</script>

<style scoped>

</style>
