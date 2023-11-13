<template>

  <!-- <Navbar_bar/> -->
  <Search_bar/>

  <div class="user-search-container">
    <div class="search-main-container">
        <div class="search-image-container">
            <img v-if="this.$store.state.searched_user.avatar==null" src="../assets/profile_picture.png"/>
            <img v-if="this.$store.state.searched_user.avatar!=null" :src="this.$store.state.searched_user.avatar"/>
        </div>
    </div>

    <div class="search-main-container">
        <a @click="someones_user_profile" style="cursor: pointer;"><p>{{ this.$store.state.searched_user.username }}</p></a>
    </div>

    <div class="search-main-container">
        <div class="search-like-container">
            <button v-if="this.$store.state.step == 2" @click="unfollow_this">Unfollow</button>
            <button v-if="this.$store.state.step == 3" @click="follow_this">Follow</button>
        </div>
    </div>
    </div>
</template>

<script>
import Customfetch from "../Customfetch.js"
import Search_bar from './Search_bar.vue';
export default {
    name:"Searched_user",
    components:{
        // Navbar_bar,
        Search_bar
    },
    data(){
        return{
            formData:{
                user:this.$store.state.searched_user.username,
                current_user:this.$store.state.username,
                avatar:this.$store.state.searched_user.avatar, // searched user avatar
                // following_users:this.$store.state.following_array,
                // user_avatar:this.$store.state.fl_avatar,
            },
            followerData:{
                friend_who_follows_user:this.$store.state.username,  // current user
                user_who_is_followedby:this.$store.state.searched_user.username,  // followed by current user
                avatar:this.$store.state.avatar
            },
            step:this.$store.state.step
        }
    },

    methods:{
        follow_this(){
            Customfetch(`http://127.0.0.1:5002/api/following/${this.formData.current_user}`,{
                method:'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.formData)
            })
            .then((data) => {
                console.log(this.formData.user)
                console.log(data)
                this.$store.state.step = 2
                console.log("following")
                // console.log("here")
                // console.log(this.formData.avatar)
                // console.log("up")

                Customfetch(`http://127.0.0.1:5002/api/followers/${this.followerData.user_who_is_followedby}`,{
                    method:'POST', 
                    headers: {
                        "Content-Type":"application/json"
                    },
                    body: JSON.stringify(this.followerData)
                })
                .then(() =>{
                    console.log("follower updated")
                })
            })
            
        },

        unfollow_this(){
            Customfetch(`http://127.0.0.1:5002/api/following/${this.formData.current_user}/${this.formData.user}`,{
                method:'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then((data) => {
                this.$store.state.step = 3
                console.log(data)
                                      
                Customfetch(`http://127.0.0.1:5002/api/followers/${this.followerData.user_who_is_followedby}/${this.followerData.friend_who_follows_user}`,{
                    method:'DELETE',
                    headers:{
                        'Content-Type': 'application/json'
                    }
                })
                .then((data) => {
                    console.log(data)
                })
            })
        }
    }
}
</script>

<style>
.user-search-conatiner{
        width:100%;
        max-width:768px;
        margin:auto;
        margin-top:10px; 
    }

    .search-main-container{
        float:left;
        width:33.33%;
        height:50px;
    }

    .search-image-container{
        width:40px;
        height:40px;
        max-width:40px;
        margin:auto;
        margin-top: 6px;
        overflow:hidden;
        border-radius:25px;
    }

    .search-image-container img{
        width:100%;
        height:100%;
    }

    .search-main-container p{
        margin-top: 15px;
        text-align: center;
    }

    .search-like-container{
        width:100px;
        max-width:100px;
        margin:auto;
    }

    .search-like-container button{
        padding: 5px;
        border: none;
        border-radius: 5px;
        background-color: #3897f0;
        color:white;
        margin-top:10px; 
    }
</style>