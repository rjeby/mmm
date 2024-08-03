<template>
  <footer class="footer-class">
    <b-container>
      <b-row
        class="justify-content-center align-items-center flex-column flex-md-row"
      >
        <b-col
          cols="auto"
          v-for="(link, index) in footerLinks"
          :key="index"
          class="footer-link"
        >
          <router-link :to="link.route">{{ link.text }}</router-link>
        </b-col>
      </b-row>
      <b-row class="justify-content-center mt-3">
        <b-col cols="auto" class="text-center copyright">
          &copy; 2024 Mes Meilleurs Menus | Propulsé par Mes Meilleurs Menus
        </b-col>
      </b-row>
    </b-container>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      footerLinks: [
        { text: "Qui sommes-nous", route: "/qui-sommes-nous" },
        { text: "Contact", route: "/contact" },
        {
          text: "Conditions générales d'utilisation et Mentions Légales",
          route: "/politique-de-confidentialite",
        },
        { text: "FAQ", route: "/faq" },
      ],
    };
  },
};
</script>

<style scoped>
.footer-class {
  background-color: #004d40;
  padding: 20px 0;
  color: white;
}

.footer-link {
  margin: 10px 0;
  text-align: center;
}

.footer-link a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.footer-link a:hover {
  text-decoration: underline;
}

.copyright {
  color: #a1c900;
  font-size: 14px;
}
</style>
