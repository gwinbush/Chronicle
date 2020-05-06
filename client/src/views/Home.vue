<template>
<v-app>
    <div>
        <Navbar/>
        <v-content>
        <h1 id="chronicle" class="header">Chronicle</h1>
        <p class="body">Welcome to chronicle, a platform for A/B Testing. To get started, open the &quot;Create A/B Test&quot; page and submit a test. </p>
        <center><img src="@/assets/test.jpg" style="max-width:50%"></center>
        </v-content>
    </div>
</v-app>
</template>
<script>
import Navbar from '@/components/Navbar.vue'
export default {
    name: 'Home',
    components: {
        Navbar
    }
}
</script>

<style scoped>
    .body {
        text-align: center;
        padding-left: 20px;
    }
    .header {
        text-align: center;
        padding: 20px;
    }
</style>