<template>
    <el-container>
      <el-header>
        <el-button round type="warning" @click="change('confirmed')">确诊人数</el-button>
        <el-button round type="danger" @click="change('deceased')">死亡人数</el-button>
        <el-button round type="success" @click="change('cured')">治愈人数</el-button>
      </el-header>
      <el-main>
        <country-infection-confirmed v-show="isShow==='confirmed'" v-bind:names="names"
                                   v-bind:times="times" v-bind:confirmed="confirmed"></country-infection-confirmed>
      <country-infection-deceased v-show="isShow==='deceased'" v-bind:names="names"
      v-bind:times="times" v-bind:deceased="deceased"></country-infection-deceased>
      <country-infection-cured v-show="isShow==='cured'" v-bind:names="names"
      v-bind:times="times" v-bind:cured="cured"></country-infection-cured>
      </el-main>
    </el-container>
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
      fetch('../static/json/charts/testInfection').then(function (response) {
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
