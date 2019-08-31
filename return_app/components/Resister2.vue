<template>
  <div class="Resister">
    <div class="top-input-area">
      <div class="input-box">
        <h1 class="title">비밀번호를 입력해주세요.</h1>
        <p class="sub">본인인증을 위해 사용할 예정입니다.</p>
        <input class="input"/>
      </div>
    </div>
    <div class="bottom-btn-area">
      <router-link to="/login"><button class="next-btn">완료</button></router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Resister2',
  data() {
    return {

    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
