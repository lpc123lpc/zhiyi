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
      <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
      <el-button @click="resetForm('ruleForm')">重置</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  name: 'FeedBackInput',
  data () {
    return {
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
      fetch('http://127.0.0.1:5000/feedback', {
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
