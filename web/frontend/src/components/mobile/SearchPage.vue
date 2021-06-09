<template>
  <div>
    <div class="title">
      <van-icon name="location-o"> {{ this.region }}</van-icon>
    </div>
    <van-collapse v-model="activeNames">
      <van-collapse-item title="感染情况" name="1">
        <div class="list-item">现有确诊:
          {{ this.data.infect.nowConfirm < 0 ? '暂未收录' : this.data.infect.nowConfirm }}
        </div>
        <div class="list-item">累计确诊:
          {{ this.data.infect.totalConfirm < 0 ? '暂未收录' : this.data.infect.totalConfirm }}
        </div>
        <div class="list-item">累计治愈：
          {{ this.data.infect.cured < 0 ? '暂未收录' : this.data.infect.cured }}
        </div>
        <div class="list-item">累计死亡：
          {{ this.data.infect.dead < 0 ? '暂未收录' : this.data.infect.dead }}
        </div>
        <div class="list-item">感染率：
          {{ this.data.infect.coverage < 0 ? '暂未收录' : (this.data.infect.coverage * 100 + '%') }}
        </div>
      </van-collapse-item>
      <van-collapse-item title="接种情况" name="2">
        <div class="list-item">接种人数：
          {{ this.data.vaccine.vaccined < 0 ? '暂未收录' : this.data.vaccine.vaccined }}
        </div>
        <div class="list-item">每百人接种量：
          {{ this.data.vaccine.coverage < 0 ? '暂未收录' : this.data.vaccine.coverage }}
        </div>
      </van-collapse-item>
      <van-collapse-item name="3" title="接种机构" v-show="show">
        <vaccine-institution v-bind:data="this.vaccineData"></vaccine-institution>
      </van-collapse-item>
    </van-collapse>
    <van-button
      color="#8cc4ff"
      plain block
      @click="goMap"
      class="button-item"
      ref="buttonItemId1">查看地图
    </van-button>
    <van-button
      color="#8cc4ff"
      plain block
      @click="goTravelAdvice"
      class="button-item"
      ref="buttonItemId2">查看出行建议
    </van-button>
  </div>
</template>

<script>
import vaccineInstitution from './VaccineInstitution'

export default {
  name: 'SearchPage',
  props: [
    'region',
    'data',
    'vaccineData'
  ],
  data () {
    return {
      mapRegion: {},
      activeNames: [],
      show: true
    }
  },
  components: {
    'vaccine-institution': vaccineInstitution
  },
  created () {
    this.getMapRegion()
  },
  watch: {
    region () {
      this.mapRegion = this.getMapRegion()
      this.showVaccineInstitution()
    }
  },
  mounted () {
    // this.set_button_length()
    // console.log(this.$route.query.data)
    this.showVaccineInstitution()
  },
  methods: {
    getMapRegion () {
      var regions = this.region.split('  ')
      // region取 0：国家/ 1：省
      if (regions[0] === '中国' && regions.length > 1) {
        return {region: regions[1], value: 1}
      } else {
        return {region: regions[0], value: 0}
      }
    },
    showVaccineInstitution () {
      // console.log(this.region.split('  ').length)
      if (this.region.split('  ').length < 3) this.show = false
      else this.show = true
    },
    goMap () {
      if (this.mapRegion.value === 0) { // 国家
        this.$router.push({path: `/InfectDetail/${this.mapRegion.region}`})
      } else { // 省（中国）
        this.$router.push({path: `/InfectProvinceDetail/${this.mapRegion.region}`})
      }
    },
    goTravelAdvice () {
      this.$router.push({path: `/TravelAdvice/${this.region}`, query: {data: this.$route.query.data}})
    },
    set_button_length () {
      // const button1 = this.getElementById('button-item-id-1')
      // const button2 = this.getElementById('button-item-id-2')
      this.$refs.buttonItemId1.style.setProperty('width', window.screen.width / 10 * 9 + 'px')
      this.$refs.buttonItemId2.style.setProperty('width', window.screen.width / 10 * 9 + 'px')
      this.$refs.buttonItemId1.style.setProperty('margin-left', window.screen.width / 20 + 'px')
      this.$refs.buttonItemId2.style.setProperty('margin-left', window.screen.width / 20 + 'px')
    }
  }
}
</script>

<style scoped>

.title {
  margin: 15px 15px;
  font-size: 18px;
  color: black;
}

.list-item {
  font-size: 14px;
  margin-bottom: 10px;
}

.button-item {
  font-size: medium;
  letter-spacing: 2px;
  width: 90%;
  margin: 10px auto;
}

</style>
