<template>
  <van-nav-bar class="mobile-header" id="mobile-header-id">
    <template #left>
      <van-image fit="contain" src='../../../static/image/111.png' class="image-item" id="image-item-id"></van-image>
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
      <van-icon name="wap-nav" size="20" class="icon-item" id="icon-item-id"/>
    </template>
    <!--<mt-field v-model="input" placeholder="请输入内容" slot="right"></mt-field>-->
    <!--<mt-button icon="search" slot="right" class="search-button" id="search-button-id"></mt-button>
    <mt-button icon="more" slot="right"></mt-button>-->
  </van-nav-bar>
</template>

<script>
import { Toast } from 'vant';
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
      input: ''
    }
  },
  mounted () {
    // this.set_height()
  },
  methods: {
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
.icon-item {

}
</style>
