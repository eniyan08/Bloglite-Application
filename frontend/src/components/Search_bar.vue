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
    <div class="top-nav">
        <div class="search-container">
            <div class="search-inner-container button">
                <button @click="search_user"><i class="fas fa-search"></i></button>
            </div>
            <div class="search-inner-container text">
                <input type="text" placeholder="Search.." name="search"
                 v-model="formData.user_being_searched"/>
            </div>
        </div>
    </div>

    <!-- <Searched_user v-for="user in searched_user"
        :user="user"
        :key="searched_user.indexOf(user)"/> -->

</body>
</html>
</template>

<script>
import Navbar_bar from './Navbar_bar.vue';
// import Searched_user from './Searched_user.vue';
import Customfetch from "../Customfetch.js"
export default {
    name:'Search_bar',
    components:{
        Navbar_bar,
        // Searched_user
    },
    data(){
        return{
            formData:{
                user_being_searched:null
            },
            searched_user:this.$store.state.searched_user
        }
    },
    methods:{
        search_user(){
            Customfetch(`http://127.0.0.1:5002/api/details/${this.formData.user_being_searched}`,{
                method:'GET',
                headers: {
                  "Content-Type":"application/json",
                  'Authentication-Token': localStorage.getItem('auth-token'),
                }
            })
            .then((data) => {
                
                this.$store.state.searched_user = data
                console.log("from here")
                console.log(data)
                console.log(this.$store.state.searched_user.username)
                // console.log(this.$store.state.searched_user.avatar)
                if(this.$store.state.searched_user.username==null){
                    this.$router.push({
                        name:'user_notfound'
                    })
                }
                else{
                this.$store.state.step = 0

                var arr_len = this.$store.state.following_array.length;
                var result = false
                for (var i = 0; i < arr_len; i++){
                if (this.$store.state.following_array[i].friend == this.$store.state.searched_user.username){
                    console.log("true")             
                    result = true
                    this.$store.state.step=2
                    }                
                } 
                if (result){
                    this.$router.push({
                    name:'Searched_user'
                })
                }
                else{
                    this.$store.state.step=3    
                    this.$router.push({
                        name:'Searched_user'
                    })
                }
            }
                
            })
        }

        }
    }

</script>

<style>
    *{
        margin:0;
        padding:0;
    }
    body{
        margin: 0;
        font-family:Arial, Helvetica, sans-serif;
    }

    .top-nav{
        height: 50px;
        background-color: #e9e9e9;
        overflow:hidden;
        /* max-width:768px; */
    }

    .search-container{
        width:100%;
        max-width: 768px;
        margin:auto;
    }

    .search-inner-container{
        float:left;
    }

    .search-inner-container.button{
        width: 30%;
    }

    .search-inner-container.text{
        width: 40%;
    }

    .search-inner-container input[type=text]{
        font-size: 17px;
        margin-top:9px;
        margin-left: 3px;
        border: none;
        padding: 5px;
        background-color: #e9e9e9;
    }

    .search-inner-container button{
        font-size: 17px;
        margin-top:5px;
        margin-left: 5px;
        border: none;
        padding: 6px;
        cursor:pointer;
        background-color: #e9e9e9;
    }




    /* .users11{
        width:100%;
        height:100%;
    } */

    

</style>