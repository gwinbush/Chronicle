import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import Vuetify from 'vuetify'
import '@babel/polyfill'
import router from './router'

Vue.config.productionTip = false

Vue.use(Vuetify)

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
