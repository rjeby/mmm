import Vue from "vue";
import App from "./App.vue";
import router from "./router";

import FontAwesomeIcon from "./utils/font-awesome.js";

Vue.component("font-awesome-icon", FontAwesomeIcon);

import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

import VueApexCharts from "vue-apexcharts";
Vue.use(VueApexCharts);

Vue.component("apexchart", VueApexCharts);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "bootstrap/dist/js/bootstrap.bundle";

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
