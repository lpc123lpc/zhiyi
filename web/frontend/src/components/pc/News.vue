<template>
  <el-container style="width: 100%">
    <el-row type="flex" :gutter="20" justify="space-between" style="flex-wrap: wrap;flex-direction: row">
      <el-col span="6" offset="2" v-for="(item,index) in items" :key="index">
        <el-card @click.native="go(item.urls)">
            <span>{{item.title}}</span>
            <span>{{item.abstracts}}</span>
            <span>{{item.time}}</span>
        </el-card>
      </el-col>
    </el-row>
  </el-container>
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
        'title': '芃村太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '芃村，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      },
      {
        'time': '2021-5-2',
        'title': '芃村太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '芃村，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      },
      {
        'time': '2021-5-2',
        'title': '芃村太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '芃村，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      },
      {
        'time': '2021-5-2',
        'title': '芃村太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '芃村，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      },
      {
        'time': '2021-5-2',
        'title': '芃村太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '芃村，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      },
      {
        'time': '2021-5-2',
        'title': '芃村太帅啦',
        'urls': 'https://www.baidu.com/?tn=80035161_1_dg',
        'source': '百度',
        'abstracts': '芃村，作为308中最帅的男人，荣获北航第一',
        'picUrls': 'C:\\Users\\lpc\\Desktop\\helao.jpg'
      }
      ]
    }
  }
}
</script>

<style scoped>

</style>
