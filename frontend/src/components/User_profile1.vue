<template>
  <Navbar_bar/>
  <!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">

</head> -->
<body>

    <div class="container1">
        <div class="profile-container box1">
            <div class="image-container">

                <img v-if="this.$store.state.avatar==null" src="../assets/profile_picture.png">
                <img v-if="this.$store.state.avatar!=null" :src="this.$store.state.avatar">
            </div>
        </div>
        <div class="profile-container box2">
            <div class="edit-container">
                <div class="follow-container">
                    <p><b>{{ this.$store.state.user_posts.length }}</b></p>
                    <p class="follow">Posts</p>
                </div>

                <div class="follow-container">
                    <p><b>{{ formData.len }}</b></p>
                    <a @click="go_to_followers_page" style="cursor: pointer;"><p class="follow">Followers</p></a>
                </div>

                <div class="follow-container">
                    <p><b>{{ formData.len1 }}</b></p>
                    <a @click="go_to_following_page" style="cursor: pointer;"><p class="follow">Following</p></a>
                </div>

                <button @click="go_to_edit_page">Edit Profile</button>
            </div>
        </div>

        <div class="profile-details">
            <p><b>{{this.formData.name_of_the_user}}</b></p>
            <p>{{ this.formData.name }}</p>
            <p>{{this.$store.state.bio}}</p>
            
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
            <user_posts v-for="post in this.$store.state.user_posts"
                :post="post"
                :key="this.$store.state.user_posts.indexOf(post)"/>
        </div>
</div>

</body>
<!-- </html> -->
</template>

<script>
import Navbar_bar from './Navbar_bar.vue';
import user_posts from './user_posts.vue';

// import Customfetch from "../Customfetch.js"
export default {
    name:'User_profile1',
    components:{
        Navbar_bar,
        user_posts
    },
    data(){
    return{     
        formData:{
            name_of_the_user: this.$store.state.username,
            name:this.$store.state.name,
            len:this.$store.state.follower_array.length,
            len1:this.$store.state.following_array.length,
        },
    }
    },
    async mounted(){

    },
    methods:{
        // go_to_followers_page(){
        //     Customfetch(`http://127.0.0.1:5002/api/followers/${this.formData.name_of_the_user}`,{
        //     method:'GET',
        //     headers: {
        //     "Content-Type":"application/json"
        //   }
        // })
        // .then((data) =>{
        //     this.$store.state.follower_array=data
        //     console.log(this.$store.state.follower_array)
        //     this.$router.push({
        //         name:'followers_list'
        //     })
        // })

        go_to_followers_page(){
            this.$router.push({
                name:'followers_list'
            })
        },    
        
        go_to_following_page(){
            this.$router.push({
                name:'following_list'
            })
        },
        go_to_edit_page(){
            this.$router.push({
                name:'Edit_profile'
            })
        },
    }

}
</script>

<style>
    *{
        margin:0;
        padding:0;
    }
    .userposts{
        margin-bottom:50px;
    }

    ul{
        list-style-type: none;
        width:100%;
        height:50px;
        background-color: #e9e9e9;
        overflow:hidden;
    }

    li{
        float:left;
        width:25%;
    }

    li a{
        display:block;
        text-decoration:none;
        text-align:center;
        color:black;
        line-height: 50px;
    }
    
    li a h4{
        line-height:50px;
    }

    @media screen and (max-width:768px) {

        .nav-name{
            width:55%
        }

        .nav-name a h4{
            line-height:50px;
            text-align: start;
            margin-left:10px;
        }

        .nav-icon{
            width:15%
        }
    }

        .container1{
            width:100%;
            height:100%;
            max-width:768px;
            margin:auto;
            padding-top:40px;
            overflow:hidden;
            border-top:1px solid #ccc;
            border-left:1px solid #ccc;
            border-right:1px solid #ccc;
            border-bottom:1px solid #ccc;
        }

        .profile-container{
            width:50%;
            float:left;
            height:100px;
            overflow:hidden;

        }
        .image-container{
            width:80px;
            height:80px;
            max-width:80px;
            margin:auto;
            border-radius:50px;
            overflow:hidden;
        }

        .image-container img{
            width:100%;
            height:100%;
        }

        .follow-container{
            width:33.33%;
            float:left;
        }

        .edit-container{
            padding:10px;
        }

        button{
            width:100%;
            padding:5px;
            border: 1px solid #ccc;
            background-color: white;
            border-radius: 25px;
            margin-top:5px;
        }

        p{
            text-align:center;
        }
        
        @media screen and (max-width:768px) {
            
            .profile-container.box1{
                width:35%;
            }

            .profile-container.box2{
                width:65%;
            }
        }

        .profile-details{
            padding-top:100px;
        }

        .profile-details p{
            text-align: start;
            margin:10px
        }

        .profile-tabs ul{
            list-style-type: none;
            width:100%;
            height:50px;
            background-color: #e9e9e9;
            overflow:hidden;
            border:1px solid #ccc
        }

        .profile-tabs li a{
            display:block;
            text-decoration:none;
            text-align:center;
            color:#ccc;
            line-height: 50px;
        }

        .follow{
            font-size: 13px;
        }
        
        /* .profile-container-inside{
            display:none;
        }

        .profile-container-inside.profile-actives{
            display:inherit;
            padding-bottom:50px;
        }

        .grid-post-container{
            width:33.33%;
            height:200px;
            float:left;
            padding:1px;         
        }

        .grid-post-container img{
            width:100%;
            height:100%;

        }

        @media screen and (max-width:768px) {
            
            .grid-post-container{
                height:100px;
            }
        } */
</style>