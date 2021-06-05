<template>
  <van-nav-bar class="mobile-header" id="mobile-header-id">
    <template #left>
      <van-image fit="contain" src='../../../static/image/111.png' class="image-item" id="image-item-id" @click="goHome()"></van-image>
    </template>
    <template #title>
      <van-search
        v-model="input"
        placeholder="请输入搜索关键词"
        @search="onSearch"
        class="search-item"
        id="search-item-id">
      </van-search>
    </template>
    <template #right>
      <van-icon name="wap-nav" size="20" class="icon-item" id="icon-item-id-1" v-show="show_nav===false" @click="showNav"/>
      <van-icon name="cross" size="20" class="icon-item" id="icon-item-id-2" v-show="show_nav===true" @click="showNav"/>
      <van-popup v-model="show_nav" position="top" style="top: 51px; height: 308px" :overlay="false" transition="van-fade" class="popup-item" :close-on-popstate="true">
        <van-cell title="国家列表" is-link to="/" class="cell-item"/>
        <van-cell title="疫苗接种" is-link to="/VaccineHome" class="cell-item"/>
        <van-cell title="感染情况" is-link to="/InfectHome" class="cell-item"/>
        <van-cell title="出行建议" is-link to="/TravelAdvice" class="cell-item"/>
        <van-cell title="新闻资讯" is-link to="/NewsInformation" class="cell-item"/>
        <van-cell title="反馈&建议" is-link to="/Feedback" class="cell-item"/>
        <van-cell title="数据来源" :clickable="true" @click="showDialog" class="cell-item"/>
      </van-popup>
      <van-dialog v-model="show_dialog" title="数据来源" confirm-button-text="关闭" confirm-button-color="#8cc4ff" @confirm="handleConfirm" class="dialog-item">
        <div style="margin-left: 2px; margin-right: 2px; margin-top: 10px; font-size: small; color: #000000">全部数据来源：腾讯新闻、Our World in Data、约翰霍普金斯大学网站</div>
        <van-divider style="color: #8cc4ff"/>
        <div style="margin-left: 2px; margin-right: 2px; margin-bottom: 10px; font-size: small; color: #000000">每日凌晨3:00进行数据更新，届时带来不便，敬请谅解</div>
      </van-dialog>
    </template>
    <!--<mt-field v-model="input" placeholder="请输入内容" slot="right"></mt-field>-->
    <!--<mt-button icon="search" slot="right" class="search-button" id="search-button-id"></mt-button>
    <mt-button icon="more" slot="right"></mt-button>-->
  </van-nav-bar>
</template>

<script>
import { Toast } from 'vant'
export default {
  name: 'PageHeader',
  props: {
    header_title: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      show_nav: false,
      show_dialog: false,
      input: ''
    }
  },
  mounted () {
    // this.set_height()
  },
  methods: {
    showNav () {
      if (this.show_nav === false) {
        this.show_nav = true
      } else {
        this.show_nav = false
      }
    },
    showDialog () {
      this.show_dialog = true
    },
    handleConfirm () {
      this.show_dialog = false
    },
    goHome () {
      this.$router.push({path: `/Home`})
    },
    set_height () {
      // const header = document.getElementById('mobile-header-id')
      // const searchButton = document.getElementById('search-button-id')
      // const imageIcon = document.getElementById('image-item-id')
      const searchBar = document.getElementById('search-item-id')
      // const iconMore = document.getElementById('icon-item-id')
      // alert(window.screen.height)
      // header.style.setProperty('height', window.screen.height / 11 + 'px')

      // imageIcon.style.setProperty('height', window.screen.height / 15 + 'px')
      // imageIcon.style.setProperty('width', (window.screen.height / 15) / 358 * 658 + 'px')
      // imageIcon.style.setProperty('margin-top', ((window.screen.height / 11) - (window.screen.height / 15)) / 2 + 'px')
      // searchButton.style.setProperty('margin-right', window.screen.width / 15 + 'px')
      // searchBar.style.setProperty('margin-top', (window.screen.height / 11 - window.screen.height / 15) / 2 + 'px')
      searchBar.style.setProperty('margin-left', (window.screen.width - 100 - 10 - 20) + 'px')

      // iconMore.style.setProperty('size', 500 + 'px')
      // iconMore.style.setProperty('margin-top', window.screen.height / 40 + 'px')
    },
    onSearch (val) {
      Toast(val)
    }
  }
}
</script>

<style scoped>
.mobile-header {
  background-color: #ffffff;
  color: #8cc4ff;
  border-style: solid;
  border-color: #ffffff #ffffff #e6e6e6 #ffffff;
  border-bottom-width: 2px;
}
.image-item {
  height: 36px;
  margin-top: -2px;
  width: 66px;
  margin-left: -8px;
}
.search-item {
  margin-right: 10px;
  height: 36px;
  margin-top: -1px;
  width: 200px;
  margin-left: 20px;
}
.popup-item {
  border-style: solid;
  border-color: #ffffff #ffffff #e6e6e6 #ffffff;
  border-bottom-width: 1px;
}
.cell-item {
  text-align: left;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font-size: medium;
  color: #8cc4ff;
}
.dialog-item {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font-size: medium;
  color: #000000;
}
</style>
