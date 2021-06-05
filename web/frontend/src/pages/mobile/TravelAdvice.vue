<template>
  <page-header v-bind:header_title="'出行建议'"></page-header>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
export default {
  name: 'TravelAdvice',
  components: {
    'page-header': pageHeader
  }
}
</script>

<style scoped>

</style>
