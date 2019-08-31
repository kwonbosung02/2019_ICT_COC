<template>
  <div class="Login">
    <div class="login_box">
      <img class="logo-img" src="@/assets/img/logo.png" />
      <input class="input" placeholder="이메일" />
      <input class="input" placeholder="비밀번호" />
      <router-link to="/main"><button class="login-btn">로그인</button></router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {

    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
