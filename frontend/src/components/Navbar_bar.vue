<template>
  <!DOCTYPE html>
  <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">
    
    <!-- <link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css"> -->
    <title>Document</title>
</head>
<body>
    <div style="text-align: center">
    <!-- <div class="nav-tops"> -->
        <!-- <li class="nav-starts"><a><i class="fas fa-camera"></i></a></li> -->
        <!-- <li class='nav-imgs'><a> -->
            <img src="../assets/bloglitelogo1.png"/>
        <!-- </a></li> -->
        <!-- <li class="nav-ends"><a><i class="fas fa-location-arrow"></i></a></li> -->
        <!-- <p>BlogLite</p> -->
    </div>
    
    <div class="container"> 

    </div>

    <div class="nav-bottom">
        <ul>
            <li><a class="tab" @click="buttonHome"><i class="fas fa-home"></i></a></li>
            <li><a class="tab" @click="buttonSearch"><i class="fas fa-search"></i></a></li>
            <li><a class="tab" @click="buttonAddPost"><i class="fas fa-plus"></i></a></li>
            <li><a class="tab" @click="buttonProfile"><i class="fas fa-user"></i></a></li>
            <li><a class="tab" @click="buttonLogout"><i class="fa fa-sign-out"></i></a></li>
        </ul>
    </div>

</body>
</html>
</template>

<script>
import Customfetch from "../Customfetch.js"
export default {
      name:'Navbar_bar',
      data(){
        return{     
            formData:{
                name_of_the_user: this.$store.state.username  
            },
        }
      },
      methods:{

        buttonHome(){
            this.$store.state.selected_posts=[]
          this.$router.push(`/home/${this.$store.state.email}`)
        },

        buttonSearch(){
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
                    name:'Search_bar'
                })
            })
        })  
        },

        buttonAddPost(){
            this.$router.push({
            name:'Add_post'
          })
        },

        buttonProfile(){
            console.log(this.$store.state.username)
            console.log(this.formData.name_of_the_user)
            Customfetch(`http://127.0.0.1:5002/api/followers/${this.$store.state.username}`,{
            method:'GET',
            headers: {"Content-Type":"application/json"}
            })
            .then((data) =>{
                this.$store.state.follower_array=data
                
                console.log("followers")
                // console.log(this.$store.state.avatar)
                console.log(this.$store.state.follower_array)
                // this.$router.push({
                //     name:'User_profile1'
                // })
            

            Customfetch(`http://127.0.0.1:5002/api/following/${this.$store.state.username}`,{
            method:'GET',
            headers: {"Content-Type":"application/json"}
            })
            .then((data1) =>{
                this.$store.state.following_array=data1
                console.log("following")
                console.log(this.$store.state.following_array)
                

                Customfetch(`http://127.0.0.1:5002/api/userposts/${this.$store.state.username}`,{
                    method:'GET',
                    headers: {"Content-Type":"application/json"}
                })
                .then((data) => {
                    this.$store.state.user_posts = data
                    this.$router.push({
                        name:'User_profile1'
                    })
                })
            })
        })
      
        },

        buttonLogout(){
          this.$store.state.username=null
          this.$store.state.password=null
          this.$store.state.avatar=null
          this.$store.state.follower_array=[]
          this.$store.state.bio=null
          this.$store.state.following_array=[]
          this.$store.state.total_posts=[]
          this.$store.state.selected_posts=[]
          this.$store.state.user_posts=[]
          localStorage.clear()
          this.$router.push({
            name:'Log_in'
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
    body{
        margin:0;
    }
    .nav-tops{
        width:100%;
        /* height:50px; */
        top:0;
        position:fixed;
        /* background-color: #f0f0f0; */
    }
    .nav-tops ul{
        list-style-type:none;
        margin:0;
        padding:0;
        overflow:hidden;
        height:50px;
        background-color: #f0f0f0;
    }
    .nav-tops img{
        width:100%;
        /* text-align: center; */
    }
    p{
        text-align: center;
    }
    li{
        float:left;
    }
    .nav-starts{
        width:15%;
    }
    .nav-imgs{
        width:20%;
        text-align: center;
    }
    .nav-ends{
        width:15%;
    }
    li a{
        display:block;
        text-decoration: none;
        text-align: center;
        line-height: 50px;
        color: black;
        cursor: pointer;
        }
    li a img{
        width:100px;
        height: 50px;
        align-self: center;
    }
    .nav-bottom{
        width:100%;     
        bottom:0;
        position:fixed;
    }
    .nav-bottom ul{
        list-style-type:none;
        margin:0;
        padding:0;
        overflow:hidden;
        height:50px;
        background-color: #f0f0f0;
    }
    .nav-bottom li{
        float:left;
        width:20%;

    }
</style>