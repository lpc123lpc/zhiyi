<template>
  <van-tabs>
    <van-tab title="累计确诊">
      <mobile-country-confirmed v-bind:names="names"
                                v-bind:times="times" v-bind:confirmed="confirmed"></mobile-country-confirmed>
    </van-tab>
    <van-tab title="累计治愈">
      <mobile-country-cured v-bind:names="names"
                            v-bind:times="times" v-bind:cured="cured"></mobile-country-cured>
    </van-tab>
    <van-tab title="累计死亡">
      <moblie-country-deceased v-bind:names="names"
                               v-bind:times="times" v-bind:deceased="deceased"></moblie-country-deceased>
    </van-tab>
  </van-tabs>
</template>

<script>
import MobileCountryConfirmed from './MobileCountryConfirmed'
import MobileCountryCured from './MobileCountryCured'
import MoblieCountryDeceased from './MoblieCountryDeceased'
export default {
  name: 'MobileCountryInfection',
  components: {MoblieCountryDeceased, MobileCountryCured, MobileCountryConfirmed},
  data: function () {
    return {
      names: [],
      times: [],
      confirmed: [],
      deceased: [],
      cured: []
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
          if (JSON.stringify(data) === '{}') {
            return
          }
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
