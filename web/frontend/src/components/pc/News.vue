<template>
  <el-tabs  stretch>
    <el-tab-pane label="疫苗新闻">
      <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto;list-style-type:none">
        <li v-for="item in items" class="infinite-list-item" style="height: 30%;width:40%;padding: 1%">
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
      <span>国外新闻</span>
      <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto;list-style-type:none">
        <li v-for="item in items" class="infinite-list-item" style="height: 30%;width:40%;padding: 1%">
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
      items: []
    }
  },
  mounted () {
    this.test()
  },
  methods: {
    getNewsData () {
      var that = this
      fetch('http://81.70.134.96:5000/news').then(function (response) {
        response.json().then((data) => {
          that.items = data
          that.searchItem = data
        })
      })
    },
    go (url) {
      window.open(url, '_blank')
    },
    test () {
      this.items = [{
        'time': '2021-5-2',
        'title': '贺佬太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '贺佬，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'http://inews.gtimg.com/newsapp_ls/0/13617707633_640330/0'
      },
      {
        'time': '2021-5-2',
        'title': '贺佬太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '贺佬，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'http://inews.gtimg.com/newsapp_ls/0/13617707633_640330/0'
      },
      {
        'time': '2021-5-2',
        'title': '贺佬太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '贺佬，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      },
      {
        'time': '2021-5-2',
        'title': '贺佬太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '贺佬，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      },
      {
        'time': '2021-5-2',
        'title': '贺佬太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '贺佬，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      },
      {
        'time': '2021-5-2',
        'title': '贺佬太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '贺佬，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      }
      ]
    }
  }
}
</script>

<style scoped>

</style>
