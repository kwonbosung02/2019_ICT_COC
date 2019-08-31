<template>
    <div class="Trashcan">
        <img src="@/assets/img/logo.png" />
    </div>
</template>

<script>
    import firebase from 'firebase';
    import router from '../router';

    let db = firebase.firestore();

    export default {
        name: 'Trashcan_main',
        data() {
            return {
                trash: 0,
            };
        },
        mounted() {
            db.collection("trashcan").doc("G9zHoOEVGMIU0tRMnEP6")
            .onSnapshot({
                // Listen for document metadata changes
                includeMetadataChanges: true
            }, function (doc) {
                if (doc.data().trash != 0) {
                        router.push({ path: '/trashcanmenu' });
                    }
            });
        },
        computed: {
            'trash_type': function () {
                if (this.trash == 1) return T1;
                else if (this.trash == 2) return T2;
                else if (this.trash == 3) return T3;
                else if (this.trash == 4) return T4;
            }
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
