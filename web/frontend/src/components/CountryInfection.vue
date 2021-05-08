<template>
    <div>
      <el-row type="flex">
        <el-col span="4" offset="4">
          <el-button type="warning" style="align-content: center" @click="change('confirmed')">确诊人数</el-button>
        </el-col>
        <el-col span="4" offset="2">
          <el-button type="danger" style="text-align: center" @click="change('deceased')">死亡人数</el-button>
        </el-col>
        <el-col span="4" offset="2">
          <el-button type="success" style="text-align: center" @click="change('cured')">治愈人数</el-button>
        </el-col>
      </el-row>
      <el-row>
      <el-main style="text-align:center">
        <country-infection-confirmed v-show="isShow==='confirmed'" v-bind:names="names"
                                   v-bind:times="times" v-bind:confirmed="confirmed"></country-infection-confirmed>
      <country-infection-deceased v-show="isShow==='deceased'" v-bind:names="names"
      v-bind:times="times" v-bind:deceased="deceased"></country-infection-deceased>
      <country-infection-cured v-show="isShow==='cured'" v-bind:names="names"
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
  props: {
    country: String
  },
  mounted () {
    this.getData()
  },
  methods: {
    getData () {
      var that = this
      fetch('http://127.0.0.1:5000/countryInfData/' + this.country).then(function (response) {
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
