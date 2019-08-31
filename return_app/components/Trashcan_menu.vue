<template>
    <div class="Trashcan">
        <h1 style="margin-bottom: 70px; margin-top: -60px;">혜택</h1>
        <router-link class="btn" to="/wifi">와이파이 사용</router-link>
        <router-link class="btn" to="/Trashcan">포인트 적립</router-link>
    </div>
</template>

<script>
    import firebase from 'firebase';
    import router from '../router';

    let db = firebase.firestore();

    export default {
        name: 'Trashcan_menu',
        data() {
            return {
                trash: 0,
            };
        },
        mounted() {
            db.collection("trashcan").doc("G9zHoOEVGMIU0tRMnEP6").onSnapshot((doc) => {
                if (doc.data().trash == 0) {
                    router.push({ path: '/trashcanmain' });
                }
                this.trash = doc.data().trash;
                console.log("Current data: ", doc.data());
            });
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
