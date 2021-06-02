<template>
  <div class="infinite-list-wrapper" style="overflow:auto">
    <ul
      v-infinite-scroll="load"
      infinite-scroll-disabled="disabled">
      <el-card
        v-for="(i, index) in this.data.slice(0, count)"
        :key="index"
        class="list-item"
        shadow="hover">
        <div class="list-item-title">{{ i.name }}</div>
        <el-row :gutter="50" class="list-item-info">
          <el-col :span="16">
            <i class="el-icon-map-location"/>
            <span>地址：{{ i.address }}</span>
          </el-col>
          <el-col :span="8">
            <i class="el-icon-phone-outline"/>
            <span>咨询电话：{{ i.tel }}</span>
          </el-col>
        </el-row>
      </el-card>
    </ul>
    <p style="width: 100%"
       v-loading="loading"
       element-loading-spinner="el-icon-loading"
       element-loading-text='加载中...'/>
    <!--    <p v-if="noMore">没有更多了</p>-->
  </div>
</template>

<script>
export default {
  name: 'VaccineInstitution',
  props: [
    'data'
  ],
  data () {
    return {
      count: Math.min(this.data.length, 10),
      loading: false
    }
  },
  // mounted() {
  //   console.log(this.data.slice(0, this.count))
  // },
  computed: {
    noMore () {
      return this.count >= this.data.length
    },
    disabled () {
      return this.loading || this.noMore
    }
  },
  methods: {
    load () {
      this.loading = true
      setTimeout(() => {
        if (this.count + 10 > this.data.length) {
          this.count = this.data.length
        } else {
          this.count += 10
        }
        this.loading = false
      }, 2000)
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/vaccineInstitution.css";
</style>
