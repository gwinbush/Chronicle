<template>
<v-app>
    <div>
        <Navbar/>
        <h1>Home Page</h1>
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