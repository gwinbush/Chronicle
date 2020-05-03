import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import CampaignAdd from '@/views/CampaignAdd.vue'
import CampaignsView from '@/views/CampaignsView.vue'

Vue.use(Router)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/campaignAdd',
        name: 'Campaign add',
        component: CampaignAdd

    },
    {
        path: '/campaignsView',
        name: 'Campaigns view',
        component: CampaignsView

    }
]

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router