import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: resolve => require(['../../pages/mobile/Home'], resolve)
    },
    {
      path: '/Home',
      name: 'Home',
      component: resolve => require(['../../pages/mobile/Home'], resolve)
    },
    {
      path: '/VaccineHome',
      name: 'VaccineHome',
      component: resolve => require(['../../pages/mobile/VaccineHome'], resolve)
    },
    {
      path: '/InfectHome',
      name: 'InfectHome',
      component: resolve => require(['../../pages/mobile/InfectHome'], resolve)
    },
    {
      path: '/Feedback',
      name: 'Feedback',
      component: resolve => require(['../../pages/mobile/Feedback'], resolve)
    },
    {
      path: '/TravelAdvice',
      name: 'TravelAdvice',
      component: resolve => require(['../../pages/mobile/TravelAdvice'], resolve)
    },
    {
      path: '/NewsInformation',
      name: 'NewsInformation',
      component: resolve => require(['../../pages/mobile/NewsInformation'], resolve)
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (!/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {
    window.location.href = '/p_index.html#/'
    return
  }
  next()
})

export default router

const VueRouterPush = Router.prototype.push
Router.prototype.push = function push (to) {
  return VueRouterPush.call(this, to).catch(err => err)
}
