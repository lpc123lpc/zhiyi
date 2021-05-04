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
      {{infect_province_sum_add}}
    </div>
    <div class="today-item">
      累计确诊
    </div>
    <div class="today-item">
      {{infect_province_sum}}
    </div>
    <el-divider></el-divider>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      {{infect_province_death_add}}
    </div>
    <div class="today-item">
      累计死亡
    </div>
    <div class="today-item">
      {{infect_province_death}}
    </div>
    <el-divider></el-divider>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      {{infect_province_cure_add}}
    </div>
    <div class="today-item">
      累计治愈
    </div>
    <div class="today-item">
      {{infect_province_cure}}
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'InfectDetailProvinceSidebar',
  props: ['province'],
  data: function () {
    return {
      infect_province_sum: '',
      infect_province_sum_add: '',
      infect_province_death: '',
      infect_province_death_add: '',
      infect_province_cure: '',
      infect_province_cure_add: ''
    }
  },
  mounted () {
    this.infect_province_sum = this.getInfectSum()
    this.infect_province_sum_add = this.getInfectSumAdd()
    this.infect_province_death = this.getInfectDeath()
    this.infect_province_death_add = this.getInfectDeathAdd()
    this.infect_province_cure = this.getInfectCure()
    this.infect_province_cure_add = this.getInfectCureAdd()
  },
  methods: {
    getInfectProvinceSum () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailProvinceSidebar/infectSum/' + this.province).then(function (response) {
        response.json().then((data) => {
          that.infect_province_sum = data
        })
      })
    },
    getInfectProvinceSumAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailProvinceSidebar/infectProvinceSumAdd/' + this.province).then(function (response) {
        response.json().then((data) => {
          that.infect_province_sum_add = data
        })
      })
    },
    getInfectProvinceDeath () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailProvinceSidebar/infectProvinceDeath/' + this.province).then(function (response) {
        response.json().then((data) => {
          that.infect_province_death = data
        })
      })
    },
    getInfectProvinceDeathAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailProvinceSidebar/infectProvinceDeathAdd/' + this.province).then(function (response) {
        response.json().then((data) => {
          that.infect_province_death_add = data
        })
      })
    },
    getInfectProvinceCure () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailProvinceSidebar/infectProvinceCure/' + this.province).then(function (response) {
        response.json().then((data) => {
          that.infect_province_cure = data
        })
      })
    },
    getInfectProvinceCureAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/infectDetailProvinceSidebar/infectProvinceCureAdd/' + this.province).then(function (response) {
        response.json().then((data) => {
          that.infect_province_cure_add = data
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
