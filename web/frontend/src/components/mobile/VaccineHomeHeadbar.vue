<template>
  <van-grid :column-num="2">
    <van-grid-item id="van-grid-item-id-1">
      <van-icon name="arrow-down" style="margin-bottom: 5px"/>
      <div class="infect-sum">累计接种</div>
      <div class="infect-sum">{{ vaccine_sum }}</div>
      <div class="infect-sum-add">+{{ vaccine_sum_add }}</div>
    </van-grid-item>
    <van-grid-item id="van-grid-item-id-2">
      <van-icon name="arrow-down" style="margin-bottom: 5px"/>
      <div class="infect-sum">每百人接种</div>
      <div class="infect-sum">{{ vaccine_cover }} 剂</div>
      <div class="infect-sum-add">NaN</div>
    </van-grid-item>
  </van-grid>
</template>

<script>
export default {
  name: 'VaccineHomeHeadbar',
  data: function () {
    return {
      vaccine_sum: '',
      vaccine_sum_add: '',
      vaccine_cover: '',
      vaccine_cover_add: ''
    }
  },
  created () {
    this.getVaccineSum()
    this.getVaccineSumAdd()
    this.getVaccineCover()
    // this.getVaccineCoverAdd()
  },
  mounted () {
    // this.set_length()
  },
  methods: {
    set_length () {
      const gridItem1 = document.getElementById('van-grid-item-id-1')
      const gridItem2 = document.getElementById('van-grid-item-id-2')
      const gridItem3 = document.getElementById('van-grid-item-id-3')
      // alert(window.screen.width)
      gridItem1.style.setProperty('width', window.screen.width / 3 + 'px')
      gridItem2.style.setProperty('width', window.screen.width / 3 + 'px')
      gridItem3.style.setProperty('width', window.screen.width / 3 + 'px')
    },
    getVaccineSum () {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineHomeHeadbar/vaccineSum').then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum = data.value
        })
      })
    },
    getVaccineSumAdd () {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineHomeHeadbar/vaccineSumAdd').then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum_add = data.value
        })
      })
    },
    getVaccineCover () {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineHomeHeadbar/vaccineCover').then(function (response) {
        response.json().then((data) => {
          that.vaccine_cover = data.value
        })
      })
    },
    getVaccineCoverAdd () {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineHomeHeadbar/vaccineCoverAdd').then(function (response) {
        response.json().then((data) => {
          that.vaccine_cover_add = data.value
        })
      })
    }
  }
}
</script>

<style scoped>
.infect-sum {
  margin-top: 5px;
  margin-bottom: 5px;
  font-size: small;
}
.infect-sum-add {
  font-size: small;
}
</style>
