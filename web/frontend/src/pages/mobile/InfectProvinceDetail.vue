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
      <infect-detail-province-map v-bind:province="provinceMsg"
                                  v-bind:provinceMapInfectionData="provinceMapInfectionDataMsg"></infect-detail-province-map>
    </div>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader'
import infectDetailProvinceMap from '../../components/mobile/ProvinceMapInfection.vue'
import {mixin} from '../../mixins'

export default {
  name: 'InfectProvinceDetail',
  components: { // 定义组件
    'page-header': pageHeader,
    'infect-detail-province-map': infectDetailProvinceMap,
  },
  data() { // 选项 / 数据
    return {
      provinceMsg: '',
      provinceMapInfectionDataMsg: ''
    }
  },
  mixins: [mixin],
  methods: { // 事件处理器
    getProvinceMsg() {
      var that = this
      that.provinceMsg = this.$route.params.province
    },
    getProvinceInfectionDataMsg() {
      var that = this
      fetch('http://81.70.134.96:5000/infectDetail/provinceMapInfectionDataMsg/' + this.$route.params.province).then(function (response) {
        response.json().then((data) => {
          that.judgeDataExist(data)
          that.provinceMapInfectionDataMsg = data
        })
      })
    },
    back() {
      this.$router.go(-1)
    }
  },
  created() {
    this.getProvinceMsg()
    this.getProvinceInfectionDataMsg()
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
