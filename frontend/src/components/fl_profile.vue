<template>
    <Navbar_bar/>
    <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">
  
  </head>
  <body>
      <!-- <div class="menu-container">
      <ul>
          <li class="nav-name"><a><h4>Display Name</h4></a></li>
          <li class="nav-icon"><a><i class="fas fa-history"></i></a></li>
          <li class="nav-icon"><a><i class="fas fa-user-plus"></i></a></li>
          <li class="nav-icon"><a><i class="fas fa-ellipsis-v"></i></a></li>
      </ul>
      </div> -->
      <div class="user-top-nav">
    <ul>
        <li class="user-tab-icon"><a @click="$router.go(-1)"><i class="fa-solid fa-arrow-left"></i></a></li>
        <li  class="user-tab-name"><a containerIds="following">FOLLOWERS</a></li>
    </ul>
    </div>
  
      <div class="container1">
          <div class="profile-container box1">
              <div class="image-container">
  
                  <img v-if="this.$store.state.fl_avatar==null" src="../assets/profile_picture.png">
                  <img v-if="this.$store.state.fl_avatar!=null" :src="this.$store.state.fl_avatar">
              </div>
          </div>
          <div class="profile-container box2">
              <div class="edit-container">
                  <div class="follow-container">
                      <p><b>{{ this.$store.state.fl_user_posts.length }}</b></p>
                      <p class="follow">Posts</p>
                  </div>
  
                  <div class="follow-container">
                      <p><b>{{ this.$store.state.fl_follower_array.length }}</b></p>
                      <a  style="cursor: pointer;"><p class="follow">Followers</p></a>
                  </div>
  
                  <div class="follow-container">
                      <p><b>{{ this.$store.state.fl_following_array.length }}</b></p>
                      <a  style="cursor: pointer;"><p class="follow">Following</p></a>
                  </div>
  
                  <!-- <button @click="go_to_edit_page">Edit Profile</button> -->
              </div>
          </div>
  
          <div class="profile-details">
              <p><b>{{ formData.username }}</b></p>
              <p>{{ this.$store.state.fl_name }}</p>
              <p>{{ this.$store.state.fl_bio }}</p>
              
          </div>
  
          <div class="profile-tabs">
              <ul>
                  <li><a><b>Posts</b></a></li>
                  <!-- <li><a><i class="fas fa-list"></i></a></li>
                  <li><a><i class="fas fa-portrait"></i></a></li>
                  <li><a><i class="fas fa-bookmark"></i></a></li> -->
              </ul>
          </div>

          <div class="userposts">
            <user_posts v-for="post in this.$store.state.fl_user_posts"
                :post="post"
                :key="this.$store.state.fl_user_posts.indexOf(post)"/>
          </div>
  
      </div>
  
  </body>
  </html>
  </template>

<script>
import Navbar_bar from './Navbar_bar.vue';
import user_posts from './user_posts.vue';
export default {
    name:'fl_profile',
    components:{
        Navbar_bar,
        user_posts
    },
    data(){
    return{
      formData:{
          username:this.$store.state.fl_username
      }
    }
  },
}
</script>

<style>

</style>