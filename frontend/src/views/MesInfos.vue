<template>
  <section class="banner">
    <b-container>
      <div class="form-container p-3">
        <h1 class="amanise p-4">
          Mes informations pour personnaliser Mes Meilleurs Menus
        </h1>
        <div class="button-group">
          <button
            class="btn btn-lg"
            type="button"
            @click="cancelEdit"
            v-if="isEditable"
          >
            Annuler
          </button>
          <button class="btn btn-lg" type="button" @click="toggleEdit">
            {{ isEditable ? "Sauvegarder" : "Modifier" }}
          </button>
        </div>
        <form @submit.prevent="submitForm">
          <b-row class="d-flex justify-content-center">
            <b-col cols="10">
              <div>
                <label>Mon Prénom:</label>
                <input
                  type="text"
                  v-model="user.prenom"
                  @input="validatePrenom(user)"
                  :disabled="!isEditable"
                  required
                />
                <span v-if="errors.prenom">{{ errors.prenom }}</span>
              </div>
              <div>
                <label>Mon Genre:</label>
                <select v-model="user.genre" :disabled="!isEditable" required>
                  <option value="homme">Homme</option>
                  <option value="femme">Femme</option>
                </select>
              </div>
              <div>
                <label for="search-input" class="search-label"
                  >Mon Code Postal:</label
                >
                <input
                  list="search-input"
                  type="text"
                  v-model="user.code_postal"
                  @input="filterCommunes"
                  placeholder="Entrer un code postal..."
                  :disabled="!isEditable"
                  required
                />
                <span v-if="errors.code_postal">{{ errors.code_postal }}</span>
                <datalist id="search-input">
                  <option
                    v-for="(commune, index) in filteredCommunes.slice(0, 10)"
                    :key="index"
                    :value="commune.Code_postal"
                  >
                    {{ commune.Code_postal }} : {{ commune.Nom_de_la_commune }}
                  </option>
                </datalist>
              </div>
              <div>
                <label>Mon Année de Naissance:</label>
                <input
                  type="number"
                  v-model="user.annee_naissance"
                  @input="validateAnnee(user)"
                  lang="fr"
                  :disabled="!isEditable"
                  required
                />
                <span v-if="errors.annee">{{ errors.annee }}</span>
              </div>
              <div>
                <label>Ma Taille (cm):</label>
                <input
                  type="number"
                  v-model="user.taille"
                  @input="validateTaille(user)"
                  :disabled="!isEditable"
                  required
                />
                <span v-if="errors.taille">{{ errors.taille }}</span>
              </div>
              <div>
                <label>Mon Poids (kg):</label>
                <input
                  type="number"
                  v-model="user.poids"
                  @input="validatePoids(user)"
                  :disabled="!isEditable"
                  required
                />
                <span v-if="errors.poids">{{ errors.poids }}</span>
              </div>
              <div>
                <label>Est-ce que je veux perdre du poids:</label>
                <select
                  v-model="user.perdre_poids"
                  :disabled="!isEditable"
                  required
                >
                  <option value="1 kg/mois">
                    Oui, je souhaite perdre 1 kg/mois
                  </option>
                  <option value="non">Non, j'ai déja mon poids de forme</option>
                </select>
              </div>
              <div>
                <label
                  >La Durée Moyenne de Mon Activité Physique Légère (heures par
                  jour):
                  <a
                    href="#"
                    class="infos"
                    v-b-popover.hover.top="
                      'Estimation du temps moyen de mon activité physique légère par jour (exemple: position debout: attente passive, cuisiner, travail statique ): '
                    "
                    title="La Durée Moyenne de Mon Activité Physique Légère (heures par jour)"
                    >?</a
                  >:</label
                >
                <select
                  v-model="user.activite_legere"
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
                  >La Durée Moyenne de Mon Activité Physique Modéré (heures par
                  jour):
                  <a
                    href="#"
                    class="infos"
                    v-b-popover.hover.top="
                      'Estimation du temps moyen de mon activité physique modéré par jour (exemple: industrie de production, menuiserie, yoga, marche,...): '
                    "
                    title="La Durée Moyenne de Mon Activité Physique Modéré (heures par jour)"
                    >?</a
                  >:</label
                >
                <select
                  v-model="user.activite_moyenne"
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
                  >La Durée Moyenne de Mon Activité Physique Élevée (heures par
                  jour):
                  <a
                    href="#"
                    class="infos"
                    v-b-popover.hover.top="
                      'Estimation du temps moyen de mon activité physique intensif par jour (exemple: travaux du bâtiment, bêchage, ménage intensif, sport en compétition, footing...) '
                    "
                    title="La Durée Moyenne de Mon Activité Physique Élevée (heures par jour)"
                    >?</a
                  >:</label
                >
                <select
                  v-model="user.activite_elevee"
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
import data from "@/data/CodePostalCommune.json";

export default {
  setup() {
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
    const filteredCommunes = ref([]);
    const isEditable = ref(false);
    const currentYear = new Date().getFullYear();

    const success = ref({
      message: "",
      color: "",
    });

    const errors = ref({
      prenom: "",
      taille: "",
      poids: "",
      annee: "",
      code_postal: "",
    });
    const user = ref({
      prenom: "",
      genre: "",
      annee_naissance: null,
      taille: null,
      poids: null,
      activite_legere: null,
      activite_moyenne: null,
      activite_elevee: null,
      perdre_poids: null,
      code_postal: null,
    });

    const userCopy = ref({});

    const validatePrenom = (member) => {
      if (!/^[a-z\-'\s]{1,128}$/i.test(member.prenom)) {
        errors.value.prenom = "Prénom invalide";
      } else {
        errors.value.prenom = "";
      }
    };

    const validateTaille = (member) => {
      const taille = member.taille;
      if (isNaN(taille) || taille < 50 || taille > 220) {
        errors.value.taille =
          "Taille invalide. La taille doit être un nombre entre 50 et 220 cm";
      } else {
        errors.value.taille = "";
      }
    };

    const validatePoids = (member) => {
      const poids = member.poids;
      if (isNaN(poids) || poids < 5 || poids > 150) {
        errors.value.poids =
          "Poids invalide. Le poids doit être un nombre entre 5 et 150 kg";
      } else {
        errors.value.poids = "";
      }
    };

    const validateAnnee = (member) => {
      const annee = member.annee_naissance;
      if (
        isNaN(annee) ||
        annee < currentYear - 114 ||
        annee > currentYear - 3
      ) {
        errors.value.annee = `L'année de naissance doit être un nombre entre ${
          currentYear - 114
        } et ${currentYear - 3}`;
      } else {
        errors.value.annee = "";
      }
    };

    const validateUser = () => {
      return (
        !errors.value.prenom &&
        !errors.value.taille &&
        !errors.value.poids &&
        !errors.value.annee &&
        !errors.value.code_postal
      );
    };

    const filterCommunes = () => {
      if (!isNaN(user.value.code_postal)) {
        errors.value.code_postal = "";
        if (!user.value.code_postal) {
          filteredCommunes.value = [];
        } else {
          filteredCommunes.value = data.filter((commune) =>
            commune.Code_postal.toString().startsWith(
              user.value.code_postal.toString()
            )
          );
          if (
            !filteredCommunes.value.filter(
              (commune) =>
                commune.Code_postal === Number(user.value.code_postal)
            ).length
          ) {
            errors.value.code_postal = "Veuillez entrer un code postal valide";
          }
        }
      } else {
        filteredCommunes.value = [];
        errors.value.code_postal = "Veuillez entrer un code postal valide";
      }
    };

    const toggleEdit = () => {
      if (!isEditable.value) {
        isEditable.value = true;
      } else {
        if (validateUser()) {
          userCopy.value = { ...user.value };
          isEditable.value = false;
          submitForm();
        }
      }
    };

    const cancelEdit = () => {
      user.value.code_postal = "";
      isEditable.value = false;
      user.value = { ...userCopy.value };
      errors.value = {
        prenom: "",
        taille: "",
        poids: "",
        annee: "",
        code_postal: "",
      };
    };

    const submitForm = async () => {
      try {
        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/mes-infos`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
              Authorization: userState.token,
            },
            body: JSON.stringify(user.value),
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
          `${process.env.VUE_APP_API_URL}/api/mes-infos`,
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
          user.value = { ...responseData };
          userCopy.value = { ...responseData };
        }
      } catch (error) {
        // Handle errors
        success.value.color = "red";
        success.value.message = "Échec: " + error.message;
      }
    });

    return {
      user,
      success,
      activityTimes,
      currentYear,
      isEditable,
      filteredCommunes,
      errors,
      filterCommunes,
      validatePrenom,
      validateTaille,
      validatePoids,
      validateAnnee,
      validateUser,
      toggleEdit,
      cancelEdit,
    };
  },
};
</script>

<style scoped>
.form-container {
  font-family: "TangoSans";
  text-align: center;
  color: #2c3e50;
  border: none;
  background-color: none;
}

.banner {
  padding-top: 250px;
  padding-bottom: 50px;
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
h1 {
  text-align: center;
  color: #333;
}

/* Section titles */
h2 {
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

.button-group {
  display: flex;
  justify-content: space-between;
}

.button-group button {
  flex: 1;
  margin: 0 5px;
}

.infos {
  color: red;
}
</style>
