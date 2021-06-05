<template>
  <div class="container-item" id="container-item-id">
    <van-field name="rate" label="评分">
      <template #input>
        <van-rate v-model="value" allow-half />
      </template>
    </van-field>
    <van-field v-model="message" rows="5"
               autosize
               label="反馈&建议"
               type="textarea"
               maxlength="200"
               placeholder="请留下您的反馈及建议"
               show-word-limit>
    </van-field>
    <van-button color="#8cc4ff" hairline plain block class="button-item" id="button-item-id-1">提交</van-button>
    <van-button color="#778899" hairline plain block class="button-item" id="button-item-id-2">重置</van-button>
  </div>
</template>

<script>
export default {
  name: 'FeedbackInput',
  data () {
    return {
      value: 0,
      message: ''
    }
  },
  mounted () {
    this.set_button_length()
    // this.set_container_pos()
  },
  methods: {
    set_button_length () {
      const button1 = document.getElementById('button-item-id-1')
      const button2 = document.getElementById('button-item-id-2')
      button1.style.setProperty('width', window.screen.width / 10 * 9 + 'px')
      button2.style.setProperty('width', window.screen.width / 10 * 9 + 'px')
      button1.style.setProperty('margin-left', window.screen.width / 20 + 'px')
      button2.style.setProperty('margin-left', window.screen.width / 20 + 'px')
    },
    set_container_pos () {
      const containerItem = document.getElementById('container-item-id')
      containerItem.style.setProperty('margin-top', (window.screen.height - 363) / 4 + 'px')
    }
  }
}
</script>

<style scoped>
.button-item {
  margin-top: 10px;
  margin-bottom: 10px;
}
.container-item {

}
</style>
