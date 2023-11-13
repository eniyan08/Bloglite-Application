<template>
  
    <div id="home">
  
  <div class="home-main-container">
  
    <div class="menu-main-container">
      <ul>
        
        <li class="menu-image-icon">
          <a>
            <img v-if="post.avatar==null" src="../assets/profile_picture.png">
            <img v-if="post.avatar!=null" :src="post.avatar">
          </a>
        </li>
        
        <li class="menu-name-icon"><a>{{ post.username }}</a></li>
        
        <li class="menu-menu-icon">
          <a v-if="post.username == this.$store.state.username"
             @click="editpost">
            <i class="fas fa-edit"></i>
          </a>
        </li> 
        
        <li class="menu-delete-icon">
          <a v-if="post.username == this.$store.state.username"
             @click="deletePost">
            <i class="fa fa-trash" aria-hidden="true"></i>
          </a>
        </li>

        <li class="menu-export-icon">
          <a v-if="post.username == this.$store.state.username" 
            @click="export_post">
            <i class="fa-solid fa-file-export"></i>
          </a>
        </li>
      </ul>
    </div>
  
    <div class="main-post-container">
      <img :src="post.posts">
      
    </div>
  
    <div class="comment-icon-container">
      <ul>
        <li v-if="step==0" class="comment-menu-icon"><a><i @click="like" class="far fa-heart"></i></a></li>
        <li v-if="step==1" class="comment-menu-icon"><a><i @click="unlike" class="fa fa-heart" style="color:red"></i></a></li>
        <!-- <img src="../assets/heart.png"/> -->
        
      </ul>
    
    </div>
    <div class="post-detail-container">
      <!-- <no_likes v-bind="liked"/> -->
      <!-- <p  v-bind="like"><b>{{ this.like }} Likes</b></p> -->
      <p>{{ total_likes }} Likes</p>
      <p>{{ post.caption }}</p>
      <p>Posted on: {{ post.timestamp.slice(0,24) }}</p>
      <!-- <p>Post time</p> -->
    </div>
  
  </div>
  </div>
  </template>

<script>
// import { thisTypeAnnotation } from "@babel/types"
import Customfetch from "../Customfetch.js"

export default {
    name:"home_arr",
    
    props:{
        post:Object,
    },
    data(){
        return{
            formData:{
                ID:this.post.ID,
                user:this.$store.state.username
            },
            liked:this.post.likes,
            step:0,
            likes:{
              likes:1
            },
            unlikes:{
              likes:0
            }
        }
    },
    computed:{
      total_likes(){
        return this.liked
      }
    },
    async mounted(){
    //   console.log(this.post)
      await Customfetch(`http://127.0.0.1:5002/api/postlike/${this.post.ID}/${this.$store.state.username}`,{
            method:'GET',
            headers: {
                'Content-Type': 'application/json'
            },
          })
          .then((data) => {
            if(data.user == this.$store.state.username){
              this.step = 1
              console.log('step is 1')
            }
            else{
              this.step=0
              console.log('step is 0')
              console.log(this.post.ID)
            }
          })

          Customfetch(`http://127.0.0.1:5002/api/boredom/${this.post.ID}`,{
            method:'GET',
            headers: {
                'Content-Type': 'application/json'
            },
          })
          .then((data) => {
            this.liked = data.likes
            console.log(data.likes)
          })

    },
    methods:{
        like(){
        this.likes.likes = this.post.likes + 1
        Customfetch(`http://127.0.0.1:5002/api/post/${this.formData.ID}`,{
                method:'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.likes)
        })
        .then((data) => {
          console.log(data)
          this.liked = this.liked + 1
          // this.$store.state.likes += 1
         
          
          Customfetch(`http://127.0.0.1:5002/api/postlike/${this.formData.ID}`,{
            method:'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.formData)
          })
          .then((data) => {
            console.log(data)
          })
          this.step = 1
        })
      },

      unlike(){
        this.unlikes.likes = this.post.likes - 1
        Customfetch(`http://127.0.0.1:5002/api/post/${this.formData.ID}`,{
                method:'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.unlikes)
        })
        .then((data) => {
          console.log(data)
          this.liked = this.liked - 1
          // this.$store.state.likes += 1
          this.step = 0

          Customfetch(`http://127.0.0.1:5002/api/postlike/${this.post.ID}/${this.$store.state.username}`,{
            method:'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
          })
          .then((data) => {
            console.log(data)
          })
        })
      },

      deletePost(){
          Customfetch(`http://127.0.0.1:5002/api/boredom/${this.post.ID}`,{
            method:'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
          })
          .then((data) => {
            console.log(data)
            // this.$router.go()
          })
        },

        editpost(){
            this.$store.state.edit_post = this.post
            // console.log(this.$store.state.edit_post)
            this.$router.push({
                name:'Edit_post'
            })
        },

        export_post(){
          Customfetch(`http://127.0.0.1:5002/api/export_post/${this.post.ID}`,{
            method:'GET',
            headers: {
                'Content-Type': 'application/json'
            },
          })
          .then(() => {
            alert("Post exported")
          })
          
        }
    }
}
</script>


<style>

/* .menu1-menu-icon a{
      display: block;
      text-align: center;
      line-height: 40px;
      font-size:17px;
    }

.menu1-delete-icon a{
      display: block;
      text-align: center;
      line-height: 40px;
      font-size:17px;
    }

.menu1-export-icon a{
      display: block;
      text-align: center;
      line-height: 40px;
      font-size:17px; */
    /* } */
</style>