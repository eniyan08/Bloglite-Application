import { createApp } from 'vue'
import App from './App.vue'
// import Vuex from 'vuex'
import router from './router.js'
import store from './store'

const app = createApp(App)
app.use(router)
app.use(store)

// app.use(Vuex)
app.mount('#app')