<template>
  <section class="banner">
    <b-container class="d-flex justify-content-center">
      <b-col cols="12" class="deconnection-container align-item-center">
        <h2>Déconnexion</h2>
        <p>Êtes-vous sûr de vouloir vous déconnecter ?</p>
        <div class="button-container">
          <button @click="logout" class="btn btn-lg btn-danger">
            Se déconnecter
          </button>
        </div>
      </b-col>
    </b-container>
  </section>
</template>

<script>
import { userState } from "@/utils/store";
import { useRouter } from "vue-router/composables";
export default {
  setup() {
    const router = useRouter();
    const logout = () => {
      userState.clearUser();
      // eslint-disable-next-line
      router.push("/").catch((error) => { });
    };
    return {
      logout,
    };
  },
};
</script>

<style scoped>
.deconnection-container {
  max-width: 600px;
  font-family: "TangoSans", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  background-color: white;
  border-radius: 5px;
  border: 2px solid rgba(0, 76, 64, 0.7);
  padding: 20px;
}

.banner {
  padding: 250px 0;
  background: url("../assets/meilleure-menus.png") center center fixed no-repeat;
  background-size: cover;
  color: black;
}

.button-container {
  margin-top: 20px; /* Adjust this value to increase/decrease space */
}

.btn {
  background-color: rgb(0, 76, 64);
  color: white;
  border: 1px solid rgb(0, 76, 64);
  transition: 0.2s ease-in-out;
}

.btn:hover {
  background-color: rgb(161, 201, 0);
  color: white;
  border: none;
  transition: 0.2s ease-in-out;
}
</style>
