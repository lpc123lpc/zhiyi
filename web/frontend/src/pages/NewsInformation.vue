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

        </el-main>
      </el-container>
  </el-container>
</template>

<script>
import vueHeader from '../components/PageHeader.vue'
import vaccineSidebar from '../components/VaccineSidebar.vue'
import infectSidebar from '../components/InfectSidebar.vue'
export default {
  name: 'NewsInformation',
  components: { // 定义组件
    'wbc-nav': vueHeader,
    'vaccine-sidebar': vaccineSidebar,
    'infect-sidebar': infectSidebar
  },
  methods: {
    set_left () {

      const elMain = document.getElementById('my-el-main')
      // console.log(elMain.offsetWidth)
      const feedBackInput = document.getElementById('feed-back-div')
      feedBackInput.style.setProperty('margin-left', elMain.offsetWidth / 2 - 350 + 'px')
    }
  },
  mounted () {
    this.set_left()
  }
}
</script>

<style scoped>

</style>
