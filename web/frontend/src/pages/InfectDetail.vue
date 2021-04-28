<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
    <el-container>
      <el-aside width="600px">
        <infect-detail-sidebar v-bind:vaccine_header_title="'疫苗接种'"></infect-detail-sidebar>
      </el-aside>
      <el-main>Main</el-main>
    </el-container>
  </el-container>
</template>

<script>
import header from '../components/Header.vue'
import infectDetailSidebar from '../components/InfectDetailSidebar.vue'
export default {
  name: 'InfectDetail',
  components: { // 定义组件
    'wbc-nav': header,
    'infect-detail-sidebar': infectDetailSidebar
  }
}
</script>

<style scoped>

</style>
