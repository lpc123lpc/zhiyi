<template>
  <el-tabs  stretch>
    <el-tab-pane label="疫苗新闻">
      <ul class="infinite-list" style="overflow:auto;list-style-type:none">
        <li v-for="(item,index) in vacData" :key="index" class="infinite-list-item" style="height: 30%;padding: 1%">
          <el-card @click.native="go(item.urls)" style="height: 100%">
            <el-row  type="flex">
              <el-col :span='6'>
                <img :src = item.picUrls style="width: 100%">
              </el-col>
              <el-col :span="16" :offset="2">
                <div class="item-title">{{item.title}}</div>
                <div class="item-ab">{{item.abstracts}}</div>
                <div style="height: 20%;width: 100%">
                  <span class="item-time">{{item.time}}</span>
                  <span class="item-source">{{item.source}}</span>
                </div>
              </el-col>
            </el-row>
          </el-card>
        </li>
      </ul>
    </el-tab-pane>
    <el-tab-pane label="疫情新闻">
      <ul class="infinite-list"  style="overflow:auto;list-style-type:none">
        <li v-for="(item,index) in infData" :key="index" class="infinite-list-item" style="height: 30%;padding: 1%">
          <el-card @click.native="go(item.urls)" style="height: 100%">
            <el-row  type="flex">
              <el-col :span="6">
                <img :src = item.picUrls style="width: 100%">
              </el-col>
              <el-col :span="16" :offset="2">
                <div class="item-title">{{item.title}}</div>
                <div class="item-ab">{{item.abstracts}}</div>
                <div class="item-time">{{item.time}}</div>
                <span class="item-source">{{item.source}}</span>
              </el-col>
            </el-row>
          </el-card>
        </li>
      </ul>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
export default {
  name: 'News',
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
@import "../../assets/css/news.css";
</style>

<style>
.el-tabs__item{
  font-size:18px !important;
}
</style>
