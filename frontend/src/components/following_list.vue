<template>
  <Navbar_bar/>
  <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">
    <title>Document</title>
</head>
<body>

    <div class="user-top-nav1">
        <ul>
            <li class="user-tab-icon1"><a @click="go_to_profile"><i class="fa-solid fa-arrow-left"></i></a></li>
            <li class="user-tab-name1"><a containerIds="following">FOLLOWING</a></li>
        </ul>
    </div>

    <following_arr v-for="following in followings"
        :following="following"
        :key="followings.indexOf(following)"
    />

    
</body>
</html>

</template>

<script>
import Navbar_bar from './Navbar_bar.vue';
import following_arr from './following_arr.vue'
import Customfetch from "../Customfetch.js"
export default {
    name:'following_list',
    components:{
        Navbar_bar,
        following_arr,
  },
  data(){
        return{     
            formData:{
                name_of_the_user: this.$store.state.username  
            },
            followings:this.$store.state.following_array
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
                console.log(this.$store.state.follower_array)

            Customfetch(`http://127.0.0.1:5002/api/following/${this.formData.name_of_the_user}`,{
            method:'GET',
            headers: {"Content-Type":"application/json"}
            })
            .then((data1) =>{
                this.$store.state.following_array=data1
                console.log("following backbutton")
                console.log(this.$store.state.following_array)
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

    .user-top-nav1 ul{
        list-style-type: none;
        width:100%;
        height: 50px;
        background-color: #e9e9e9;
        overflow:hidden;
    }

    .user-top-nav1 .user-tab-icon1{
        float:left;
        width:15%;
    }

    .user-top-nav1 .user-tab-icon1 a{
        display: block;
        text-align: center;
        font-size: 17px;
        line-height: 50px;
        cursor:pointer;
    }

    .user-top-nav1 .user-tab-name1{
        float:left;
        width:70%;
    }

    .user-top-nav1 .user-tab-name1 a{
        /* display:block;
        text-decoration:none;
        text-align: center;
        line-height: 50px;
        cursor: pointer;
        color:#1b1717; */
        display: block;
        text-align: center;
        font-size: 17px;
        line-height: 50px;
    }

    .user-tab1{
        color:black;
    }


    

</style>