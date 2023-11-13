import { createStore } from 'vuex'

export default createStore({
    state: {
        email:null,
        username: null,
        password: null,
        avatar:null,
        name:null,
        bio:null,
        follower_array:[],
        fl_username:null,
        fl_name:null,
        fl_avatar:null,
        fl_bio:null,
        following_array:[],
        recent_post:null,
        total_posts:[],
        selected_posts:[],
        user_posts:[],
        searched_user:[],
        step:0,
        fl_following_array:[],
        fl_follower_array:[],
        likes:0,
        like_step:0,
        own_post_list:[],
        edit_post:{},
        editted_post:[]
      },
    mutations: {
        UPDATE_USER(state, payload) {
            state.username = payload
          }
    },
    actions: {
        currentUser(context, payload) {
            // const usernames = context.state.username  
            // usernames.push(payload)       
            context.commit('UPDATE_USER', payload)
            // return username
          }
    },
    getters: {
      comp: function (state) {
        return `${state.username}`
      }
}
})