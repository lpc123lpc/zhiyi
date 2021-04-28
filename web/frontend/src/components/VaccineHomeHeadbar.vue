<template>
  <el-card class="box-card" shadow="always">
    <el-row>
      <el-col :span="8"><div class="vaccine-sum">累计接种XX</div></el-col>
      <el-col :span="4"><div class="vaccine-sum-add">+XX</div></el-col>
      <el-col :span="4"><div class="vaccine-sum">覆盖率XX</div></el-col>
      <el-col :span="8"><div class="vaccine-sum-add">+XX</div></el-col>
    </el-row>
  </el-card>
</template>

<script>
export default {
  name: 'VaccineHomeHeadbar'
}
</script>

<style scoped>
.vaccine-sum {
  font-size: 20px;
  text-align: right;
  margin-top: 3px;
}
.vaccine-sum-add {
  font-size: 16px;
  margin-top: 8px;
  margin-left: 5px;
}

.box-card {
  width: 1600px;
  height: 75px;
  border-radius: 10px;
  position: absolute;
  margin: auto;
  right: 0;
  left: 0;
  margin-top: 50px;
}
</style>
