<template>
  <div id="you" class="users1"> 
        <div class="users2">
            <div class="follows1">
                <div class="follows2">
                    <img v-if="this.follower.avatar==null" src="../assets/profile_picture.png">
                    <img v-if="this.follower.avatar!=null" :src="follower.avatar">
                </div>
            </div>

            <div class="follows1">
                <a @click="someones_user_profile" style="cursor: pointer;"><p>{{ follower.friend_who_follows_user }}</p></a>
            </div>

            <div class="follows1">
                <div class="follows3">
                    <button v-if="step === 2" @click="unfollow_this">Unfollow</button>
                    <button v-if="step === 3" @click="follow_this">Follow</button>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import Customfetch from "../Customfetch.js"
export default {
    name:"follower_arr",
    
    props:{
        follower:Object,
    },
    data(){
        return{
            formData:{
                user:this.follower.friend_who_follows_user,
                current_user:this.$store.state.username,
                following_users:this.$store.state.following_array,
                avatar:this.follower.avatar,
            },
            followerData:{
                friend_who_follows_user:this.$store.state.username,  // current user
                user_who_is_followedby:this.follower.friend_who_follows_user,  // followed by current user
            },
            step:0
            
        }
    },
    // beforeCreate(){
    //     Customfetch(`http://127.0.0.1:5002/api/details/${this.follower.friend_who_follows_user}`,{
    //             method:'GET',
    //             headers: {
    //                 "Content-Type":"application/json"
    //             },
                
    //         })
    //         .then((data) => {
    //             this.$store.state.fl_avatar = data.avatar
    //             console.log(this.$store.state.fl_avatar)
    //         })
    // },

    mounted(){

        var arr_len = this.formData.following_users.length;
        var result = false
        for (var i = 0; i < arr_len; i++){
                if (this.formData.following_users[i].friend == this.follower.friend_who_follows_user){
                  console.log("true")             
                  result = true
                  this.step=2
                  return result
                } 
                      
            } 
            this.step=3    
            return result
        },
            


    

    methods:{

        someones_user_profile(){
            Customfetch(`http://127.0.0.1:5002/api/details/${this.follower.friend_who_follows_user}`,{
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

        follow_this(){
            Customfetch(`http://127.0.0.1:5002/api/following/${this.formData.current_user}`,{
                method:'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.formData)
            })
            .then(() => {
                this.step = 2
                console.log("following")

                Customfetch(`http://127.0.0.1:5002/api/followers/${this.followerData.user_who_is_followedby}`,{
            method:'POST',
            headers: {"Content-Type":"application/json"},
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
                this.step = 3
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
.users1{
        width:100%;
        height:100%;
    }

    .users2{
        width:100%;
        max-width:768px;
        margin:auto;
        margin-top:10px; 
    }

    .follows1{
        float:left;
        width:33.33%;
        height:50px;
    }

    .follows2{
        width:35px;
        height:35px;
        max-width:40px;
        margin:auto;
        margin-top: 6px;
        overflow:hidden;
        border-radius:25px;
    }

    .follows2 img{
        
        width:100%;
        height:100%;
    }

    .follows1 p{
        margin-top: 15px;
        text-align: center;
    }

    .follows3{
        width:100px;
        max-width:100px;
        margin:auto;
    }

    .follows3 button{
        padding: 5px;
        border: none;
        border-radius: 5px;
        background-color: #3897f0;
        color:white;
        margin-top:10px; 
    }
</style>