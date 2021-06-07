<template>
  <el-card class="box-card" shadow="always" id="card-head-bar">
    <el-row>
      <el-col :span="8">
        <div class="infect-sum-add">+{{ infect_sum_add }}</div>
      </el-col>
      <el-col :span="8">
        <div class="infect-sum-add">+{{ infect_death_add }}</div>
      </el-col>
      <el-col :span="8"></el-col>
    </el-row>
    <el-row>
      <el-col :span="8">
        <div class="infect-sum">累计确诊{{ infect_sum }}</div>
      </el-col>
      <el-col :span="8">
        <div class="infect-sum">累计死亡{{ infect_death }}</div>
      </el-col>
      <el-col :span="8">
        <div class="infect-sum">累计治愈{{ infect_cure }}</div>
      </el-col>
      <!--<el-col :span="6"><div class="infect-sum-add">+{{infect_cure_add}}</div></el-col>-->
    </el-row>
  </el-card>
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
  created() {
    this.getInfectSum()
    this.getInfectSumAdd()
    this.getInfectDeath()
    this.getInfectDeathAdd()
    this.getInfectCure()
    // this.getInfectCureAdd()
  },
  mounted() {
    this.set_length()
  },
  methods: {
    set_length() {
      const headBar = document.getElementById('card-head-bar')
      // alert(document.body.offsetWidth)
      headBar.style.setProperty('width', document.body.offsetWidth * 4 / 5 + 'px')
    },
    getInfectSum() {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectSum').then(function (response) {
        response.json().then((data) => {
          that.infect_sum = data.value
        })
      })
    },
    getInfectSumAdd() {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectSumAdd').then(function (response) {
        response.json().then((data) => {
          that.infect_sum_add = data.value
        })
      })
    },
    getInfectDeath() {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectDeath').then(function (response) {
        response.json().then((data) => {
          that.infect_death = data.value
        })
      })
    },
    getInfectDeathAdd() {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectDeathAdd').then(function (response) {
        response.json().then((data) => {
          that.infect_death_add = data.value
        })
      })
    },
    getInfectCure() {
      var that = this
      fetch('http://81.70.134.96:5000/infectHomeHeadbar/infectCure').then(function (response) {
        response.json().then((data) => {
          that.infect_cure = data.value
        })
      })
    },
    getInfectCureAdd() {
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
  font-size: 10px;
  text-align: center;
}

.infect-sum-add {
  font-size: 5px;
  text-align: center;
}

.box-card {
  width: 250px;
  height: 80px;
  border-radius: 10px;
  position: absolute;
  margin: auto;
  right: 0;
  left: 0;
  margin-top: 30px;
}
</style>
