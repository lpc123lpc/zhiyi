<template>
  <div>
    <el-cascader
      placeholder="请输入/选择地名"
      ref="cascader"
      :options="this.data"
      @change="handleSelect"
      filterable
      clearable/>
    <el-button
      class="button"
      slot="append"
      type="primary" plain
      icon="el-icon-search"
      @click="goSearch()"
    ></el-button>
  </div>
</template>

<script>
import data from '../../../../../database/static/searchData.json'

export default {
  name: 'SearchBar',
  // props: [
  //   'data'
  // ],
  data() {
    return {
      data: '',
      searchRegion: '',
    }
  },
  mounted() {
    this.data = data
    // console.log(this.data)
  },
  watch: {
    '$route'() { // 监听路由是否变化, 解决更新搜索结果后不刷新界面的问题
      if (this.$route.params.region) {
        this.$router.go(0)
      }
    }
  },
  methods: {
    handleSelect() {
      var regions = []  // 将级联地区名以'/'连接
      var node = this.$refs['cascader'].getCheckedNodes()[0]
      regions.push(node.label)
      while (node.parent != null) {
        node = node.parent
        regions.push(node.label)
      }
      // console.log(regions)
      let type = regions.pop()
      if (type === '国内') regions.push('中国')
      // 处理最后两个名字相同的情况
      if (regions.length > 1 && regions[regions.length - 1] === regions[regions.length - 2]) {
        regions.pop()
      }
      this.searchRegion = regions.reverse().join('|')
      // console.log(this.searchRegion)
    },
    goSearch() {
      this.$router.push({path: `/Search/${this.searchRegion}`})
    }
  }
}
</script>

<style scoped>
.button {
  padding: 9.4px 20px;
  font-size: 17px;
}
</style>
