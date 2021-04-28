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
import vaccineHomeHeadbar from '../components/VaccineHomeHeadbar.vue'
export default {
  name: 'VaccineHome',
  data () { // 选项 / 数据
    return {
    }
  },
  methods: { // 事件处理器
    infect_info () {
      this.$router.replace('/VaccineDetail')
    }
  },
  components: { // 定义组件
    'wbc-nav': header,
    'home-info': vaccineHomeHeadbar
  },
  created () { // 生命周期函数

  }
}
</script>

<style scoped>

</style>
