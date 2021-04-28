<template>
  <el-card class="box-card" shadow="always">
    <el-row>
      <el-col :span="6"><div class="infect-sum">累计确诊XX</div></el-col>
      <el-col :span="2"><div class="infect-sum-add">+XX</div></el-col>
      <el-col :span="4"><div class="infect-sum">累计死亡XX</div></el-col>
      <el-col :span="4"><div class="infect-sum-add">+XX</div></el-col>
      <el-col :span="2"><div class="infect-sum">累计治愈XX</div></el-col>
      <el-col :span="6"><div class="infect-sum-add">+XX</div></el-col>
    </el-row>
  </el-card>
</template>

<script>
export default {
  name: 'InfectHomeHeadbar'
}
</script>

<style scoped>
.infect-sum {
  font-size: 20px;
  text-align: right;
  margin-top: 3px;
}
.infect-sum-add {
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
