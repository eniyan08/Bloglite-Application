<template>
  <div id="wrapper">
  <div class="main-content">
    <div class="header">
      <h1>BLOGLITE APPLICATION</h1>
    </div>
    
    <div class="l-part">

      <input type="text"
       placeholder="Username" 
       class="input-1"
       v-model='formData.username' />

      <div class="overlap-text">

        <input 
        type="password" 
        placeholder="Password" 
        class="input-2"
        v-model="formData.userpassword" />


      </div>
      <!-- <input type="button" value="Log in" class="btn" /> -->
      <button @click.prevent="userLogin" class="btn">Log in</button>
    </div>
  
  </div>
  <div class="sub-content">
    
    <div class="s-part">
      Don't have an account? 
      <router-link to="/signup">Sign up</router-link>
    </div>
  
  </div>
</div>
</template>


<script>
import Customfetch from "../Customfetch.js"
export default {
    
    data(){
    return{
      formData:{
          username:this.$store.state.username,
          userpassword:null,
      }
    }
  },


  methods:{
    async userLogin(){
      if(this.formData.username==null){
        alert("Username is empty")
      }
      else if(this.formData.userpassword==null){
        alert("Password is empty")
      }
      else{
        Customfetch(`http://127.0.0.1:5002/api/tasks/${this.formData.username}/${this.formData.userpassword}`,{
          method:'GET',
          headers: {
            "Content-Type":"application/json"
          }
        })
        

        .then((data) => {
          this.$store.state.username = data.username
          this.$store.state.password = data.password
          this.$store.state.name = data.name
          this.$store.state.avatar=data.avatar
          this.$store.state.bio=data.bio

          Customfetch(`http://127.0.0.1:5002/api/following/${this.formData.username}`,{
            method:'GET',
            headers: {"Content-Type":"application/json"}
            })
            .then((data1) =>{
                this.$store.state.following_array=data1
                console.log(this.$store.state.following_array)
            })

          Customfetch(`http://127.0.0.1:5002/api/posts`,{
            method:'GET',
            headers: {"Content-Type":"application/json"}
            })
            .then((data2) =>{
                this.$store.state.total_posts=data2
                var posts = data2

                for ( let i=0; i<posts.length; i++){
                  var username = posts[i].username
                  for (let j=0; j<this.$store.state.following_array.length; j++){
                    var friend = this.$store.state.following_array[j].friend
                    if (username == friend){
                      this.$store.state.selected_posts.unshift(posts[i])
                    }
                  }
                  if (username == this.$store.state.username){
                      this.$store.state.selected_posts.unshift(posts[i])
                    }
                }
                console.log(this.$store.state.selected_posts)
                this.$router.push({
                    name:'Home_itis'
                })
            })
          
        })
        
        

        .catch(error => {
          console.log(error)
          
          alert("Username or Password incorrect")
        })
      }
    }

  }

}
</script>


<style>

* {
  margin: 0px;
  padding: 0px;
}

body {
  background-color: #fbf2f2;
}

#wrapper {
  width: 300px;
  height: 0%;
  overflow: hidden;
  border: 0px solid #fff7f7;
  margin: 50px auto;
  padding: 0px;
}

.main-content {
  width: 250px;
  height: 100%;
  margin: 20px auto;
  background-color: #b86969;
  border: 0px solid #f5f3f3;
  padding: 10px 10px;
}

.header {
  /* border: 0px solid #d7b0e1; */
  margin-top: 100px;
  margin-bottom: 20px;
}

/* .header img {
  height: 50px;
  width: 175px;
  margin: auto;
  position: relative;
  left: 40px;
} */

.input-1,
.input-2 {
  width: 100%;
  margin-bottom: 5px;
  padding: 6px 10px;
  border: 2px solid #fcf8f8;
  box-sizing: border-box;
  border-radius: 3px;
}

.overlap-text {
  position: relative;
}

.overlap-text a {
  position: absolute;
  top: 8px;
  right: 10px;
  color: #003569;
  font-size: 14px;
  text-decoration: none;
  font-family: 'Overpass Mono', monospace;
  letter-spacing: -1px;
}

.btn {
  width: 100%;
  background-color: #3897f0;
  border: 1px solid #3897f0;
  padding: 5px 12px;
  color: #fdfffd;
  font-weight: bold;
  cursor: pointer;
  border-radius: 3px;
}

.sub-content {
  width: 250px;
  height: 40%;
  margin: 10px auto;
  border: 1px solid #e6e6e6;
  padding: 20px 50px;
  background-color: #fff;
}

.s-part {
  text-align: center;
  font-family: 'Overpass Mono', monospace;
  word-spacing: -3px;
  letter-spacing: -2px;
  font-weight: normal;
}

.s-part a {
  text-decoration: none;
  cursor: pointer;
  color: #3897f0;
  font-family: 'Overpass Mono', monospace;
  word-spacing: -3px;
  letter-spacing: -2px;
  font-weight: normal;
}

input:focus {
    background-color: rgb(253, 250, 250);
}

</style>