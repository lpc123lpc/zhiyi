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
        <div class="title">
          <i class="el-icon-edit"> 请为我们平台留下您的使用反馈&建议</i>
        </div>
        <div id="feed-back-div" style="margin-left: 250px; margin-top: 50px">
          <feed-back-content></feed-back-content>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import vueHeader from '../../components/pc/PageHeader.vue'
import feedBackInput from '../../components/pc/FeedBackInput.vue'
import vaccineSidebar from '../../components/pc/VaccineSidebar.vue'
import infectSidebar from '../../components/pc/InfectSidebar.vue'

export default {
  name: 'Feedback',
  components: { // 定义组件
    'wbc-nav': vueHeader,
    'vaccine-sidebar': vaccineSidebar,
    'infect-sidebar': infectSidebar,
    'feed-back-content': feedBackInput
  },
  methods: {
    set_left() {
      const elMain = document.getElementById('my-el-main')
      // console.log(elMain.offsetWidth)
      const feedBackInput = document.getElementById('feed-back-div')
      feedBackInput.style.setProperty('margin-left', elMain.offsetWidth / 2 - 350 + 'px')
    }
  },
  mounted() {
    this.set_left()
  }
}
</script>

<style scoped>
.title {
  margin-top: 50px;
  margin-left: 60px;
  font-size: 26px;
}
</style>
