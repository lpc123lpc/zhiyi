import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'


const Home = resolve => require(['@/views/Home'], resolve)

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ],
  routes: [
      {
          path: '/',
          name: 'Home',
          component: Home
      },
  ]
})
