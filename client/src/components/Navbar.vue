<template>
    <div>
        <v-app-bar
            color="#013D5B"
            dark
        >
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
            <v-toolbar-title>Chronicle A/B Testing Platform</v-toolbar-title>
        </v-app-bar>

        <v-navigation-drawer
            v-model="drawer"
            absolute
            temporary
        >
            <v-list
                nav
                dense
            >
                <v-list-item-group
                    v-model="group"
                    active-class="light-blue--text text--accent-4"
                >
                <v-list-item router to="/">
                    <v-list-item-icon>
                    <v-icon>mdi-home</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>Home</v-list-item-title>
                </v-list-item>

                <v-list-item router to="campaignAdd">
                    <v-list-item-icon>
                    <v-icon>mdi-email-newsletter</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>Create A/B Test</v-list-item-title>
                </v-list-item>

                <v-list-item router to="campaignsView">
                    <v-list-item-icon>
                    <v-icon>mdi-chart-areaspline</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>View A/B Tests</v-list-item-title>
                </v-list-item>

                </v-list-item-group>
            </v-list>
        </v-navigation-drawer>
    </div>
</template>


<script>
    export default {
        data: () => ({
            drawer: false,
        }),
    }
</script>