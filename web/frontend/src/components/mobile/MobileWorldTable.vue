<template>
  <van-tabs>
    <van-tab title="累计确诊">
      <van-list
        v-model="loading"
        :finished="finished"
        >
        <van-cell v-for="(item,index) in items" :key="index" :title="item.name" :value="matter(item.confirmed)" />
      </van-list>
    </van-tab>
    <van-tab title="新增确诊">
      <van-list
        v-model="loading"
        :finished="finished"
        >
        <van-cell v-for="(item,index) in items" :key="index" :title="item.name" :value="matter(item.newConfirmed)" />
      </van-list>
    </van-tab>
    <van-tab title="累计接种">
      <van-list
        v-model="loading"
        :finished="finished"
        >
        <van-cell v-for="(item,index) in items" :key="index" :title="item.name" :value="matter(item.vaccined)" />
      </van-list>
    </van-tab>
    <van-tab title="百人接种">
      <van-list
        v-model="loading"
        :finished="finished"
        >
        <van-cell v-for="(item,index) in items" :key="index" :title="item.name" :value="matter(item.vaccine_coverage)" />
      </van-list>
    </van-tab>
  </van-tabs>
</template>

<script>
export default {
  name: 'MobileWorldTable',
  data () {
    return {
      items: [],
      loading: false,
      finished: false
    }
  },
  mounted () {
    this.getWorldData()
  },
  methods: {
    getWorldData () {
      var that = this
      fetch('http://81.70.134.96:5000/worldData').then(function (response) {
        response.json().then((data) => {
          that.items = data
        })
      }).catch(function (err) {
        alert(err.toString())
      })
      this.finished = true
    },
    matter (cellValue) {
      cellValue += ''
      if (!cellValue.includes('.')) cellValue += '.'
      var out = cellValue.replace(/(\d)(?=(\d{3})+\.)/g, function ($0, $1) {
        return $1 + ','
      }).replace(/\.$/, '')
      if (out === 'null') {
        return ''
      } else {
        return out
      }
    }
  }
}
</script>

<style scoped>

</style>
