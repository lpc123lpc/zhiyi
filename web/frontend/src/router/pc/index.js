import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      name: 'Cover',
      component: resolve => require(['../../pages/pc/Cover'], resolve)
    },
    {
      path: '/Home',
      name: 'Home',
      component: resolve => require(['../../pages/pc/Home'], resolve)
    },
    {
      path: '/VaccineHome',
      name: 'VaccineHome',
      component: resolve => require(['../../pages/pc/VaccineHome'], resolve)
    },
    {
      path: '/VaccineDetail/:country',
      name: 'VaccineDetail',
      component: resolve => require(['../../pages/pc/VaccineDetail'], resolve)
    }
    ,
    {
      path: '/InfectHome',
      name: 'InfectHome',
      component: resolve => require(['../../pages/pc/InfectHome'], resolve)
    },
    {
      path: '/InfectDetail/:country',
      name: 'InfectDetail',
      component: resolve => require(['../../pages/pc/InfectDetail'], resolve)
    },
    {
      path: '/InfectProvinceDetail/:province',
      name: 'InfectProvinceDetail',
      component: resolve => require(['../../pages/pc/InfectProvinceDetail'], resolve)
    },
    {
      path: '/Feedback',
      name: 'Feedback',
      component: resolve => require(['../../pages/pc/Feedback'], resolve)
    },
    {
      path: '/TravelAdvice',
      name: 'TravelAdvice',
      component: resolve => require(['../../pages/pc/TravelAdvice'], resolve)
    },
    {
      path: '/NewsInformation',
      name: 'NewsInformation',
      component: resolve => require(['../../pages/pc/NewsInformation'], resolve)
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {
    window.location.href = '/m_index.html#/'
    return
  }
  next()
})

export default router

const VueRouterPush = Router.prototype.push
Router.prototype.push = function push (to) {
  return VueRouterPush.call(this, to).catch(err => err)
}
