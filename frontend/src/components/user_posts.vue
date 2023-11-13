<template>
  <div id="grid" class="profile-container-inside profile-actives">
        <div class="grid-main-container">
            <div class="grid-post-container">
               <a @click="go_to_ownpost"> 
                <img :src="post.posts"/>
               </a>
                    
            </div>
        </div>
    </div>
</template>

<script>
import Customfetch from "../Customfetch.js"
export default {
    name:"user_posts",
    props:{
        post:Object,
    },
    methods:{
        go_to_ownpost(){
            console.log(this.post)
            Customfetch(`http://127.0.0.1:5002/api/userposts/${this.$store.state.username}`,{
              method:'GET',
              headers: {"Content-Type":"application/json"}
            })
            .then((data) => {
                this.$store.state.own_post_list = data
                this.$router.push({
                    name:'own_posts'
                })
            })
        }
    }
}
</script>

<style>
.profile-container-inside{
    display:none;
      /* margin-bottom:40px; */
}

.profile-container-inside.profile-actives{
    display:inherit;
    /* padding-bottom:50px; */
}

.grid-post-container{
    width:33.33%;
    height:200px;
    float:left;
    padding:3px;         
}
.grid-post-container img{
    width:100%;
    height:100%;

}

@media screen and (max-width:768px) {
            
    .grid-post-container{
        height:100px;
    }
}
</style>