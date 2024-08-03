<template>
  <div id="app">
    <Navbar />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";

export default {
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style>
html {
  height: 100%;
  box-sizing: border-box;
}

body {
  font-family: "TangoSans";
  position: relative;
  margin: 0;
  min-height: 100%;
  box-sizing: inherit;
  padding-bottom: 6.76rem;

  /* display: grid;

  grid: auto / 1em 1fr 1em; */
}

footer {
  margin-top: 10px;
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
}

@font-face {
  font-family: "Amanise";
  src: url("./assets/fonts/Amanise.ttf");
  font-style: normal;
}

@font-face {
  font-family: "Redressed";
  src: url("./assets/fonts/Redressed-Regular.ttf");
  font-style: normal;
}

@font-face {
  font-family: "Merriweather";
  src: url("./assets/fonts/Merriweather-Regular.ttf");
  font-style: normal;
}

@font-face {
  font-family: "TangoSans";
  src: url("./assets/fonts/TangoSans.ttf");
  font-weight: normal;
  font-style: normal;
}

.tangosans {
  font-family: "TangoSans";
}

.amanise {
  font-family: "Amanise";
}

.merriweather {
  font-family: "Merriweather";
}

.redressed {
  font-family: "Redressed";
}
</style>
