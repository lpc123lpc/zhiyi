<template>
  <el-card class="box-card" shadow="always">
    <!--<div slot="header" class="clearfix">
      <span>卡片名称</span>
    </div>
    <div v-for="o in 4" :key="o" class="text item">
      {{'列表内容 ' + o }}
    </div>-->
    <div slot="header" class="clearfix">
      <span style="font-size: 20px">感染情况</span>
    </div>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      +{{infect_sum_add}}
    </div>
    <div class="today-item">
      累计确诊
    </div>
    <div class="today-item">
      {{infect_sum}}
    </div>
    <el-divider></el-divider>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      +{{infect_death_add}}
    </div>
    <div class="today-item">
      累计死亡
    </div>
    <div class="today-item">
      {{infect_death}}
    </div>
    <el-divider></el-divider>
    <!--<div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      {{infect_cure_add}}
    </div>-->
    <div class="today-item">
      累计治愈
    </div>
    <div class="today-item">
      {{infect_cure}}
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'InfectDetailSidebar',
  props: ['country'],
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
  methods: {
    getInfectSum () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailSidebar/infectSum/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.infect_sum = data.value
        })
      })
    },
    getInfectSumAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailSidebar/infectSumAdd/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.infect_sum_add = data.value
        })
      })
    },
    getInfectDeath () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailSidebar/infectDeath/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.infect_death = data.value
        })
      })
    },
    getInfectDeathAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailSidebar/infectDeathAdd/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.infect_death_add = data.value
        })
      })
    },
    getInfectCure () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailSidebar/infectCure/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.infect_cure = data.value
        })
      })
    },
    getInfectCureAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailSidebar/infectCureAdd/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.infect_cure_add = data.value
        })
      })
    }
  }
}
</script>

<style scoped>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.yersterday-item {
  margin-top: 20px;
  font-size: 16px;
  text-align: center;
  margin-bottom: 15px;
}
.today-item {
  font-size: 18px;
  text-align: center;
  margin-bottom: 15px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}

.box-card {
  width: 320px;
  margin-left: 50px;
  margin-top: 50px;
  border-radius: 20px;
}
</style>
