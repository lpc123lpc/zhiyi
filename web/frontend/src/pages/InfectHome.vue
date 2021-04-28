<template>
  <el-container>
    <el-header>
      <wbc-nav></wbc-nav>
    </el-header>
    <el-main>
      <div style="align: center;">
        <home-info></home-info>
      </div>
      <div style="align: center;">
        <el-button type="info" @click="infect_info">详情页面</el-button>
      </div>
    </el-main>
    <!--<div class="container">
        <el-row  :gutter="30">
            <el-col :sm="24" :md="16" style="transition:all .5s ease-out;margin-bottom:30px;">
                <wbc-sharelist></wbc-sharelist>
            </el-col>
            <el-col :sm="24"  :md="8" >
                <wbc-rightlist></wbc-rightlist>
            </el-col>
        </el-row>
    </div>
    <wbc-footer></wbc-footer>-->
  </el-container>
</template>

<script>
import header from '../components/Header.vue'
import infectHomeHeadbar from '../components/InfectHomeHeadbar.vue'
export default {
  name: 'InfectHome',
  components: { // 定义组件
    'wbc-nav': header,
    'home-info': infectHomeHeadbar
  },
  methods: {
    infect_info () {
      this.$router.replace('/InfectDetail')
    }
  }
}
</script>

<style scoped>

</style>
