<template>
    <div id="wrapper">
    <div class="main-content">
      <div class="header">
        <h1>BLOGLITE APPLICATION</h1>
      </div>
      
      <div class="l-part">
  
        <input type="text"
         placeholder="Email" 
         class="input-1"
         v-model='formData.email' />
  
        <div class="overlap-text">
  
          <input 
          type="password" 
          placeholder="Password" 
          class="input-2"
          v-model="formData.password" />
  
  
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
// import Customfetch from "../Customfetch.js"
export default {
    
    data(){
    return{
      formData:{
          email:null,  //this.$store.state.username,
          password:null,
      }
    }
  },

  methods:{
    async userLogin(){
      if(this.formData.email==null){
        alert("Username is empty")
      }
      else if(this.formData.password==null){
        alert("Password is empty")
      }
      else{
        const response = await fetch('http://127.0.0.1:5002/login?include_auth_token',{
            method:'post',
            headers:{
                'Content-Type': "application/json",
            },
            body: JSON.stringify(this.formData),
        })

        if(response.ok){
                const data=await response.json()
                // console.log(data.response.user.authentication_token)
                localStorage.setItem(  // this is stored and can be seen by pressing F12key and go to application and go to local storage
                    'auth-token',     // key
                    data.response.user.authentication_token  //value
                )
                this.$store.state.email = this.formData.email
                this.$router.push(`/home/${this.formData.email}`)
                // console.log("THIS BITCH")
            }
        else{
          alert("Email or Password incorrect")
            console.log("something went wrong while logging in")
        }
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