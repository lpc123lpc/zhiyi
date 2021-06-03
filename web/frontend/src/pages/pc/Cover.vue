<template>
  <el-container>
  <el-header></el-header>
  <el-main>
    <div class="block" style="text-align: center">
      <el-image src='../../../static/image/Cover.png'></el-image>
    </div>
    <div style="text-align: center">
      <el-button type="primary" @click="goHome()" plain style="height: 80px;width: 300px;font-size: 30px">开始</el-button>
    </div>
  </el-main>
  <el-footer>
    <div style="text-align: center">
      <el-link type="info" href="https://beian.miit.gov.cn/">京ICP备2021014159号</el-link>
    </div>
  </el-footer>
</el-container>
</template>

<script>
export default {
  name: 'Cover',
  methods: {
    goHome () {
      this.$router.push({path: `/Home`})
    }
  }
}
</script>

<style scoped>

</style>
