<template>
  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" style="width: 700px;" class="demo-ruleForm">
    <el-form-item label="" prop="desc">
      <el-input type="textarea"
                v-model="ruleForm.desc"
                :rows="8"
                maxlength="200"
                show-word-limit
                style="width: 700px;"></el-input>
    </el-form-item>
    <el-form-item style="text-align:center">
      <el-button type="primary" @click="submitForm('ruleForm')" :disabled="isDisabled">{{content}}</el-button>
      <el-button @click="resetForm('ruleForm')">重置</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  name: 'FeedBackInput',
  data () {
    return {
      isDisabled:false,
      content:'提交',
      ruleForm: {
        desc: ''
      },
      rules: {
        desc: [
          { required: true, message: '请填写您的建议', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    postFeedBack () {
      var formData = JSON.stringify(this.ruleForm)
      fetch('http://81.70.134.96:5000/feedback', {
        method: 'POST',
        body: formData,
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(res => {
        return res.json()
      }).then(res => {
        console.log(res)
      })
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.postFeedBack()
          alert('提交成功，感谢您的意见！')
          this.resetForm(formName)
          this.isDisabled = true
          /*setTimeout(() => {
            this.isDisabled = false
          }, 5000)*/
          const TIME_COUNT = 30
          let vm = this
          vm.count = TIME_COUNT
          vm.timer = window.setInterval(() => {
            if (vm.count > 0 && vm.count <= TIME_COUNT){
          	  // 倒计时时不可点击
              vm.isDisabled = true
              // 计时秒数
              vm.count--
              // 更新按钮的文字内容
              vm.content = vm.count + 's后再次提交'
            } else {
          	  // 倒计时完，可点击
             vm.isDisabled = false
              // 更新按钮文字内容
              vm.content = '提交'
              // 清空定时器!!!
              clearInterval(vm.timer)
              vm.timer = null
           }
         }, 1000)
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style scoped>
</style>
