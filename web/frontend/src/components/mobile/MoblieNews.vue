<template>
  <van-tabs>
    <van-tab title="疫苗新闻">
      <van-list
      >
        <van-cell v-for="(item,index) in infData" :key="index" style="padding: 20px" @click="go(item.urls)">
          <template #title>
            <img :src = item.picUrls style="width: 100%">
          </template>
          <template #label>
          <div style="height: 20%;color: black">{{item.title}}</div>
          <div style="height: 60%">{{item.abstracts}}</div>
          <div style="height: 20%;width: 100%">
            <span style="float:left">{{item.time}}</span>
            <span style="float: right">{{item.source}}</span>
          </div>
          </template>
        </van-cell>
      </van-list>
    </van-tab>
    <van-tab title="疫情新闻">
      <van-list
      >
        <van-cell v-for="(item,index) in vacData" :key="index" style="padding: 20px" @click="go(item.urls)">
          <template #title>
            <img :src = item.picUrls style="width: 100%">
          </template>
          <template #label>
            <div style="height: 20%;color: black">{{item.title}}</div>
            <div style="height: 60%">{{item.abstracts}}</div>
            <div style="height: 20%;width: 100%">
              <span style="float:left">{{item.time}}</span>
              <span style="float: right">{{item.source}}</span>
            </div>
          </template>
        </van-cell>
      </van-list>
    </van-tab>
  </van-tabs>
</template>

<script>
export default {
  name: 'MoblieNews',
  data: function () {
    return {
      infData: [],
      vacData: []
    }
  },
  mounted () {
    this.getNewsData()
  },
  methods: {
    getNewsData () {
      var that = this
      fetch('http://81.70.134.96:5000/news').then(function (response) {
        response.json().then((data) => {
          that.infData = data.infNews
          that.vacData = data.vacNews
        })
      })
    },
    go (url) {
      window.open(url, '_blank')
    }
  }
}
</script>

<style scoped>

</style>
