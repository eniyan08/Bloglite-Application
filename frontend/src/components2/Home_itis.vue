<template>
    <Navbar_bar/>
  
    <home_arr v-for="post in posts"
        :post="post"
        :key="posts.indexOf(post)"/>
  
  </template>
  
  <script>
  
  import Navbar_bar from './Navbar_bar.vue'
  import home_arr from './home_arr.vue'
  // import Customfetch from "../Customfetch.js"
  export default {
    name: 'Home_itis',
    components: {
      Navbar_bar,
      home_arr
    },
    data(){
      return{     
          name_of_the_user: this.$store.state.username ,
          posts:this.$store.state.selected_posts
      }
    },
    
  }
  </script>
  
  <style>
  
  
  </style>