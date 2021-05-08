<template>
  <el-card class="box-card" shadow="always">
    <!--<div slot="header" class="clearfix">
      <span>卡片名称</span>
    </div>
    <div v-for="o in 4" :key="o" class="text item">
      {{'列表内容 ' + o }}
    </div>-->
    <div slot="header" class="clearfix">
      <span style="font-size: 20px">{{infect_header_title}}</span>
    </div>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      {{infect_sum_add}}
    </div>
    <div class="today-item">
      现有确诊
    </div>
    <div class="today-item">
      {{infect_sum}}
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
  name: 'InfectSidebar',
  props: {
    infect_header_title: {
      type: String,
      default: ''
    }
  },
  data: function () {
    return {
      infect_sum: '',
      infect_sum_add: '',
      infect_cure: '',
      infect_cure_add: ''
    }
  },
  created () {
    this.getInfectSum()
    this.getInfectSumAdd()
    this.getInfectCure()
    // this.getInfectCureAdd()
  },
  methods: {
    getInfectSum () {
      var that = this
      fetch('http://127.0.0.1:5000/infectSidebar/infectSum').then(function (response) {
        response.json().then((data) => {
          that.infect_sum = data.value
        })
      })
    },
    getInfectSumAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/infectSidebar/infectSumAdd').then(function (response) {
        response.json().then((data) => {
          that.infect_sum_add = data.value
        })
      })
    },
    getInfectCure () {
      var that = this
      fetch('http://127.0.0.1:5000/infectSidebar/infectCure').then(function (response) {
        response.json().then((data) => {
          that.infect_cure = data.value
        })
      })
    },
    getInfectCureAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/infectSidebar/infectCureAdd').then(function (response) {
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
