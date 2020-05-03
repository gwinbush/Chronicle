<template>
<v-app>
    <div>
        <Navbar/>
        <h1>Campaigns View Page</h1>
    </div>
</v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
export default {
    name: 'CampaignsAdd',
    components: {
        Navbar
    }
}
</script>
