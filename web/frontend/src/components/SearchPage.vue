<template>
  <div>
    <el-row>
      <el-col :span=25 class="regionTitle">{{ this.region }}</el-col>
      <el-col :span=75 class="button-list">
        <el-button type="primary" plain @click="goMap">地图</el-button>
        <el-button type="primary" plain @click="goTravelAdvice">查看出行建议</el-button>
        <el-button type="primary" plain @click="goVaccineInstitution">查看接种机构</el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span=50>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span class="title">感染情况</span>
          </div>
          <div class="el-card__body">
            <div class="text item">现有确诊：{{ this.data.infect.nowConfirm }}</div>
            <div class="text item">累计确诊：{{ this.data.infect.totalConfirm }}</div>
            <div class="text item">累计治愈：{{ this.data.infect.cured }}</div>
            <div class="text item">累计死亡：{{ this.data.infect.dead }}</div>
            <div class="text item">感染率：{{ this.data.infect.coverage * 100 }}%</div>
          </div>
        </el-card>
      </el-col>
      <el-col :span=50>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span class="title">接种情况</span>
          </div>
          <div class="el-card__body">
            <div class="text item">接种人数：{{ this.data.infect.nowConfirm }}</div>
            <div class="text item">每百人接种量：{{ this.data.infect.totalConfirm }}</div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "SearchPage",
  props: [
    'region',
    'data',
    'mapRegion'
  ],
  methods: {
    goMap() {
      if (this.mapRegion.value === 0) { // 国家
        this.$router.push({path: `/InfectDetail/${this.mapRegion.region}`})
      } else {  // 省（中国）
        this.$router.push({path: `/InfectProvinceDetail/${this.mapRegion.region}`})
      }
    },
    goTravelAdvice() {
      this.$router.push({path: `/TravelAdvice/${this.region}`})
    },
    goVaccineInstitution() {
      this.$router.push({path: `/TravelAdvice/${this.region}`})
    }
  }
}
</script>

<style scoped>
@import "../assets/css/searchPage.css";
</style>
