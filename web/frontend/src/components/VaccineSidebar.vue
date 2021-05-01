<template>
  <el-card class="box-card" shadow="always">
    <!--<div slot="header" class="clearfix">
      <span>卡片名称</span>
    </div>
    <div v-for="o in 4" :key="o" class="text item">
      {{'列表内容 ' + o }}
    </div>-->
    <div slot="header" class="clearfix">
      <span style="font-size: 20px">{{vaccine_header_title}}</span>
    </div>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      {{vaccine_sum_add}}
    </div>
    <div class="today-item">
      累计接种
    </div>
    <div class="today-item">
      {{vaccine_sum}}
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'VaccineSidebar',
  props: {
    vaccine_header_title: {
      type: String,
      default: ''
    }
  },
  data: function () {
    return {
      vaccine_sum: '',
      vaccine_sum_add: ''
    }
  },
  mounted () {
    this.vaccine_sum = this.getVaccineSum()
    this.vaccine_sum_add = this.getVaccineSumAdd()
  },
  methods: {
    getVaccineSum () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineSidebar/vaccineSum').then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum = data
        })
      })
    },
    getVaccineSumAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineSidebar/vaccineSumAdd').then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum_add = data
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
  width: 480px;
  margin-left: 50px;
  margin-top: 50px;
  border-radius: 20px;
}
</style>
