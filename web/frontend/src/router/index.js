import Vue from 'vue'
import Router from 'vue-router'
<<<<<<< HEAD
import HelloWorld from '@/components/HelloWorld'
=======

const Home = resolve => require(['@/views/Home'], resolve)
>>>>>>> master

Vue.use(Router)

export default new Router({
<<<<<<< HEAD
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})
=======
  mode: 'history',
  base: './',
  routes: [
      {
          path: '/',
          name: 'Home',
          component: Home
      },
  ]
})
>>>>>>> master
