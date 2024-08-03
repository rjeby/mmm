<template>
  <div class="fixed-top">
    <header>
      <b-container fluid class="bg-light p-0">
        <b-row class="align-items-start">
          <b-col
            cols="12"
            lg="8"
            class="d-flex justify-content-center justify-content-lg-start p-1 p-lg-0"
          >
            <router-link to="/">
              <img
                class="img-logo"
                src="../assets/app/logo-version-allongee-baseline-couleur.png"
                fluid
              />
            </router-link>
          </b-col>
          <b-col
            cols="12"
            lg="4"
            class="py-1 d-flex align-self-center justify-content-center flex-wrap"
            style="gap: 10px"
          >
            <PersonalSpace />
            <button @click="handleClick" class="btn btn-order">
              Je m'inscris gratuitement
              <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
            </button>
            <a
              href="https://www.leetchi.com/c/mes-meilleurs-menus"
              class="ms-2 d-none d-md-block"
              target="_blank"
            >
              <button class="btn btn-order">
                Je fais un don
                <font-awesome-icon :icon="['fas', 'hand-holding-heart']" />
              </button>
            </a>
          </b-col>
        </b-row>
      </b-container>
    </header>

    <b-navbar toggleable="lg" variant="faded" class="nav-background-color">
      <b-container class="d-flex justify-content-center align-items-center">
        <!-- Centered Toggle Button -->
        <b-navbar-toggle
          target="nav-collapse"
          class="mx-auto my-1 custom-toggle"
        ></b-navbar-toggle>

        <!-- Centered Nav Items -->
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class=" ">
            <b-nav-item :to="{ name: 'connection' }"
              >Mes Meilleurs Menus</b-nav-item
            >
            <b-nav-item :to="{ name: 'meilleurs-mangeurs' }"
              >Meilleurs Mangeurs</b-nav-item
            >
            <b-nav-item :to="{ name: 'lalimentation-positive-et-durable' }"
              >Alimentation Positive et durable</b-nav-item
            >
            <b-nav-item :to="{ name: 'nos-9-engagements' }"
              >Nos 9 Engagements</b-nav-item
            >
            <b-nav-item :to="{ name: 'conseils' }">Conseils</b-nav-item>
            <b-nav-item :to="{ name: 'conseils-scientifique' }"
              >Conseils Scientifique</b-nav-item
            >
            <b-nav-item :to="{ name: 'actualites' }">Actualités</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </div>
</template>

<script>
import PersonalSpace from "./PersonalSpace.vue";
import { personalSpaceState } from "@/utils/store";
import { useRouter } from "vue-router/composables";

export default {
  name: "Navbar",
  components: {
    PersonalSpace,
  },
  setup() {
    const router = useRouter();
    const handleClick = () => {
      if (!personalSpaceState.show) {
        router.push({ name: "inscription" });
      } else {
        router.push({ name: "deconnection" });
      }
    };

    return {
      personalSpaceState,
      handleClick,
    };
  },
};
</script>

<style scoped>
/* .navbar-collapse {
    float: left;
    background-color: #FFFFFF;
    color: #004C40;
    border-color: #004C40;
} */
.custom-toggle {
  background-color: rgba(255, 255, 255, 1);
  border: none;
}

a button span {
  color: white;
  text-decoration: none;
  list-style: none;
}

.b-collapse {
  display: flex;
  justify-content: center;
}

.navbar-nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 100%;
}

.navbar {
  padding: 0;
  font-family: "TangoSans";
}

.nav-link {
  white-space: nowrap;
  color: white;
  transition: 0.3s;
  padding: 13px;
}

.nav-link:hover {
  color: #ffffff;
  background-color: rgb(133, 187, 47);
}

a.nav-link.router-link-exact-active {
  color: #ffffff;
  background-color: rgb(133, 187, 47);
}

.nav-background-color {
  background-color: #004c40;
  font-size: 18px;
  font-weight: 300;
  text-transform: capitalize;
  letter-spacing: 0.4px;
}

.btn-order {
  color: white;
  background-color: #004c40;
  transition: 0.3s;
  font-family: "TangoSans";
}

.btn-order:hover,
.btn-order:active {
  color: #004c40;
  background-color: white;
  border-color: #004c40;
}

.img-logo {
  height: 100px;
}
</style>
