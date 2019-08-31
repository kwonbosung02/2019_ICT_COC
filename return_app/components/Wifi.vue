<template>
    <div class="Trashcan">
        <h1>와이파이 <br>비밀번호<br> 알려줄꼬얌</h1>
    </div>
</template>

<script>
    import firebase from 'firebase';
    import router from '../router';

    let db = firebase.firestore();

    export default {
        name: 'Wifi',
        data() {
            return {
                trash: 0,
            };
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
