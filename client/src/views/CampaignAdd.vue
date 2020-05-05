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
                    v-model="subject1"
                    :error-messages="nameErrors"
                    label="Subject"
                    required
                    @input="$v.name.$touch()"
                    @blur="$v.name.$touch()"
                ></v-text-field>
                <v-textarea
                    v-model="message1"
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
                    v-model="subject2"
                    :error-messages="nameErrors"
                    :counter="10"
                    label="Subject"
                    required
                    @input="$v.name.$touch()"
                    @blur="$v.name.$touch()"
                ></v-text-field>
                <v-textarea
                    v-model="message2"
                    :error-messages="emailErrors"
                    label="Message Body"
                    required
                    outlined
                    textarea
                    @input="$v.email.$touch()"
                    @blur="$v.email.$touch()"
                ></v-textarea>
                <v-select
                    v-model="selected_cohort"
                    :items="Object.keys(cohorts)"
                    :error-messages="selectErrors"
                    label="Cohort feature"
                    required
                    @change="$v.select.$touch()"
                    @blur="$v.select.$touch()"
                    v-on:change="updateSelectedCohort"
                ></v-select>
                <v-select
                    v-model="selected_value"
                    :items="selected_cohort_values"
                    :error-messages="selectErrors"
                    label="Cohort value"
                    required
                    @change="$v.select.$touch()"
                    @blur="$v.select.$touch()"
                    no-data-text="Please select cohort feature"
                ></v-select>
            <v-btn class="mr-4" @click="submitTest">submit</v-btn>
            </form>
        
        <v-dialog
        v-model="dialog"
        width="500"
        >
        <v-card>
          <v-card-title
            class="headline grey lighten-2"
            primary-title
          >
            A/B Test Created
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            Your test has been created.<br> The ID is: {{campaign_id}}. <br> Go to the "View A/B Tests" page to see the results.
          </v-card-text>
  
          <v-divider></v-divider>
  
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="blue"
              text
              @click="dialog = false"
            >
              Close
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
            
        </div>
    </v-content>
</v-app>
</template>


<script>
import axios from "axios";
import Navbar from '@/components/Navbar.vue';
export default {
    name: 'CampaignsView',
    components: {
        Navbar
    },
    data () {
        return {
            subject1:"",
            message1: "",
            subject2:"",
            message2:"",
            cohorts: {
                "age": [ 21, 22, 23 ],
                "city": [
                    "Pittsburgh",
                    "Ithaca",
                    "McLean"
                ]
            },
            selected_cohort:"",
            selected_cohort_values:[],
            selected_value:"",
            dialog: false,
            campaign_id:""
        }
    },
    mounted() {

    },
    methods: {

        clear () {
            this.subject1 = ''
            this.subject2 = ''
            this.message1 = ''
            this.message2 = ''
            this.selected_cohort = ''
            this.selected_value = ''

        },
        updateSelectedCohort(value) {
            
            console.log(value)
            console.log(this.cohorts[value])
            this.selected_cohort_values = this.cohorts[value]
        },
        submitTest() {
            this.dialog = true
            var body = {
                "distribution_channel": "EMAIL",
                "cohort_name": this.selected_cohort,
                "cohort_value": this.selected_value,
                "subject1": this.subject1,
                "message1": this.message1,
                "subject2": this.subject2,
                "message2": this.message2
            }
            console.log(JSON.stringify(body))
            var self = this
            axios.post('https://drtk2lbaij.execute-api.us-east-1.amazonaws.com/api/v1/campaign', JSON.stringify(body))
            .then(function (response) {
                console.log(response['data']['CampaignResponse']['Id']);
                self.campaign_id = response['data']['CampaignResponse']['Id'].toString()
            })
            .catch(function (error) {
                console.log(error);
            });
            this.clear()
        }

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