<template>
  <b-modal size="xl" ref="ChangementRepas" centered hide-footer hide-header>
    <div class="text-center">
      <h1>
        Changement du plat en fonction d'un ingrédient que vous possédez ou
        souhaitez acheter
      </h1>
    </div>
    <div>
      <b-form-input
        v-model="ingredient"
        list="my-list-id"
        placeholder="Veuillez saisir le nom de l'ingrédient"
      ></b-form-input>
      <datalist id="my-list-id">
        <option v-for="(ingredient, index) in ingredients.file" :key="index">
          {{ ingredient.alim_nom_fr }}
        </option>
      </datalist>
    </div>
    <div class="button-group">
      <button class="btn btn-lg" type="button" @click="sendIngredient">
        Changer
      </button>
    </div>
  </b-modal>
</template>

<script>
import { ref } from "vue";

export default {
  props: {
    ingredients: {
      type: Object,
      required: true,
    },
  },
  setup(props, { emit }) {
    const ingredient = ref(null);
    const ChangementRepas = ref(null);
    const sendIngredient = () => {
      // Check if the ingredient is correct
      if (ingredient.value) {
        const isIn = props.ingredients.file.find(
          (ingredientRepas) => ingredientRepas.alim_nom_fr === ingredient.value
        );
        if (isIn) {
          emit(props.ingredients.signal, {
            ingredient: isIn,
            toChange: props.ingredients.toChange,
          });
          ChangementRepas.value.hide();
        }
      }
    };
    const show = () => {
      ChangementRepas.value.show();
    };
    return {
      ChangementRepas,
      ingredient,
      sendIngredient,
      show,
    };
  },
};
</script>

<style scoped>
h1 {
  font-family: "TangoSans";
  font-size: 18px;
  color: #004c40;
}

.button-group {
  margin-top: 10px;
  display: flex;
  justify-content: center;
}

.button-group button {
  flex: 1;
  margin: 0 5px;
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
</style>
