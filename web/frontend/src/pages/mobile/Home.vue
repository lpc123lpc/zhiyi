<template>
  <page-header v-bind:header_title="'国家列表'"></page-header>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
export default {
  name: 'Home',
  components: {
    'page-header': pageHeader
  }
}
</script>

<style scoped>

</style>
