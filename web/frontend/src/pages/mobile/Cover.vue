<template>
  <div id="cover-id">
    <van-image src="../../../static/image/MobileCover.png">
      <template v-slot:loading>
        <van-loading type="spinner" size="20" />
      </template>
    </van-image>
    <van-button color="#8cc4ff" plain block @click="goHome" class="button-item" id="button-item-id-1">开始</van-button>
    <div style="text-align: center; margin-top: 10px">
      <el-link type="info" href="https://beian.miit.gov.cn/">京ICP备2021014159号</el-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cover',
  data () {
    return {
    }
  },
  methods: {
    goHome () {
      this.$router.push({path: `/Home`})
    },
    set_button_length () {
      const button1 = document.getElementById('button-item-id-1')
      button1.style.setProperty('width', window.screen.width / 10 * 9 + 'px')
      button1.style.setProperty('margin-left', window.screen.width / 20 + 'px')
    },
    set_cover_margin_top () {
      const coverId = document.getElementById('cover-id')
      coverId.style.setProperty('margin-top', (window.screen.height - (window.screen.width + 77)) * 0.382 + 'px')
    }
  },
  mounted () {
    // this.set_button_length()
    this.set_cover_margin_top()
  }
}
</script>

<style scoped>
.button-item {
  margin: auto;
  font-size: medium;
  letter-spacing: 2px;
  width: 90%;
}
</style>
