<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
  </el-container>
</template>

<script>
import header from '../components/Header.vue'
export default {
  name: 'Feedback',
  components: { // 定义组件
    'wbc-nav': header
  }
}
</script>

<style scoped>

</style>
