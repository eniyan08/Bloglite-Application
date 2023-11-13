<template>
    <Navbar_bar/>
    <div class="user-top-nav">
    <ul>
        <li class="user-tab-icon"><a @click="this.$router.go(-1)"><i class="fa-solid fa-arrow-left"></i></a></li>
        <li  class="user-tab-name"><a containerIds="following">Your Posts</a></li>
        
    </ul>
    </div>
    <div class="no_post">
      
      <ownpost_arr v-for="post in this.$store.state.own_post_list"
        :post="post"
        :key="this.$store.state.own_post_list.indexOf(post)"/>
    </div>
     
</template>

<script>

import Navbar_bar from './Navbar_bar.vue'
import ownpost_arr from './ownpost_arr.vue'
// import Customfetch from "../Customfetch.js"
export default {
  name: 'Home_itis',
  components: {
    Navbar_bar,
    ownpost_arr
  },
  data(){
    return{
        formData:{
            
        }
    }
  },
}
</script>