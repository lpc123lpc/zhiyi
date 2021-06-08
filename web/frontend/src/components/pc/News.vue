<template>
  <el-tabs  stretch>
    <el-tab-pane label="疫苗新闻">
      <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto;list-style-type:none">
        <li v-for="item in infData" class="infinite-list-item" style="height: 30%;padding: 1%">
          <el-card @click.native="go(item.urls)" style="height: 100%">
            <el-row  type="flex">
              <el-col span="6">
                <img :src = item.picUrls style="width: 100%">
              </el-col>
              <el-col span="16" offset="2">
                <div style="height: 20%">{{item.title}}</div>
                <div style="height: 60%">{{item.abstracts}}</div>
                <div style="height: 20%;width: 100%">
                  <span style="float:left">{{item.time}}</span>
                  <span style="float: right">{{item.source}}</span>
                </div>
              </el-col>
            </el-row>
          </el-card>
        </li>
      </ul>
    </el-tab-pane>
    <el-tab-pane label="疫情新闻">
      <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto;list-style-type:none">
        <li v-for="item in vacData" class="infinite-list-item" style="height: 30%;padding: 1%">
          <el-card @click.native="go(item.urls)" style="height: 100%">
            <el-row  type="flex">
              <el-col span="6">
                <img :src = item.picUrls style="width: 100%">
              </el-col>
              <el-col span="16" offset="2">
                <div style="height: 20%">{{item.title}}</div>
                <div style="height: 60%">{{item.abstracts}}</div>
                <div style="height: 20%">{{item.time}}</div>
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

</style>
