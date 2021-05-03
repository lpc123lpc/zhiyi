import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'TestWorldMapInfection',
      component: resolve => require(['../test/TestWorldMapInfection'], resolve)
    },
    ,
    {
      path: '/TestInfectDetail/:country',
      name: 'TestCountryMapInfection',
      component: resolve => require(['../test/TestCountryMapInfection'], resolve)
    },
    {
      path: '/Home',
      name: 'Home',
      component: resolve => require(['../components/FeedBackInput'], resolve)
    },
    {
      path: '/VaccineHome',
      name: 'VaccineHome',
      component: resolve => require(['../pages/VaccineHome'], resolve)
    },
    {
      path: '/VaccineDetail/:country',
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
      path: '/InfectDetail/:country',
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
