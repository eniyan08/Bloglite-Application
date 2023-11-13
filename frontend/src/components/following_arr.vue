<template>
  <div id="you" class="users11"> 
        <div class="users22">
            <div class="following1">
                <div class="following2">
                    <img v-if="this.following.avatar==null" src="../assets/profile_picture.png">
                    <img v-if="this.following.avatar!=null" :src="following.avatar">
                </div>
            </div>

            <div class="following1">
                <a @click="someones_user_profile" style="cursor: pointer;"><p>{{ following.friend }}</p></a>
            </div>

            <div class="following1">
                <div class="following3">
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
    name:"following_arr",
    
    props:{
        following:Object,
    },
    data(){
        return{
            formData:{
                user:this.following.friend,
                current_user:this.$store.state.username,
                following_users:this.$store.state.following_array
            },
            followerData:{
                friend_who_follows_user:this.$store.state.username,  // current user
                user_who_is_followedby:this.following.friend,  // followed by current user
            },
            step:0
            
        }
    },
    mounted(){
        var arr_len = this.formData.following_users.length;
        var result = false
        for (var i = 0; i < arr_len; i++){
                if (this.formData.following_users[i].friend == this.following.friend){
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
            Customfetch(`http://127.0.0.1:5002/api/details/${this.formData.user}`,{
                method:'GET',
                headers: {
                    "Content-Type":"application/json"
                },
                
            })
            .then((data) => {
                console.log(this.formData.user)
                
                this.$store.state.fl_username=data.username
                this.$store.state.fl_name = data.name
                this.$store.state.fl_avatar=data.avatar
                this.$store.state.fl_bio=data.bio
                this.$router.push({
                    name:'fl_profile'
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
.users11{
        width:100%;
        height:100%;
    }

    .users22{
        width:100%;
        max-width:768px;
        margin:auto;
        margin-top:10px; 
    }

    .following1{
        float:left;
        width:33.33%;
        height:50px;
    }

    .following2{
        width:40px;
        height:40px;
        max-width:40px;
        margin:auto;
        margin-top: 6px;
        overflow:hidden;
        border-radius:25px;
    }

    .following2 img{
        width:100%;
        height:100%;
    }

    .following1 p{
        margin-top: 15px;
        text-align: center;
    }

    .following3{
        width:80px;
        max-width:80px;
        margin:auto;
    }

    .following3 button{
        padding: 5px;
        border: none;
        border-radius: 5px;
        background-color: #3897f0;
        color:white;
        margin-top:10px; 
    }
</style>