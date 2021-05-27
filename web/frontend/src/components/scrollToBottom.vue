<template>
  <div class="scroll" @click="toBottom(100)">
    <el-tooltip class="item" content="查看折线图" placement="top" popper-class="tip" >
      <el-button class="button" type="primary" plain icon="el-icon-arrow-down"></el-button>
    </el-tooltip>
  </div>
</template>

<script>
export default {
  name: "scrollToBottom",
  props: [
    'isBottom'
  ],
  methods: {
    toBottom(i) {
      let clientHeight =
        document.documentElement.clientHeight || document.body.clientHeight;
      let scrollHeight = document.documentElement.scrollHeight;
      let rollheight = scrollHeight - clientHeight; //超出窗口上界的值就是底部的scrolTop的值
      document.documentElement.scrollTop += 200;
      if (document.documentElement.scrollTop + 1 <= rollheight) {//之所以+1，可以打印这两个值的日志就知道了，下面+1也是同理
        var c = setTimeout(() => this.toBottom(i), 1); //调用setTimeout是为了“回到底部”这过程不是一瞬间
      } else {
        clearTimeout(c);
      }
    },
    scrollHandle(e) {
      let clientHeight =
        document.documentElement.clientHeight || document.body.clientHeight;
      let scrollHeight = document.documentElement.scrollHeight;
      let rollheight = scrollHeight - clientHeight;
      let top = e.srcElement.scrollingElement.scrollTop; // 获取页面滚动高度
      if (rollheight <= top + 1) {
        this.isBottom = true;
      } else {
        this.isBottom = false;
      }
    }
  },
  mounted() {
    window.addEventListener("scroll", this.scrollHandle); //绑定页面滚动事件
  }
}
</script>

<style scoped>
.scroll {
  position: absolute;
  display: inline-block;
  box-shadow: 0 0 6px rgba(0, 0, 0, .12);
}
.item {
  text-align: center;
  line-height: 20px;
  font-size: 16px;
}
.button {
  width: 70px;
  height: 60px;
  font-size: 30px;
}
</style>

<style>
/* 修改箭头颜色  */
.tip.el-tooltip__popper[x-placement^="top"] .popper__arrow {
  border-top-color: #409eff;
}
.tip.el-tooltip__popper[x-placement^="top"] .popper__arrow:after {
  border-top-color: #409eff;
}
.tip {
  font-size: 15px;
  background: #409eff !important;
}
</style>
