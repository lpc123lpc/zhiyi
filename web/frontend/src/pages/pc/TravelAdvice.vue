<template>
  <el-container>
  <el-header>
    <wbc-nav></wbc-nav>
  </el-header>
  <el-container>
        <el-aside width="400px">
          <vaccine-sidebar v-bind:vaccine_header_title="'疫苗接种'"></vaccine-sidebar>
          <infect-sidebar v-bind:infect_header_title="'感染情况'"></infect-sidebar>
        </el-aside>
        <el-main id="my-el-main">
          <div style="float: right" v-show="show">
            <el-button type="primary" plain @click="back()">返回</el-button>
          </div>
          <travel-advice-content></travel-advice-content>
        </el-main>
      </el-container>
  </el-container>
</template>

<script>
import vueHeader from '../../components/pc/PageHeader.vue'
import vaccineSidebar from '../../components/pc/VaccineSidebar.vue'
import infectSidebar from '../../components/pc/InfectSidebar.vue'
import travelAdviceContent from '../../components/pc/TravelAdviceCom.vue'
export default {
  name: 'TravelAdvice',
  components: {
    'wbc-nav': vueHeader,
    'vaccine-sidebar': vaccineSidebar,
    'infect-sidebar': infectSidebar,
    'travel-advice-content': travelAdviceContent
  },
  data() {
    return {
      show: this.$route.params.region !== '\'\''
    }
  },
  methods: {
    set_left () {
      const elMain = document.getElementById('my-el-main')
      // console.log(elMain.offsetWidth)
      const feedBackInput = document.getElementById('feed-back-div')
      feedBackInput.style.setProperty('margin-left', elMain.offsetWidth / 2 - 350 + 'px')
    },
    back() {
      this.$router.go(-1)
    }
  },
  mounted () {
    // this.set_left()
  }
}
</script>

<style scoped>

</style>
