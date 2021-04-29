<template>
  <el-card class="box-card" shadow="always">
    <!--<div slot="header" class="clearfix">
      <span>卡片名称</span>
    </div>
    <div v-for="o in 4" :key="o" class="text item">
      {{'列表内容 ' + o }}
    </div>-->
    <div slot="header" class="clearfix">
      <span style="font-size: 20px">感染情况</span>
    </div>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      XX
    </div>
    <div class="today-item">
      累计确诊
    </div>
    <div class="today-item">
      XX
    </div>
    <el-divider></el-divider>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      XX
    </div>
    <div class="today-item">
      累计死亡
    </div>
    <div class="today-item">
      XX
    </div>
    <el-divider></el-divider>
    <div class="yersterday-item">
      较昨日
    </div>
    <div class="yersterday-item">
      XX
    </div>
    <div class="today-item">
      累计治愈
    </div>
    <div class="today-item">
      XX
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'InfectDetailSidebar'
}
</script>

<style scoped>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.yersterday-item {
  margin-top: 20px;
  font-size: 16px;
  text-align: center;
  margin-bottom: 15px;
}
.today-item {
  font-size: 18px;
  text-align: center;
  margin-bottom: 15px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}

.box-card {
  width: 480px;
  margin-left: 50px;
  margin-top: 50px;
  border-radius: 20px;
}
</style>
