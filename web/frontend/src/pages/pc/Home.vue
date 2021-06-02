<!-- 首页 -->
<template>
    <el-container>
        <el-header>
          <wbc-nav></wbc-nav>
        </el-header>
        <el-container>
          <el-aside width="400px">
            <vaccine-sidebar v-bind:vaccine_header_title="'疫苗接种'"></vaccine-sidebar>
            <infect-sidebar v-bind:infect_header_title="'感染情况'"></infect-sidebar>
          </el-aside>
          <el-main>
            <div style="align: center; margin-top: 50px">
              <world-table></world-table>
            </div>
            <!--<div style="align: center; margin-top: 50px">
              <line-chart></line-chart>
            </div>-->
          </el-main>
        </el-container>
        <!--<div class="container">
            <el-row  :gutter="30">
                <el-col :sm="24" :md="16" style="transition:all .5s ease-out;margin-bottom:30px;">
                    <wbc-sharelist></wbc-sharelist>
                </el-col>
                <el-col :sm="24"  :md="8" >
                    <wbc-rightlist></wbc-rightlist>
                </el-col>
            </el-row>
        </div>
        <wbc-footer></wbc-footer>-->
    </el-container>
</template>

<script>
import vueHeader from '../../components/pc/PageHeader.vue'
import vaccineSidebar from '../../components/pc/VaccineSidebar.vue'
import infectSidebar from '../../components/pc/InfectSidebar.vue'
import worldTable from '../../components/pc/WorldTable.vue'
import lineChart from '../../components/pc/CountryVaccine'
// import footer from '../components/footer.vue'
// import temSharelist from '../components/temSharelist.vue'
// import temRightlist from '../components/temRightlist.vue'
export default {
  name: 'Home',
  data () { // 选项 / 数据
    return {
    }
  },
  methods: { // 事件处理器

  },
  components: { // 定义组件
    'wbc-nav': vueHeader,
    'vaccine-sidebar': vaccineSidebar,
    'infect-sidebar': infectSidebar,
    'world-table': worldTable,
    'line-chart': lineChart
    // 'wbc-sharelist': temSharelist,
    // 'wbc-rightlist': temRightlist,
    // 'wbc-footer': footer
  },
  created () { // 生命周期函数

  }
}
</script>

<style>

</style>
