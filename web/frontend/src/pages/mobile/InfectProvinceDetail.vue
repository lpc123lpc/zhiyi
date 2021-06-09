<template>
  <div>
    <page-header v-bind:header_title="'感染情况'"></page-header>
    <!--<van-button
      class="button"
      type="default" plain
      size="mini"
      color="#8cc4ff"
      @click.native="back()"
    >返回</van-button>-->
    <van-cell style="align: center; margin-top: 10px">
      <infect-detail-province-map v-bind:province="provinceMsg"
                                  v-bind:provinceMapInfectionData="provinceMapInfectionDataMsg"></infect-detail-province-map>
      <mobile-province-infection-chart style="margin-top: 10px"></mobile-province-infection-chart>
    </van-cell>
    <van-button color="#8cc4ff" plain block @click="back" class="button-item" id="button-item-id-1">返回</van-button>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader'
import infectDetailProvinceMap from '../../components/mobile/ProvinceMapInfection.vue'
import {mixin} from '../../mixins'
import mobileProvinceInfectionChart from '../../components/mobile/ProvinceInfectionChartMobile.vue'
export default {
  name: 'InfectProvinceDetail',
  components: { // 定义组件
    'page-header': pageHeader,
    'infect-detail-province-map': infectDetailProvinceMap,
    'mobile-province-infection-chart': mobileProvinceInfectionChart
  },
  data () { // 选项 / 数据
    return {
      provinceMsg: '',
      provinceMapInfectionDataMsg: ''
    }
  },
  mixins: [mixin],
  methods: { // 事件处理器
    getProvinceMsg () {
      var that = this
      that.provinceMsg = this.$route.params.province
    },
    getProvinceInfectionDataMsg () {
      var that = this
      fetch('http://81.70.134.96:5000/infectDetail/provinceMapInfectionDataMsg/' + this.$route.params.province).then(function (response) {
        response.json().then((data) => {
          that.judgeDataExistMobile(data)
          that.provinceMapInfectionDataMsg = data
        })
      })
    },
    back () {
      this.$router.go(-1)
    },
    set_button_length () {
      const button1 = document.getElementById('button-item-id-1')
      button1.style.setProperty('width', window.screen.width / 10 * 9 + 'px')
      button1.style.setProperty('margin-left', window.screen.width / 20 + 'px')
    }
  },
  created () {
    this.getProvinceMsg()
    this.getProvinceInfectionDataMsg()
  },
  mounted () {
    this.set_button_length()
  }
}
</script>

<style scoped>
.button {
  position: absolute;
  margin-top: 20px;
  margin-left: 330px;
  font-size: 8px;
}
.button-item {
  margin-bottom: 10px;
  font-size: medium;
  letter-spacing: 2px;
}
</style>
