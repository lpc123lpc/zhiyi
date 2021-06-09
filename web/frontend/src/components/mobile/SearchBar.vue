<template>
  <div>
    <van-field
      v-model="this.state.fieldValue"
      is-link
      readonly
      placeholder="请选择地名"
      @click="state.show = true"
    />
    <van-popup v-model:show="state.show" position="bottom">
      <van-cascader
        v-model="this.selectData"
        title="请选择所在地区"
        :options="this.data"
        :field-names="{ text: 'label'}"
        active-color="#8cc4ff"
        @close="state.show = false"
        @finish="onFinish"
      />
    </van-popup>
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
      searchRegion: '',
      state: {show: false, fieldValue: ''}
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
    onFinish ({ selectedOptions }) {
      this.state.show = false
      this.state.fieldValue = selectedOptions.map((option) => option.label).join('/')
      // console.log(this.state.fieldValue)
      // console.log(this.selectData)
      var regions = this.state.fieldValue.split('/')
      if (regions[0] === '国内') regions[0] = '中国'
      else regions = regions.slice(1)
      // 处理最后两个名字相同的情况
      if (regions.length > 1 && regions[regions.length - 1] === regions[regions.length - 2]) {
        regions.pop()
      }
      this.searchRegion = regions.join('  ')
      // console.log(this.searchRegion)
      this.$router.push({path: `/Search/${this.searchRegion}`, query: {data: this.selectData}})
    }
  }
}
</script>

<style scoped>

</style>
