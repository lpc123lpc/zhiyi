<template>
  <el-row type="flex">
  </el-row>
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
    }
  }
}
</script>

<style scoped>

</style>
