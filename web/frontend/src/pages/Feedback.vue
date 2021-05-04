<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
    <el-container>
          <el-aside width="450px">
            <vaccine-sidebar v-bind:vaccine_header_title="'疫苗接种'"></vaccine-sidebar>
            <infect-sidebar v-bind:infect_header_title="'感染情况'"></infect-sidebar>
          </el-aside>
          <el-main>
            <div style="margin-left: 350px; margin-top: 150px">
              <feed-back></feed-back>
            </div>
          </el-main>
        </el-container>
  </el-container>
</template>

<script>
import header from '../components/Header.vue'
import feedBackInput from '../components/FeedBackInput.vue'
import vaccineSidebar from '../components/VaccineSidebar.vue'
import infectSidebar from '../components/InfectSidebar.vue'
export default {
  name: 'Feedback',
  components: { // 定义组件
    'wbc-nav': header,
    'vaccine-sidebar': vaccineSidebar,
    'infect-sidebar': infectSidebar,
    'feed-back': feedBackInput
  }
}
</script>

<style scoped>

</style>
