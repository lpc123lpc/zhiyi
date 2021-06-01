<template>
  <div>
    <!--    <el-autocomplete-->
    <!--      class="inline-input"-->
    <!--      v-model="state"-->
    <!--      :fetch-suggestions="querySearch"-->
    <!--      placeholder="请输入地名"-->
    <!--      :trigger-on-focus="true"-->
    <!--      @select="handleSelect"-->
    <!--    ></el-autocomplete>-->
    <el-cascader
      placeholder="请输入/选择地名"
      ref="cascader"
      :options="data"
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
export default {
  name: "SearchBar",
  props: [
    'data'
  ],
  data() {
    return {
      searchRegion: ''
    };
  },
  watch: {
    '$route'() { //监听路由是否变化, 解决更新搜索结果后不刷新界面的问题
      if (this.$route.params.region) {
        this.$router.go(0)
      }
    }
  },
  methods: {
    handleSelect() {
      this.searchRegion = this.$refs['cascader'].getCheckedNodes(true)[0].label
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
