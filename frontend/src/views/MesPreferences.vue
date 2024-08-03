<template>
  <section class="banner">
    <b-container>
      <div class="preferences-container">
        <h1 class="amanise p-4">
          Mes Préférences Alimentaires
          <a
            href="#"
            class="infos"
            v-b-popover.hover.top="
              `Sans modification de votre part, les préférences choisies seront celles par défaut. Une fois que vous aurez choisi vos préférences, vous pourrez ensuite les modifier chaque semaine si vous le désirez. Une fois vos préférences enregistrées, chaque semaine, ces préférences seront retenues pour toutes les semaines de menus à venir.`
            "
            title="Mes Préférences Alimentaires"
            >?</a
          >:
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
          <!-- Choix du type d’alimentation -->
          <div>
            <div>
              <label for="type_alimentation">
                <h1 class="amanise p-4">
                  Type d'alimentation
                  <a
                    href="#"
                    class="infos"
                    v-b-popover.hover.top="
                      `Il vous sera toujours proposé une alimentation méditerranéenne, mais vous pouvez y rajouter différentes options : l'option végétarienne qui vous permettra de bénéficier d'une alimentation saine sans viande et sans poisson mais équilibrée en nutriments (notamment en vitamine B12, protéines, oméga-3 et en fer). L'option cétogène vous permettra de bénéficier d'une alimentation méditerranéenne mais limitée en sucre (maximum de 15 à 25 g par jour). Cette alimentation est équilibrée en nutriments (notamment au niveau des protéines, des apports caloriques, très riche en bons lipides, équilibrée en vitamines et minéraux). L'option limitée en sel vous garantit un apport limité en sodium et un apport modéré en phosphore chaque jour (maximum de 7 g de sodium pour les hommes et 6 g de sodium pour les femmes). L'alimentation à indice glycémique (IG) bas vous assure que l'ensemble des repas a un faible indice glycémique. Sans cocher cette case, une minorité de repas pourront avoir un IG moyen qui vous sera indiqué.`
                    "
                    title="Type d'alimentation"
                    >?</a
                  >:
                </h1>
              </label>
            </div>
            <div class="d-flex justify-content-center">
              <select
                class="d-flex justify-content-center customised-select"
                v-model="originalForm.type_alimentation"
                required
                :disabled="!isEditable"
              >
                <option
                  v-for="option in alimentationOptions"
                  :key="option.type"
                  :value="option.type"
                >
                  {{ option.type }}
                </option>
              </select>
            </div>
            <div class="d-flex justify-content-center p-1">
              <div class="card">
                <div class="card-body">
                  <p class="fw-bold text-decoration-underline">Description:</p>
                  <p>{{ getDescription(originalForm.type_alimentation) }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Choix multiples des éventuelles allergies -->
          <div>
            <label>
              <h1 class="amanise p-4">
                Allergies
                <a
                  href="#"
                  class="infos"
                  v-b-popover.hover.top="
                    `En cochant l'une de ces cases, vous êtes assuré(e) qu'aucun de ces ingrédients ne sera présent dans l'ensemble des plats de votre programme de menus.`
                  "
                  title="Allergies"
                  >?</a
                >:
              </h1>
            </label>
            <div class="horizontal-checkboxes">
              <div v-for="option in allergiesOptions" :key="option">
                <input
                  type="checkbox"
                  :value="option"
                  v-model="originalForm.allergies"
                  :disabled="!isEditable"
                />
                {{ option }}
              </div>
            </div>
          </div>

          <!-- Liste des ingrédients -->
          <div
            class="d-flex flex-column justify-content-center align-item-center"
          >
            <label for="search-input" class="search-label me-2">
              <h1 class="amanise p-4">
                Autres ingrédients que je veux exclure
                <a
                  href="#"
                  class="infos"
                  v-b-popover.hover.top="
                    `Vous pouvez supprimer jusqu'à 10 ingrédients qui ne seront jamais présents dans vos menus. Nos plats sont principalement à base de légumes, donc nous vous encourageons à limiter la suppression de légumes et à explorer de nouvelles préparations qui pourraient surprendre vos papilles. Si vous ne trouvez pas l'ingrédient que vous souhaitez supprimer, c'est qu'il n'apparaît pas dans nos menus.`
                  "
                  title="Liste des ingrédients"
                  >?</a
                >:
              </h1>
            </label>
            <div class="d-flex align-item-center justify-content-center">
              <input
                class="me-2"
                list="search-input"
                type="text"
                v-model="ingredient"
                @input="filterIngredients"
                placeholder="Saisir le nom d'un ingrédient..."
                required
                :disabled="!isEditable"
              />
              <datalist id="search-input">
                <option
                  v-for="(ingredient, index) in filteredIngredients.slice(
                    0,
                    10
                  )"
                  :key="index"
                  :value="ingredient.alim_nom_fr"
                >
                  {{ ingredient.nom }}
                </option>
              </datalist>
            </div>
            <div class="d-flex justify-content-center align-item-center m-1">
              <button
                class="btn me-2"
                type="button"
                @click="updateIngredientList"
                aria-label="Exclure"
                v-if="originalForm.ingredients_exclus.length < 10 && isEditable"
              >
                Exclure
              </button>
            </div>
          </div>

          <!-- Liste des ingrédients exclus -->

          <div>
            <h1 class="amanise p-4">
              Mes Ingrédients exclus
              <a
                href="#"
                class="infos"
                data-bs-toggle="popover"
                data-bs-trigger="hover focus"
                data-bs-content="Liste de tous les ingrédients que j'ai exclu."
                title="Mes Ingrédients Exclus"
              >
                ?
              </a>
              :
            </h1>
            <div class="dropdown">
              <button
                class="btn btn-order2 dropdown-toggle"
                type="button"
                id="dropdownMenuButton"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Ingrédients exclus
              </button>
              <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a
                  class="dropdown-item d-flex justify-content-between align-items-center"
                  v-if="!originalForm.ingredients_exclus.length"
                  >Vous n'avez pas d'ingrédients exclus</a
                >
                <a
                  class="dropdown-item d-flex justify-content-between align-items-center"
                  v-for="(ingredient, index) in originalForm.ingredients_exclus"
                  :key="index"
                >
                  <span>{{ ingredient.alim_nom_fr }}</span>
                  <span
                    v-if="isEditable"
                    class="delete-cross"
                    @click="removeExcludedIngredient(index)"
                    >x</span
                  >
                </a>
              </div>
            </div>
          </div>

          <!-- Choix du niveau de difficulté de préparation des menus -->
          <div>
            <label for="difficulte_menu">
              <h1 class="amanise p-4">
                Niveau de difficulté de préparation des menus
                <a
                  href="#"
                  class="infos"
                  v-b-popover.hover.top="
                    `La plupart de nos plats sont faciles à préparer. En cochant aussi la case (Moyenne), vous aurez à la fois des plats faciles et moyennement faciles à préparer. En cochant la case (Difficile), vous aurez accès à tous les plats, qu'ils soient faciles, moyens ou difficiles à préparer.`
                  "
                  title="Niveau de difficulté maximale"
                  >?</a
                >:
              </h1>
            </label>
          </div>

          <div class="d-flex justify-content-center">
            <select
              class="d-flex justify-content-center customised-select"
              v-model="originalForm.difficulte_menu"
              required
              :disabled="!isEditable"
            >
              <option
                v-for="option in difficulteOptions"
                :key="option"
                :value="option"
              >
                {{ option }}
              </option>
            </select>
          </div>

          <!-- Tableau des jours de la semaine et temps de préparation -->
          <div>
            <label class="me-3" for="temps-preparation">
              <h1 class="amanise p-4">
                Temps maximum de préparation (Repas / Jour)
                <a
                  href="#"
                  class="infos"
                  v-b-popover.hover.top="
                    `Ce temps représente le temps total de préparation d'un repas (entrée, plat, dessert), avec la cuisson. `
                  "
                  title="Temps maximum de préparation"
                  >?</a
                >:
              </h1>
            </label>
            <div class="table-responsive d-none d-sm-block">
              <table class="table table-striped table-hover">
                <thead>
                  <tr>
                    <th>Repas</th>
                    <th v-for="jour in joursSemaine" :key="jour">{{ jour }}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Déjeuner</td>
                    <td v-for="jour in joursSemaine" :key="jour + '-dejeuner'">
                      <b-form-select
                        v-model="
                          originalForm[jour.toLowerCase() + '_dejeuner_max']
                        "
                        :options="tempsOptions"
                        :disabled="!isEditable"
                        required
                      >
                      </b-form-select>
                    </td>
                  </tr>
                  <tr>
                    <td>Diner</td>
                    <td v-for="jour in joursSemaine" :key="jour + '-diner'">
                      <b-form-select
                        v-model="
                          originalForm[jour.toLowerCase() + '_diner_max']
                        "
                        :options="tempsOptions"
                        :disabled="!isEditable"
                        required
                      ></b-form-select>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="d-block d-sm-none">
              <div
                v-for="jour in joursSemaine"
                :key="jour + '-mobile'"
                class="mb-3"
              >
                <h5>{{ jour }}</h5>
                <table class="table table-bordered">
                  <thead>
                    <tr>
                      <th>Repas</th>
                      <th>Option</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Déjeuner</td>
                      <td>
                        <b-form-select
                          v-model="
                            originalForm[jour.toLowerCase() + '_dejeuner_max']
                          "
                          :options="tempsOptions"
                          :disabled="!isEditable"
                          required
                        ></b-form-select>
                      </td>
                    </tr>
                    <tr>
                      <td>Diner</td>
                      <td>
                        <b-form-select
                          v-model="
                            originalForm[jour.toLowerCase() + '_diner_max']
                          "
                          :options="tempsOptions"
                          :disabled="!isEditable"
                          required
                        ></b-form-select>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- Nombre de repas contenant de la viande par semaine -->
          <div>
            <div class="row p-1">
              <div class="d-flex justify-content-center">
                <label class="me-3" for="nbr_repas_viande_semaine">
                  <h1 class="amanise p-4">
                    Nombre de repas contenant de la viande par semaine :
                  </h1>
                </label>
              </div>
              <div class="d-flex justify-content-center">
                <select
                  class="customised-select"
                  v-model="originalForm.nbr_repas_viande_semaine"
                  required
                  :disabled="!isEditable"
                >
                  <option
                    v-for="option in repasViandeOptions"
                    :key="option"
                    :value="option"
                  >
                    {{ option }}
                  </option>
                </select>
              </div>
            </div>

            <!-- Nombre de repas contenant du poisson par semaine -->
            <div class="row p-1">
              <div class="d-flex justify-content-center">
                <label class="me-3" for="nbr_repas_poisson_semaine">
                  <h1 class="amanise p-4">
                    Nombre de repas contenant du poisson par semaine :
                  </h1>
                </label>
              </div>
              <div class="d-flex justify-content-center">
                <select
                  class="customised-select"
                  v-model="originalForm.nbr_repas_poisson_semaine"
                  required
                  :disabled="!isEditable"
                >
                  <option
                    v-for="option in repasPoissonOptions"
                    :key="option"
                    :value="option"
                  >
                    {{ option }}
                  </option>
                </select>
              </div>
            </div>

            <!-- Préférence pour manger la viande -->
            <div class="row p-1">
              <div class="d-flex justify-content-center">
                <label class="me-3" for="preference_viande">
                  <h1 class="amanise p-4">
                    Préférence pour manger la viande et le poisson :
                  </h1>
                </label>
              </div>
              <div class="d-flex justify-content-center">
                <select
                  class="customised-select"
                  v-model="originalForm.preference_viande"
                  required
                  :disabled="!isEditable"
                >
                  <option value="Midi">Midi</option>
                  <option value="Soir">Soir</option>
                </select>
              </div>
            </div>

            <!-- Petit déjeuner sucré et/ou salé -->
            <div class="row p-1">
              <div class="d-flex justify-content-center">
                <label class="me-3" for="petit_dejeuner">
                  <h1 class="amanise p-4">Petit déjeuner :</h1>
                </label>
              </div>
              <div class="d-flex justify-content-center">
                <select
                  class="customised-select"
                  v-model="originalForm.petit_dejeuner"
                  required
                  :disabled="!isEditable"
                >
                  <option value="Sucré">Sucré</option>
                  <option value="Salé">Salé</option>
                  <option value="Sucré et salé">Sucré et Salé</option>
                </select>
              </div>
            </div>

            <!-- Jour de la semaine pour les courses -->
            <div class="row p-1">
              <div>
                <label class="me-3" for="jour_courses">
                  <h1 class="amanise p-4">Jour des courses principales :</h1>
                </label>
              </div>
              <div class="d-flex justify-content-center">
                <select
                  class="customised-select"
                  v-model="originalForm.jour_courses"
                  required
                  :disabled="!isEditable"
                >
                  <option
                    v-for="option in jourOptions"
                    :key="option"
                    :value="option"
                  >
                    {{ option }}
                  </option>
                </select>
              </div>
            </div>

            <!-- Jour préféré de début de la semaine -->
            <div class="row p-1">
              <div>
                <label class="me-3" for="jour_debut_semaine">
                  <h1 class="amanise p-4">
                    Jour préféré de début de semaine
                    <a
                      href="#"
                      class="infos"
                      v-b-popover.hover.top="
                        `Ce sera le jour de début de vos semaines de menus. Il est préférable de commencer sa semaine 1 ou 2 jours après avoir réalisé ses courses.`
                      "
                      title="Jour préféré de début de semaine"
                      >?</a
                    >:
                  </h1>
                </label>
              </div>
              <div class="d-flex justify-content-center">
                <select
                  class="customised-select"
                  v-model="originalForm.jour_debut_semaine"
                  required
                  :disabled="!isEditable"
                >
                  <option
                    v-for="option in jourOptions"
                    :key="option"
                    :value="option"
                  >
                    {{ option }}
                  </option>
                </select>
              </div>
            </div>

            <!-- Jour préféré pour recevoir les menus -->
            <div class="row p-1">
              <div>
                <label class="me-3" for="jour_semaine_suivante">
                  <h1 class="amanise p-4">
                    Jour préféré pour recevoir les menus
                    <a
                      href="#"
                      class="infos"
                      v-b-popover.hover.top="
                        `Il est conseillé de recevoir le programme des menus 1 ou 2 jours avant le jour des courses.`
                      "
                      title="Jour préféré pour recevoir les menus"
                      >?</a
                    >:
                  </h1>
                </label>
              </div>
              <div class="d-flex justify-content-center">
                <select
                  class="customised-select"
                  v-model="originalForm.jour_semaine_suivante"
                  required
                  :disabled="!isEditable"
                >
                  <option
                    v-for="option in jourOptions"
                    :key="option"
                    :value="option"
                  >
                    {{ option }}
                  </option>
                </select>
              </div>
            </div>
          </div>
          <div
            v-if="success.message"
            class="success"
            :style="{ backgroundColor: success.color }"
          >
            {{ success.message }}
          </div>
        </form>
      </div>
    </b-container>
  </section>
</template>

<script>
import { ref, onMounted } from "vue";
import data from "@/data/Ciqual.json";
import { userState } from "@/utils/store";

export default {
  name: "PreferencesForm",
  setup() {
    const alimentationOptions = [
      {
        type: "Méditerranéene",
        description: `Il vous sera toujours proposé une alimentation méditerranéenne, mais vous pouvez y rajouter différentes options (Végétarienne, Cétogène, Limité en sel, À IG bas).`,
      },
      {
        type: "Végétarienne",
        description: `L'option végétarienne vous permettra de bénéficier d'une alimentation saine sans viande et sans poisson mais équilibrée en nutriments (notamment en vitamine B12, protéines, oméga-3 et en fer).`,
      },
      {
        type: "Cétogène",
        description: `L'option cétogène vous permettra de bénéficier d'une alimentation méditerranéenne mais limitée en sucre (maximum de 15 à 25 g par jour). Cette alimentation est équilibrée en nutriments (notamment au niveau des protéines, des apports caloriques, très riche en bons lipides, équilibrée en vitamines et minéraux).`,
      },
      {
        type: "Limité en sel",
        description: `L'option limitée en sel vous garantit un apport limité en sodium et un apport modéré en phosphore chaque jour (maximum de 7 g de sodium pour les hommes et 6 g de sodium pour les femmes).`,
      },
      {
        type: "À IG bas",
        description: ` L'alimentation à indice glycémique (IG) bas vous assure que l'ensemble des repas a un faible indice glycémique. Sans sélectionner cette case, une minorité de repas pourront avoir un IG moyen qui vous sera indiqué.`,
      },
    ];
    const allergiesOptions = [
      "Œufs",
      "Arachide",
      "Fruits à coque",
      "Gluten",
      "Lait de vache",
      "Poissons",
      "Crustacés",
      "Soja",
      "Céleri",
      "Moutarde",
      "Sésame",
    ];
    const difficulteOptions = ["Facile", "Moyenne", "Difficile"];
    const tempsOptions = [
      "20 min",
      "30 min",
      "40 min",
      "45 min",
      "50 min",
      "60 min",
      "75 min",
      "90 min",
    ];
    const jourOptions = [
      "Lundi",
      "Mardi",
      "Mercredi",
      "Jeudi",
      "Vendredi",
      "Samedi",
      "Dimanche",
    ];
    const joursSemaine = [
      "Lundi",
      "Mardi",
      "Mercredi",
      "Jeudi",
      "Vendredi",
      "Samedi",
      "Dimanche",
    ];
    const repasViandeOptions = [0, 1, 2, 3, 4];
    const repasPoissonOptions = [0, 1, 2, 3];

    const originalForm = ref({
      type_alimentation: "",
      allergies: [],
      difficulte_menu: "",
      lundi_dejeuner_max: "",
      lundi_diner_max: "",
      mardi_dejeuner_max: "",
      mardi_diner_max: "",
      mercredi_dejeuner_max: "",
      mercredi_diner_max: "",
      jeudi_dejeuner_max: "",
      jeudi_diner_max: "",
      vendredi_dejeuner_max: "",
      vendredi_diner_max: "",
      samedi_dejeuner_max: "",
      samedi_diner_max: "",
      dimanche_dejeuner_max: "",
      dimanche_diner_max: "",
      preference_viande: "",
      petit_dejeuner: "",
      jour_courses: "",
      jour_debut_semaine: "",
      jour_semaine_suivante: "",
      nbr_repas_viande_semaine: null,
      nbr_repas_poisson_semaine: null,
      ingredients_exclus: [],
    });

    const form = ref({});

    const ingredient = ref("");
    const filteredIngredients = ref([]);

    const isEditable = ref(false);
    const success = ref({
      message: "",
      color: "",
    });

    const getDescription = (type) => {
      const option = alimentationOptions.find((option) => option.type === type);
      return option ? option.description : "";
    };

    const filterIngredients = () => {
      if (ingredient.value) {
        filteredIngredients.value = data.filter(
          (aliment) =>
            aliment.alim_nom_fr
              .toLowerCase()
              .startsWith(ingredient.value.toLowerCase()) &&
            !originalForm.value.ingredients_exclus.some(
              (excl) => excl.alim_code === aliment.alim_code
            )
        );
      } else {
        filteredIngredients.value = [];
      }
    };

    const updateIngredientList = () => {
      const isIn = data.find(
        (aliment) => aliment.alim_nom_fr === ingredient.value
      );
      if (ingredient.value && isIn) {
        const ingredientObject = {
          alim_nom_fr: isIn.alim_nom_fr,
          alim_code: isIn.alim_code,
        };

        if (
          !originalForm.value.ingredients_exclus.some(
            (excl) => excl.alim_code === isIn.alim_code
          )
        ) {
          originalForm.value.ingredients_exclus.push(ingredientObject);
        }
        ingredient.value = "";
      }
    };

    const removeExcludedIngredient = (index) => {
      originalForm.value.ingredients_exclus.splice(index, 1);
    };

    const toggleEdit = () => {
      if (!isEditable.value) {
        isEditable.value = true;
      } else {
        // Save
        form.value = JSON.parse(JSON.stringify(originalForm.value));
        isEditable.value = false;
        submitForm();
      }
    };

    const cancelEdit = () => {
      ingredient.value = "";
      isEditable.value = false;
      originalForm.value = JSON.parse(JSON.stringify(form.value));
    };

    const submitForm = async () => {
      try {
        // eslint-disable-next-line no-unused-vars
        const { allergies, ...body } = originalForm.value;
        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/mes-preferences`,
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
          `${process.env.VUE_APP_API_URL}/api/mes-preferences`,
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
          originalForm.value = JSON.parse(JSON.stringify(responseData));
          originalForm.value.allergies = [];
          form.value = JSON.parse(JSON.stringify(responseData));
        }
      } catch (error) {
        // Handle errors
        success.value.color = "red";
        success.value.message = "Échec: " + error.message;
      }
    });

    return {
      alimentationOptions,
      allergiesOptions,
      difficulteOptions,
      tempsOptions,
      jourOptions,
      repasViandeOptions,
      repasPoissonOptions,
      joursSemaine,
      originalForm,
      form,
      ingredient,
      filteredIngredients,
      isEditable,
      success,
      getDescription,
      toggleEdit,
      cancelEdit,
      filterIngredients,
      updateIngredientList,
      removeExcludedIngredient,
      submitForm,
    };
  },
};
</script>

<style scoped>
.customised-select {
  width: 200px;
  height: 40px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.customised-select option {
  text-align: center;
}

option {
  display: flex;
  justify-content: center;
}
.preferences-container {
  font-family: "TangoSans", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  transition: 0.3s;
  padding: 16px;
  border-radius: 5px;
}

.banner {
  padding-top: 250px;
  padding-bottom: 100px;
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

.card {
  width: 400px;
  height: 1;
}

input {
  padding: 5px 10px 5px 10px;
}

form {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  padding: 16px;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 5px;
}

table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  font-family: "TangoSans";
}

th {
  background-color: #f2f2f2;
}

.horizontal-checkboxes {
  display: flex;
  flex-wrap: wrap;
  gap: 1em;
  justify-content: center;
}

.ingredient-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.delete-cross {
  color: red;
  cursor: pointer;
  margin-left: 10px;
}

.button-group {
  display: flex;
  justify-content: space-between;
}

.button-group button {
  flex: 1;
  margin: 0 5px;
}

.success {
  margin-top: 10px;
  padding: 10px;
  border-radius: 5px;
  color: white;
}

.btn {
  background-color: rgb(0, 76, 64);
  color: white;
  border: 1px solid rgb(0, 76, 64);
  transition: 0.2s ease-in-out;
  padding-left: 30px;
  padding-right: 30px;
}

.btn:hover {
  background-color: rgb(161, 201, 0);
  color: white;
  transition: 0.2s ease-in-out;
  padding-left: 30px;
  padding-right: 30px;
}
.btn-order {
  color: white;
  background-color: #004c40;
  transition: 0.3s;
  font-family: "TangoSans";
}

.btn-order:hover {
  color: #004c40;
  background-color: white;
  border-color: #004c40;
}

.btn-order2 {
  color: white;
  background-color: rgb(133, 187, 47);
  transition: 0.3s;
  font-family: "TangoSans";
  width: 300px;
  height: 50px;
}

.btn-order2:hover {
  color: white;
  background-color: #004c40;
  border-color: #004c40;
}

.dropdown-menu {
  width: 300px;
}

.dropdown-item {
  cursor: pointer;
  overflow: hidden;
  white-space: normal;
}

.dropdown-item:hover {
  color: white;
  background-color: #004c40;
}

.dropdown-item .icon {
  width: 35px;
}
</style>
