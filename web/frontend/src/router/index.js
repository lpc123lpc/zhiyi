import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: resolve => require(['../pages/Home.vue'], resolve)
    },
    {
      path: '/Home',
      name: 'Home',
      component: resolve => require(['../pages/Home.vue'], resolve)
    }
  ]
})
