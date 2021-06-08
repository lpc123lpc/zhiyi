<template>
  <div>
    <el-cascader
      placeholder="请输入/选择地名"
      ref="cascader"
      :options="this.data"
      v-model="selectData"
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
import data from '../../../static/json/searchData.json'

export default {
  name: 'SearchBar',
  data () {
    return {
      data: '',
      selectData: [],
      searchRegion: ''
    }
  },
  mounted () {
    this.data = data
    // console.log(this.data)
  },
  watch: {
    '$route' () { // 监听路由是否变化, 解决更新搜索结果后不刷新界面的问题
      if (this.$route.params.region) {
        this.$router.go(0)
      }
    }
  },
  methods: {
    handleSelect (val) {
      // console.log(this.selectData)
      var regions = [] // 将级联地区名以'  '连接
      // console.log(val)
      // console.log(this.$refs['cascader'].panel.getNodeByValue(val))
      var node = this.$refs['cascader'].panel.getNodeByValue(val)
      regions.push(node.label)
      while (node.parent != null) {
        node = node.parent
        regions.push(node.label)
      }
      // console.log(regions)
      let type = regions.pop()
      if (type === '国内') regions.push('中国')
      // 处理最后两个名字相同的情况
      regions = regions.reverse()
      if (regions.length > 1 && regions[regions.length - 1] === regions[regions.length - 2]) {
        regions.pop()
      }
      this.searchRegion = regions.join('  ')
      // console.log(this.searchRegion)
    },
    goSearch () {
      this.$router.push({path: `/Search/${this.searchRegion}`, query: {data: this.selectData}})
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
