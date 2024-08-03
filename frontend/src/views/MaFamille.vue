<template>
  <section class="banner">
    <b-container>
      <div class="form-container p-3">
        <h1 class="form-title">
          Ma Famille
          <a
            href="#"
            class="infos"
            v-b-popover.hover.top="'Vous pouvez ajouter au maximum 5 personnes'"
            title="Ma Famille"
            >?</a
          >:
        </h1>
        <form @submit.prevent="submitForm">
          <b-row class="d-flex justify-content-center">
            <b-col cols="10">
              <div>
                <div v-if="!members.length">
                  <h2 class="tangosans">
                    Vous n'avez ajouter aucune personne jusqu'à présent!
                  </h2>
                </div>
                <div
                  v-for="(member, index) in members"
                  :key="index"
                  class="associated-member"
                >
                  <h3>Personne n°{{ index + 1 }}</h3>
                  <div>
                    <label>Mon Prénom:</label>
                    <input
                      type="text"
                      v-model="member.prenom"
                      @input="validatePrenom(member)"
                      :disabled="!isEditable"
                      required
                    />
                    <span v-if="member.errors.prenom">{{
                      member.errors.prenom
                    }}</span>
                  </div>
                  <div>
                    <label>Mon Genre:</label>
                    <select
                      v-model="member.genre"
                      :disabled="!isEditable"
                      required
                    >
                      <option value="homme">Homme</option>
                      <option value="femme">Femme</option>
                    </select>
                  </div>
                  <div>
                    <label>Mon Année de Naissance:</label>
                    <input
                      type="number"
                      v-model="member.annee_naissance"
                      @input="validateAnnee(member)"
                      lang="fr"
                      :disabled="!isEditable"
                      required
                    />
                    <span v-if="member.errors.annee">{{
                      member.errors.annee
                    }}</span>
                  </div>
                  <div>
                    <label>Ma Taille (cm):</label>
                    <input
                      type="number"
                      v-model="member.taille"
                      @input="validateTaille(member)"
                      :disabled="!isEditable"
                      required
                    />
                    <span v-if="member.errors.taille">{{
                      member.errors.taille
                    }}</span>
                  </div>
                  <div>
                    <label>Mon Poids (kg):</label>
                    <input
                      type="number"
                      v-model="member.poids"
                      @input="validatePoids(member)"
                      :disabled="!isEditable"
                      required
                    />
                    <span v-if="member.errors.poids">{{
                      member.errors.poids
                    }}</span>
                  </div>
                  <div>
                    <label>Est-ce que je veux perdre du poids:</label>
                    <select
                      v-model="member.perdre_poids"
                      :disabled="!isEditable"
                      required
                    >
                      <option value="1 kg/mois">
                        Oui, je souhaite perdre 1 kg/mois
                      </option>
                      <option value="non">
                        Non, j'ai déja mon poids de forme
                      </option>
                    </select>
                  </div>
                  <div>
                    <label
                      >La Durée Moyenne de Mon Activité Physique Légère (heures
                      par jour):</label
                    >
                    <select
                      v-model="member.activite_legere"
                      :disabled="!isEditable"
                      required
                    >
                      <option
                        v-for="time in activityTimes"
                        :key="time"
                        :value="time"
                      >
                        {{ time }}
                      </option>
                    </select>
                  </div>
                  <div>
                    <label
                      >La Durée Moyenne de Mon Activité Physique Modéré (heures
                      par jour):</label
                    >
                    <select
                      v-model="member.activite_moyenne"
                      :disabled="!isEditable"
                      required
                    >
                      <option
                        v-for="time in activityTimes"
                        :key="time"
                        :value="time"
                      >
                        {{ time }}
                      </option>
                    </select>
                  </div>
                  <div>
                    <label
                      >La Durée Moyenne de Mon Activité Physique Élevée (heures
                      par jour):</label
                    >
                    <select
                      v-model="member.activite_elevee"
                      :disabled="!isEditable"
                      required
                    >
                      <option
                        v-for="time in activityTimes"
                        :key="time"
                        :value="time"
                      >
                        {{ time }}
                      </option>
                    </select>
                  </div>
                  <button
                    class="btn"
                    type="button"
                    @click="removeMember(index)"
                    v-if="isEditable && members.length > 0"
                    :disabled="!isEditable"
                  >
                    Supprimer l'inscription de cette personne
                  </button>
                </div>
                <b-row class="mb-2">
                  <b-col>
                    <button
                      class="btn"
                      type="button"
                      @click="addMember"
                      v-if="isEditable && members.length < 5"
                    >
                      Ajouter une Personne
                    </button>
                  </b-col>
                </b-row>
                <b-row class="m-2">
                  <b-col class="d-flex justify-content-center">
                    <b-button
                      class="btn text-nowrap me-2"
                      type="button"
                      @click="cancelEdit"
                      v-if="isEditable"
                      >Annuler</b-button
                    >
                    <b-button
                      class="btn text-nowrap"
                      type="button"
                      @click="toggleEdit"
                    >
                      {{ isEditable ? "Sauvegarder" : "Modifier" }}
                    </b-button>
                  </b-col>
                </b-row>
              </div>
              <div
                v-if="success.message"
                class="success"
                :style="{ backgroundColor: success.color }"
              >
                {{ success.message }}
              </div>
            </b-col>
          </b-row>
        </form>
      </div>
    </b-container>
  </section>
</template>
<script>
import { onMounted, ref } from "vue";
import { userState } from "@/utils/store";

export default {
  setup() {
    const isEditable = ref(false);
    const success = ref({
      message: "",
      color: "",
    });
    const currentYear = new Date().getFullYear();
    const members = ref([]);
    const membersCopy = ref([]);
    const activityTimes = [
      "0 min",
      "15 min",
      "30 min",
      "1 heure",
      "1 heure 30 min",
      "2 heures",
      "3 heures",
      "4 heures",
    ];

    const validatePrenom = (member) => {
      if (!/^[a-z\-'\s]{1,128}$/i.test(member.prenom)) {
        member.errors.prenom = "Prénom invalide";
      } else {
        member.errors.prenom = "";
      }
    };

    const validateTaille = (member) => {
      const taille = member.taille;
      if (isNaN(taille) || taille < 50 || taille > 220) {
        member.errors.taille =
          "Taille invalide. La taille doit être un nombre entre 50 et 220 cm";
      } else {
        member.errors.taille = "";
      }
    };

    const validatePoids = (member) => {
      const poids = member.poids;
      if (isNaN(poids) || poids < 5 || poids > 150) {
        member.errors.poids =
          "Poids invalide. Le poids doit être un nombre entre 5 et 150 kg";
      } else {
        member.errors.poids = "";
      }
    };

    const validateAnnee = (member) => {
      const annee = member.annee_naissance;
      if (
        isNaN(annee) ||
        annee < currentYear - 114 ||
        annee > currentYear - 3
      ) {
        member.errors.annee = `L'année de naissance doit être un nombre entre ${
          currentYear - 114
        } et ${currentYear - 3}`;
      } else {
        member.errors.annee = "";
      }
    };

    const validateMember = (member) => {
      validatePrenom(member);
      validatePoids(member);
      validateTaille(member);
      validateAnnee(member);
      return (
        !member.errors.prenom &&
        !member.errors.taille &&
        !member.errors.poids &&
        !member.errors.annee &&
        member.genre &&
        member.perdre_poids &&
        member.activite_legere &&
        member.activite_moyenne &&
        member.activite_elevee
      );
    };

    const validateMembers = () => {
      return members.value.every((member) => validateMember(member));
    };

    const addMember = () => {
      if (members.value.length < 5) {
        members.value.push({
          prenom: "",
          genre: "",
          annee_naissance: "",
          taille: null,
          poids: null,
          activite_legere: "",
          activite_moyenne: "",
          activite_elevee: "",
          perdre_poids: "",
          errors: {
            prenom: "",
            taille: "",
            poids: "",
            annee: "",
          },
        });
      }
    };

    const removeMember = (index) => {
      members.value.splice(index, 1);
    };

    const toggleEdit = () => {
      if (!isEditable.value) {
        isEditable.value = true;
      } else {
        if (validateMembers()) {
          membersCopy.value = JSON.parse(JSON.stringify(members.value));
          isEditable.value = false;
          submitForm();
        }
      }
    };

    const cancelEdit = () => {
      isEditable.value = false;
      members.value = JSON.parse(JSON.stringify(membersCopy.value));
    };

    const submitForm = async () => {
      try {
        const body = JSON.parse(JSON.stringify(members.value));
        body.every((member) => delete member.errors);
        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/ma-famille`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
              Authorization: userState.token,
            },
            body: JSON.stringify(body),
          }
        );
        const responseData = await response.json();
        if (!response.ok) {
          throw new Error(responseData.message);
        }
      } catch (error) {
        // Handle errors
        success.value.color = "red";
        success.value.message = "Échec: " + error.message;
      }
    };

    onMounted(async () => {
      try {
        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/ma-famille`,
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
        } else {
          const parsedData = JSON.parse(JSON.stringify(responseData));
          parsedData.every(
            (member) =>
              (member.errors = {
                prenom: "",
                taille: "",
                poids: "",
                annee: "",
              })
          );
          members.value = parsedData;
          membersCopy.value = parsedData;
        }
      } catch (error) {
        // Handle errors
        success.value.color = "red";
        success.value.message = "Échec: " + error.message;
      }
    });

    return {
      success,
      currentYear,
      members,
      activityTimes,
      isEditable,
      validatePrenom,
      validateAnnee,
      validatePoids,
      validateTaille,
      addMember,
      removeMember,
      cancelEdit,
      toggleEdit,
      submitForm,
    };
  },
};
</script>

<style scoped>
.form-container {
  font-family: "TangoSans", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.banner {
  padding-top: 250px;
  padding-bottom: 50px;
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

form {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  padding: 16px;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 5px;
}

/* Form title */
.form-title {
  text-align: center;
  font-family: "Amanise";
  font-weight: 500;
  font-size: clamp(35px, 2vw + 26px, 48px);
  padding: 10px;
}

/* Section titles */
h2 {
  font-size: clamp(18px, 2vw + 8px, 32px);
  margin-top: 20px;
  color: #555;
}

h3 {
  margin-top: 10px;
  color: #666;
}

/* Form labels */
label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

/* Form inputs */
input[type="text"],
input[type="date"],
input[type="number"],
input[type="tel"],
select {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

/* Error messages */
span {
  display: block;
  color: red;
  margin-top: -8px;
  margin-bottom: 10px;
}

/* Form buttons */
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

/* Associated members section */
.associated-member {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  background-color: #f1f1f1;
}

.success {
  margin-top: 10px;
  padding: 10px;
  border-radius: 5px;
  color: white;
}

.button-container {
  display: flex;
  justify-content: center;
  gap: 10px;
  /* Adjusts the spacing between the buttons */
}

.infos {
  color: red;
}
</style>
