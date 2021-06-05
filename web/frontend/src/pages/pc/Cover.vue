<template>
  <!--  <el-container>-->
  <!--  <el-header></el-header>-->
  <!--  <el-main>-->
  <!--    <div class="block" style="text-align: center">-->
  <!--      <el-image src='../../../static/image/Cover.png'></el-image>-->
  <!--    </div>-->
  <!--    <div style="text-align: center">-->
  <!--      <el-button type="primary" @click="goHome()" plain style="height: 80px;width: 300px;font-size: 30px">开始</el-button>-->
  <!--    </div>-->
  <!--  </el-main>-->
  <!--  <el-footer>-->
  <!--    <div style="text-align: center">-->
  <!--      <el-link type="info" href="https://beian.miit.gov.cn/">京ICP备2021014159号</el-link>-->
  <!--    </div>-->
  <!--  </el-footer>-->
  <!--</el-container>-->
  <div>
    <!--    <div class="image-menu-item">-->
    <!--      <el-image src='../../../static/image/Cover.png'></el-image>-->
    <!--    </div>-->
    <el-row style="margin-bottom: 60px">
      <el-col :span="2">
        <img src='../../../static/image/top-icon.jpg' style="height: 100px"/>
      </el-col>
      <el-col :span="22" class="title">
        <span>知疫</span>
      </el-col>
    </el-row>
    <el-carousel
      :interval="2000"
      type="card"
      class="carousel">
      <el-carousel-item v-for="(item, index) in swiperList" :key="index" class="el-carousel__item">
        <img :src="item.picImg"/>
      </el-carousel-item>
    </el-carousel>
    <div style="text-align: center">
      <el-button type="primary" @click="goHome()" plain class="button">开始</el-button>
    </div>
    <el-footer>
      <div style="text-align: center; margin-top: 5px">
        <el-link type="info" href="https://beian.miit.gov.cn/">京ICP备2021014159号</el-link>
      </div>
    </el-footer>
  </div>
</template>

<script>
import {swiperList} from "../../assets/js/swiper";

export default {
  name: 'Cover',
  data() {
    return {
      swiperList: []
    }
  },
  created() {
    this.swiperList = swiperList
  },
  // mounted() {
  //   document.body.style.backgroundColor = 'rgba(167,219,255,0.64)'
  // },
  // beforeDestroy() {
  //   document.querySelector('body').removeAttribute('style')
  // },
  methods: {
    goHome() {
      this.$router.push({path: `/Home`})
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/cover.css";
</style>
