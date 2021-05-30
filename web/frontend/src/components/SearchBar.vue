<template>
  <div>
    <el-autocomplete
      class="inline-input"
      v-model="state"
      :fetch-suggestions="querySearch"
      placeholder="请输入地名"
      :trigger-on-focus="true"
      @select="handleSelect"
    ></el-autocomplete>
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
      state: '',
      searchRegion: ''
    };
  },
  methods: {
    querySearch(queryString, cb) {
      var results = queryString ? this.data.filter(this.createFilter(queryString)) : this.data;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    createFilter(queryString) {
      return (restaurant) => {
        return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
      };
    },
    handleSelect(item) {
      // console.log(item);
      this.searchRegion = item.value
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
