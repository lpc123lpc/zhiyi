<template>
  <el-container>
    <el-row type="flex" justify="space-around" v-for="(index,item) in items" :key="index">
      <el-col span="6" @click="go(item.urls)">
        <img src="item.picUrls" alt="" class="image">
        <div style="padding: 10px">
          <span>item.title</span>
          <span>item.abstracts</span>
          <span>item.time</span>
        </div>
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
    }
  }
}
</script>

<style scoped>

</style>
