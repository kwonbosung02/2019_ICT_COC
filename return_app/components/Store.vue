<template>
  <div class="Store">
    <div class="top_bar">
      <router-link to="/main">
        <img class="back_btn" src="@/assets/img/left-arrow.png" />
      </router-link>
      <span class="text">상점</span>
    </div>
    <div class="Store_box">
      <div class="header">
        <div class="text-area">
          <h1 class="text">버리세요,<br>받으세요,<br>살리세요!</h1>
        </div>
        <div class="img-area">
          <img class="img" src="@/assets/img/store_img.png"/>
        </div>
      </div>
      <div class="point_box">
        <span class="title">적립금</span>
        <span class="point">{{point}} <span style="color: #0006b7; font-weight: 600; margin-left: 1px;">P</span></span>
      </div>
      <div class="btn_box">
        <div class="row">
          <div class="btn">
            <div class="img_area">
              <img class="img" src="@/assets/img/card_icon.svg" />
            </div>
            <div class="text_area">
              <span class="text">교통카드</span>
            </div>
          </div>
          <div class="btn">
            <div class="img_area">
              <img class="img" src="@/assets/img/coffee_icon.svg" />
            </div>
            <div class="text_area">
              <span class="text">커피/음료</span>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="btn">
            <div class="img_area">
              <img class="img" src="@/assets/img/store_icon.svg" />
            </div>
            <div class="text_area">
              <span class="text">편의점</span>
            </div>
          </div>
          <div class="btn">
            <div class="img_area">
              <img class="img" src="@/assets/img/food_icon.svg" />
            </div>
            <div class="text_area">
              <span class="text">음식점</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import firebase from 'firebase';
    let db = firebase.firestore();
export default {
  name: 'Store',
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
