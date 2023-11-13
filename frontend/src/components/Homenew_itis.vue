<template>
    <Navbar_bar/>
    <div v-if="this.$store.state.selected_posts.length==0">
      <h2 style="text-align: center; margin-top:50px">There are no posts to show here</h2>
      
    </div> 
  
    <div class="no_post" v-else>
      
      <home_arr v-for="post in this.$store.state.selected_posts"
        :post="post"
        :key="this.$store.state.selected_posts.indexOf(post)"/>
    </div>
  
  </template>
  
  <script>
  
  import Navbar_bar from './Navbar_bar.vue'
  import home_arr from './home_arr.vue'
  import Customfetch from "../Customfetch.js"
  export default {
    name: 'Home_itis',
    components: {
      Navbar_bar,
      home_arr
    },
    data(){
      return{     
          // name_of_the_user: this.$store.state.username ,
          // posts:this.$store.state.selected_posts,
          formData:{
            id:0,
            username:null,
            email:null,
            password:null,
            avatar:null,
            bio:null,
            no_of_posts:0,
            active:0,
            fs_uniquifier:null
          },
          success:false,
          error:null
        }
    },
    async mounted(){
    
        // obj = new EventSource("/stream");
        // obj.addEventListener('sample', event =>{
        //     let data = JSON.parse(event.data);
        //     this.message.push(data.name);
        // })


      const email = this.$route.params.email;
  
      const response = await fetch(`http://127.0.0.1:5002/api/tasks/${email}`,{
        headers:{
            'Content-Type': 'application/json',
            'Authentication-Token': localStorage.getItem('auth-token'),  
        },
      })
      // .then((data)=>{
      //   console.log(data)
      // })
      const data = await response.json()
      // console.log("vanakam")
      // console.log(data)
      // console.log(localStorage.getItem('auth-token'))
      // console.log("vanthanam")
  
      if (response.ok){
        this.formData = data
        this.success = true
  
        this.$store.state.username = data.username
        this.$store.state.name = data.name
        this.$store.state.avatar=data.avatar
        this.$store.state.bio=data.bio
        // console.log(this.$store.state.username)
      }
      else if(response.status == 401){
        this.success = false
        this.error = data.response.errors[0]  
        //  console.log(data)
      }
      else{
        this.success = false
        this.error = data.message     
      }
  
      await Customfetch(`http://127.0.0.1:5002/api/following/${this.formData.username}`,{
              method:'GET',
              headers: {"Content-Type":"application/json"}
              })
              .then((data1) =>{
                  this.$store.state.following_array=data1
              //     console.log("enapa ithu")
              //     console.log(this.$store.state.following_array)
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
                  // console.log("ivan inga irukan")
                  // console.log(this.$store.state.selected_posts)
                  
                })
    }
  }
  </script>
  
  <style>
  *{
    margin:0;
    padding:0;
  }
  .no_post{
    margin-bottom:50px;
  }
  
  </style>