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
      <infect-detail-country-map v-bind:country="countryMsg"
                                 v-bind:countryMapInfectionData="countryMapInfectionDataMsg"></infect-detail-country-map>
    </van-cell>
    <van-button color="#8cc4ff" hairline plain block @click="back" class="button-item" id="button-item-id-1">返回</van-button>
    <div>
      <mobile-country-infection></mobile-country-infection>
    </div>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import infectDetailCountryMap from '../../components/mobile/CountryMapInfection.vue'
import {mixin} from '../../mixins'
import MobileCountryInfection from '../../components/mobile/MobileCountryInfection'

export default {
  name: 'InfectDetail',
  components: {
    MobileCountryInfection, // 定义组件
    'page-header': pageHeader,
    'infect-detail-country-map': infectDetailCountryMap
  },
  mixins: [mixin],
  data () { // 选项 / 数据
    return {
      countryMsg: '',
      countryMapInfectionDataMsg: ''
    }
  },
  methods: { // 事件处理器
    getCountryMsg () {
      var that = this
      that.countryMsg = this.$route.params.country
    },
    getCountryInfectionDataMsg () {
      var that = this
      fetch('http://81.70.134.96:5000/infectDetail/countryMapInfectionDataMsg/' + this.$route.params.country).then(function (response) {
        response.json().then((data) => {
          that.judgeDataExist(data)
          that.countryMapInfectionDataMsg = data
        })
      })
    },
    back () {
      // alert('come in button click')
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
    this.getCountryInfectionDataMsg()
  },
  mounted () {
    this.set_button_length()
  }
}
</script>

<style scoped>

</style>
