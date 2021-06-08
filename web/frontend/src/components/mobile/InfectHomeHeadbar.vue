<template>
  <van-grid :column-num="3">
    <van-grid-item id="van-grid-item-id-1">
      <van-icon name="arrow-down" style="margin-bottom: 5px"/>
      <div class="infect-sum">累计确诊</div>
      <div class="infect-sum">{{ infect_sum }}</div>
      <div class="infect-sum-add">+{{ infect_sum_add }}</div>
    </van-grid-item>
    <van-grid-item id="van-grid-item-id-2">
      <van-icon name="arrow-down" style="margin-bottom: 5px"/>
      <div class="infect-sum">累计死亡</div>
      <div class="infect-sum">{{ infect_death }}</div>
      <div class="infect-sum-add">+{{ infect_death_add }}</div>
    </van-grid-item>
    <van-grid-item id="van-grid-item-id-3">
      <van-icon name="arrow-down" style="margin-bottom: 5px"/>
      <div class="infect-sum">累计治愈</div>
      <div class="infect-sum">{{ infect_cure }}</div>
      <div class="infect-sum-add">NaN</div>
    </van-grid-item>
  </van-grid>
</template>

<script>
export default {
  name: 'InfectHomeHeadbar',
  data: function () {
    return {
      infect_sum: '',
      infect_sum_add: '',
      infect_death: '',
      infect_death_add: '',
      infect_cure: '',
      infect_cure_add: ''
    }
  },
  created () {
    this.getInfectSum()
    this.getInfectSumAdd()
    this.getInfectDeath()
    this.getInfectDeathAdd()
    this.getInfectCure()
    // this.getInfectCureAdd()
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
    getInfectSum () {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectSum').then(function (response) {
        response.json().then((data) => {
          that.infect_sum = data.value
        })
      })
    },
    getInfectSumAdd () {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectSumAdd').then(function (response) {
        response.json().then((data) => {
          that.infect_sum_add = data.value
        })
      })
    },
    getInfectDeath () {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectDeath').then(function (response) {
        response.json().then((data) => {
          that.infect_death = data.value
        })
      })
    },
    getInfectDeathAdd () {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectDeathAdd').then(function (response) {
        response.json().then((data) => {
          that.infect_death_add = data.value
        })
      })
    },
    getInfectCure () {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectCure').then(function (response) {
        response.json().then((data) => {
          that.infect_cure = data.value
        })
      })
    },
    getInfectCureAdd () {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectCureAdd').then(function (response) {
        response.json().then((data) => {
          that.infect_cure_add = data.value
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
