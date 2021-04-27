<template>
    <div id = 'WorldTable'>
      <table class="table table-hover" id="world">
        <thead>
          <tr>
            <th>国家名称</th>
            <th >累计确诊人数</th>
            <th>新增确诊人数</th>
            <th>累计治愈人数</th>
            <th>累计死亡人数</th>
            <th>累计接种人数</th>
            <th>新增接种人数</th>
            <th>接种率</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item) in items" :key="item.name">
            <td>{{item.name}}</td>
            <td>{{item.confirmed}}</td>
            <td>{{item.newConfirmed}}</td>
            <td>{{item.cured}}</td>
            <td>{{item.deceased}}</td>
            <td>{{item.vaccined}}</td>
            <td>{{item.newVaccined}}</td>
            <td>{{item.vaccined_coverage}}</td>
          </tr>
        </tbody>
      </table>
    </div>
</template>

<script>
import $ from 'jquery'
import 'datatables/media/js/jquery.dataTables.js'
export default {

  name: 'WorldTable',
  data: function () {
    return {
      items: []
    }
  },
  watch: {
    items: function () {
      this.$nextTick(function () {
        $('#world').dataTable({
          bSort: 'true',
          bRetrieve: 'true'
        })
      })
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
