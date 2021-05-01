<template>
  <el-menu
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#ffffff"
    text-color="#8cc4ff"
    active-text-color="#409eff"
    router
    :default-active = "path">

    <el-menu-item index="/Home" class="nav-menu-item" >国家列表</el-menu-item>
    <el-menu-item index="/VaccineHome" class="nav-menu-item" >疫苗接种</el-menu-item>
    <!--<el-submenu index="2">
      <template slot="title">我的工作台</template>
      <el-menu-item index="2-1">选项1</el-menu-item>
      <el-menu-item index="2-2">选项2</el-menu-item>
      <el-menu-item index="2-3">选项3</el-menu-item>
      <el-submenu index="2-4">
        <template slot="title">选项4</template>
        <el-menu-item index="2-4-1">选项1</el-menu-item>
        <el-menu-item index="2-4-2">选项2</el-menu-item>
        <el-menu-item index="2-4-3">选项3</el-menu-item>
      </el-submenu>
    </el-submenu>-->
    <el-menu-item index="/InfectHome" class="nav-menu-item">感染情况</el-menu-item>
    <el-menu-item index="3" class="nav-menu-item">出行建议</el-menu-item>
    <el-menu-item index="4" class="nav-menu-item">新闻资讯</el-menu-item>
    <el-menu-item index="/Feedback" class="nav-menu-item">反馈&建议</el-menu-item>
    <el-container index="6" class="input-container">
      <el-input placeholder="请输入内容" v-model="input" class="input-with-select">
        <el-button slot="append" icon="el-icon-search"></el-button>
      </el-input>
    </el-container>
  </el-menu>
</template>

<script>
export default {
  name: 'header',
  data () {
    return {
      activeIndex: '1',
      input: '',
      path: ''
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    onRouteChanged () {
      let that = this
      var posVaccine = that.$route.path.search('/VaccineDetail')
      if (posVaccine === -1) {
        var posInfect = that.$route.path.search('/InfectDetail')
        if (posInfect === -1) {
          if (that.$route.path === '/') {
            that.path = '/Home'
          } else {
            that.path = that.$route.path
          }
        } else {
          that.path = '/InfectHome'
        }
      } else {
        that.path = '/VaccineHome'
      }
    }
  },
  watch: {
    '$route': 'onRouteChanged'
  },
  created () {
    this.onRouteChanged()
  }
}
</script>

<style scoped>
.input-container {
  /*position: absolute;*/
  width: 300px;
  margin-top: 10px;
  float: right;
}
.el-menu-demo {
  height: 60px;
  padding-right: 20px;
}
.nav-menu-item {
  width: 150px;
  margin-left: 10px;
  margin-right: 10px;
  text-align: center;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font-size: medium;
}
.nav-menu-item:hover {
  background-color: #ffffff !important;
  color: #409eff !important;
}
</style>
