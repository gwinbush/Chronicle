<template>
<v-app>
    <div>
        <Navbar/>
        <h1 style='padding-top:20px; padding-bottom:20px; text-align:center'>Create a new A/B Test</h1>
    </div>
    <v-content>
        <div class="column" style='background-color:#cbf1f5'>
            <form>
                <v-text-field
                    v-model="name"
                    :error-messages="nameErrors"
                    :counter="10"
                    label="Subject"
                    required
                    @input="$v.name.$touch()"
                    @blur="$v.name.$touch()"
                ></v-text-field>
                <v-textarea
                    v-model="email"
                    :error-messages="emailErrors"
                    label="Message Body"
                    required
                    outlined
                    textarea
                    @input="$v.email.$touch()"
                    @blur="$v.email.$touch()"
                ></v-textarea>
            </form>
        </div>
        <div class="column" style='background-color:#ffaaa6'>
            <form>
                <v-text-field
                    v-model="name"
                    :error-messages="nameErrors"
                    :counter="10"
                    label="Subject"
                    required
                    @input="$v.name.$touch()"
                    @blur="$v.name.$touch()"
                ></v-text-field>
                <v-textarea
                    v-model="email"
                    :error-messages="emailErrors"
                    label="Message Body"
                    required
                    outlined
                    textarea
                    @input="$v.email.$touch()"
                    @blur="$v.email.$touch()"
                ></v-textarea>
                <v-select
                    v-model="select"
                    :items="items"
                    :error-messages="selectErrors"
                    label="Cohort feature"
                    required
                    @change="$v.select.$touch()"
                    @blur="$v.select.$touch()"
                ></v-select>
                <v-select
                    v-model="select"
                    :items="items"
                    :error-messages="selectErrors"
                    label="Cohort value"
                    required
                    @change="$v.select.$touch()"
                    @blur="$v.select.$touch()"
                ></v-select>
            <v-btn class="mr-4" @click="submit">submit</v-btn>
            </form>
            
        </div>
    </v-content>
</v-app>
</template>


<script>
import axios from "axios";
import Navbar from '@/components/Navbar.vue'
export default {
    name: 'CampaignsView',
    components: {
        Navbar
    },
    data () {
        return {
            campaigns: []
        }
    },
    mounted() {
        axios({ method: "GET", "url": "https://drtk2lbaij.execute-api.us-east-1.amazonaws.com/api/v1/campaigns/list" }).then(result => {
                this.campaigns = result.data;
            }, error => {
                console.error(error);
            });
    },
    methods: {
        submit () {
            this.$v.$touch()
            },
        clear () {
            this.$v.$reset()
            this.name = ''
            this.email = ''
            this.select = null
            this.checkbox = false
        },
    }
}
</script>

<style scoped>
.column {
  float: left;
  width: 50%;
  padding: 10px;
  height:100%;
}
</style>