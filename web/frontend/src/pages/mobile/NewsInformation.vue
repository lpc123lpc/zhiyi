<template>
  <div>
    <page-header v-bind:header_title="'新闻资讯'"></page-header>
    <moblie-news></moblie-news>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import MoblieNews from '../../components/mobile/MoblieNews';
export default {
  name: 'NewsInformation',
  components: {
    MoblieNews,
    'page-header': pageHeader
  }
}
</script>

<style scoped>

</style>
