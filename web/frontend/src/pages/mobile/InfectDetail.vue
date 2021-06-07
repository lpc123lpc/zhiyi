<template>
  <div>
    <page-header v-bind:header_title="'感染情况'"></page-header>
    <van-button
      class="button"
      type="default" plain
      size="mini"
      color="#8cc4ff"
      @click.native="back()"
    >返回</van-button>
    <div style="align: center; margin-top: 20px">
      <infect-detail-country-map v-bind:country="countryMsg"
                                 v-bind:countryMapInfectionData="countryMapInfectionDataMsg"></infect-detail-country-map>
    </div>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import infectDetailCountryMap from '../../components/mobile/CountryMapInfection.vue'
import {mixin} from '../../mixins'

export default {
  name: 'InfectDetail',
  components: { // 定义组件
    'page-header': pageHeader,
    'infect-detail-country-map': infectDetailCountryMap,
  },
  mixins: [mixin],
  data() { // 选项 / 数据
    return {
      countryMsg: '',
      countryMapInfectionDataMsg: ''
    }
  },
  methods: { // 事件处理器
    getCountryMsg() {
      var that = this
      that.countryMsg = this.$route.params.country
    },
    getCountryInfectionDataMsg() {
      var that = this
      fetch('http://81.70.134.96:5000/infectDetail/countryMapInfectionDataMsg/' + this.$route.params.country).then(function (response) {
        response.json().then((data) => {
          that.judgeDataExist(data)
          that.countryMapInfectionDataMsg = data
        })
      })
    },
    back() {
      console.log("come in button click")
      this.$router.go(-1)
    }
  },
  created() {
    this.getCountryMsg()
    this.getCountryInfectionDataMsg()
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
</style>
