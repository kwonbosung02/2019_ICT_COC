<template>
    <div class="Trashcan">
        <img :src="trash_type" class="qrcode"/>
    </div>
</template>

<script>
    import firebase from 'firebase';
    import router from '../router';
    import T1 from '@/assets/img/플라스틱.png';
    import T2 from '@/assets/img/캔.png';
    import T3 from '@/assets/img/종이.png';
    import T4 from '@/assets/img/일반쓰레기.png';

    let db = firebase.firestore();

    export default {
        name: 'Trashcan.vue',
        data() {
            return {
                trash: 0,
            };
        },
        mounted() {
            db.collection("trashcan").doc("G9zHoOEVGMIU0tRMnEP6").get().then((doc) => {
                if (doc.exists) {
                     if (doc.data().trash == 0) {
                        router.push({ path: '/trashcanmain' });
                    }
                    this.trash = doc.data().trash;
                    console.log("Current data: ", doc.data());
                } else {
                    console.log("No such document!");
                }
            }).catch(function (error) {
                console.log("Error getting document:", error);
            });
        },
        computed: {
            'trash_type' : function() {
                if(this.trash == 1) return T1; 
                else if(this.trash == 2) return T2;
                else if (this.trash == 3) return T3;
                else if (this.trash == 4) return T4;
            }
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
