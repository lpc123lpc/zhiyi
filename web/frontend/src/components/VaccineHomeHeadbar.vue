<template>
  <el-card class="box-card" shadow="always">
    <el-row>
      <el-col :span="8"><div class="vaccine-sum">累计接种{{vaccine_sum}}</div></el-col>
      <el-col :span="4"><div class="vaccine-sum-add">+{{vaccine_sum_add}}</div></el-col>
      <el-col :span="4"><div class="vaccine-sum">覆盖率{{vaccine_cover}}</div></el-col>
      <el-col :span="8"><div class="vaccine-sum-add">+{{vaccine_cover_add}}</div></el-col>
    </el-row>
  </el-card>
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
  mounted () {
    this.getVaccineSum()
    this.getVaccineSumAdd()
    this.getVaccineCover()
    this.getVaccineCoverAdd()
  },
  methods: {
    getVaccineSum () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineHomeHeadbar/vaccineSum').then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum = data
        })
      })
    },
    getVaccineSumAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineHomeHeadbar/vaccineSumAdd').then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum_add = data
        })
      })
    },
    getVaccineCover () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineHomeHeadbar/vaccineCover').then(function (response) {
        response.json().then((data) => {
          that.vaccine_cover = data
        })
      })
    },
    getVaccineCoverAdd () {
      var that = this
      fetch('http://127.0.0.1:5000/vaccineHomeHeadbar/vaccineCoverAdd').then(function (response) {
        response.json().then((data) => {
          that.vaccine_cover_add = data
        })
      })
    }
  }
}
</script>

<style scoped>
.vaccine-sum {
  font-size: 20px;
  text-align: right;
  margin-top: 3px;
}
.vaccine-sum-add {
  font-size: 16px;
  margin-top: 8px;
  margin-left: 5px;
}

.box-card {
  width: 1600px;
  height: 75px;
  border-radius: 10px;
  position: absolute;
  margin: auto;
  right: 0;
  left: 0;
  margin-top: 50px;
}
</style>
