<template>
  <div class="Resister">
    <div class="top-input-area">
      <div class="input-box">
        <h1 class="title">이메일를 입력해주세요.</h1>
        <p class="sub">본인인증을 위해 사용할 예정입니다.</p>
        <input class="input"/>
      </div>
    </div>
    <div class="bottom-btn-area">
      <router-link to="/resister2"><button class="next-btn">다음</button></router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Resister1',
  data() {
    return {

    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
