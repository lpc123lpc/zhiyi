<template>
  <div>
    <el-row class="regionTitle">
      <el-col :span=15 style="font-size: 26px" class="el-icon-location-information"> {{ this.region }}</el-col>
      <el-col :span=9>
        <el-button type="primary" plain
                   @click="showVaccineInstitution"
                   class="el-icon-view"
                   id="vaccine-institution-button"> 接种机构
        </el-button>
        <el-button type="primary" plain @click="goMap">查看地图</el-button>
        <el-button type="primary" plain @click="goTravelAdvice">查看出行建议</el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span=50>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span class="title">感染情况</span>
          </div>
          <div class="el-card__body">
            <div class="text item">现有确诊：
              {{ this.data.infect.nowConfirm < 0 ? '暂未收录' : this.data.infect.nowConfirm }}
            </div>
            <div class="text item">累计确诊：
              {{ this.data.infect.totalConfirm < 0 ? '暂未收录' : this.data.infect.totalConfirm }}
            </div>
            <div class="text item">累计治愈：
              {{ this.data.infect.cured < 0 ? '暂未收录' : this.data.infect.cured }}
            </div>
            <div class="text item">累计死亡：
              {{ this.data.infect.dead < 0 ? '暂未收录' : this.data.infect.dead }}
            </div>
            <div class="text item">感染率：
              {{ this.data.infect.coverage < 0 ? '暂未收录' : (this.data.infect.coverage * 100 + '%') }}
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span=50>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span class="title">接种情况</span>
          </div>
          <div class="el-card__body">
            <div class="text item">接种人数：
              {{ this.data.vaccine.vaccined < 0 ? '暂未收录' : this.data.vaccine.vaccined }}
            </div>
            <div class="text item">每百人接种量：
              {{ this.data.vaccine.coverage < 0 ? '暂未收录' : this.data.vaccine.coverage }}
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <div id="vaccineInstitution" style="display: none">
      <div class="regionTitle" style="font-size: 24px">
        <i class="el-icon-office-building"> 接种机构</i>
      </div>
      <vaccine-institution v-bind:data="this.vaccineData"></vaccine-institution>
    </div>
  </div>
</template>

<script>
import vaccineInstitution from "./VaccineInstitution";

export default {
  name: "SearchPage",
  props: [
    'region',
    'data',
    'mapRegion',
    'vaccineData'
  ],
  components: {
    'vaccine-institution': vaccineInstitution
  },
  mounted() {
    if (this.mapRegion.value === 0) {
      document.getElementById('vaccine-institution-button').style.display = 'none'
    }
  },
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
    showVaccineInstitution() {
      document.getElementById('vaccineInstitution').style.display = 'block'
    }
  }
}
</script>

<style scoped>
@import "../assets/css/searchPage.css";
</style>
