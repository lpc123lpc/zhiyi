<template>
  <page-header v-bind:header_title="'新闻资讯'"></page-header>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
export default {
  name: 'NewsInformation',
  components: {
    'page-header': pageHeader
  }
}
</script>

<style scoped>

</style>
