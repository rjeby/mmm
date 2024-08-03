<template>
  <section class="banner">
    <b-container class="d-flex justify-content-center">
      <b-col cols="12" class="login-container align-item-center">
        <h2 class="form-title">Connexion</h2>
        <form @submit.prevent="submitForm" class="form">
          <div class="form-group">
            <label for="email" class="form-label">Adresse Email :</label>
            <input
              type="email"
              id="email"
              v-model="email"
              @input="validateEmail"
              class="form-input"
              required
            />
            <div v-if="emailError" class="error">{{ emailError }}</div>
          </div>
          <div class="form-group">
            <label for="password" class="form-label">Mot de passe :</label>
            <input
              type="password"
              id="password"
              v-model="password"
              @input="validatePassword"
              class="form-input"
              required
            />
            <div v-if="passwordError" class="error">{{ passwordError }}</div>
          </div>
          <button type="submit" class="btn btn-lg">Se connecter</button>
          <div class="forget-password">
            <a href="#" @click="forgetPassword = true">Mot de passe oublié ?</a>
          </div>
        </form>
        <div
          v-if="successMessage"
          class="success"
          :style="{ backgroundColor: successColor }"
        >
          {{ successMessage }}
        </div>
      </b-col>

      <!-- Change Password Modal -->
      <div v-if="forgetPassword" class="modal">
        <div class="modal-content">
          <span class="close" @click="close">&times;</span>
          <h2>Mot de passe oublié ?</h2>
          <form @submit.prevent="submitForgetPassword">
            <div class="form-group">
              <label for="change-email" class="form-label"
                >Adresse Email :</label
              >
              <input
                type="email"
                id="forget-email"
                v-model="resetEmail"
                @input="validateResetEmail"
                class="form-input"
                required
              />
              <div v-if="resetEmailError" class="error">
                {{ resetEmailError }}
              </div>
            </div>
            <button type="submit" class="btn btn-lg">Envoyer</button>
          </form>
          <div
            v-if="resetSuccessMessage"
            class="success"
            :style="{ backgroundColor: resetSuccessColor }"
          >
            {{ resetSuccessMessage }}
          </div>
        </div>
      </div>
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
    const resetEmail = ref("");
    const password = ref("");
    const emailError = ref("");
    const resetEmailError = ref("");
    const passwordError = ref("");
    const errorMessage = ref("");
    const successMessage = ref("");
    const resetSuccessMessage = ref("");
    const successColor = ref("");
    const resetSuccessColor = ref("");
    const forgetPassword = ref(false);
    const router = useRouter();

    const validateEmail = () => {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/i;
      emailError.value = re.test(email.value) ? "" : "Adresse email non valide";
    };

    const validateResetEmail = () => {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/i;
      resetEmailError.value = re.test(resetEmail.value)
        ? ""
        : "Adresse email non valide";
    };

    const validatePassword = () => {
      const re =
        /^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*])[\w!@#$%^&*]{8,}$/;
      passwordError.value = re.test(password.value)
        ? ""
        : "Le mot de passe doit contenir au moins 8 caractères, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial parmi !@#$%^&*";
    };

    const submitForm = async () => {
      try {
        if (emailError.value || passwordError.value) {
          return;
        }
        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/login`,
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
          // successMessage.value = 'Connexion réussie';
          // successColor.value = 'green'
          clearForm();
          userState.setUser(responseData);
          if (!responseData.is_confirmed) {
            // eslint-disable-next-line
            router.push("/inactive").catch((error) => { });
          } else if (!responseData.has_infos) {
            // eslint-disable-next-line
            router.push("/formulaire-inscription").catch((error) => { });
          } else {
            // eslint-disable-next-line
            router.push("/mes-meilleurs-menus").catch((error) => { });
          }
        }
      } catch (error) {
        successMessage.value = "Connection échoué: " + error.message;
        successColor.value = "red";
      }
    };

    const submitForgetPassword = async () => {
      try {
        if (resetEmailError.value) {
          return;
        }

        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/forgot-password`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email: resetEmail.value,
            }),
          }
        );
        const responseData = await response.json();
        if (!response.ok) {
          throw new Error(responseData.message);
        } else {
          clearForm();
          resetSuccessMessage.value =
            "Un email de réinitialisation a été envoyé à votre adresse";
          resetSuccessColor.value = "green";
        }
      } catch (error) {
        resetSuccessMessage.value = error.message;
        resetSuccessColor.value = "red";
      }
    };

    const clearForm = () => {
      resetEmail.value = "";
      email.value = "";
      password.value = "";
    };

    const close = () => {
      resetEmail.value = "";
      forgetPassword.value = false;
      resetSuccessMessage.value = "";
    };

    return {
      userState,
      email,
      emailError,
      resetEmail,
      password,
      passwordError,
      errorMessage,
      resetEmailError,
      successMessage,
      successColor,
      forgetPassword,
      resetSuccessMessage,
      resetSuccessColor,
      close,
      validateEmail,
      validateResetEmail,
      validatePassword,
      submitForm,
      submitForgetPassword,
    };
  },
};
</script>

<style scoped>
.login-container {
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

.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 500px;
  border-radius: 10px;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.forget-password {
  margin-top: 10px;
  text-align: center;
}

.forget-password a {
  color: #007bff;
  text-decoration: none;
}

.forget-password a:hover {
  text-decoration: underline;
}
</style>
