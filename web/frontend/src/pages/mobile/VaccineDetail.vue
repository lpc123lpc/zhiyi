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
      <vaccine-detail-country-map v-bind:country="countryMsg"
                                  v-bind:countryMapVaccineData="countryMapVaccineDataMsg"></vaccine-detail-country-map>
    </van-cell>
    <van-button color="#8cc4ff" hairline plain block @click="back" class="button-item" id="button-item-id-1">返回</van-button>
    <mobile-country-vaccine></mobile-country-vaccine>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import vaccineDetailCountryMap from '../../components/mobile/CountryMapVaccine.vue'
import {mixin} from '../../mixins'
import MobileCountryVaccine from '../../components/mobile/MobileCountryVaccine';

export default {
  name: 'VaccineDetail',
  components: {
    MobileCountryVaccine, // 定义组件
    'page-header': pageHeader,
    'vaccine-detail-country-map': vaccineDetailCountryMap,
  },
  data () { // 选项 / 数据
    return {
      countryMsg: '',
      countryMapVaccineDataMsg: ''
    }
  },
  mixins: [mixin],
  methods: { // 事件处理器
    getCountryMsg () {
      var that = this
      that.countryMsg = this.$route.params.country
    },
    getCountryMapVaccineDataMsg () {
      var that = this
      fetch('http://81.70.134.96:5000/vaccineDetail/countryMapVaccineDataMsg/' + this.$route.params.country).then(function (response) {
        response.json().then((data) => {
          that.judgeDataExist(data)
          // console.log(data)
          that.countryMapVaccineDataMsg = data
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
    this.getCountryMsg()
    this.getCountryMapVaccineDataMsg()
  },
  mounted () {
    this.set_button_length()
  }
}
</script>

<style scoped>

</style>
