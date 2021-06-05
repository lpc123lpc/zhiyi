<template>
  <div>
    <page-header v-bind:header_title="'反馈&建议'"></page-header>
    <feedback-content class="feed-back-content-item"></feedback-content>
  </div>
</template>

<script>
import pageHeader from '../../components/mobile/PageHeader.vue'
import feedBackContent from '../../components/mobile/FeedbackInput.vue'
export default {
  name: 'Feedback',
  components: {
    'page-header': pageHeader,
    'feedback-content': feedBackContent
  }
}
</script>

<style scoped>

</style>
