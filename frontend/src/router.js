import {createRouter, createWebHistory} from 'vue-router'
// import MainLayout from './components/MainLayout.vue'
import Home_itis from './components/Home_itis.vue'
import Homenew_itis from './components/Homenew_itis.vue'
import Sign_up from './components/Sign_up.vue'
import Log_in from './components/Log_in.vue'
import User_profile1 from './components/User_profile1.vue'
import Edit_profile from './components/Edit_profile.vue'
import Search_bar from './components/Search_bar.vue'
import Add_post from './components/Add_post.vue'
import followers_list from './components/followers_list.vue'
import following_list from './components/following_list.vue'
import fl_profile from './components/fl_profile.vue'
import Searched_user from './components/Searched_user.vue'
import user_notfound from './components/user_notfound.vue'
import own_posts from './components/own_posts.vue'
import Edit_post from './components/Edit_post.vue'


const routes = [

    // {
    //     path:'/',
    //     name:'MainLayout',
    //     component:MainLayout
    // },
    
    {
        path:'/',
        name:'Log_in',
        component:Log_in
    },
    {
        path:'/signup',
        name:'Sign_up',
        component:Sign_up
    },
    {
        path:'/home/:email',
        name:'Home_itis',
        component:Home_itis
        
    },
    {
        path:'/home/new/:email',
        name:'Homenew_itis',
        component:Homenew_itis
        
    },
    {
        path:'/profile',
        name:'User_profile1',
        component:User_profile1
    },
    {
        path:'/editprofile',
        name:'Edit_profile',
        component:Edit_profile
    },
    {
        path:'/search',
        name:'Search_bar',
        component:Search_bar
    },
    {
        path:'/addpost',
        name:'Add_post',
        component:Add_post
    },
    {
        path:'/followers',
        name:'followers_list',
        component:followers_list
    },
    {
        path:'/following',
        name:'following_list',
        component:following_list
    },
    {
        path:'/flprofile',
        name:'fl_profile',
        component:fl_profile
    },
    {
        path:'/searched_user',
        name:'Searched_user',
        component:Searched_user
    },
    {
        path:'/user_notfound',
        name:'user_notfound',
        component:user_notfound
    },
    {
        path:'/own_posts',
        name:'own_posts',
        component:own_posts
    },
    {
        path:'/Edit_post',
        name:'Edit_post',
        component:Edit_post
    },
]


const router = createRouter({
    history : createWebHistory(),
    routes,
})

export default router