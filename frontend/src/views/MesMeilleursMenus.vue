<template>
  <section class="mmm-page">
    <div class="container text-center">
      <div class="page-title text-center">
        {{ getTitle() }}
      </div>
      <div
        class="legend-mmm d-flex justify-content-center"
        @click.prevent="showLegende"
      >
        <p>
          Comment utiliser <img src="../assets/icons/shopping-basket.png" />,
          <img src="../assets/icons/heart.png" />,
          <img
            src="../assets/icons/circle-of-two-clockwise-arrows-rotation.png"
          />, <img src="../assets/icons/magic-wand.png" />,
          <img src="../assets/icons/fork-and-knife-in-cross.png" />, et
          <img src="../assets/icons/cloche.png" /> pour personnaliser Mes
          Meilleurs Menus
          <font-awesome-icon
            icon="fa-solid fa-circle-question"
            style="color: #276020; height: 20px"
          />
        </p>
        <Legende ref="LegendeRef" />
      </div>
      <div class="navigation-bar">
        <div class="left-bar">
          <img src="../assets/icons/right-arrow.png" />Semaine avant
        </div>
        <div class="right-bar">
          Semaine après <img src="../assets/icons/left-arrow.png" />
        </div>
      </div>
      <!-- Modal For displaying BreakFast / Menus Infos -->
      <ModalRepas ref="ModalRepasRef" :repas="repasInfos" />
      <!-- Modal for changing actual meal by another containing a specific ingredient -->
      <ChangementRepas
        ref="ChangementRepasRef"
        @change-plat="handlePlatChange"
        @change-petitDejeuner="handlePetitDejeunerChange"
        :ingredients="ingredientsInfos"
      />
      <div class="button-group">
        <button
          class="btn btn-lg"
          type="button"
          @click="cancelEdit"
          v-if="isEditable"
        >
          Annuler
        </button>
        <button
          class="btn btn-lg"
          type="button"
          v-if="isEditable"
          @click="loadDefault"
        >
          programme par défaut
        </button>
        <button class="btn btn-lg" type="button" @click="toggleEdit">
          {{ isEditable ? "Sauvegarder" : "Modifier" }}
        </button>
      </div>
      <div class="tableau row row-cols-1 row-cols-sm-2 row-cols-md-4">
        <div class="col menu-style">
          <div class="title-style">Petits-déjeuner</div>
          <div>
            <div class="repas">
              {{ goutsMap[petitsDejeuners[0].petitDejeuner.Goût] }}
              <input
                type="checkbox"
                v-model="listeDeCoursesVisibility.isZeroVisible"
              />
            </div>
            <div class="image-plat text-center">L'image du plat</div>
            <div class="plat-title">
              <a href="#" @click.prevent="showModalRepas(petitsDejeuners[0])">
                {{ petitsDejeuners[0].petitDejeuner.NomFamPetitDejeuner }}
              </a>
            </div>
            <div>
              <span class="duree"
                >{{ petitsDejeuners[0].petitDejeuner.DurPrep }} min</span
              >
              -
              <span class="difficulte">{{
                petitsDejeuners[0].petitDejeuner.Diff
              }}</span>
            </div>
            <div class="func-icons">
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="showChangementRepasPetitDejeuner(0)"
              >
                <img src="../assets/icons/shopping-basket.png" />
              </a>
              <img src="../assets/icons/heart.png" />
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="generateRandomBreakfest(0)"
              >
                <img
                  src="../assets/icons/circle-of-two-clockwise-arrows-rotation.png"
                />
              </a>
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="improveBreakfast(0)"
              >
                <img src="../assets/icons/magic-wand.png" />
              </a>
              <img src="../assets/icons/fork-and-knife-in-cross.png" />
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="clochePetitDejeuner(0)"
              >
                <img src="../assets/icons/cloche.png" />
              </a>
            </div>
          </div>
          <div class="middle">
            Vinaigrette de la semaine
            <input
              type="checkbox"
              v-model="
                listeDeCoursesVisibility['isVinaigretteDeLaSemaineVisible']
              "
            />
            <a href="#" @click.prevent="showModalRepas(vinaigretteDeLaSemaine)">
              <p>{{ vinaigretteDeLaSemaine.vinaigrette.NomFamVinaigrette }}</p>
            </a>
          </div>

          <div>
            <div class="repas">
              {{ goutsMap[petitsDejeuners[1].petitDejeuner.Goût] }}
              <input
                type="checkbox"
                v-model="listeDeCoursesVisibility.isOneVisible"
              />
            </div>
            <div class="image-plat text-center">L'image du plat</div>
            <div class="plat-title">
              <a href="#" @click.prevent="showModalRepas(petitsDejeuners[1])">
                {{ petitsDejeuners[1].petitDejeuner.NomFamPetitDejeuner }}
              </a>
            </div>
            <div>
              <span class="duree"
                >{{ petitsDejeuners[1].petitDejeuner.DurPrep }} min</span
              >
              -
              <span class="difficulte">{{
                petitsDejeuners[1].petitDejeuner.Diff
              }}</span>
            </div>
            <div class="func-icons">
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="showChangementRepasPetitDejeuner(1)"
              >
                <img src="../assets/icons/shopping-basket.png" />
              </a>
              <img src="../assets/icons/heart.png" />
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="generateRandomBreakfest(1)"
              >
                <img
                  src="../assets/icons/circle-of-two-clockwise-arrows-rotation.png"
                />
              </a>
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="improveBreakfast(1)"
              >
                <img src="../assets/icons/magic-wand.png" />
              </a>
              <img src="../assets/icons/fork-and-knife-in-cross.png" />
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="clochePetitDejeuner(1)"
              >
                <img src="../assets/icons/cloche.png" />
              </a>
            </div>
          </div>
        </div>

        <div
          class="col menu-style"
          v-for="(jour, index) in semaine[infos.preferences.jour_debut_semaine]"
          :key="index"
        >
          <div class="title-style">
            {{ jour }}
          </div>
          <div>
            <div class="repas">
              Déjeuner
              <input
                type="checkbox"
                v-model="listeDeCoursesVisibility[`is${jour}DejeunerVisible`]"
              />
            </div>
            <div class="image-plat text-center">L'image du plat</div>
            <div class="plat-title">
              <a
                href="#"
                @click.prevent="showModalRepas(menus[`${jour}Dejeuner`])"
              >
                {{ menus[`${jour}Dejeuner`].plat.NomFamPlat }}
              </a>
            </div>
            <div>
              <span class="duree"
                >{{ menus[`${jour}Dejeuner`].plat.DurPrep }} min</span
              >
              -
              <span class="difficulte">{{
                menus[`${jour}Dejeuner`].plat.Diff
              }}</span>
            </div>
            <div class="func-icons">
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="showChangementRepasPlat(`${jour}Dejeuner`)"
              >
                <img src="../assets/icons/shopping-basket.png" />
              </a>
              <img src="../assets/icons/heart.png" />
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="generateRandomMenu(`${jour}Dejeuner`)"
              >
                <img
                  src="../assets/icons/circle-of-two-clockwise-arrows-rotation.png"
                />
              </a>
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="improveMenu(`${jour}Dejeuner`)"
              >
                <img src="../assets/icons/magic-wand.png" />
              </a>
              <img src="../assets/icons/fork-and-knife-in-cross.png" />
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="clocheDejeuner(`${jour}Dejeuner`)"
              >
                <img src="../assets/icons/cloche.png" />
              </a>
            </div>
          </div>
          <div class="middle">
            Collation
            <input
              type="checkbox"
              v-model="listeDeCoursesVisibility[`is${jour}EncasVisible`]"
            />
            <p>
              {{ encas[jour].encas.NomFamEncas }} •
              {{ Math.round(encas[jour].apportCaloriqueEncas) }} Kcal
            </p>
          </div>

          <div>
            <div class="repas">
              Diner
              <input
                type="checkbox"
                v-model="listeDeCoursesVisibility[`is${jour}DinerVisible`]"
              />
            </div>
            <div class="image-plat text-center">L'image du plat</div>
            <div class="plat-title">
              <a
                href="#"
                @click.prevent="showModalRepas(menus[`${jour}Diner`])"
              >
                {{ menus[`${jour}Diner`].plat.NomFamPlat }}
              </a>
            </div>
            <div>
              <span class="duree"
                >{{ menus[`${jour}Diner`].plat.DurPrep }} min</span
              >
              -
              <span class="difficulte">{{
                menus[`${jour}Diner`].plat.Diff
              }}</span>
            </div>
            <div class="func-icons">
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="showChangementRepasPlat(`${jour}Diner`)"
              >
                <img src="../assets/icons/shopping-basket.png" />
              </a>
              <img src="../assets/icons/heart.png" />
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="generateRandomMenu(`${jour}Diner`)"
              >
                <img
                  src="../assets/icons/circle-of-two-clockwise-arrows-rotation.png"
                />
              </a>
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="improveMenu(`${jour}Diner`)"
              >
                <img src="../assets/icons/magic-wand.png" />
              </a>
              <img src="../assets/icons/fork-and-knife-in-cross.png" />
              <a
                :class="{ disabled: !isEditable }"
                href="#"
                @click.prevent="clocheDejeuner(`${jour}Diner`)"
              >
                <img src="../assets/icons/cloche.png" />
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="bottom-panel">
        <div><img src="../assets/icons/download-pdf.png" />Fichier PDF</div>
        <div>
          <a href="#" @click.prevent="showMaListeDeCourses">
            <img src="../assets/icons/wish-list.png" />Ma Liste de Courses
            (Repas sélectionnés)
          </a>
          <!-- Composant pour afficher la liste de courses -->
          <MaListeDeCourses
            :listeDeCourses="listeDeCourses"
            ref="MaListeDeCoursesRef"
          />
        </div>
        <div>
          <a href="#" @click.prevent="showRepartitionApportsCaloriques">
            <img src="../assets/icons/pie-chart.png" />Répartition des apports
            caloriques de la semaine
          </a>
          <!-- Composant pour affichier les apports nutrtionnels hebdomadaires -->
          <RepartitionApportsCaloriques
            :infos="infos"
            ref="RepartitionApportsCaloriquesRef"
          />
        </div>
        <div>
          <a href="#" @click.prevent="showMesApportsNutritionnels">
            <img src="../assets/icons/bar-chart.png" />Mes Apports Nutritionnels
            de la semaine
          </a>
          <!-- Composant pour affichier les apports nutrtionnels hebdomadaires -->
          <MesApportsNutritionnels
            :apportsNutritionnels="apportsNutritionnelsHebdomadaire"
            ref="MesApportsNutritionnelsRef"
          />
        </div>
      </div>
      <div
        v-if="success.message"
        class="success"
        :style="{ backgroundColor: success.color }"
      >
        {{ success.message }}
      </div>
    </div>
  </section>
</template>

<script>
import { onMounted, ref } from "vue";
import Vinaigrettes from "@/data/Vinaigrettes.json";
import Encas from "@/data/Encas.json";
import PetitsDejeuners from "@/data/PetitsDejeuners.json";
import Entrees from "@/data/Entrees.json";
import Plats from "@/data/Plats.json";
import Desserts from "@/data/Desserts.json";
import Ciqual from "@/data/Ciqual.json";
import valeursNutritionnels from "@/data/ValeursNutritionnelles.json";
import MesApportsNutritionnels from "@/components/MesApportsNutritionnels.vue";
import ModalRepas from "@/components/ModalRepas.vue";
import MaListeDeCourses from "@/components/MaListeDeCourses.vue";
import Legende from "@/components/Legende.vue";
import { userState } from "@/utils/store";
import RepartitionApportsCaloriques from "@/components/RepartitionApportsCaloriques.vue";
import ChangementRepas from "@/components/ChangementRepas.vue";
import IngredientsPlat from "@/data/IngredientsPlats.json";
import IngredientsPetitDejeuner from "@/data/IngredientsPetitsDejeuners.json";

export default {
  /* eslint-disable */
  components: { MesApportsNutritionnels, RepartitionApportsCaloriques, ModalRepas, ChangementRepas, MaListeDeCourses, Legende },
  setup() {
    // Backup object used to restore old state
    const backup = ref({});
    const backup_id = ref(null);
    const isEditable = ref(false);
    // This is used to store fetched user data
    const infos = ref({prenom: '', genre: 'homme', annee_naissance: 0, taille: 0, poids: 0, activite_legere: '', activite_moyenne: '', activite_elevee: '', membres_famille: [], preferences: { type_alimentation: '', difficulte_menu: '', nbr_repas_viande_semaine: 0, nbr_repas_poisson_semaine: 0, preference_viande: '', petit_dejeuner: '', jour_courses: '', jour_debut_semaine: 'Lundi', jour_semaine_suivante: 'Lundi', lundi_dejeuner_max: 'Lundi', lundi_diner_max: '', mardi_dejeuner_max: '', mardi_diner_max: '', mercredi_dejeuner_max: '', mercredi_diner_max: '', jeudi_dejeuner_max: '', jeudi_diner_max: '', vendredi_dejeuner_max: '', vendredi_diner_max: '', samedi_dejeuner_max: '', samedi_diner_max: '', dimanche_dejeuner_max: '', dimanche_diner_max: '', ingredients_exclus: [] }, perdre_poids: ''});
    // This is used to reference the ModalRepas component in order to show it from parent component
    const ModalRepasRef = ref(null);
    // This is used to reference the MesApportsNutritionnels component in order to show it from parent component
    const MesApportsNutritionnelsRef = ref(null);
    // This is used to reference the MaListeDeCourses component in order to show it from parent component
    const MaListeDeCoursesRef = ref(null);
    // This is used to reference RepartitionApportsCaloriques component in order to show it from parent component
    const RepartitionApportsCaloriquesRef = ref(null);
    // This is used to reference ChangementRepas component in order to show it from parent component
    const ChangementRepasRef = ref(null);
    // This is used to reference Legene component in order to show it from parent component
    const LegendeRef = ref(null);
    const menuObject = () => {
      return {entree: { NomFamEntree: "Titre du Plat", DurPrep: "25", Diff: "Facile", Prix: "bon marché" }, ingredientsEntree: [], apportCaloriqueEntree: 0, apportsNutritionnelsEntree: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 }, rayonsEntree: { "Traiteur": [], "Fruits et légumes": [], "Epicerie": [], "Boulangerie": [], "Frais": [], "Boucherie": [], "Charcuterie": [], "Poissonnerie": [], "Œufs": [], "Produits laitiers": [], "Fromagerie": [], "Crèmerie": [], "Boissons": [], "Pâtisserie": [] }, plat: { NomFamPlat: "Titre du Plat", DurPrep: "25", Diff: "Facile", Prix: "bon marché" }, ingredientsPlat: [], apportCaloriquePlat: 0, apportsNutritionnelsPlat: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 }, rayonsPlat: { "Traiteur": [], "Fruits et légumes": [], "Epicerie": [], "Boulangerie": [], "Frais": [], "Boucherie": [], "Charcuterie": [], "Poissonnerie": [], "Œufs": [], "Produits laitiers": [], "Fromagerie": [], "Crèmerie": [], "Boissons": [], "Pâtisserie": [] }, dessert: { NomFamDessert: "Titre du Plat", DurPrep: "25", Diff: "Facile", Prix: "bon marché" }, ingredientsDessert: [], apportCaloriqueDessert: 0, apportsNutritionnelsDessert: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 }, rayonsDessert: { "Traiteur": [], "Fruits et légumes": [], "Epicerie": [], "Boulangerie": [], "Frais": [], "Boucherie": [], "Charcuterie": [], "Poissonnerie": [], "Œufs": [], "Produits laitiers": [], "Fromagerie": [], "Crèmerie": [], "Boissons": [], "Pâtisserie": [] }};
    }

    const petitDejeunerObject = (count) => {
      return {petitDejeuner: { NomFamPetitDejeuner: "Titre du Plat", DurPrep: "25", Diff: "Facile", Goût: "salé", Prix: "bon marché" }, ingredientsPetitDejeuner: [], apportCaloriquePetitDejeuner: 0, nombrePropositionsPetitDejeuner: count, apportsNutritionnelsPetitDejeuner: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 }, rayonsPetitDejeuner: { "Traiteur": [], "Fruits et légumes": [], "Epicerie": [], "Boulangerie": [], "Frais": [], "Boucherie": [], "Charcuterie": [], "Poissonnerie": [], "Œufs": [], "Produits laitiers": [], "Fromagerie": [], "Crèmerie": [], "Boissons": [], "Pâtisserie": [] }};
    }

    const encasObject = () => {
      return {encas: {NomFamEncas: "Fruits frais et à coque"}, ingredientsEncas: [], apportCaloriqueEncas: 0, apportsNutritionnelsEncas: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 }, rayonsEncas: { "Traiteur": [], "Fruits et légumes": [], "Epicerie": [], "Boulangerie": [], "Frais": [], "Boucherie": [], "Charcuterie": [], "Poissonnerie": [], "Œufs": [], "Produits laitiers": [], "Fromagerie": [], "Crèmerie": [], "Boissons": [], "Pâtisserie": [] }};
    }

    const repasInfos = ref(menuObject());
    const ingredientsInfos = ref({signal: "change-plat", file: IngredientsPlat, toChange: "LundiDejeuner"});
    const apportsNutritionnelsHebdomadaire = ref([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
    const apportsNutritionnelsHebdomadaireCopy = ref([]);
    const nutrimentIndex = { "fibres": 0, "iode": 1, "magnesium": 2, "fer": 3, "cuivre": 4, "sodium": 5, "selenium": 6, "zinc": 7, "phosphore": 8, "calcium": 9, "manganese": 10, "potassium": 11, "vitamineK1": 12, "vitamineE": 13, "vitamineD": 14, "vitamineC": 15, "vitamineB12": 16, "vitamineB9": 17, "vitamineB6": 18, "vitamineB5": 19, "vitamineB3": 20, "vitamineB2": 21, "vitamineB1": 22, "vitamineA": 23 };
    const semaine = {
      Lundi: ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
      Mardi: ["Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche", "Lundi"],
      Mercredi: ["Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche", "Lundi", "Mardi"],
      Jeudi: ["Jeudi", "Vendredi", "Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi"],
      Vendredi: ["Vendredi", "Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi"],
      Samedi: ["Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"],
      Dimanche: ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    };
    const success = ref({message: "", color: "",});
    const clocheMap = { LundiDejeuner: ["LundiDiner", "MardiDejeuner", "MardiDiner", "MercrediDejeuner", "MercrediDiner", "JeudiDejeuner", "JeudiDiner", "VendrediDejeuner", "VendrediDiner", "SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], LundiDiner: ["MardiDejeuner", "MardiDiner", "MercrediDejeuner", "MercrediDiner", "JeudiDejeuner", "JeudiDiner", "VendrediDejeuner", "VendrediDiner", "SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], MardiDejeuner: ["MardiDiner", "MercrediDejeuner", "MercrediDiner", "JeudiDejeuner", "JeudiDiner", "VendrediDejeuner", "VendrediDiner", "SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], MardiDiner: ["MercrediDejeuner", "MercrediDiner", "JeudiDejeuner", "JeudiDiner", "VendrediDejeuner", "VendrediDiner", "SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], MercrediDejeuner: ["MercrediDiner", "JeudiDejeuner", "JeudiDiner", "VendrediDejeuner", "VendrediDiner", "SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], MercrediDiner: ["JeudiDejeuner", "JeudiDiner", "VendrediDejeuner", "VendrediDiner", "SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], JeudiDejeuner: ["JeudiDiner", "VendrediDejeuner", "VendrediDiner", "SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], JeudiDiner: ["VendrediDejeuner", "VendrediDiner", "SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], VendrediDejeuner: ["VendrediDiner", "SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], VendrediDiner: ["SamediDejeuner", "SamediDiner", "DimancheDejeuner", "DimancheDiner"], SamediDejeuner: ["SamediDiner", "DimancheDejeuner", "DimancheDiner"], SamediDiner: ["DimancheDejeuner", "DimancheDiner"], DimancheDejeuner: ["DimancheDiner"], DimancheDiner: [] };
    const goutsMap = {sucré: "Sucré", salé: "Salé"};
    const nutriments = ["fibres", "calcium", "cuivre", "fer", "iode", "magnesium", "manganese", "phosphore", "potassium", "selenium", "sodium", "zinc", "vitamineD", "vitamineE", "vitamineK1", "vitamineC", "vitamineB1", "vitamineB2", "vitamineB3", "vitamineB5", "vitamineB6", "vitamineB9", "vitamineB12", "vitamineA"];
    const petitsDejeuners = ref({
      // First breakfast is proposed Day1, Day3, Day5, Day7
      0: petitDejeunerObject(4),
      // Second breakfast is proposed Day2, Day4, Day6
      1: petitDejeunerObject(3)
    });
    const petitsDejeunersCopy = ref({});
    const menus = ref({
      LundiDejeuner: menuObject(),
      LundiDiner: menuObject(),
      MardiDejeuner: menuObject(),
      MardiDiner: menuObject(),
      MercrediDejeuner: menuObject(),
      MercrediDiner: menuObject(),
      JeudiDejeuner: menuObject(),
      JeudiDiner: menuObject(),
      VendrediDejeuner: menuObject(),
      VendrediDiner: menuObject(),
      SamediDejeuner: menuObject(),
      SamediDiner: menuObject(),
      DimancheDejeuner: menuObject(),
      DimancheDiner: menuObject(),
    });
    const menusCopy = ref({});
    const encas = ref({ Lundi: encasObject(), Mardi: encasObject(), Mercredi: encasObject(), Jeudi: encasObject(), Vendredi: encasObject(), Samedi: encasObject(), Dimanche: encasObject() });
    const encasCopy = ref({});
    const vinaigretteDeLaSemaine = ref({vinaigrette: { NomFamVinaigrette: "Vinaigrette échalottes et basilic" }, ingredientsVinaigrette: [], apportCaloriqueVinaigrette: 0, apportsNutritionnelsVinaigrette: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 }, rayonsVinaigrette: { "Traiteur": [], "Fruits et légumes": [], "Epicerie": [], "Boulangerie": [], "Frais": [], "Boucherie": [], "Charcuterie": [], "Poissonnerie": [], "Œufs": [], "Produits laitiers": [], "Fromagerie": [], "Crèmerie": [], "Boissons": [], "Pâtisserie": [] }}); 
    const vinaigretteDeLaSemaineCopy = ref({});
    // This is used for showing Ma Liste de Courses
    const listeDeCoursesVisibility = ref({isZeroVisible: true, isOneVisible: true, isLundiDejeunerVisible: true, isLundiDinerVisible: true, isMardiDejeunerVisible: true, isMardiDinerVisible: true, isMercrediDejeunerVisible: true, isMercrediDinerVisible: true, isJeudiDejeunerVisible: true, isJeudiDinerVisible: true, isVendrediDejeunerVisible: true, isVendrediDinerVisible: true, isSamediDejeunerVisible: true, isSamediDinerVisible: true, isDimancheDejeunerVisible: true, isDimancheDinerVisible: true, isLundiEncasVisible: true, isMardiEncasVisible: true, isMercrediEncasVisible: true, isJeudiEncasVisible: true, isVendrediEncasVisible: true, isSamediEncasVisible: true, isDimancheEncasVisible: true, isVinaigretteDeLaSemaineVisible: true});
    const listeDeCoursesVisibilityCopy = ref({});
    const listeDeCourses = ref({ "Traiteur": {}, "TraiteurCount": 0, "Fruits et légumes": {}, "Fruits et légumesCount": 0, "Epicerie": {}, "EpicerieCount": 0, "Boulangerie": {}, "BoulangerieCount": 0, "Frais": {}, "FraisCount": 0, "Boucherie": {}, "BoucherieCount": 0, "Charcuterie": {}, "CharcuterieCount": 0, "Poissonnerie": {}, "PoissonnerieCount": 0, "Œufs": {}, "ŒufsCount": 0, "Produits laitiers": {}, "Produits laitiersCount": 0, "Fromagerie": {}, "FromagerieCount": 0, "Crèmerie": {}, "CrèmerieCount": 0, "Boissons": {}, "BoissonsCount": 0, "Pâtisserie": {}, "PâtisserieCount": 0 });
    // Planning en termes de macronutriments
    const planning = {LundiDejeuner: "P-L", LundiDiner: "P-G", MardiDejeuner: "P-G", MardiDiner: "P-L", MercrediDejeuner: "P-L-G", MercrediDiner: "P-G", JeudiDejeuner: "P-L", JeudiDiner: "P-L", VendrediDejeuner: "P-L", VendrediDiner: "P-G", SamediDejeuner: "P-L", SamediDiner: "P-L-G", DimancheDejeuner: "P-L-G", DimancheDiner: "P-L"};
    const planningMap = {"L-G": "P-L-G", "L": "P-L", "G": "P-G", "P-L-G": "P-L-G", "P-L": "P-L", "P-G": "P-G"};
    const updateApportsNutritionnelsMenus = (jour, ancienApportsNutritionnels) => {
        // TODO: Add ingredients from 16 to 20
        const columnsIndex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
        const repasMenu = ["entree", "plat", "dessert"];
        const repasMap = {"entree": "apportsNutritionnelsEntree", "plat": "apportsNutritionnelsPlat", "dessert": "apportsNutritionnelsDessert"};
        const rayonsMap = {"entree": "rayonsEntree", "plat": "rayonsPlat", "dessert": "rayonsDessert"};
        const caloriesMap = {"entree": "apportCaloriqueEntree", "plat": "apportCaloriquePlat", "dessert": "apportCaloriqueDessert"};
        const repasIngredientsMap = {"entree": "ingredientsEntree", "plat": "ingredientsPlat", "dessert": "ingredientsDessert"}; 
        nutriments.forEach((nutriment) => {
          apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] -= (ancienApportsNutritionnels.apportsNutritionnelsEntree[nutriment] + ancienApportsNutritionnels.apportsNutritionnelsPlat[nutriment] + ancienApportsNutritionnels.apportsNutritionnelsDessert[nutriment]) / valeursNutritionnels["week"][nutriment][infos.value.genre];
        })
        // First we iterate over "entree", "plat", "dessert", since all of them change when we generate a random menu
        repasMenu.forEach((repas) => {
          // Then we iterate over ingredients
          columnsIndex.forEach((index) => {
            const code = menus.value[jour][repas][`NumIng${index}`];
            const quantity = menus.value[jour][repas][`QteIng${index}`];
            const unit = menus.value[jour][repas][`UniteIng${index}`];
            if (code) {
              const ingredient = Ciqual.find((ingredient) => ingredient.alim_code === code);
              if (ingredient) {
                const ingredientObject = {ingredient: ingredient, quantity: quantity, unit: unit};
                menus.value[jour][repasIngredientsMap[repas]].push(ingredientObject);
                menus.value[jour][rayonsMap[repas]][ingredient.rayon].push(ingredientObject);
                // We add calories for each ingredient
                menus.value[jour][caloriesMap[repas]] += (ingredient["energieKcal"] * quantity) / 100;
                // Finally, for a valid ingredient code, we compute "l'apport nutritionnel" for each nutrient
                nutriments.forEach((nutriment) => {
                  // We don't divide by 100, since we will convert this value to percentage
                  menus.value[jour][repasMap[repas]][nutriment] += ingredient[nutriment] * quantity;

                })
              } 
            }
          })
        })
        nutriments.forEach((nutriment) => {
          apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] += (menus.value[jour].apportsNutritionnelsEntree[nutriment] + menus.value[jour].apportsNutritionnelsPlat[nutriment] + menus.value[jour].apportsNutritionnelsDessert[nutriment]) / valeursNutritionnels["week"][nutriment][infos.value.genre]; // Replace with gender
        })
    }

    const updateApportsNutritionnelsPetitDejeuner = (indice, ancienApportsNutritionnels) => {
      // By default: first Breakfast is proposed 4 times, seconde one 3 times: This can be replaced by using same logic in petitsDejeuners (Lundi, Mardi ...)
      const coeff = petitsDejeuners.value[indice].nombrePropositionsPetitDejeuner;
      // Breakfasts only contain 10 ingredients
      const columnsIndex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      nutriments.forEach((nutriment) => {
        apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] -= (ancienApportsNutritionnels.apportsNutritionnelsPetitDejeuner[nutriment] / valeursNutritionnels["week"][nutriment][infos.value.genre]) * coeff;
      })
      columnsIndex.forEach((index) => {
        const code = petitsDejeuners.value[indice].petitDejeuner[`NumIng${index}`];
        const quantity = petitsDejeuners.value[indice].petitDejeuner[`QteIng${index}`];
        const unit = petitsDejeuners.value[indice].petitDejeuner[`UniteIng${index}`];
        if (code) {
          const ingredient = Ciqual.find((ingredient) => ingredient.alim_code === code);
          if (ingredient) {
            const ingredientObject = {ingredient: ingredient, quantity: quantity, unit: unit};
            petitsDejeuners.value[indice].ingredientsPetitDejeuner.push(ingredientObject);
            petitsDejeuners.value[indice].rayonsPetitDejeuner[ingredient.rayon].push(ingredientObject);
            // We add calories for each ingredient
            petitsDejeuners.value[indice].apportCaloriquePetitDejeuner += (ingredient["energieKcal"] * quantity) / 100;
            nutriments.forEach((nutriment) => {
              petitsDejeuners.value[indice].apportsNutritionnelsPetitDejeuner[nutriment] += ingredient[nutriment] * quantity;

            })
          } 
        }
      })
      nutriments.forEach((nutriment) => {
        apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] += (petitsDejeuners.value[indice].apportsNutritionnelsPetitDejeuner[nutriment] / valeursNutritionnels["week"][nutriment][infos.value.genre]) * coeff;
      })
    }

    const updateApportsNutritionnelsVinaigrette = () => {
      const columnsIndex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
      // TODO: Add apports nutritionnels to apportsNutritionnelsHebdomadaires
      columnsIndex.forEach((index) => {
        const code = vinaigretteDeLaSemaine.value.vinaigrette[`NumIng${index}`];
        const quantity = vinaigretteDeLaSemaine.value.vinaigrette[`QteIng${index}`];
        const unit = vinaigretteDeLaSemaine.value.vinaigrette[`UniteIng${index}`];
        if (code) {
          const ingredient = Ciqual.find((ingredient) => ingredient.alim_code === code);
          if (ingredient) {
            const ingredientObject = {ingredient: ingredient, quantity: quantity, unit: unit};
            vinaigretteDeLaSemaine.value.ingredientsVinaigrette.push(ingredientObject);
            vinaigretteDeLaSemaine.value.rayonsVinaigrette[ingredient.rayon].push(ingredientObject);
            // We add calories for each ingredient
            vinaigretteDeLaSemaine.value.apportCaloriqueVinaigrette += (ingredient["energieKcal"] * quantity) / 100;
            nutriments.forEach((nutriment) => {
              vinaigretteDeLaSemaine.value.apportsNutritionnelsVinaigrette[nutriment] += ingredient[nutriment] * quantity;
            })
          } 
        }
      })
    }

    const updateApportsNutritionnelsEncas = (jour) => {
      const columnsIndex = [1];
      // TODO: Add apports nutritionnels to apportsNutritionnelsHebdomadaires
      columnsIndex.forEach((index) => {
        const code = encas.value[jour].encas[`NumIng${index}`];
        const quantity = encas.value[jour].encas[`QteIng${index}`];
        const unit = encas.value[jour].encas[`UniteIng${index}`];
        if (code) {
          const ingredient = Ciqual.find((ingredient) => ingredient.alim_code === code);
          if (ingredient) {
            const ingredientObject = {ingredient: ingredient, quantity: quantity, unit: unit};
            encas.value[jour].ingredientsEncas.push(ingredientObject);
            encas.value[jour].rayonsEncas[ingredient.rayon].push(ingredientObject);
            // We add calories for each ingredient
            encas.value[jour].apportCaloriqueEncas += (ingredient["energieKcal"] * quantity) / 100;
            nutriments.forEach((nutriment) => {
              encas.value[jour].apportsNutritionnelsEncas[nutriment] += ingredient[nutriment] * quantity;
            })
          } 
        }
      })
      nutriments.forEach((nutriment) => {
          apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] += (encas.value[jour].apportsNutritionnelsEncas[nutriment]) / valeursNutritionnels["week"][nutriment][infos.value.genre];
        })
    }



    
    const generateRandomMenu = (jour) => {
      // jour (parameter) can be: LundiDejeuner, LundiDiner ... DimancheDejeuner, DimancheDiner
      // TODO: Filter data using preferences
      const entree = getRandomElement(Entrees.filter((entreeItem) => planningMap[entreeItem['MacroN']] === planning[jour]));
      const plat = getRandomElement(Plats.filter((platItem) => planningMap[platItem['MacroN']] === planning[jour]));
      const dessert = getRandomElement(Desserts); 
      // We save the old "ApportsNutritionnels"
      const ancienApportsNutritionnels = {
        apportsNutritionnelsEntree: menus.value[jour].apportsNutritionnelsEntree,
        apportsNutritionnelsPlat: menus.value[jour].apportsNutritionnelsPlat,
        apportsNutritionnelsDessert: menus.value[jour].apportsNutritionnelsDessert,
      }
      // We reset the old menu
      menus.value[jour] = menuObject(); 
      menus.value[jour].entree = entree;
      menus.value[jour].plat = plat;
      menus.value[jour].dessert = dessert;
      updateApportsNutritionnelsMenus(jour, ancienApportsNutritionnels);
    };

    const generateRandomBreakfest = (index) => {
      // TODO: Filter data using preferences
      const petitDejeuner = getRandomElement(PetitsDejeuners);
      // We save the old "ApportsNutritionnels"
      const ancienApportsNutritionnels = {
        apportsNutritionnelsPetitDejeuner: petitsDejeuners.value[index].apportsNutritionnelsPetitDejeuner,
      }
      // We reset the old breakfast, the breakfast proposals count is passed as parameter and stays unchanged
      petitsDejeuners.value[index] = petitDejeunerObject(petitsDejeuners.value[index].nombrePropositionsPetitDejeuner);
      petitsDejeuners.value[index].petitDejeuner = petitDejeuner;
      updateApportsNutritionnelsPetitDejeuner(index, ancienApportsNutritionnels);
    };

    const generateRandomEncas = (jour) => {
      // TODO: Filter data using preferences, calcul des apports
      const encasItem = getRandomElement(Encas);
      encas.value[jour].encas = encasItem;
      updateApportsNutritionnelsEncas(jour);
    }

    const generateRandomVinaigrette = () => {
      // TODO: Filter data using preferences, calcul des apports
      const vinaigretteItem = getRandomElement(Vinaigrettes);
      vinaigretteDeLaSemaine.value.vinaigrette = vinaigretteItem;
      updateApportsNutritionnelsVinaigrette();
      
    }

    const getRandomElement = (array) => {
      const randomIndex = Math.floor(Math.random() * array.length);
      return array[randomIndex];
    }

    const showModalRepas = (repas) => {
      repasInfos.value = repas;
      ModalRepasRef.value.show();
    }

    const showMesApportsNutritionnels = () => {
      MesApportsNutritionnelsRef.value.show();
    }

    const showRepartitionApportsCaloriques = () => {
      RepartitionApportsCaloriquesRef.value.show();
    }

    const showLegende = () => {
      LegendeRef.value.show();
    }

    const showChangementRepasPlat = (toChange) => {
      ingredientsInfos.value = {signal: "change-plat", file: IngredientsPlat, toChange: toChange};    
      ChangementRepasRef.value.show();
    }

    const showChangementRepasPetitDejeuner = (toChange) => {
      ingredientsInfos.value = {signal: "change-petitDejeuner", file: IngredientsPetitDejeuner, toChange: toChange};    
      ChangementRepasRef.value.show();
    }

    const showMaListeDeCourses = () => {
      // We reset listeDeCourses each time (before recomputing it again)
      listeDeCourses.value = { "Traiteur": {}, "TraiteurCount": 0, "Fruits et légumes": {}, "Fruits et légumesCount": 0, "Epicerie": {}, "EpicerieCount": 0, "Boulangerie": {}, "BoulangerieCount": 0, "Frais": {}, "FraisCount": 0, "Boucherie": {}, "BoucherieCount": 0, "Charcuterie": {}, "CharcuterieCount": 0, "Poissonnerie": {}, "PoissonnerieCount": 0, "Œufs": {}, "ŒufsCount": 0, "Produits laitiers": {}, "Produits laitiersCount": 0, "Fromagerie": {}, "FromagerieCount": 0, "Crèmerie": {}, "CrèmerieCount": 0, "Boissons": {}, "BoissonsCount": 0, "Pâtisserie": {}, "PâtisserieCount": 0 };      
      const rayons = ["Traiteur", "Fruits et légumes", "Epicerie", "Boulangerie", "Frais", "Boucherie", "Charcuterie", "Poissonnerie", "Œufs", "Produits laitiers", "Fromagerie", "Crèmerie", "Boissons", "Pâtisserie"];
      const options = ["isZeroVisible", "isOneVisible", "isLundiDejeunerVisible", "isLundiDinerVisible", "isMardiDejeunerVisible", "isMardiDinerVisible", "isMercrediDejeunerVisible", "isMercrediDinerVisible", "isJeudiDejeunerVisible", "isJeudiDinerVisible", "isVendrediDejeunerVisible", "isVendrediDinerVisible", "isSamediDejeunerVisible", "isSamediDinerVisible", "isDimancheDejeunerVisible", "isDimancheDinerVisible", "isLundiEncasVisible", "isMardiEncasVisible", "isMercrediEncasVisible", "isJeudiEncasVisible", "isVendrediEncasVisible", "isSamediEncasVisible", "isDimancheEncasVisible", "isVinaigretteDeLaSemaineVisible"];
      const optionsMap = {"isZeroVisible": [petitsDejeuners.value[0].rayonsPetitDejeuner], "isOneVisible": [petitsDejeuners.value[1].rayonsPetitDejeuner], "isLundiDejeunerVisible": [menus.value["LundiDejeuner"].rayonsEntree, menus.value["LundiDejeuner"].rayonsPlat, menus.value["LundiDejeuner"].rayonsDessert], "isLundiDinerVisible": [menus.value["LundiDiner"].rayonsEntree, menus.value["LundiDiner"].rayonsPlat, menus.value["LundiDiner"].rayonsDessert], "isMardiDejeunerVisible": [menus.value["MardiDejeuner"].rayonsEntree, menus.value["MardiDejeuner"].rayonsPlat, menus.value["MardiDejeuner"].rayonsDessert], "isMardiDinerVisible": [menus.value["MardiDiner"].rayonsEntree, menus.value["MardiDiner"].rayonsPlat, menus.value["MardiDiner"].rayonsDessert], "isMercrediDejeunerVisible": [menus.value["MercrediDejeuner"].rayonsEntree, menus.value["MercrediDejeuner"].rayonsPlat, menus.value["MercrediDejeuner"].rayonsDessert], "isMercrediDinerVisible": [menus.value["MercrediDiner"].rayonsEntree, menus.value["MercrediDiner"].rayonsPlat, menus.value["MercrediDiner"].rayonsDessert], "isJeudiDejeunerVisible": [menus.value["JeudiDejeuner"].rayonsEntree, menus.value["JeudiDejeuner"].rayonsPlat, menus.value["JeudiDejeuner"].rayonsDessert], "isJeudiDinerVisible": [menus.value["JeudiDiner"].rayonsEntree, menus.value["JeudiDiner"].rayonsPlat, menus.value["JeudiDiner"].rayonsDessert], "isVendrediDejeunerVisible": [menus.value["VendrediDejeuner"].rayonsEntree, menus.value["VendrediDejeuner"].rayonsPlat, menus.value["VendrediDejeuner"].rayonsDessert], "isVendrediDinerVisible": [menus.value["VendrediDiner"].rayonsEntree, menus.value["VendrediDiner"].rayonsPlat, menus.value["VendrediDiner"].rayonsDessert], "isSamediDejeunerVisible": [menus.value["SamediDejeuner"].rayonsEntree, menus.value["SamediDejeuner"].rayonsPlat, menus.value["SamediDejeuner"].rayonsDessert], "isSamediDinerVisible": [menus.value["SamediDiner"].rayonsEntree, menus.value["SamediDiner"].rayonsPlat, menus.value["SamediDiner"].rayonsDessert], "isDimancheDejeunerVisible": [menus.value["DimancheDejeuner"].rayonsEntree, menus.value["DimancheDejeuner"].rayonsPlat, menus.value["DimancheDejeuner"].rayonsDessert], "isDimancheDinerVisible": [menus.value["DimancheDiner"].rayonsEntree, menus.value["DimancheDiner"].rayonsPlat, menus.value["DimancheDiner"].rayonsDessert], "isLundiEncasVisible": [encas.value["Lundi"].rayonsEncas], "isMardiEncasVisible": [encas.value["Mardi"].rayonsEncas], "isMercrediEncasVisible": [encas.value["Mercredi"].rayonsEncas], "isJeudiEncasVisible": [encas.value["Jeudi"].rayonsEncas], "isVendrediEncasVisible": [encas.value["Vendredi"].rayonsEncas], "isSamediEncasVisible": [encas.value["Samedi"].rayonsEncas], "isDimancheEncasVisible": [encas.value["Dimanche"].rayonsEncas], "isVinaigretteDeLaSemaineVisible": [vinaigretteDeLaSemaine.value.rayonsVinaigrette]};
      options.forEach((option) => {
          // option is the rayon we are working on below
          if (listeDeCoursesVisibility.value[option]) {
              const repas = optionsMap[option];
              repas.forEach((repasRayon) => {
                  rayons.forEach((rayon) => {
                    const rayonIngredients = repasRayon[rayon];
                    rayonIngredients.forEach((ingredientObject) => {
                    // We check if the ingredient is already present
                      if (listeDeCourses.value[rayon][ingredientObject.ingredient.alim_code]) {
                        listeDeCourses.value[rayon][ingredientObject.ingredient.alim_code].quantity += ingredientObject.quantity;
                      } else {
                        listeDeCourses.value[rayon][ingredientObject.ingredient.alim_code] = {alim_nom_fr: ingredientObject.ingredient.alim_nom_fr, quantity: ingredientObject.quantity, unit: ingredientObject.unit };
                        listeDeCourses.value[`${rayon}Count`]++;
                      }
                  })
                  })
              })
          }
      })
      MaListeDeCoursesRef.value.show();
    }
  
    const getTitle = () => {
      // Get 'jour préféré'
      const favoriteDay = infos.value.preferences.jour_semaine_suivante;
      // Get member name  
      const name = infos.value.prenom;
      // Get all family member names
      const familyNames = infos.value.membres_famille.map(member => member.prenom);
      // Join all names with a comma and a space
      const namesString = familyNames.join(', ');
      // Construct the final title
      return `Mes Meilleurs Menus de la semaine du ${favoriteDay} jj moisX pour ${name}${namesString ? `, ${familyNames}` : ''}`;
    }

    const updateApportsNutritionnelsPlat = (jour, ancienApportsNutritionnels) => {
        // TODO: Add ingredients from 16 to 20
        const columnsIndex = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15];
        nutriments.forEach((nutriment) => {
          apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] -= (ancienApportsNutritionnels.apportsNutritionnelsPlat[nutriment]) / valeursNutritionnels["week"][nutriment][infos.value.genre];
        })
          columnsIndex.forEach((index) => {
            const code = menus.value[jour].plat[`NumIng${index}`];
            const quantity = menus.value[jour].plat[`QteIng${index}`];
            const unit = menus.value[jour].plat[`UniteIng${index}`];
            if (code) {
              const ingredient = Ciqual.find((ingredient) => ingredient.alim_code === code);
              if (ingredient) {
                const ingredientObject = {ingredient: ingredient, quantity: quantity, unit: unit};
                menus.value[jour]["ingredientsPlat"].push(ingredientObject);
                menus.value[jour].rayonsPlat[ingredient.rayon].push(ingredientObject);
                // We add calories for each ingredient
                menus.value[jour].apportCaloriquePlat += (ingredient["energieKcal"] * quantity) / 100;
                // Finally, for a valid ingredient code, we compute "l'apport nutritionnel" for each nutrient
                nutriments.forEach((nutriment) => {
                  // We don't divide by 100, since we will convert this value to percentage
                  menus.value[jour].apportsNutritionnelsPlat[nutriment] += ingredient[nutriment] * quantity;

                })
              } 
            }
          })
        nutriments.forEach((nutriment) => {
          apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] += (menus.value[jour].apportsNutritionnelsPlat[nutriment]) / valeursNutritionnels["week"][nutriment][infos.value.genre]; // Replace with gender
        })
    }

    const handlePlatChange = (ingredientInfos) => {
      const newPlat = {plat: null};
      // TODO: Add ingredients from 16 to 21
      const { ingredient, toChange } = ingredientInfos;
      // First we filter by macro nutrients
      const filteredMacroN = Plats.filter((platItem) => planningMap[platItem['MacroN']] === planning[toChange]);
      // We keep only the plats having the specific ingredient from plats filtered by macro nutrients
      const filteredPlats = filteredMacroN.filter((plat) => plat.NumIng1 === ingredient.alim_code || plat.NumIng2 === ingredient.alim_code || plat.NumIng3 === ingredient.alim_code || plat.NumIng4 === ingredient.alim_code || plat.NumIng5 === ingredient.alim_code || plat.NumIng6 === ingredient.alim_code || plat.NumIng7 === ingredient.alim_code || plat.NumIng8 === ingredient.alim_code || plat.NumIng9 === ingredient.alim_code || plat.NumIng10 === ingredient.alim_code || plat.NumIng11 === ingredient.alim_code || plat.NumIng12 === ingredient.alim_code || plat.NumIng13 === ingredient.alim_code || plat.NumIng14 === ingredient.alim_code || plat.NumIng15 === ingredient.alim_code);
      if (!filteredPlats.length) {
        newPlat.plat = getRandomElement(filteredMacroN);
      } else {
        newPlat.plat = getRandomElement(filteredPlats);
      }
      // We save the old "ApportsNutritionnels"
      const ancienApportsNutritionnelsPlat = {apportsNutritionnelsPlat: menus.value[toChange].apportsNutritionnelsPlat};
      // We reset the old Plat
      menus.value[toChange].plat = { NomFamPlat: "Titre du Plat", DurPrep: "25", Diff: "Facile" };
      menus.value[toChange].apportCaloriquePlat = 0;
      menus.value[toChange].apportsNutritionnelsPlat = { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 };
      menus.value[toChange].ingredientsPlat = [];
      menus.value[toChange].rayonsPlat = { "Traiteur": [], "Fruits et légumes": [], "Epicerie": [], "Boulangerie": [], "Frais": [], "Boucherie": [], "Charcuterie": [], "Poissonnerie": [], "Œufs": [], "Produits laitiers": [], "Fromagerie": [], "Crèmerie": [], "Boissons": [], "Pâtisserie": [] };
      // We change the plat
      menus.value[toChange].plat = newPlat.plat;
      // Update Apports Nutritionnels
      updateApportsNutritionnelsPlat(toChange, ancienApportsNutritionnelsPlat);
    
    }

    const handlePetitDejeunerChange = (ingredientInfos) => {
      const { ingredient, toChange } = ingredientInfos;
      const filteredPetitsDejeuners = PetitsDejeuners.filter((petitDejeuner) => petitDejeuner.NumIng1 === ingredient.alim_code || petitDejeuner.NumIng2 === ingredient.alim_code || petitDejeuner.NumIng3 === ingredient.alim_code || petitDejeuner.NumIng4 === ingredient.alim_code || petitDejeuner.NumIng5 === ingredient.alim_code || petitDejeuner.NumIng6 === ingredient.alim_code || petitDejeuner.NumIng7 === ingredient.alim_code || petitDejeuner.NumIng8 === ingredient.alim_code || petitDejeuner.NumIng9 === ingredient.alim_code || petitDejeuner.NumIng10 === ingredient.alim_code);
      const petitDejeuner = getRandomElement(filteredPetitsDejeuners);
      // We save the old "ApportsNutritionnels"
      const ancienApportsNutritionnelsPetitDejeuner = {apportsNutritionnelsPetitDejeuner: petitsDejeuners.value[toChange].apportsNutritionnelsPetitDejeuner};
      // We reset the old PetitDejeuner
      petitsDejeuners.value[toChange] = petitDejeunerObject(petitsDejeuners.value[toChange].nombrePropositionsPetitDejeuner);
      petitsDejeuners.value[toChange].petitDejeuner = petitDejeuner; 
      updateApportsNutritionnelsPetitDejeuner(toChange, ancienApportsNutritionnelsPetitDejeuner);
    }

    const upgrade = (jour, typeMenu) => {
          const upgradedMenu = { entree: null, plat: null, dessert: null };
          const filteredEntreeMacroN = Entrees.filter((entreeItem) => planningMap[entreeItem['MacroN']] === planning[jour]); 
          const filteredEntree = filteredEntreeMacroN.filter((entreeItem) => entreeItem.Prix === typeMenu);
          const filteredPlatMacroN =   Plats.filter((platItem) => planningMap[platItem['MacroN']] === planning[jour]);
          const filteredPlat = filteredPlatMacroN.filter((platItem) => platItem.Prix === typeMenu);
          if (!filteredEntree.length) {
            upgradedMenu.entree = getRandomElement(fileteredEntreeMacroN);
          } else {
            upgradedMenu.entree = getRandomElement(filteredEntree);
          }

           if (!filteredPlat.length) {
            upgradedMenu.plat = getRandomElement(filteredPlatMacroN);
          } else {
            upgradedMenu.plat = getRandomElement(filteredPlat);
          }
          upgradedMenu.dessert = getRandomElement(Desserts.filter((dessertKey) => dessertKey.Prix === typeMenu)); 
          return upgradedMenu;
    }
    
    const improveMenu = (jour) => {

      const menu = {entree: null, plat: null, dessert: null};
      if (!(menus.value[jour].entree.Prix === "amélioré" && menus.value[jour].plat.Prix === "amélioré" && menus.value[jour].plat.Prix === "amélioré")) { 
        if (!(menus.value[jour].entree.Prix === "repas de fête" && menus.value[jour].plat.Prix === "repas de fête" && menus.value[jour].plat.Prix === "repas de fête")) {
          // We upgrade all menu meals to "Amélioré"
          ({ entree: menu.entree, plat: menu.plat, dessert: menu.dessert } = upgrade(jour, "amélioré"));          
        } else {
          // All menu meals are "Repas de Fête", we don't change anything
          return;
        }
        
      } else {
          // We upgrade all menu meals are "Amélioré", we upgrade them to "Repas de Fête"
          ({ entree: menu.entree, plat: menu.plat, dessert: menu.dessert } = upgrade(jour, "repas de fête"));          

      }
      if (menu.entree && menu.plat && menu.dessert) {
          // If all the changes are valid
          const ancienApportsNutritionnels = {
            apportsNutritionnelsEntree: menus.value[jour].apportsNutritionnelsEntree,
            apportsNutritionnelsPlat: menus.value[jour].apportsNutritionnelsPlat,
            apportsNutritionnelsDessert: menus.value[jour].apportsNutritionnelsDessert,
          }
          // We reset the old menu
          menus.value[jour] = menuObject(); 
          menus.value[jour].entree = menu.entree;
          menus.value[jour].plat = menu.plat;
          menus.value[jour].dessert = menu.dessert;
          updateApportsNutritionnelsMenus(jour, ancienApportsNutritionnels);
      } else {

        return;
      }
    }

    const improveBreakfast = (index) => {
      const breakfast = {petitDejeuner: null};
      if (petitsDejeuners.value[index].petitDejeuner.Prix != "amélioré") {
        if (petitsDejeuners.value[index].petitDejeuner.Prix != "repas de fête") {

          breakfast.petitDejeuner = getRandomElement(PetitsDejeuners.filter((petitDejeunerKey) => petitDejeunerKey.Prix === "amélioré"));
        } else {
          return;
      }
    } else {
        breakfast.petitDejeuner = getRandomElement(PetitsDejeuners.filter((petitDejeunerKey) => petitDejeunerKey.Prix === "repas de fête"));
    }

    if (breakfast.petitDejeuner) {
       const ancienApportsNutritionnels = {
          apportsNutritionnelsPetitDejeuner: petitsDejeuners.value[index].apportsNutritionnelsPetitDejeuner,
      }
      petitsDejeuners.value[index] = petitDejeunerObject(petitsDejeuners.value[index].nombrePropositionsPetitDejeuner);
      petitsDejeuners.value[index].petitDejeuner = breakfast.petitDejeuner;
      updateApportsNutritionnelsPetitDejeuner(index, ancienApportsNutritionnels);
    }
  }

  const clocheDejeuner = (jour) => {
    const duplicateIn = clocheMap[jour];
    for (const repasJour of duplicateIn) {
      if (!(menus.value[repasJour].entree.NomFamEntree === menus.value[jour].entree.NomFamEntree && menus.value[repasJour].plat.NomFamPlat === menus.value[jour].plat.NomFamPlat && menus.value[repasJour].dessert.NomFamDessert === menus.value[jour].dessert.NomFamDessert)) {
        // We save the old "ApportsNutritionnels"
        const ancienApportsNutritionnels = {
          apportsNutritionnelsEntree: menus.value[repasJour].apportsNutritionnelsEntree,
          apportsNutritionnelsPlat: menus.value[repasJour].apportsNutritionnelsPlat,
          apportsNutritionnelsDessert: menus.value[repasJour].apportsNutritionnelsDessert,
        }
        // We duplicate the menu
        menus.value[repasJour] = menus.value[jour];
        nutriments.forEach((nutriment) => {
          apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] -= (ancienApportsNutritionnels.apportsNutritionnelsEntree[nutriment] + ancienApportsNutritionnels.apportsNutritionnelsPlat[nutriment] + ancienApportsNutritionnels.apportsNutritionnelsDessert[nutriment]) / valeursNutritionnels["week"][nutriment][infos.value.genre];
          apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] += (menus.value[repasJour].apportsNutritionnelsEntree[nutriment] + menus.value[repasJour].apportsNutritionnelsPlat[nutriment] + menus.value[repasJour].apportsNutritionnelsDessert[nutriment]) / valeursNutritionnels["week"][nutriment][infos.value.genre];

        })
        // After modification, we break the loop by returning
        return;
      }
    }
  }

  const clochePetitDejeuner = (index) => {
    // nombre propositions petit déjeuner (min: 1, max: 6)
    const count = petitsDejeuners.value[index].nombrePropositionsPetitDejeuner;
    if (count < 6) {
      const otherIndex = (!index) ? 1 : 0;
      petitsDejeuners.value[index].nombrePropositionsPetitDejeuner++;
      petitsDejeuners.value[otherIndex].nombrePropositionsPetitDejeuner--;
      nutriments.forEach((nutriment) => {
        apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] -= (petitsDejeuners.value[otherIndex].apportsNutritionnelsPetitDejeuner[nutriment] / valeursNutritionnels["week"][nutriment][infos.value.genre]);
        apportsNutritionnelsHebdomadaire.value[nutrimentIndex[nutriment]] += (petitsDejeuners.value[index].apportsNutritionnelsPetitDejeuner[nutriment] / valeursNutritionnels["week"][nutriment][infos.value.genre]);
      })
      

    }

  }

  const cancelEdit = () => {
    // TODO: restore old state
    isEditable.value = false;
    apportsNutritionnelsHebdomadaire.value = JSON.parse(JSON.stringify(apportsNutritionnelsHebdomadaireCopy.value));
    petitsDejeuners.value = JSON.parse(JSON.stringify(petitsDejeunersCopy.value));
    menus.value = JSON.parse(JSON.stringify(menusCopy.value));
    encas.value = JSON.parse(JSON.stringify(encasCopy.value));
    vinaigretteDeLaSemaine.value = JSON.parse(JSON.stringify(vinaigretteDeLaSemaineCopy.value));
    listeDeCoursesVisibility.value = JSON.parse(JSON.stringify(listeDeCoursesVisibilityCopy.value));

  }

  const toggleEdit = () => {
    if (!isEditable.value) {
      isEditable.value = true;
      // TODO: REMOVE AFTER FETCHING MENUS AND BREAKFATS FROM BACKEND
      apportsNutritionnelsHebdomadaireCopy.value = JSON.parse(JSON.stringify(apportsNutritionnelsHebdomadaire.value));
      petitsDejeunersCopy.value = JSON.parse(JSON.stringify(petitsDejeuners.value));
      menusCopy.value = JSON.parse(JSON.stringify(menus.value));
      encasCopy.value = JSON.parse(JSON.stringify(encas.value));
      vinaigretteDeLaSemaineCopy.value = JSON.parse(JSON.stringify(vinaigretteDeLaSemaine.value));
      listeDeCoursesVisibilityCopy.value = JSON.parse(JSON.stringify(listeDeCoursesVisibility.value));
    } else {
      isEditable.value = false;
      // save changes
      apportsNutritionnelsHebdomadaireCopy.value = JSON.parse(JSON.stringify(apportsNutritionnelsHebdomadaire.value));
      petitsDejeunersCopy.value = JSON.parse(JSON.stringify(petitsDejeuners.value));
      menusCopy.value = JSON.parse(JSON.stringify(menus.value));
      encasCopy.value = JSON.parse(JSON.stringify(encas.value));
      vinaigretteDeLaSemaineCopy.value = JSON.parse(JSON.stringify(vinaigretteDeLaSemaine.value));
      listeDeCoursesVisibilityCopy.value = JSON.parse(JSON.stringify(listeDeCoursesVisibility.value));


      // TODO: validate changes and submit them
      submitChange();
    }
  }

  const readData = (programme_hebdomadaire) => {
    
    const ancienApportsNutritionnelsPetitDejeuner = {
        apportsNutritionnelsPetitDejeuner: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 },
    }
    const ancienApportsNutritionnelsMenu = {
        apportsNutritionnelsEntree: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 },
        apportsNutritionnelsPlat: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 },
        apportsNutritionnelsDessert: { "fibres": 0, "calcium": 0, "cuivre": 0, "fer": 0, "iode": 0, "magnesium": 0, "manganese": 0, "phosphore": 0, "potassium": 0, "selenium": 0, "sodium": 0, "zinc": 0, "vitamineA": 0, "vitamineD": 0, "vitamineE": 0, "vitamineK1": 0, "vitamineC": 0, "vitamineB1": 0, "vitamineB2": 0, "vitamineB3": 0, "vitamineB5": 0, "vitamineB6": 0, "vitamineB9": 0, "vitamineB12": 0 }
    }
    const daysMap = {"Lundi": "lundi", "Mardi": "mardi", "Mercredi": "mercredi", "Jeudi": "jeudi", "Vendredi": "vendredi", "Samedi": "samedi", "Dimanche": "dimanche"};
    const repasList = ["Dejeuner", "Diner"];
    const repasMap = {"Dejeuner": "dejeuner", "Diner": "diner"};
    // Breakfest
    petitsDejeuners.value[0].petitDejeuner = PetitsDejeuners.find((breakfest) => breakfest.Identifiant === programme_hebdomadaire.petit_dejeuner_0_id);
    petitsDejeuners.value[0].nombrePropositionsPetitDejeuner = programme_hebdomadaire.petit_dejeuner_0_count;
    updateApportsNutritionnelsPetitDejeuner(0, ancienApportsNutritionnelsPetitDejeuner);
    petitsDejeuners.value[1].petitDejeuner = PetitsDejeuners.find((breakfest) => breakfest.Identifiant === programme_hebdomadaire.petit_dejeuner_1_id);
    petitsDejeuners.value[1].nombrePropositionsPetitDejeuner = programme_hebdomadaire.petit_dejeuner_1_count;
    updateApportsNutritionnelsPetitDejeuner(1, ancienApportsNutritionnelsPetitDejeuner);
    // Vinaigrette
    vinaigretteDeLaSemaine.value.vinaigrette = Vinaigrettes.find((vinaigretteItem) => vinaigretteItem.Identifiant === programme_hebdomadaire.vinaigrette_semaine_id);
    updateApportsNutritionnelsVinaigrette();
    semaine[infos.value.preferences.jour_debut_semaine].forEach((jour) => {
      // Encas
      encas.value[jour].encas = Encas.find((encasItem) => encasItem.Identifiant === programme_hebdomadaire[`${daysMap[jour]}_encas_id`]);
      updateApportsNutritionnelsEncas(jour);
      // Menus
      repasList.forEach((repas) => {
        menus.value[`${jour}${repas}`].entree = Entrees.find((entreeItem) => entreeItem.Identifiant === programme_hebdomadaire[`${daysMap[jour]}_${repasMap[repas]}`].entree_id);
        menus.value[`${jour}${repas}`].plat = Plats.find((platItem) => platItem.Identifiant === programme_hebdomadaire[`${daysMap[jour]}_${repasMap[repas]}`].plat_id);
        menus.value[`${jour}${repas}`].dessert = Desserts.find((dessertItem) => dessertItem.Identifiant === programme_hebdomadaire[`${daysMap[jour]}_${repasMap[repas]}`].dessert_id);
        updateApportsNutritionnelsMenus(`${jour}${repas}`, ancienApportsNutritionnelsMenu);
      })
    })
  }

  const loadDefault = () => {
    const daysMap = {"Lundi": "lundi", "Mardi": "mardi", "Mercredi": "mercredi", "Jeudi": "jeudi", "Vendredi": "vendredi", "Samedi": "samedi", "Dimanche": "dimanche"};
    const repasList = ["Dejeuner", "Diner"];
    const repasMap = {"Dejeuner": "dejeuner", "Diner": "diner"};
    let boolean = true;
    boolean &&= petitsDejeuners.value[0].petitDejeuner.Identifiant === backup.value.petit_dejeuner_0_id;
    boolean &&= petitsDejeuners.value[0].nombrePropositionsPetitDejeuner === backup.value.petit_dejeuner_0_count; 
    boolean &&= petitsDejeuners.value[1].petitDejeuner.Identifiant === backup.value.petit_dejeuner_1_id;
    boolean &&= petitsDejeuners.value[1].nombrePropositionsPetitDejeuner === backup.value.petit_dejeuner_1_count; 
    boolean &&= vinaigretteDeLaSemaine.value.vinaigrette.Identifiant === backup.value.vinaigrette_semaine_id;
    semaine[infos.value.preferences.jour_debut_semaine].forEach((jour) => {
      // Encas
      boolean &&= encas.value[jour].encas.Identifiant === backup.value[`${daysMap[jour]}_encas_id`];
      // Menus
      repasList.forEach((repas) => {
        boolean &&= menus.value[`${jour}${repas}`].entree.Identifiant === backup.value[[`${daysMap[jour]}_${repasMap[repas]}`]].entree_id
        && menus.value[`${jour}${repas}`].plat.Identifiant === backup.value[[`${daysMap[jour]}_${repasMap[repas]}`]].plat_id
        && menus.value[`${jour}${repas}`].dessert.Identifiant === backup.value[[`${daysMap[jour]}_${repasMap[repas]}`]].dessert_id
      })
    })

    if (!boolean) {
      readData(backup.value);
    }

  }

  const submitChange = async () => {

    try {
        const data = { id: backup_id.value, default: false, vinaigrette_semaine_id: vinaigretteDeLaSemaine.value.vinaigrette.Identifiant, petit_dejeuner_0_id: petitsDejeuners.value[0].petitDejeuner.Identifiant, petit_dejeuner_0_count: petitsDejeuners.value[0].nombrePropositionsPetitDejeuner, petit_dejeuner_1_id: petitsDejeuners.value[1].petitDejeuner.Identifiant, petit_dejeuner_1_count: petitsDejeuners.value[1].nombrePropositionsPetitDejeuner, lundi_encas_id: encas.value["Lundi"].encas.Identifiant, lundi_dejeuner: { entree_id: menus.value.LundiDejeuner.entree.Identifiant, plat_id: menus.value.LundiDejeuner.plat.Identifiant, dessert_id: menus.value.LundiDejeuner.dessert.Identifiant }, lundi_diner: { entree_id: menus.value.LundiDiner.entree.Identifiant, plat_id: menus.value.LundiDiner.plat.Identifiant, dessert_id: menus.value.LundiDiner.dessert.Identifiant }, mardi_encas_id: encas.value["Mardi"].encas.Identifiant, mardi_dejeuner: { entree_id: menus.value.MardiDejeuner.entree.Identifiant, plat_id: menus.value.MardiDejeuner.plat.Identifiant, dessert_id: menus.value.MardiDejeuner.dessert.Identifiant }, mardi_diner: { entree_id: menus.value.MardiDiner.entree.Identifiant, plat_id: menus.value.MardiDiner.plat.Identifiant, dessert_id: menus.value.MardiDiner.dessert.Identifiant }, mercredi_encas_id: encas.value["Mercredi"].encas.Identifiant, mercredi_dejeuner: { entree_id: menus.value.MercrediDejeuner.entree.Identifiant, plat_id: menus.value.MercrediDejeuner.plat.Identifiant, dessert_id: menus.value.MercrediDejeuner.dessert.Identifiant }, mercredi_diner: { entree_id: menus.value.MercrediDiner.entree.Identifiant, plat_id: menus.value.MercrediDiner.plat.Identifiant, dessert_id: menus.value.MercrediDiner.dessert.Identifiant }, jeudi_encas_id: encas.value["Jeudi"].encas.Identifiant, jeudi_dejeuner: { entree_id: menus.value.JeudiDejeuner.entree.Identifiant, plat_id: menus.value.JeudiDejeuner.plat.Identifiant, dessert_id: menus.value.JeudiDejeuner.dessert.Identifiant }, jeudi_diner: { entree_id: menus.value.JeudiDiner.entree.Identifiant, plat_id: menus.value.JeudiDiner.plat.Identifiant, dessert_id: menus.value.JeudiDiner.dessert.Identifiant }, vendredi_encas_id: encas.value["Vendredi"].encas.Identifiant, vendredi_dejeuner: { entree_id: menus.value.VendrediDejeuner.entree.Identifiant, plat_id: menus.value.VendrediDejeuner.plat.Identifiant, dessert_id: menus.value.VendrediDejeuner.dessert.Identifiant }, vendredi_diner: { entree_id: menus.value.VendrediDiner.entree.Identifiant, plat_id: menus.value.VendrediDiner.plat.Identifiant, dessert_id: menus.value.VendrediDiner.dessert.Identifiant }, samedi_encas_id: encas.value["Samedi"].encas.Identifiant, samedi_dejeuner: { entree_id: menus.value.SamediDejeuner.entree.Identifiant, plat_id: menus.value.SamediDejeuner.plat.Identifiant, dessert_id: menus.value.SamediDejeuner.dessert.Identifiant }, samedi_diner: { entree_id: menus.value.SamediDiner.entree.Identifiant, plat_id: menus.value.SamediDiner.plat.Identifiant, dessert_id: menus.value.SamediDiner.dessert.Identifiant }, dimanche_encas_id: encas.value["Dimanche"].encas.Identifiant, dimanche_dejeuner: { entree_id: menus.value.DimancheDejeuner.entree.Identifiant, plat_id: menus.value.DimancheDejeuner.plat.Identifiant, dessert_id: menus.value.DimancheDejeuner.dessert.Identifiant }, dimanche_diner: { entree_id: menus.value.DimancheDiner.entree.Identifiant, plat_id: menus.value.DimancheDiner.plat.Identifiant, dessert_id: menus.value.DimancheDiner.dessert.Identifiant } };
        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/mes-meilleurs-menus`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
              Authorization: userState.token,

            },
            body: JSON.stringify(data)
          }
        );
        const responseData = await response.json();
        if (!response.ok) {
          throw new Error(responseData.message);
        }

      } catch(error) {
        // Handle errors
        success.value.color = "red";
        success.value.message = "Échec: " + error.message;
      }

  }

    onMounted(async () => {

      try {
        const response = await fetch(
          `${process.env.VUE_APP_API_URL}/api/mes-meilleurs-menus`,
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
          infos.value = JSON.parse(JSON.stringify(responseData.inscrit));
          backup.value = JSON.parse(JSON.stringify(responseData.programme_hebdomadaire_default));
          backup_id.value = responseData.programme_hebdomadaire.id;
          readData(responseData.programme_hebdomadaire);
          // semaine[infos.value.preferences.jour_debut_semaine].forEach((jour) => {
          //   generateRandomEncas(jour);
          // });
          // generateRandomVinaigrette();
        }
      } catch(error) {
        // Handle errors
        success.value.color = "red";
        success.value.message = "Échec: " + error.message;
      }
    });



    return {
      infos,
      backup,
      success,
      semaine,
      petitsDejeuners,
      menus,
      apportsNutritionnelsHebdomadaire,
      generateRandomMenu,
      generateRandomBreakfest,
      repasInfos,
      ingredientsInfos,
      showModalRepas,
      showMesApportsNutritionnels,
      showRepartitionApportsCaloriques,
      showMaListeDeCourses,
      showLegende,
      showChangementRepasPlat,
      showChangementRepasPetitDejeuner,
      ModalRepasRef,
      MesApportsNutritionnelsRef,
      RepartitionApportsCaloriquesRef,
      MaListeDeCoursesRef,
      ChangementRepasRef,
      LegendeRef,
      listeDeCoursesVisibility,
      listeDeCourses,
      goutsMap,
      getTitle,
      handlePlatChange,
      handlePetitDejeunerChange,
      improveMenu,
      improveBreakfast,
      clocheMap,
      clocheDejeuner,
      clochePetitDejeuner,
      isEditable,
      cancelEdit,
      toggleEdit,
      submitChange,
      apportsNutritionnelsHebdomadaireCopy,
      petitsDejeunersCopy,
      menusCopy,
      listeDeCoursesVisibilityCopy,
      encas,
      encasCopy,
      vinaigretteDeLaSemaine,
      vinaigretteDeLaSemaineCopy,
      generateRandomEncas,
      generateRandomVinaigrette,
      loadDefault,
      backup_id,
      planning,
      planningMap
    };
  },
};
</script>

<style scoped>
.mmm-page {
  padding: 250px 0 100px 0;
  background: url("../assets/meilleure-menus.png") center center fixed no-repeat;
  background-size: cover;
  font-family: "TangoSans";
  font-size: 15px;
  font-weight: 100;
}

@media only screen and (max-width: 991px) {
  .mmm-page {
    padding-bottom: 250px;
  }
}
.legend-mmm img {
  padding: 5px;
  height: 35px;
  width: 35px;
}

.tableau {
  padding: 20px;
}

.page-title {
  font-family: "Amanise";
  font-size: clamp(24px, 3vw + 20px, 60px);
  font-weight: 400;
  color: #004c40;
}

.navigation-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}

.navigation-bar div {
  cursor: pointer;
}

.navigation-bar div img {
  padding: 5px;
  height: 35px;
  width: 35px;
}

.menu-style {
  border: 1px solid rgb(0, 0, 0);
  padding: 0;
}

.func-icons {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.func-icons img {
  padding: 5px;
  height: 35px;
  width: 35px;
  cursor: pointer;
}

.repas {
  padding: 5px;
}

.title-style {
  border-bottom: 1px solid rgb(0, 0, 0);
  background-color: #c5e0b3;
  padding: 5px;
}

.image-plat {
  padding: 10px;
  height: 100px;
  background-color: aquamarine;
  display: flex;
  align-items: center;
  justify-content: center;
}

.plat-title {
  min-height: 55px;
  padding: 5px;
  text-decoration: underline;
}

.middle {
  border-top: 0.5px solid rgb(0, 0, 0);
  border-bottom: 0.5px solid rgb(0, 0, 0);
  padding: 10px;
  height: 80px;
}

.bottom-panel {
  padding-top: 10px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
}

.bottom-panel div {
  cursor: pointer;
}

.bottom-panel div img {
  padding: 5px;
  height: 45px;
  widows: 45px;
}

.success {
  margin-top: 10px;
  padding: 10px;
  border-radius: 5px;
  color: white;
}

.disabled {
  opacity: 0.3;
  pointer-events: none; /* Makes the element not respond to mouse events */
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

.button-group {
  display: flex;
  justify-content: space-between;
}

.button-group button {
  flex: 1;
  margin: 0 5px;
}
</style>
