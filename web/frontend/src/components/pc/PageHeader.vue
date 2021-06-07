<template>
  <div>
    <div class="image-menu-item" @click="goHome()">
      <el-image fit="contain" src='../../../static/image/111.png' class="image-item"></el-image>
    </div>
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#ffffff"
      text-color="#8cc4ff"
      active-text-color="#409eff"
      router
      :default-active="path">

      <el-menu-item index="/Home" class="nav-menu-item">国家列表</el-menu-item>
      <el-menu-item index="/VaccineHome" class="nav-menu-item">疫苗接种</el-menu-item>
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
      <el-menu-item index="/TravelAdvice/''" class="nav-menu-item">出行建议</el-menu-item>
      <el-menu-item index="/NewsInformation" class="nav-menu-item">新闻资讯</el-menu-item>
      <el-menu-item index="/Feedback" class="nav-menu-item">反馈&建议</el-menu-item>
      <svg class="icon" aria-hidden="true" @click="showDataSource()">
        <use xlink:href="#icon-question"></use>
      </svg>
      <el-container index="6" class="input-container">
        <search-bar></search-bar>
      </el-container>
    </el-menu>
  </div>
</template>

<script>
import SearchBar from './SearchBar'

export default {
  name: 'PageHeader',
  components: {
    'search-bar': SearchBar
  },
  data () {
    return {
      activeIndex: '1',
      input: '',
      path: '',
      dataSource: ['全部数据来源：腾讯新闻、Our World in Data、约翰',
        '              霍普金斯大学网站',
        '每日凌晨3:00进行数据更新，届时带来不便，敬请谅解']
    }
  },
  methods: {
    goHome () {
      this.$router.push({path: `/Home`})
    },
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    onRouteChanged () {
      let that = this
      var posVaccine = that.$route.path.search('/VaccineDetail')
      if (posVaccine === -1) {
        var posInfect = that.$route.path.search('/InfectDetail')
        if (posInfect === -1) {
          var posProvinceInfect = that.$route.path.search('/InfectProvinceDetail')
          if (posProvinceInfect === -1) {
            if (that.$route.path === '/') {
              that.path = '/Home'
            } else {
              that.path = that.$route.path
            }
          } else {
            that.path = '/InfectHome'
          }
        } else {
          that.path = '/InfectHome'
        }
      } else {
        that.path = '/VaccineHome'
      }
    },
    showDataSource () {
      const data = []
      const h = this.$createElement
      for (let i in this.dataSource) {
        data.push(h('p', null, this.dataSource[i]))
      }
      this.$alert(h('pre', null, data), '数据来源', {
        // customClass: 'message-alert'
      }).catch(() => {
      }) // 注意这里，这里是重点！！！
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
.icon {
  width: 20px;
  height: 20px;
  margin-top: 20px;
  fill: #56aafdc4;
  overflow: hidden;
  outline: none
}

.input-container {
  /*position: absolute;*/
  width: 300px;
  margin-top: 10px;
  float: right;
}

.el-menu-demo {
  height: 60px;
  margin-left: 170px;
  padding-right: 20px;
}

.nav-menu-item {
  width: 130px;
  margin-left: 10px;
  margin-right: 10px;
  text-align: center;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: medium;
}

.nav-menu-item:hover {
  background-color: #ffffff !important;
  color: #409eff !important;
}

.image-item {
  height: 70px;
  margin-top: -8px;
}

.image-menu-item {
  position: absolute;
  width: 150px;
  margin-left: 5px;
  margin-right: 10px;
}

.image-menu-item img {
  width: 100%;
}

/* .message-alert {
  word-break: break-all !important;
  white-space: pre;
} */
</style>
