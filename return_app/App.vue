<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
  import firebase from 'firebase';
  let firebaseConfig = {
    apiKey: "AIzaSyDcWTYvFvx36A4duLThLuWI50MNVBm2Dgk",
    authDomain: "return-coc.firebaseapp.com",
    databaseURL: "https://return-coc.firebaseio.com",
    projectId: "return-coc",
    storageBucket: "return-coc.appspot.com",
    messagingSenderId: "92534923117",
    appId: "1:92534923117:web:f952cc1e4d6ace91"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  export default {
    name: 'App',
  };
</script>

<style src="@/assets/css/style.css">
</style>
