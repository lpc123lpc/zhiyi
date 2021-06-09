<template>
  <div>
    <div v-show="show" style="text-align: center;">暂未收录</div>
    <div v-for="(i, index) in this.data" :key="index">
      <div class="card">
        <div class="list-item-title">{{ i.name }}</div>
        <div class="list-item-info">
            <i class="el-icon-map-location"/>
            <span>地址：{{ i.address }}</span>
        </div>
        <div class="list-item-info">
          <van-icon name="phone-o"/>
          <span>咨询电话：{{ i.tel }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VaccineInstitution',
  props: [
    'data'
  ],
  data() {
    return {
      count: Math.min(this.data.length, 10),
      loading: false,
      show: true
    }
  },
  mounted() {
    this.showNodataHint()
  },
  created() {
    this.showNodataHint()
  },
  methods: {
    showNodataHint() {
      if (this.data.length !== 0) this.show = false
      else this.show = true
    }
  }
}
</script>

<style scoped>
.card {
  position: relative;
  box-sizing: border-box;
  padding: 8px 16px;
  color: #323233;
  font-size: 12px;
  background-color: #fafafa;
  margin-bottom: 5px;
}

.list-item-title {
  font-family: "Microsoft YaHei", serif;
  font-size: 14px;
  margin-bottom: 8px;
}

.list-item-info {
  margin-bottom: 5px;
  font-family: "Microsoft Yi Baiti", serif;
  font-size: 12px;
}
</style>
