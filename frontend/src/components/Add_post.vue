<template>
    <Navbar_bar/>
    <div class="upload-top">
      <ul>
        <li class="upload-start"><a><b>Add a post</b></a></li>
        <li class="upload-end"><a><button 
          @click="add_post"
          style="background-color: #f0f0f0; border:none; color:#3897f0; font-size:20px">
          <b>Share</b></button></a>
        </li>
      </ul>
    </div>
    
    <div class="upload-container">
      <div class="upload-image-container">
        <img v-if="this.$store.state.recent_post==null" src="../assets/image-solid.png"/>
        <img v-if="this.$store.state.recent_post!=null" :src="this.$store.state.recent_post">
        <button @click="$refs.fileInput.click()">+ Add Photo
          <span>
            <input type="file" name="imagefile" 
            ref="fileInput"
            @change="add_photo"/>
          </span>
        </button>
        <input type="text" name="caption" 
        placeholder="Write a caption..."
        v-model="formData.caption"/>
      </div>
    </div>

</template>
  
  <script>
  import Navbar_bar from './Navbar_bar.vue';
  import Customfetch from "../Customfetch.js";
  export default {
      name:'Add_post',
      components:{
          Navbar_bar
      },
      data(){
        return{
          formData:{
            username:this.$store.state.username,
            posts:this.$store.state.recent_post,
            caption:null,
            timestamp:null,
            avatar:this.$store.state.avatar,
          }
        }
      },
      methods:{
        add_photo(event){
          const file = event.target.files[0]
          const reader = new FileReader();
          reader.addEventListener("load", () => {
            this.formData.posts = reader.result;
            this.$store.state.recent_post = reader.result;
          });

          reader.readAsDataURL(file)
        },

        add_post(){

          if(this.formData.posts==null){
            console.log("no photo selected to share")
          }
          else{
          this.formData.timestamp = Date().toLocaleString()
          
          Customfetch(`http://127.0.0.1:5002/api/posts/${this.formData.username}`,{
            method:'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.formData)
          })
          .then((data) => {
            console.log(data)
            this.$store.state.recent_post = null
            // console.log('here')
            // console.log(this.formData.posts)
            // console.log(this.formData.timestamp)
            this.$store.state.selected_posts=[]
            this.$router.push(`/home/${this.$store.state.email}`)
          })
        }

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
}

.upload-top{
  width:100%;
  
  position:fixed;
}

.upload-top ul{
  list-style-type:none;
  margin:0;
  padding:0;
  overflow:hidden;
  height: 50px;
  background-color: #f0f0f0;
}
.upload-start{
  float: left;
  width:70%;
}
.upload-end{
  float: right;
  width:30%;
  
}
.upload-start a{
  display: block;
  text-decoration: none;
  text-align: start;
  margin-left:100px;
  line-height: 50px;
  cursor:pointer;
  font-size: 17px;
}

.upload-end a{
  display: block;
  text-decoration: none;
  text-align: center;
  line-height: 50px;
  cursor:pointer;
  font-size: 25px;
  
}

.upload-container{
  width:100%;
  max-width:768px;
  margin:auto;
  margin-top: 60px;
}

.upload-image-container{
  width:100%;
  max-width:400px;
  margin:auto;
}

.upload-image-container img{
  width:100%;
  height:100%;
  border:1px solid #ccc;
}

span input[type=text]{
  opacity:0;
}

input[type=text]{
  width:100%;
  padding:8px;
  margin-top:6px;
  display: inline-block;
  box-sizing: border-box;
  font-size:12px;
  border:none;
  border-radius:4px;
  background-color: white;
}

 
</style>