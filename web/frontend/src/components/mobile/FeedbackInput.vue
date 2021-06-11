<template>
  <van-form class="container-item" id="container-item-id">
    <van-field name="rate" label="评分">
      <template #input>
        <van-rate v-model="ruleForm.value" allow-half />
      </template>
    </van-field>
    <van-field v-model="ruleForm.desc" rows="5"
               autosize
               label="反馈&建议"
               type="textarea"
               maxlength="200"
               placeholder="请留下您的反馈及建议"
               show-word-limit>
    </van-field>
    <van-button color="#8cc4ff" plain block @click="submitForm()" :disabled="isDisabled" class="button-item" id="button-item-id-1">{{content}}</van-button>
    <van-button color="#778899" plain block @click="resetForm()" class="button-item" id="button-item-id-2">重置</van-button>
  </van-form>
</template>

<script>
import { Toast } from 'vant'
export default {
  name: 'FeedbackInput',
  data () {
    return {
      isDisabled: false,
      content: '提交',
      ruleForm: {
        value: 0,
        desc: ''
      }
    }
  },
  mounted () {
    // this.set_button_length()
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
      containerItem.style.setProperty('margin-top', (window.screen.height - 363) * 0.382 + 'px')
    },
    postFeedBack () {
      var formData = JSON.stringify(this.ruleForm)
      fetch('http://81.70.134.96:5000/feedback', {
        method: 'POST',
        body: formData,
        headers: new Headers({
          'Content-Type': 'application/json'
        })
      }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => console.log('Success:', response))
    },
    submitForm () {
      if (this.ruleForm.desc === '') {
        Toast.fail('建议内容\n   不能为空！')
      } else {
        this.postFeedBack()
        Toast.success('提交成功\n   感谢反馈！')
        this.resetForm()
        this.isDisabled = true
        /* setTimeout(() => {
        this.isDisabled = false
      }, 5000) */
        const TIME_COUNT = 30
        let vm = this
        vm.count = TIME_COUNT
        vm.timer = window.setInterval(() => {
          if (vm.count > 0 && vm.count <= TIME_COUNT) { // 倒计时时不可点击
            vm.isDisabled = true
            // 计时秒数
            vm.count--
            // 更新按钮的文字内容
            vm.content = vm.count + 's后再次提交'
          } else { // 倒计时完，可点击
            vm.isDisabled = false
            // 更新按钮文字内容
            vm.content = '提交'
            // 清空定时器!!!
            clearInterval(vm.timer)
            vm.timer = null
          }
        }, 1000)
      }
    },
    resetForm () {
      this.ruleForm.value = 0
      this.ruleForm.desc = ''
    }
  }
}
</script>

<style scoped>
.button-item {
  margin-top: 10px;
  font-size: medium;
  letter-spacing: 2px;
  width: 90%;
  float:left;
  left: 5%;
}
.container-item {

}
</style>
