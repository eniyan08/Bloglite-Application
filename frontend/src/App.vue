<template>
  <div class="app-wrapper">
  <div id="app">
    <router-view />
  </div>
</div>
</template>
<script>
export default {
  name: 'App'
}
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Quicksand", sans-serif;
}

.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.container {
  max-width: 1440px;
  margin: 0 auto;
}

.link {
  cursor: pointer;
  text-decoration: none;
  text-transform: uppercase;
  color: black;
}

.link-light {
  color: #fff;
}
</style>



<!-- <template>
  <div id="app">
    <Navbar_bar/>
    <router-view/>
  </div>
</template>

<script>
import Navbar_bar from './components/Navbar_bar.vue'
//import Home_itis from './components/Home_itis.vue'

export default {
  name: 'App',
  components: {
    Navbar_bar
  }
}
</script>

<style>

</style> -->
