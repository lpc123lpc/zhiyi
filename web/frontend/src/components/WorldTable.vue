<template>
    <div id = 'WorldTable'>
      <el-table :data="items" border highlight-current-row>
        <el-table-column
          prop="name"
          label="国家">
        </el-table-column>
        <el-table-column
          prop="confirmed"
          label="累计确诊人数"
          sortable>
        </el-table-column>
        <el-table-column
          prop="newConfirmed"
          label="新增确诊人数"
          sortable>
        </el-table-column>
        <el-table-column
          prop="cured"
          label="累计治愈人数"
          sortable>
        </el-table-column>
        <el-table-column
          prop="deceased"
          label="累计死亡人数"
          sortable>
        </el-table-column>
        <el-table-column
          prop="vaccined"
          label="累计接种人数"
          sortable>
        </el-table-column>
        <el-table-column
          prop="newVaccined"
          label="新增接种人数"
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
export default {

  name: 'WorldTable',
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
