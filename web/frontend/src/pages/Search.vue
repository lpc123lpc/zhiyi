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
        <search-page v-bind:region="this.region"
                     v-bind:data="{infect: { nowConfirm: 10, totalConfirm: 10, cured: 10, dead: 10, coverage:	0.1},
                                                  vaccine: { vaccined: 10, coverage: 0.1 }}"
                     v-bind:map-region="{ region: '北京', value: 1 }"
        ></search-page>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import vueHeader from '../components/PageHeader.vue'
import vaccineSidebar from '../components/VaccineSidebar.vue'
import infectSidebar from '../components/InfectSidebar.vue'
import searchPage from '../components/SearchPage'

export default {
  name: 'Search',
  components: { // 定义组件
    'wbc-nav': vueHeader,
    'vaccine-sidebar': vaccineSidebar,
    'infect-sidebar': infectSidebar,
    'search-page': searchPage
  },
  data() {
    return {
      region: ''
    }
  },
  mounted() {
    this.region = this.$route.params.region
    this.set_left()
  },
  methods: {
    set_left() {
      const elMain = document.getElementById('my-el-main')
      // console.log(elMain.offsetWidth)
      const feedBackInput = document.getElementById('feed-back-div')
      feedBackInput.style.setProperty('margin-left', elMain.offsetWidth / 2 - 350 + 'px')
    }
  }
}
</script>

<style scoped>

</style>
