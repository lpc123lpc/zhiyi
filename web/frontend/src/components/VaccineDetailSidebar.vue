<template>
  <el-card class="box-card" shadow="always">
    <!--<div slot="header" class="clearfix">
      <span>卡片名称</span>
    </div>
    <div v-for="o in 4" :key="o" class="text item">
      {{'列表内容 ' + o }}
    </div>-->
    <div slot="header" class="clearfix">
      <span style="font-size: 20px">疫苗接种</span>
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
    <el-divider></el-divider>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      {{vaccine_cover_add}}
    </div>
    <div class="today-item">
      覆盖率
    </div>
    <div class="today-item">
      {{vaccine_cover}}
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'VaccineDetailSidebar',
  props: ['country'],
  data: function () {
    return {
      vaccine_sum: '',
      vaccine_sum_add: '',
      vaccine_cover: '',
      vaccine_cover_add: ''
    }
  },
  mounted () {
    this.vaccine_sum = this.getVaccineSum()
    this.vaccine_sum_add = this.getVaccineSumAdd()
    this.vaccine_cover = this.getVaccineCover()
    this.vaccine_cover_add = this.getVaccineCoverAdd()
  },
  methods: {
    getVaccineSum () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineDetailSidebar/vaccineSum/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum = data
        })
      })
    },
    getVaccineSumAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineDetailSidebar/vaccineSumAdd/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum_add = data
        })
      })
    },
    getVaccineCover () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineDetailSidebar/vaccineCover/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.vaccine_cover = data
        })
      })
    },
    getVaccineCoverAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineDetailSidebar/vaccineCoverAdd/' + this.country).then(function (response) {
        response.json().then((data) => {
          that.vaccine_cover_add = data
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
