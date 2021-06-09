<template>
  <div>
    <page-header v-bind:header_title="'出行建议'"></page-header>
    <mobile-travel-advice></mobile-travel-advice>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import MobileTravelAdvice from '../../components/mobile/MobileTravelAdvice'
export default {
  name: 'TravelAdvice',
  components: {
    MobileTravelAdvice,
    'page-header': pageHeader
  }
}
</script>

<style scoped>

</style>
