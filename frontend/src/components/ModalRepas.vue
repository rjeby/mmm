<template>
  <div>
    <b-modal size="xl" ref="ModalRepas" centered hide-footer hide-header>
      <div class="tangosans">
        <!-- If repas is a menu -->
        <div v-if="repas.plat">
          <div class="row first-row">
            <div class="col-5 menu_infos">
              <div class="row dish_image">L'image du plat</div>
              <div class="row menu_title">
                {{ repas.plat.NomFamPlat }}
              </div>
              <div class="row dur-diff">
                {{ repas.plat.DurPrep }} min - {{ repas.plat.Diff }}
              </div>
            </div>
            <div class="col-7 ingredientsMenu">
              <h3>Ingrédients Menu:</h3>
              <div v-for="rep in repasList" :key="rep">
                <h4>Ingrédients {{ namesMap[rep] }}:</h4>
                <div
                  v-for="(ingredient, index) in repas[repasMap[rep]]"
                  :key="index"
                >
                  <p>
                    {{ ingredient.ingredient.alim_nom_fr }} -
                    {{ ingredient.quantity }} {{ ingredient.unit }}
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div class="row second-row text-left">
            <h3>
              Entrée: {{ repas.entree.NomFamEntree }} •
              {{ prixMap[repas.entree.Prix] }} •
              {{ macroNutrientsMap[repas.entree.MacroN] }} •
              {{ Math.round(repas.apportCaloriqueEntree) }}
              Kcal
            </h3>
            <p>{{ repas.entree.TextRecette }}</p>
            <h3>
              Plat: {{ repas.plat.NomFamPlat }} •
              {{ prixMap[repas.plat.Prix] }} •
              {{ macroNutrientsMap[repas.plat.MacroN] }} •
              {{ Math.round(repas.apportCaloriquePlat) }}
              Kcal
            </h3>
            <p>{{ repas.plat.TextRecette }}</p>
            <h3>
              Dessert: {{ repas.dessert.NomFamDessert }} •
              {{ prixMap[repas.dessert.Prix] }} •
              {{ Math.round(repas.apportCaloriqueDessert) }}
              Kcal
            </h3>
            <p>{{ repas.dessert.TextRecette }}</p>
          </div>
          <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 third-row">
            <div class="text-center">
              <img src="../assets/icons/like.png" /> Ajouter ce menu à mes menus
              favoris
            </div>
            <div class="text-center">
              <a href="#" @click.prevent="showApportsNutritionnelsRepas">
                <img src="../assets/icons/bar-chart.png" /> Apports
                Nutritionnels
              </a>
              <!-- Composant pour afficher les apports nutrtionnels du menu -->
              <ApportsNutritionnelsRepas
                :repas="repas"
                ref="ApportsNutritionnelsRepasRef"
              />
            </div>
            <div class="text-center">
              <img src="../assets/icons/dislike.png" /> Ne plus me proposer ce
              menu
            </div>
          </div>
        </div>
        <!-- If repas is a breakfast -->
        <div v-if="repas.petitDejeuner">
          <div>
            <h1 class="text-center">
              Ce petit déjeuner est à consommez dans
              {{ repas.nombrePropositionsPetitDejeuner }} jours de votre choix
            </h1>
          </div>
          <div class="row first-row">
            <div class="col-5 menu_infos">
              <div class="row dish_image">L'image du plat</div>
              <div class="row menu_title">
                {{ repas.petitDejeuner.NomFamPetitDejeuner }}
              </div>
              <div class="row dur-diff">
                {{ repas.petitDejeuner.DurPrep }} min -
                {{ repas.petitDejeuner.Diff }}
              </div>
            </div>
            <div class="col-7 ingredientsPetitDejeuner">
              <h3>Ingrédients Petit Déjeuner:</h3>
              <div
                v-for="(ingredient, index) in repas['ingredientsPetitDejeuner']"
                :key="index"
              >
                <p>
                  {{ ingredient.ingredient.alim_nom_fr }} -
                  {{ ingredient.quantity }} {{ ingredient.unit }}
                </p>
              </div>
            </div>
          </div>
          <div class="row second-row text-left">
            <h3>
              Petit Déjeuner: {{ repas.petitDejeuner.NomFamPetitDejeuner }} •
              {{ prixMap[repas.petitDejeuner.Prix] }} •
              {{ Math.round(repas.apportCaloriquePetitDejeuner) }}
              Kcal
            </h3>
            <p>{{ repas.petitDejeuner.TextRecette }}</p>
          </div>
          <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 third-row">
            <div class="text-center">
              <img src="../assets/icons/like.png" /> Ajouter ce menu à mes menus
              favoris
            </div>
            <div class="text-center">
              <a href="#" @click.prevent="showApportsNutritionnelsRepas">
                <img src="../assets/icons/bar-chart.png" /> Apports
                Nutritionnels
              </a>
              <!-- Composant pour afficher les apports nutrtionnels du petit déjeuner -->
              <ApportsNutritionnelsRepas
                :repas="repas"
                ref="ApportsNutritionnelsRepasRef"
              />
            </div>
            <div class="text-center">
              <img src="../assets/icons/dislike.png" /> Ne plus me proposer ce
              menu
            </div>
          </div>
        </div>
        <!-- Vinaigrette de la semaine -->
        <div v-if="repas.vinaigrette">
          <div class="row first-row">
            <div class="col-5 menu_infos">
              <div class="row dish_image">L'image du plat</div>
              <div class="row menu_title">
                {{ repas.vinaigrette.NomFamVinaigrette }}
              </div>
            </div>
            <div class="col-7 ingredientsVinaigrette">
              <h3>Ingrédients Vinaigrettes:</h3>
              <div
                v-for="(ingredient, index) in repas['ingredientsVinaigrette']"
                :key="index"
              >
                <p>
                  {{ ingredient.ingredient.alim_nom_fr }} -
                  {{ ingredient.quantity }} {{ ingredient.unit }}
                </p>
              </div>
            </div>
          </div>
          <div class="row second-row text-left">
            <h3>
              Vinaigrette De La Semaine:
              {{ repas.vinaigrette.NomFamVinaigrette }} •
              {{ Math.round(repas.apportCaloriqueVinaigrette) }}
              Kcal
            </h3>
            <p>{{ repas.vinaigrette.TextRecette }}</p>
          </div>
          <div
            class="row row-cols-1 row-cols-sm-2 row-cols-md-3 justify-content-center third-row"
          >
            <div class="text-center">
              <a href="#" @click.prevent="showApportsNutritionnelsRepas">
                <img src="../assets/icons/bar-chart.png" /> Apports
                Nutritionnels
              </a>
              <!-- Composant pour afficher les apports nutrtionnels de la vinaigrette -->
              <ApportsNutritionnelsRepas
                :repas="repas"
                ref="ApportsNutritionnelsRepasRef"
              />
            </div>
          </div>
        </div>
      </div>
    </b-modal>
  </div>
</template>

<script>
import { ref } from "vue";
import ApportsNutritionnelsRepas from "@/components/ApportsNutritionnelsRepas.vue";
export default {
  components: { ApportsNutritionnelsRepas },
  props: {
    repas: {
      type: Object,
      required: true,
    },
  },
  setup() {
    const ApportsNutritionnelsRepasRef = ref(null);
    const macroNutrientsMap = ref({
      "L-G": "glucido-lipidique",
      L: "lipidique",
      G: "glucidique",
      "P-L-G": "glucido-lipidique",
      "P-L": "lipidique",
      "P-G": "glucidique",
    });
    const repasList = ["entree", "plat", "dessert"];
    const prixMap = {
      "bon marché": "Bon Marché",
      "repas de fête": "Repas de Fête",
      amélioré: "Amélioré",
    };
    const repasMap = {
      entree: "ingredientsEntree",
      plat: "ingredientsPlat",
      dessert: "ingredientsDessert",
    };
    const namesMap = {
      entree: "Entrée",
      plat: "Plat",
      dessert: "Dessert",
    };
    const ModalRepas = ref(null);
    const show = () => {
      ModalRepas.value.show();
    };
    const showApportsNutritionnelsRepas = () => {
      ApportsNutritionnelsRepasRef.value.show();
    };
    return {
      ApportsNutritionnelsRepasRef,
      ModalRepas,
      repasList,
      repasMap,
      namesMap,
      prixMap,
      macroNutrientsMap,
      show,
      showApportsNutritionnelsRepas,
    };
  },
};
</script>

<style scoped>
h1 {
  font-family: "TangoSans";
  font-size: 20px;
  color: #004c40;
}

.first-row {
  border: 1px solid rgb(0, 0, 0);
}

.dur-diff {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.ingredientsPetitDejeuner .ingredientsVinaigrette {
  display: flex;
  flex-direction: column;
  text-align: left;
}

.ingredientsMenu {
  display: flex;
  flex-direction: column;
  text-align: left;
}

.ingredientsMenu div div p {
  margin: 0;
  padding: 0;
}

.ingredientsPetitDejeuner div p {
  margin: 0;
  padding: 0;
}

.second-row {
  border: 1px solid rgb(0, 0, 0);
  padding: 5px;
  display: flex;
  flex-direction: column;
  text-align: left;
}

.third-row {
  border: 1px solid rgb(0, 0, 0);
  padding: 5px;
  padding-top: 10px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  font-size: 13px;
}

.menu_infos {
  border-right: 1px solid rgb(0, 0, 0);
  padding: 5px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.dish_image {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: aquamarine;
  height: 400px;
  width: 100%;
  padding: 10px;
}

.menu_title {
  text-decoration: underline;
}

.third-row img {
  height: 35px;
  padding: 5px;
}

.third-row div {
  padding: 0;
  margin: 0;
}
</style>
