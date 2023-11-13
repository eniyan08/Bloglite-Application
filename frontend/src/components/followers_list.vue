<template>
    <Navbar_bar/>
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">
    <title>Document</title>
</head>
<body>

    <div class="user-top-nav">
    <ul>
        <li class="user-tab-icon"><a @click="go_to_profile"><i class="fa-solid fa-arrow-left"></i></a></li>
        <li  class="user-tab-name"><a containerIds="following">FOLLOWERS</a></li>
    </ul>
    </div>

    <follower_arr v-for="follower in followers"
        :follower="follower"
        :key="followers.indexOf(follower)"
    />

</body>
</html>
</template>

<script>

import Navbar_bar from './Navbar_bar.vue';
import follower_arr from './follower_arr.vue'
import Customfetch from "../Customfetch.js"
export default {
    name:'followers_list',
    components:{
        Navbar_bar,
        follower_arr,
    },

    data(){
        return{     
            formData:{
                name_of_the_user: this.$store.state.username  
            },
            followers:this.$store.state.follower_array
        }
    },

    methods:{
        go_to_profile(){
             Customfetch(`http://127.0.0.1:5002/api/followers/${this.formData.name_of_the_user}`,{
            method:'GET',
            headers: {"Content-Type":"application/json"}
            })
            .then((data) =>{
                this.$store.state.follower_array=data
                console.log("followers backbutton")
                // console.log(this.$store.state.follower_array)

            Customfetch(`http://127.0.0.1:5002/api/following/${this.formData.name_of_the_user}`,{
            method:'GET',
            headers: {"Content-Type":"application/json"}
            })
            .then((data1) =>{
                this.$store.state.following_array=data1
                // console.log("following backbutton")
                // console.log(this.$store.state.following_array)
                this.$router.push({
                    name:'User_profile1'
                })
            })
        })  
    }
  },

}
</script>

<style>
    *{
        margin:0;
        padding:0;
    }

    .user-top-nav ul{
        list-style-type: none;
        width:100%;
        height: 50px;
        background-color: #e9e9e9;
        overflow:hidden;
    }

    .user-top-nav .user-tab-icon{
        float:left;
        width:15%;
    }

    .user-top-nav .user-tab-icon a{
        display: block;
        text-align: center;
        font-size: 17px;
        line-height: 50px;
        cursor:pointer;
    }

    .user-top-nav .user-tab-name{
        float:left;
        width:70%;
    }

    .user-top-nav .user-tab-name a{
        display: block;
        text-align: center;
        font-size: 17px;
        line-height: 50px;
    }

    .user-tab{
        color:black;
    }

    

</style>