// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Home from './views/Home.vue'
import 'jquery'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  render: h => h(Home),
}).$mount('#app')
