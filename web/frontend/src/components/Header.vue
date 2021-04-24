<template>
<div class="header navbar animated">
  <div class="container">
    <nav id="primary-navigation" class="site-navigation primary-navigation">
      <div class="menum">
        <ul class="nav-menu">
          <li class="menu-item"><router-link href="#" to="/blog"><i class="fa fa-home"></i>首页</router-link></li>
          <li id="collapse" class="menu-item">
            <a target="_blank"><i class="fa fa-cog"></i>分类</a>
            <ul class="collapse-menum">
              <!--<li class="menu-item" v-for="item in tags">
                <a href="javascript:;" @click="getOne(item.tag)">{{item.tag}}</a>
              </li>-->
            </ul>
          </li>
          <li class="menu-item"><router-link to="/messages"><i class="fa fa-comment"></i>留言</router-link></li>
          <li class="menu-item"><router-link to="/about"><i class="fa fa-user"></i>关于</router-link></li>
        </ul>
      </div>
    </nav>
  </div>
</div>
</template>

<script>
    export default {
        name: "Header"
    }
</script>

<style scoped>
    @import '../assets/css/header.css';
</style>