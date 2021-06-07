<template>
  <el-card class="box-card" shadow="always" id="card-head-bar">
    <el-row>
      <div class="vaccine-add">+{{ vaccine_sum_add }}</div>
    </el-row>
    <el-row>
      <el-col :span="12">
        <div class="vaccine-sum">累计接种{{ vaccine_sum }}</div>
      </el-col>
      <el-col :span="12">
        <div class="vaccine-sum">每百人接种{{ vaccine_cover }}剂</div>
      </el-col>
      <!--<el-col :span="8"><div class="vaccine-sum-add">+{{vaccine_cover_add}}</div></el-col>-->
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
  created() {
    this.getVaccineSum()
    this.getVaccineSumAdd()
    this.getVaccineCover()
    // this.getVaccineCoverAdd()
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
    getVaccineSum() {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineHomeHeadbar/vaccineSum').then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum = data.value
        })
      })
    },
    getVaccineSumAdd() {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineHomeHeadbar/vaccineSumAdd').then(function (response) {
        response.json().then((data) => {
          that.vaccine_sum_add = data.value
        })
      })
    },
    getVaccineCover() {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineHomeHeadbar/vaccineCover').then(function (response) {
        response.json().then((data) => {
          that.vaccine_cover = data.value
        })
      })
    },
    getVaccineCoverAdd() {
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
.vaccine-sum {
  font-size: 10px;
}

.vaccine-add {
  font-size: 5px;
  margin-left: 25px;
}

.box-card {
  width: 180px;
  height: 65px;
  border-radius: 10px;
  position: absolute;
  margin: auto;
  right: 0;
  left: 0;
  margin-top: 30px;
}
</style>
