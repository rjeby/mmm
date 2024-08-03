<template>
  <section class="banner">
    <b-container class="d-flex justify-content-center">
      <b-col cols="12" class="inscription-container">
        <div>
          <h2 class="form-title">Inscription</h2>
          <form @submit.prevent="submitForm" class="form">
            <div class="form-group">
              <label for="email" class="form-label">Adresse Email :</label>
              <input
                type="email"
                id="email"
                v-model="email"
                class="form-input"
                @input="validateEmail"
                required
              />
              <div v-if="emailError" class="error">{{ emailError }}</div>
            </div>
            <div class="form-group">
              <label for="password" class="form-label"
                >Mot de passe
                <a
                  href="#"
                  class="infos"
                  v-b-popover.hover.top="
                    `Le mot de passe doit contenir au moins 8 caractères, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial parmi !@#$%^&*`
                  "
                  title="Mot de passe"
                  >?</a
                >:</label
              >
              <input
                type="password"
                id="password"
                v-model="password"
                class="form-input"
                @input="validatePassword"
                required
              />
              <div v-if="passwordError" class="error">{{ passwordError }}</div>
            </div>
            <div class="form-group">
              <label for="confirmPassword" class="form-label"
                >Confirmer le mot de passe :</label
              >
              <input
                type="password"
                id="confirmPassword"
                v-model="confirmPassword"
                class="form-input"
                @input="validateConfirmPassword"
                required
              />
              <div v-if="confirmPasswordError" class="error">
                {{ confirmPasswordError }}
              </div>
            </div>
            <button type="submit" class="btn btn-lg">S'inscrire</button>
            <div class="existing-account">
              <a class="existing-account-a" href="#"
                >Vous avez déja un compte ?
                <router-link class="hover-underline" to="/connection"
                  >Se connecter</router-link
                ></a
              >
            </div>
          </form>
          <div
            v-if="successMessage"
            class="success"
            :style="{ backgroundColor: successColor }"
          >
            {{ successMessage }}
          </div>
        </div>
      </b-col>
    </b-container>
  </section>
</template>

<script>
import { ref } from "vue";
import { userState } from "@/utils/store";
import { useRouter } from "vue-router/composables";

export default {
  setup() {
    const email = ref("");
    const password = ref("");
    const confirmPassword = ref("");
    const emailError = ref("");
    const passwordError = ref("");
    const confirmPasswordError = ref("");
    const successMessage = ref("");
    const successColor = ref("");
    const router = useRouter();

    const validateEmail = () => {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/i;
      emailError.value = re.test(email.value) ? "" : "Adresse email non valide";
    };

    const validatePassword = () => {
      const re =
        /^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*])[\w!@#$%^&*]{8,}$/;
      passwordError.value = re.test(password.value)
        ? ""
        : "Le mot de passe doit contenir au moins 8 caractères, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial parmi !@#$%^&*";
    };

    const validateConfirmPassword = () => {
      confirmPasswordError.value =
        password.value === confirmPassword.value
          ? ""
          : "Les mots de passe ne correspondent pas";
    };

    const submitForm = async () => {
      validateEmail();
      validatePassword();
      validateConfirmPassword();

      if (
        emailError.value ||
        passwordError.value ||
        confirmPasswordError.value
      ) {
        return;
      }

      try {
        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/register`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email: email.value,
              password: password.value,
            }),
          }
        );

        const responseData = await response.json();
        if (!response.ok) {
          throw new Error(responseData.message);
        } else {
          // successMessage.value = 'Inscription réussie';
          // successColor.value = 'green';
          clearForm();
          // Redirect the user directly to the inactive view after registering
          userState.setUser(responseData);
          // eslint-disable-next-line
          router.push("/inactive").catch((error) => { });
        }
      } catch (error) {
        successMessage.value = "Échec de l'inscription: " + error.message;
        successColor.value = "red";
      }
    };

    const clearForm = () => {
      email.value = "";
      password.value = "";
      confirmPassword.value = "";
    };

    return {
      email,
      password,
      confirmPassword,
      emailError,
      passwordError,
      confirmPasswordError,
      successMessage,
      successColor,
      validateEmail,
      validatePassword,
      validateConfirmPassword,
      submitForm,
    };
  },
};
</script>

<style scoped>
.inscription-container {
  max-width: 600px;

  font-family: "TangoSans", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  padding: 16px;
  background-color: white;
  border-radius: 5px;
  border: 2px solid rgba(0, 76, 64, 0.7);
}

/* .signup-form {
  max-width: 400px;
  margin: 200px auto;
} */

.form-title {
  text-align: center;
}

.banner {
  padding-top: 250px;
  background: url("../assets/meilleure-menus.png") center center fixed no-repeat;
  background-size: cover;

  color: black;
}

/* Media query for phone-sized screens */
@media only screen and (max-width: 991px) {
  .banner {
    padding-bottom: 250px;
  }
}

.form {
  /* background-color: #f4f4f4; */
  padding: 20px;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 20px;
}

.form-title {
  text-align: center;
  font-family: "Amanise";
  font-weight: 500;
  font-size: clamp(33px, 2vw + 26px, 48px);
  padding: 10px;
}

.form-label {
  display: block;
  margin-bottom: 5px;
}

.form-input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn {
  background-color: rgb(0, 76, 64);

  color: white;
  border: 1px solid rgb(0, 76, 64);
  transition: 0.2s ease-in-out;

  border: none;
}

.btn:hover {
  background-color: rgb(161, 201, 0);
  color: white;
  border: none;
  transition: 0.2s ease-in-out;
}

.error,
.success {
  margin-top: 10px;
  padding: 10px;
  border-radius: 5px;
}

.error {
  background-color: #f44336;
  color: white;
}

.success {
  color: white;
}

.existing-account {
  margin-top: 10px;
  text-align: center;
}

.existing-account-a {
  color: #004c40;
  text-decoration: none;
}

.hover-underline {
  color: #007bff;
  text-decoration: none;
}
.hover-underline:hover {
  text-decoration: underline;
}
</style>
