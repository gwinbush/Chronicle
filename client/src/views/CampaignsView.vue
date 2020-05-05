<template>
<v-app>
    <div>
        <Navbar/>
    </div>

    <v-content>
        <v-container fluid>
          <h1 style='padding-top:20px; padding-bottom:20px; text-align:center'>View A/B Test Results</h1>
          <v-row justify="center">
          <v-col class="d-flex" cols="12" sm="6" center>
          <v-select
            :items="campaigns"
            label="Test ID"
            solo
            v-on:change="updateMetrics"
          ></v-select>
        </v-col>
        </v-row>
        <v-row>     
        <v-col>   
            <v-card
                class="mx-auto"
                max-width="344"
                >
                <v-card-text>
                    <div></div>
                    <p class="display-1 text--primary">Test A</p>
                    <div class="text--primary"><b>Subject</b></div>
                    <p>{{metrics["0"]["subject"]}}</p>
                    <div class="text--primary"><b>Body</b></div>
                    <p>{{metrics["0"]["body"]}}</p>
                    <v-row>
                        <v-col><v-icon>mdi-email-check</v-icon><p>{{metrics["0"]["emails_sent"]}} deliveries</p></v-col>
                        <v-col><v-icon>mdi-email-open</v-icon><p>{{metrics["0"]["emails_opened"]}} opens</p></v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>
        <v-col>
            <v-card
                class="mx-auto"
                max-width="344"
                >
                <v-card-text>
                    <div></div>
                    <p class="display-1 text--primary">Test A</p>
                    <div class="text--primary"><b>Subject</b></div>
                    <p>{{metrics["1"]["subject"]}}</p>
                    <div class="text--primary"><b>Body</b></div>
                    <p>{{metrics["1"]["body"]}}</p>
                    <v-row>
                        <v-col><v-icon>mdi-email-check</v-icon><p>{{metrics["1"]["emails_sent"]}} deliveries</p></v-col>
                        <v-col><v-icon>mdi-email-open</v-icon><p>{{metrics["1"]["emails_opened"]}} opens</p></v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>
        </v-row>
        
        </v-container>
    </v-content>
</v-app>
</template>

<script>
import axios from "axios";
import Navbar from '@/components/Navbar.vue';
export default {
    name: 'CampaignsAdd',
    components: {
        Navbar
    },
    data () {
        return {
            campaigns: [],
            metrics: {
                "0":{
                    "subject": "",
                    "body": "",
                    "emails_sent": 0,
                    "emails_opened": 0
                },
                "1":{
                    "subject": "",
                    "body": "",
                    "emails_sent": 0,
                    "emails_opened": 0
                }
            }
        }
    },
    mounted() {
        axios({ method: "GET", "url": "https://drtk2lbaij.execute-api.us-east-1.amazonaws.com/api/v1/campaigns/list" }).then(result => {
                this.campaigns = result.data['campaign_ids'];
            }, error => {
                console.error(error);
            });
    },
    methods: {
        updateMetrics(campaign_id) {
            axios({ method: "GET", "url": `https://drtk2lbaij.execute-api.us-east-1.amazonaws.com/api/v1/metrics?campaign_id=${campaign_id}`}).then(result => {
                this.metrics = result.data;
            }, error => {
                console.error(error);
            });
        }
    }
}
</script>
