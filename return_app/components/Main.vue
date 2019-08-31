<template>
  <div class="Main">
    <div class="main_box">
      <p class="describe">적립금을 통해 다양한 상품을 구매할 수 있습니다.</p>
      <div class="point_box">
        <div class="top_box">
          <p class="title">적립금</p>
        </div>
        <div class="bottom_box">
          <div class="point">{{point}} <span style="color: #0006B7; font-weight: 600; margin-left: 1px;">P</span></div>
          <router-link to="/store"><span class="use-btn">사용하기</span></router-link>
        </div>
      </div>
      <div class="qrcode_wrap">
        <div class="qrcode_box">
          <router-link to="/qrcode">
            <div class="inner">
              <img class="frame left_top" src="@/assets/img/left_top.png" />
              <img class="frame left_bottom" src="@/assets/img/left_bottom.png" />
              <img class="frame right_top" src="@/assets/img/right_top.png" />
              <img class="frame right_bottom" src="@/assets/img/right_bottom.png" />
              <img class="icon" src="@/assets/img/trashcan.png" />
              <p class="title">적립하기</p>
              <p class="sub">클릭하면 QR코드를 스캔할 수 있습니다.</p>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import firebase from 'firebase';
    let db = firebase.firestore();
export default {
  name: 'Main',
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
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
