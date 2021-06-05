<template>
  <page-header v-bind:header_title="'感染情况'"></page-header>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
export default {
  name: 'InfectHome',
  components: {
    'page-header': pageHeader
  }
}
</script>

<style scoped>

</style>
