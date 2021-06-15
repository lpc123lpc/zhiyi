<template>
    <div id = 'WorldTable'>
      <div style="font-size: 25px;text-align: center">全球概要数据
      </div>
      <el-table v-loading="loading"
                :data="searchItem"
                empty-text=""
                :default-sort ="{prop:'confirmed',order:'descending'}"
                highlight-current-row height="600">
        <el-table-column type="expand">
          <template slot-scope="props">
            <country_data v-bind:country="props.row.name"></country_data>
          </template>
        </el-table-column>
        <el-table-column
          prop="name">
          <template slot="header" slot-scope="scope">
            <el-input
              class="inline-input"
              v-model="input"
              placeholder="搜索国家"
              filterable
              clearable
              :trigger-on-focus="false"
              @input="changeItem"
            ></el-input>
          </template>
        </el-table-column>
        <el-table-column
          prop="confirmed"
          label="累计确诊"
          sortable :formatter="matter">
        </el-table-column>
        <el-table-column
          prop="newConfirmed"
          label="新增确诊"
          sortable :formatter="matter">
        </el-table-column>
        <el-table-column
          prop="cured"
          label="累计治愈"
          sortable :formatter="matter">
        </el-table-column>
        <el-table-column
          prop="deceased"
          label="累计死亡"
          sortable :formatter="matter">
        </el-table-column>
        <el-table-column
          prop="vaccined"
          label="累计接种"
          sortable :formatter="matter">
        </el-table-column>
        <el-table-column
          prop="newVaccined"
          label="新增接种"
          sortable :formatter="matter">
        </el-table-column>
        <el-table-column
          prop="vaccine_coverage"
          label="百人接种"
          sortable>
        </el-table-column>
      </el-table>
    </div>
</template>

<script>
import CountryData from './countryData'
export default {
  name: 'WorldTable',
  components: {
    'country_data': CountryData},
  data: function () {
    return {
      items: [],
      searchItem: [],
      input: '',
      names: [],
      loading: true
    }
  },
  mounted () {
    this.getWorldData()
  },
  methods: {
    getWorldData () {
      var that = this
      fetch('http://81.70.134.96:5000/worldData').then(function (response) {
        response.json().then((data) => {
          that.items = data
          that.searchItem = data
          that.loading = false
        })
      })
    },
    matter (row, column, cellValue) {
      cellValue += ''
      if (!cellValue.includes('.')) cellValue += '.'
      var out = cellValue.replace(/(\d)(?=(\d{3})+\.)/g, function ($0, $1) {
        return $1 + ','
      }).replace(/\.$/, '')
      if (out === 'null') {
        return ''
      } else {
        return out
      }
    },
    querySearch (queryString, cb) {
      cb(this.names)
    },
    handleSelect (item) {
    },
    changeItem () {
      var items = this.items
      var tempItem = []
      var names = []
      for (var i = 0; i < 133; i++) {
        if (items[i].name.indexOf(this.input) >= 0) {
          tempItem.push(items[i])
          names.push(items[i].name)
        }
      }
      this.searchItem = tempItem
      this.names = names
    }
  }
}
</script>

<style>
  .el-table__expand-icon{
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  .el-table__expand-icon
  .el-icon-arrow-right:before{
    content: "\e6d9";
    border: 1px solid #ccc;
    border-radius: 50%;
    padding: 2px;
  }
  .el-table__expand-icon--expanded
  .el-icon-arrow-right:before{
    content: "\e6d8";
    border: 1px solid #ccc;
    border-radius: 50%;
    padding: 2px;
  }
</style>
