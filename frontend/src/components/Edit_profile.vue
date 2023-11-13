<template>
  <Navbar_bar/>

  <div class="edit-menu-container">
    <ul>
      <li class="edit-icon"><a @click="cancel_edit"><i class="fas fa-times"></i></a></li>
      <li class="edit-name"><a>Edit Profile</a></li>
      <li class="edit-icon"><a @click="editted_profile" style="color:#3897f0"><i class="fas fa-check"></i></a></li>
    </ul>
  </div>

  <div class="edit-main-container">
    
    <div class="edit-image-container">
      <img v-if="this.$store.state.avatar==null" src="../assets/profile_picture.png">
      <img v-if="this.$store.state.avatar!=null" :src="this.$store.state.avatar">
     
      <button @click="$refs.fileInput.click()">Change Photo
        <span>
          <input type="file" name="imagefile" 
          ref="fileInput"
          @change="addAvatar"/>
          
        </span>
      </button>
      <button @click="remove_photo" style="color:red">Remove Photo</button>
  
    </div>

    <div class="edit-profile-detail-container">

      <label>Name</label>
      <input type="text" name="fullname" placeholder="Name"
      v-model="edit_form_data.name"/>

      <label>Username</label>
      <input type="text" name="username" placeholder="Username"
      v-model="edit_form_data.username"/>

      <label>Bio</label>
      <input type="text" name="bio" placeholder="Bio" row="4"
      v-model="edit_form_data.bio"/>
    </div>
  </div>

</template>


<script>
import Navbar_bar from './Navbar_bar.vue';
import Customfetch from "../Customfetch.js";

export default {
    name:'Edit_profile',
    components:{
        Navbar_bar
  },
  data(){
    return{
      edit_form_data:{
        avatar:this.$store.state.avatar,
        username:this.$store.state.username,
        name:this.$store.state.name,
        bio:this.$store.state.bio,
      },
      form_data:{
        username:this.$store.state.username,
        userpassword:this.$store.state.password,
        // avatar:this.$store.state.avatar,
        avatar_alt:"../assets/profile_picture.png"
      }
     
    }
  },

  methods:{
    
    getPhoto(){
      return '../assets/profile_picture.png'
    },

    addAvatar(event){
      
      const file = event.target.files[0]                    
      const reader = new FileReader();
      reader.addEventListener("load", () => {

      this.edit_form_data.avatar = reader.result;
      this.$store.state.avatar = reader.result;
      });

      reader.readAsDataURL(file)

    },
    editted_profile(){
      
      Customfetch(`http://127.0.0.1:5002/api/tasks/${this.$store.state.email}`,{
          method:'PUT',
          headers: {
            'Content-Type': 'application/json',
            'Authentication-Token': localStorage.getItem('auth-token'),
          },
          body: JSON.stringify(this.edit_form_data)
        })
        .then((data) => {
            console.log(data)
            this.$store.state.username = this.edit_form_data.username
            this.$store.state.bio = this.edit_form_data.bio
            this.$store.state.name = this.edit_form_data.name
            this.$router.push({
            name:"User_profile1"  
          })
        })
    },
    
    cancel_edit(){

      Customfetch(`http://127.0.0.1:5002/api/tasks/${this.form_data.username}/${this.form_data.userpassword}`,{
          method:'GET',
          headers: {
            "Content-Type":"application/json"
          },
          
        })
        .then((data) => {
          this.$store.state.avatar=data.avatar
          this.$router.push({
              name:"User_profile1"
          });
        }
        )
      
    },

    remove_photo(){
      this.$store.state.avatar=null
      Customfetch(`http://127.0.0.1:5002/api/tasks/${this.form_data.username}`,{
          method:'DELETE',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.edit_form_data)
        })
    }
  }
}
</script>

<style>

*{
  margin:0;
  padding:0;
  box-sizing:border-box;
}

.edit-menu-container{
  width:100%;
  
}

.edit-menu-container ul{
  width:100%;
  /* max-width:768px; */
  height:50px;
  list-style-type: none;
  overflow:hidden;
  background-color: #f0f0f0;
}

.edit-menu-container .edit-icon{
  float:left;
  width:15%;
}

.edit-menu-container .edit-name{
  float:left;
  width:70%;
}

.edit-menu-container .edit-name a{
  display: block;
  text-align: center;
  font-size: 17px;
  line-height: 50px;
}

.edit-menu-container .edit-icon a{
  display: block;
  text-align: center;
  font-size: 17px;
  line-height: 50px;
  cursor:pointer;
}

.edit-main-container{
  width: 100%;
  max-width:768px;
  margin:auto;
}

.edit-image-container{
  width: 100%;
  max-width:100px;
  margin:auto;
  padding-top:20px;
  padding-bottom: 20px;
}

.edit-image-container img{
  width: 100px;
  height:100px;
  overflow:hidden;
  border-radius:50px;
}

.edit-image-container button{
  width: 100px;
  border:none;
  margin-top:5px;
  background-color:white;
  color:#3897f0;
  font-size:16px;
}

span input[type=file]{
  width:0;
  height:0;
}

.edit-profile-detail-container{
  width:100%;
  padding:10px;
}

.edit-profile-detail-container input[type=text]{
  width:100%;
  padding:5px;
  margin-top:8px;
  margin-bottom:8px;
  border:none;
  border-bottom:1px solid #f0f0f0;
}

.edit-profile-detail-container label{
  padding:5px;
  margin-top:8px;
}

</style>



<!-- // const fileInput = document.getElementById("fileInput")

// fileInput.addEventListener("change", () => {
//   const file = fileInput.files[0];
//   const reader = new FileReader();

//   reader.addEventListener("load", () => {
//     console.log(reader.result);
//   });

//   reader.readAsDataURL(file)
// }) -->