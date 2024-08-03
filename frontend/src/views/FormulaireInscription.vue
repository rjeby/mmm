<template>
  <section class="banner">
    <b-container>
      <b-card class="form-container p-3">
        <h1 class="amanise p-4">Formulaire d'inscription</h1>
        <form @submit.prevent="submitForm">
          <b-row class="d-flex justify-content-center">
            <b-col cols="10">
              <h2 class="amanise p-4">
                Mes informations pour personnaliser Mes Meilleurs Menus
              </h2>
              <div>
                <label>Mon Prénom:</label>
                <input
                  type="text"
                  v-model="user.prenom"
                  @input="validatePrenom(user)"
                  required
                />
                <span v-if="user.errors.prenom">{{ user.errors.prenom }}</span>
              </div>
              <div>
                <label>Mon Genre:</label>
                <select v-model="user.genre" required>
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
                  required
                />
                <span v-if="user.errors.code_postal">{{
                  user.errors.code_postal
                }}</span>
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
                  required
                />
                <span v-if="user.errors.annee">{{ user.errors.annee }}</span>
              </div>
              <div>
                <label>Ma Taille (cm):</label>
                <input
                  type="number"
                  v-model="user.taille"
                  @input="validateTaille(user)"
                  required
                />
                <span v-if="user.errors.taille">{{ user.errors.taille }}</span>
              </div>
              <div>
                <label>Mon Poids (kg):</label>
                <input
                  type="number"
                  v-model="user.poids"
                  @input="validatePoids(user)"
                  required
                />
                <span v-if="user.errors.poids">{{ user.errors.poids }}</span>
              </div>
              <div>
                <label>Est-ce que je veux perdre du poids:</label>
                <select v-model="user.perdre_poids" required>
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
                <select v-model="user.activite_legere" required>
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
                <select v-model="user.activite_moyenne" required>
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
                <select v-model="user.activite_elevee" required>
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
                <h2 v-if="members.length" class="amanise p-4">
                  Ma famille
                  <a
                    href="#"
                    class="infos"
                    v-b-popover.hover.top="
                      'Vous pouvez ajouter au maximum 5 personnes'
                    "
                    title="Ma Famille"
                    >?</a
                  >:
                </h2>
                <div
                  v-for="(member, index) in members"
                  :key="index"
                  class="associated-member"
                >
                  <h3>Personne n° {{ index + 1 }}</h3>
                  <div>
                    <label>Mon Prénom:</label>
                    <input
                      type="text"
                      v-model="member.prenom"
                      @input="validatePrenom(member)"
                      required
                    />
                    <span v-if="member.errors.prenom">{{
                      member.errors.prenom
                    }}</span>
                  </div>
                  <div>
                    <label>Mon Genre:</label>
                    <select v-model="member.genre" required>
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
                      required
                    />
                    <span v-if="member.errors.poids">{{
                      member.errors.poids
                    }}</span>
                  </div>
                  <div>
                    <label>Est-ce que je veux perdre du poids:</label>
                    <select v-model="member.perdre_poids" required>
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
                    <select v-model="member.activite_legere" required>
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
                    <select v-model="member.activite_moyenne" required>
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
                    <select v-model="member.activite_elevee" required>
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
                    type="button"
                    @click="removeMember(index)"
                    v-if="members.length > 0"
                  >
                    Supprimer l'inscription de cette personne
                  </button>
                </div>
                <div class="button-container">
                  <button
                    type="button"
                    @click="addMember"
                    v-if="members.length < 5"
                  >
                    Ajouter une personne
                  </button>
                  <button type="submit">Soumettre</button>
                </div>
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
      </b-card>
    </b-container>
  </section>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router/composables";
import data from "@/data/CodePostalCommune.json";
import { userState } from "@/utils/store";

export default {
  setup() {
    const router = useRouter();
    const success = ref({
      message: "",
      color: "",
    });
    const user = ref({
      prenom: "",
      genre: "homme",
      annee_naissance: null,
      taille: null,
      poids: null,
      activite_legere: "0 min",
      activite_moyenne: "0 min",
      activite_elevee: "0 min",
      perdre_poids: "non",
      code_postal: null,
      errors: {
        prenom: "",
        taille: "",
        poids: "",
        annee: "",
        code_postal: "",
      },
    });
    const filteredCommunes = ref([]);

    const currentYear = new Date().getFullYear();

    const members = ref([]);
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
      return (
        !member.errors.prenom &&
        !member.errors.taille &&
        !member.errors.poids &&
        !member.errors.annee
      );
    };

    const validateUser = () => {
      return (
        !user.value.errors.prenom &&
        !user.value.errors.taille &&
        !user.value.errors.poids &&
        !user.value.errors.annee &&
        !user.value.errors.code_postal
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

    const filterCommunes = () => {
      if (!isNaN(user.value.code_postal)) {
        user.value.errors.code_postal = "";
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
            user.value.errors.code_postal =
              "Veuillez entrer un code postal valide";
          }
        }
      } else {
        filteredCommunes.value = [];
        user.value.errors.code_postal = "Veuillez entrer un code postal valide";
      }
    };

    const submitForm = async () => {
      if (validateUser() && validateMembers()) {
        try {
          const membres_famille = members.value.map(
            // eslint-disable-next-line no-unused-vars
            ({ errors, ...rest }) => rest
          );
          const response = await fetch(
            `${process.env.VUE_APP_API_URL}/api/formulaire-inscription`,
            {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                Authorization: userState.token,
              },
              body: JSON.stringify({
                prenom: user.value.prenom,
                genre: user.value.genre,
                annee_naissance: user.value.annee_naissance,
                taille: user.value.taille,
                poids: user.value.poids,
                activite_legere: user.value.activite_legere,
                activite_moyenne: user.value.activite_moyenne,
                activite_elevee: user.value.activite_elevee,
                perdre_poids: user.value.perdre_poids,
                code_postal: user.value.code_postal,
                membres_famille: membres_famille,
              }),
            }
          );

          const responseData = await response.json();
          if (!response.ok) {
            throw new Error(responseData.message);
          } else {
            userState.hasInfos = true;
            // eslint-disable-next-line
            router.push("/mes-meilleurs-menus").catch((error) => { });
          }
        } catch (error) {
          success.value.color = "red";
          success.value.message = "Échec: " + error.message;
        }
      } else {
        success.value.color = "red";
        success.value.message =
          "Échec: Veuillez vérifier les informations saisies";
      }
    };

    return {
      user,
      members,
      activityTimes,
      success,
      currentYear,
      filteredCommunes,
      filterCommunes,
      validatePrenom,
      validateTaille,
      validatePoids,
      validateAnnee,
      addMember,
      removeMember,
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
  padding-top: 200px;
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
  background-color: white;
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
button {
  padding: 10px 20px;
  margin-top: 10px;
  border: none;
  border-radius: 5px;
  background-color: green;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

/* Button hover effect */
button:hover {
  background-color: #0056b3;
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
