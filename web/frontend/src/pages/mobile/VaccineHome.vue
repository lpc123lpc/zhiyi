<template>
  <page-header v-bind:header_title="'疫苗接种'"></page-header>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
export default {
  name: 'VaccineHome',
  components: {
    'page-header': pageHeader
  }
}
</script>

<style scoped>

</style>
