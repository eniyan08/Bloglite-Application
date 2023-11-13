<template>
    <Navbar_bar/>
    
    <div class="upload-top">
      <ul>
        <li class="upload-start"><a><b>Edit Post </b></a></li>
        <li class="upload-end"><a><button 
          @click="edit_done"
          style="background-color: #f0f0f0; border:none; color:#3897f0; font-size:20px">
          <b>Done</b></button></a>
        </li>
      </ul>
    </div>
    
    <div class="upload-container">
      <div class="upload-image-container">
        <!-- <img v-if="this.$store.state.recent_post==null" src="../assets/image-solid.png"/> -->
        <img v-if="this.$store.state.edit_post.posts" :src="this.$store.state.edit_post.posts">
        <button @click="$refs.fileInput.click()">+ Add Photo
          <span>
            <input type="file" name="imagefile" 
            ref="fileInput"
            @change="edit_photo"/>
          </span>
        </button>
        <input type="text" name="caption" 
        placeholder="Write a caption..."
        v-model="edit_form_data.caption"/>
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
            edit_form_data:{
                posts:this.$store.state.edit_post.posts,
                caption:this.$store.state.edit_post.caption,
                timestamp:null,
            },

        }
    },
    methods:{
        edit_photo(event){
          const file = event.target.files[0]
          const reader = new FileReader();
          reader.addEventListener("load", () => {
            this.$store.state.edit_post.posts = reader.result;
            this.edit_form_data.posts = reader.result;
            
          });

          reader.readAsDataURL(file)
        },
        edit_done(){
            console.log(this.$store.state.edit_post.ID)
            this.$store.state.edit_post.posts = this.edit_form_data.posts
            this.$store.state.edit_post.caption = this.edit_form_data.caption
            this.$store.state.edit_post.timestamp = this.edit_form_data.timestamp
            this.edit_form_data.timestamp = Date().toLocaleString()
            Customfetch(`http://127.0.0.1:5002/api/edit_post/${this.$store.state.edit_post.ID}`,{
          method:'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.edit_form_data)
        })
        .then((data) => {
            console.log('log')
            console.log(data)
            console.log(this.edit_form_data)
            console.log('log')
            this.$store.state.edit_post.posts = this.edit_form_data.posts
            this.$store.state.edit_post.caption = this.edit_form_data.caption
            this.$store.state.edit_post.timestamp = this.edit_form_data.timestamp
            this.$router.go(-1)
        })
        }
    }
}
</script>