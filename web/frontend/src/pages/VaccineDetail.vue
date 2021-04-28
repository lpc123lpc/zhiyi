<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
    <el-container>
      <el-aside width="600px">
        <vaccine-detail-sidebar v-bind:vaccine_header_title="'疫苗接种'"></vaccine-detail-sidebar>
      </el-aside>
      <el-main>Main</el-main>
    </el-container>
  </el-container>
</template>

<script>
import header from '../components/Header.vue'
import vaccineDetailSidebar from '../components/VaccineDetailSidebar.vue'
export default {
  name: 'VaccineDetail',
  components: { // 定义组件
    'wbc-nav': header,
    'vaccine-detail-sidebar': vaccineDetailSidebar
  }
}
</script>

<style scoped>

</style>
