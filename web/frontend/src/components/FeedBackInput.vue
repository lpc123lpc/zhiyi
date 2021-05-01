<template>
  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" style="width: 600px;" class="demo-ruleForm">
  <el-form-item label="" prop="desc">
    <el-input type="textarea"
              v-model="ruleForm.desc"
              :rows="5"
              style="width: 600px;"></el-input>
  </el-form-item>
  <el-form-item style="text-align:center">
    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
  </el-form-item>
</el-form>
</template>

<script>
export default {
name: "FeedBackInput",
  data() {
      return {
        ruleForm: {
          desc: ''
        },
        rules: {
          desc: [
            { required: true, message: '请填写您的建议', trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
}
</script>

<style scoped>

</style>
