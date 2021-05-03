<template>
    <div id = 'WorldTable'>
      <el-table :data="items" highlight-current-row height="600">
        <el-table-column type="expand">
          <country_data></country_data>
        </el-table-column>
        <el-table-column
          prop="name"
          label="国家">
        </el-table-column>
        <el-table-column
          prop="confirmed"
          label="累计确诊"
          sortable>
        </el-table-column>
        <el-table-column
          prop="newConfirmed"
          label="新增确诊"
          sortable>
        </el-table-column>
        <el-table-column
          prop="cured"
          label="累计治愈"
          sortable>
        </el-table-column>
        <el-table-column
          prop="deceased"
          label="累计死亡"
          sortable>
        </el-table-column>
        <el-table-column
          prop="vaccined"
          label="累计接种"
          sortable>
        </el-table-column>
        <el-table-column
          prop="newVaccined"
          label="新增接种"
          sortable>
        </el-table-column>
        <el-table-column
          prop="vaccined_coverage"
          label="接种率"
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
      items: []
    }
  },
  mounted () {
    this.items = this.getWorldData()
  },
  methods: {
    getWorldData () {
      var that = this
      fetch('../static/json/charts/testWorld').then(function (response) {
        response.json().then((data) => {
          that.items = data
        })
      })
    }
  }
}
</script>

<style scoped>

</style>
