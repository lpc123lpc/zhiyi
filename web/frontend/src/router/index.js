import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'TestCountryMapInfection',
      component: resolve => require(['../test/TestCountryMapInfection.vue'], resolve)
    },
    {
      path: '/Home',
      name: 'Home',
      component: resolve => require(['../pages/Home.vue'], resolve)
    },
    {
      path: '/VaccineHome',
      name: 'VaccineHome',
      component: resolve => require(['../pages/VaccineHome'], resolve)
    },
    {
      path: '/VaccineDetail',
      name: 'VaccineDetail',
      component: resolve => require(['../pages/VaccineDetail'], resolve)
    }
    ,
    {
      path: '/InfectHome',
      name: 'InfectHome',
      component: resolve => require(['../pages/InfectHome'], resolve)
    },
    {
      path: '/InfectDetail',
      name: 'InfectDetail',
      component: resolve => require(['../pages/InfectDetail'], resolve)
    },
    {
      path: '/Feedback',
      name: 'Feedback',
      component: resolve => require(['../pages/Feedback'], resolve)
    }
  ]
})
