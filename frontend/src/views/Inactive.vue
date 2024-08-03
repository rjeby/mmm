<template>
  <div class="box">
    <div class="container">
      <h2>Activation de Compte Requise</h2>
      <p>
        Votre compte n'est pas encore activé. Veuillez vérifier votre boîte de
        réception pour l'e-mail d'activation et suivre les instructions.
      </p>
      <p>
        Si vous n'avez pas reçu l'e-mail d'activation, cliquez sur le bouton
        ci-dessous pour recevoir un nouveau lien d'activation.
      </p>
      <p class="text-danger text-center">
        Si vous avez activé votre compte, veuillez vous déconnecter en utilisant
        le bouton ci-dessous, puis vous reconnecter pour que le changement soit
        pris en compte.
      </p>
      <div class="button-group">
        <button
          class="btn btn-lg me-3"
          @click="sendActivationLink"
          :disabled="loading"
        >
          {{
            loading
              ? "Veuillez vérifier votre boîte mail..."
              : "Envoyer un nouveau lien d'activation"
          }}
        </button>
        <button class="btn btn-lg" @click="logout">Se déconnecter</button>
      </div>
      <p v-if="message">{{ message }}</p>
    </div>
  </div>
</template>

<script>
import { userState } from "@/utils/store";
import { useRouter } from "vue-router/composables";
import { ref } from "vue";

export default {
  setup() {
    const loading = ref(false);
    const message = ref("");
    const router = useRouter();

    const logout = () => {
      userState.clearUser();
      // eslint-disable-next-line
      router.push("/").catch((error) => { });
    };

    const sendActivationLink = async () => {
      loading.value = true;
      message.value = "";

      try {
        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/resend`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              Authorization: userState.token,
            },
          }
        );
        const responseData = await response.json();
        if (!response.ok) {
          throw new Error(responseData.message);
        }
      } catch (error) {
        message.value = "Opération échoué: " + error.message;
      }
    };

    return {
      loading,
      message,
      logout,
      sendActivationLink,
    };
  },
};
</script>

<style scoped>
.box {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

.button-group {
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  background-color: #ffffff;
  padding: 100px;
  border: 1px solid #dddddd;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
h2 {
  color: #333333;
}
button {
  padding: 10px 20px;
  font-size: 16px;
  color: #ffffff;
  background-color: green;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
p {
  color: #666666;
}
</style>
