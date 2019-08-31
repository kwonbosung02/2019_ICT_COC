<template>
  <div class="Qrcode">
    <div class="aim_box">
      <img class="frame left-top" src="@/assets/img/left-top.png" />
      <img class="frame right-top" src="@/assets/img/right-top.png" />
      <img class="frame left-bottom" src="@/assets/img/left-bottom.png" />
      <img class="frame right-bottom" src="@/assets/img/right-bottom.png" />
    </div>
    <qrcode-stream class="qrcode_reader" @decode="onDecode" @init="onInit" />
    <router-link to="/main">
      <div class="bottom-btn">취소하기</div>
    </router-link>
  </div>
</template>

<script>
  import { QrcodeStream } from 'vue-qrcode-reader';
  import firebase from 'firebase';
  import router from '../router';
  
  let db = firebase.firestore();

  export default {
    name: 'Qrcode',
    components: { QrcodeStream },
    data() {
      return {
        error: ''
      };
    },
    methods: {
      onDecode(result) {
        db.collection("user").doc("XwK4fpIwAjvklM72ka3D").get().then((doc) => {
          if (doc.exists) {
            if(result == "플라스틱") {
              db.collection('user').doc("XwK4fpIwAjvklM72ka3D").update({ point: doc.data().point + 100 });
              db.collection('trashcan').doc("G9zHoOEVGMIU0tRMnEP6").update({ trash: 0 });
              router.push({ path: '/reward/1' });
            }
            else if (result == "캔") {
              db.collection('user').doc("XwK4fpIwAjvklM72ka3D").update({ point: doc.data().point + 150 });
              db.collection('trashcan').doc("G9zHoOEVGMIU0tRMnEP6").update({ trash: 0 });
              router.push({ path: '/reward/2' });
            }
            else if (result == "종이") {
              db.collection('user').doc("XwK4fpIwAjvklM72ka3D").update({ point: doc.data().point + 80 });
              db.collection('trashcan').doc("G9zHoOEVGMIU0tRMnEP6").update({ trash: 0 });
              router.push({ path: '/reward/3' });
            }
            else if (result == "일반쓰레기") {
              db.collection('user').doc("XwK4fpIwAjvklM72ka3D").update({ point: doc.data().point + 50});
              db.collection('trashcan').doc("G9zHoOEVGMIU0tRMnEP6").update({ trash: 0 });
              router.push({ path: '/reward/4' });
            }
            else {
              alert('올바른 QR코드가 아닙니다.');
            }
          } else {
            console.log("No such document!");
          }
        }).catch(function (error) {
          console.log("Error getting document:", error);
        });
      },

      async onInit(promise) {
        try {
          await promise
        } catch (error) {
          if (error.name === 'NotAllowedError') {
            this.error = "ERROR: you need to grant camera access permisson"
          } else if (error.name === 'NotFoundError') {
            this.error = "ERROR: no camera on this device"
          } else if (error.name === 'NotSupportedError') {
            this.error = "ERROR: secure context required (HTTPS, localhost)"
          } else if (error.name === 'NotReadableError') {
            this.error = "ERROR: is the camera already in use?"
          } else if (error.name === 'OverconstrainedError') {
            this.error = "ERROR: installed cameras are not suitable"
          } else if (error.name === 'StreamApiNotSupportedError') {
            this.error = "ERROR: Stream API is not supported in this browser"
          }
        }
      }
    }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
