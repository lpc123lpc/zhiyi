<template>
  <van-tabs>
    <van-tab title="累计确诊">
      <van-list
        v-model="loading"
        :finished="finished"
        @load="getWorldData">
        <van-cell v-for="(item,index) in items" :key="index" :title="item.name" :value="matter(item.confirmed)" is-link @click="showCountryInfectionChart(item.name)">
        </van-cell>
        <van-popup v-model="showCountryInfectionChartVariable" position="bottom" closeable class="popup-item" ref="popupId1">
          <mobile-country-infection-chart v-bind:country="countryMsg" ></mobile-country-infection-chart>
        </van-popup>
      </van-list>
    </van-tab>
    <van-tab title="新增确诊">
      <van-list
        v-model="loading"
        :finished="finished"
        @load="getWorldData">
        <van-cell v-for="(item,index) in items" :key="index" :title="item.name" :value="matter(item.newConfirmed)" />
      </van-list>
    </van-tab>
    <van-tab title="累计接种">
      <van-list
        v-model="loading"
        :finished="finished"
        @load="getWorldData">
        <van-cell v-for="(item,index) in items" :key="index" :title="item.name" :value="matter(item.vaccined)"  is-link @click="showCountryVaccineChart(item.name)">
        </van-cell>
        <van-popup v-model="showCountryVaccineChartVariable" position="bottom" closeable class="popup-item" ref="popupId2">
          <mobile-country-vaccine-chart v-bind:country="countryMsg" ></mobile-country-vaccine-chart>
        </van-popup>
      </van-list>
    </van-tab>
    <van-tab title="百人接种">
      <van-list
        v-model="loading"
        :finished="finished"
        @load="getWorldData">
        <van-cell v-for="(item,index) in items" :key="index" :title="item.name" :value="matter(item.vaccine_coverage)" />
      </van-list>
    </van-tab>
  </van-tabs>
</template>

<script>
import mobileCountryInfectionChart from '../../components/mobile/CountryInfectionChartMobile.vue'
import mobileCountryVaccineChart from '../../components/mobile/CountryVaccineChartMobile.vue'
export default {
  name: 'MobileWorldTable',
  components: {
    'mobile-country-infection-chart': mobileCountryInfectionChart,
    'mobile-country-vaccine-chart': mobileCountryVaccineChart
  },
  data () {
    return {
      items: [],
      loading: false,
      finished: false,
      countryMsg: '',
      showCountryInfectionChartVariable: false,
      showCountryVaccineChartVariable: false
    }
  },
  mounted () {
    // this.setPopupHeight()
  },
  methods: {
    setPopupHeight () {
      console.log(this.$refs.popupId1)
      this.$refs.popupId1.style.setProperty('height', window.screen.width + 'px')
      this.$refs.popupId2.style.setProperty('height', window.screen.width + 'px')
    },
    showCountryInfectionChart (countryName) {
      this.countryMsg = countryName
      this.showCountryInfectionChartVariable = true
    },
    showCountryVaccineChart (countryName) {
      this.countryMsg = countryName
      this.showCountryVaccineChartVariable = true
    },
    getWorldData () {
      var that = this
      fetch('http://81.70.134.96:5000/worldData').then(function (response) {
        response.json().then((data) => {
          that.items = data
        })
      }).catch(function (err) {
        alert(err.toString())
      })
      this.finished = true
    },
    matter (cellValue) {
      cellValue += ''
      if (!cellValue.includes('.')) cellValue += '.'
      var out = cellValue.replace(/(\d)(?=(\d{3})+\.)/g, function ($0, $1) {
        return $1 + ','
      }).replace(/\.$/, '')
      if (out === 'null') {
        return ''
      } else {
        return out
      }
    }
  }
}
</script>

<style scoped>

</style>
