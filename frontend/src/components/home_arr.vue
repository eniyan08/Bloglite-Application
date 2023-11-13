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
      
      <li class="menu-name-icon"><a @click="someones_user_profile">{{ post.username }}</a></li>
      
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
    // components:{
    //   no_likes
    // },
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
      console.log(this.post)
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


      someones_user_profile(){
            Customfetch(`http://127.0.0.1:5002/api/details/${this.post.username}`,{
                method:'GET',
                headers: {
                    "Content-Type":"application/json",
                    'Authentication-Token': localStorage.getItem('auth-token'),
                },
                
            })
            .then((data) => {
                console.log(this.formData.user)
                console.log(data)
                this.$store.state.fl_username=data.username
                this.$store.state.fl_name = data.name
                this.$store.state.fl_avatar=data.avatar
                this.$store.state.fl_bio=data.bio
                
                Customfetch(`http://127.0.0.1:5002/api/followers/${this.$store.state.fl_username}`,{
            method:'GET',
            headers: {"Content-Type":"application/json"}
            })
            .then((data) =>{
                this.$store.state.fl_follower_array=data
                
                console.log("fl_followers")
                // console.log(this.$store.state.avatar)
                console.log(this.$store.state.fl_follower_array)
                // this.$router.push({
                //     name:'User_profile1'
                // })
            

            Customfetch(`http://127.0.0.1:5002/api/following/${this.$store.state.fl_username}`,{
            method:'GET',
            headers: {"Content-Type":"application/json"}
            })
            .then((data1) =>{
                this.$store.state.fl_following_array=data1
                console.log("fl_following")
                console.log(this.$store.state.fl_following_array)
                

                Customfetch(`http://127.0.0.1:5002/api/userposts/${this.$store.state.fl_username}`,{
                    method:'GET',
                    headers: {"Content-Type":"application/json"}
                })
                .then((data) => {
                    this.$store.state.fl_user_posts = data
                    console.log(this.$store.state.fl_user_posts)
                    this.$router.push({
                    name:'fl_profile'
                })
                })
            })
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
            this.$router.go()
          })
        }

    }
}
</script>

<style>
* {
  padding: 0;
  margin: 0;
}

.home-main-container{
        width:100%;
        height:100%;
        max-width: 500px;
        margin:auto;
        overflow:hidden;
        margin-top:10px; 
        margin-bottom: 20px;
    }

    .menu-main-container{
        width:100%;
    }

    .menu-main-container ul{
        list-style-type: none;
        height:40px;
        background-color:white;
    }

    .menu-main-container .menu-image-icon{
        float:left;
        width:20%;
        
    }

    .menu-main-container .menu-name-icon{
        float:left;
        width:50%;
    }

    .menu-main-container .menu-menu-icon{
        float:left;
        width:10%;
    }

    .menu-main-container .menu-delete-icon{
        float:left;
        width:10%;
    }

    .menu-main-container .menu-export-icon{
        float:left;
        width:10%;
    }

    .menu-image-icon img{
      width:35px;
      height:35px;
      margin-top:3px;
      margin-left:5px;
      overflow:hidden;
      border-radius:50px;
    }

    .menu-name-icon a{
      display: block;
      text-align: start;
      line-height: 40px;
      font-size:17px;
    }

    .menu-menu-icon a{
      display: block;
      text-align: center;
      line-height: 40px;
      font-size:17px;
    }

    .menu-delete-icon a{
      display: block;
      text-align: center;
      line-height: 40px;
      font-size:17px;
    }

    .menu-export-icon a{
      display: block;
      text-align: center;
      line-height: 40px;
      font-size:17px;
    }

    

    .main-post-container{
      width:100%;
      height:300px;
    }

    .main-post-container img{
      width:100%;
      height:100%;
    }

    .comment-icon-container{
      width:100%;
      /* padding-left:10px;
      margin:5px;
      text-align: start; */
    }
    
    .comment-icon-container ul{
      list-style-type: none;
      height:50px;
      background-color:white;
    }

    .comment-icon-container .comment-menu-icon{
      float:left;
      width:15%
    }

    /* .comment-menu-icon a{
      display: block;
      text-align: center;
      line-height:50px;
      font-size:20px;
    } */

    .post-detail-container{
        background-color:white;
    }

    .post-detail-container p{
      padding-left:10px;
      margin:5px;
      text-align: start;
      
    }
</style>