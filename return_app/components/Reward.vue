<template>
  <div class="Reward">
    <div class="reward_box">
      <div class="top_box">
        <img class="check_icon" src="@/assets/img/check_icon.png" />
        <h1 class="title">적립 완료</h1>
        <p class="sub"><span style="color: #0006b7; font-weight: 600;">{{price}}P</span>가 적립되었습니다!</p>
      </div>
      <div class="bottom_box">
        <div class="sec">
          <span class="title">내가 버린 쓰레기</span>
          <span class="value">{{trash}}</span>
        </div>
        <div class="sec">
          <span class="title">현재 적립금</span>
          <span class="value">{{point}}P</span>
        </div>
        <div class="btn_box">
          <span class="btn">
            <router-link to="/store">
              적립금 사용
            </router-link>
          </span>
        
        
          <span class="btn">
            <router-link to="/main">
              확인
            </router-link>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import firebase from 'firebase';
  let db = firebase.firestore();
export default {
  name: 'Reward',
  data() {
    return {
      point: null,
    };
  },
  mounted() {
    db.collection("user").doc("XwK4fpIwAjvklM72ka3D").get().then((doc) => {
      if (doc.exists) {
        this.point = doc.data().point;
      } else {
        console.log("No such document!");
      }
    }).catch(function (error) {
      console.log("Error getting document:", error);
    });
  },
  computed: {
    'trash' : function() {
      if(this.$route.params.id == 1) return '플라스틱';
      else if (this.$route.params.id == 2) return '캔';
      else if (this.$route.params.id == 3) return '종이';
      else if (this.$route.params.id == 4) return '일반쓰레기';
    },
    'price': function () {
      if (this.$route.params.id == 1) return '100';
      else if (this.$route.params.id == 2) return '150';
      else if (this.$route.params.id == 3) return '120';
      else if (this.$route.params.id == 4) return '60';
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
