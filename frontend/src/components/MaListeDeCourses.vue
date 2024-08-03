<template>
  <b-modal size="xl" ref="MaListeDeCourses" centered hide-footer hide-header>
    <div class="list-pdf">
      <h1 class="text-center title-style">Ma liste de Courses</h1>
      <b-table-simple bordered responsive small>
        <colgroup></colgroup>
        <colgroup></colgroup>
        <colgroup></colgroup>
        <colgroup></colgroup>
        <thead>
          <b-tr class="table-success">
            <b-th>Rayon</b-th>
            <b-th>Quantité</b-th>
            <b-th>Unité</b-th>
            <b-th>Aliments</b-th>
          </b-tr>
        </thead>
        <b-tbody>
          <template v-for="rayon in rayons">
            <b-tr
              v-for="(item, code, index) in listeDeCourses[rayon]"
              :key="code"
            >
              <b-th
                class="rayon"
                v-if="index === 0"
                :rowspan="listeDeCourses[`${rayon}Count`]"
                ><h2>{{ rayon }}</h2></b-th
              >
              <b-th>{{ item.quantity }}</b-th>
              <b-th>{{ item.unit }}</b-th>
              <b-th>{{ item.alim_nom_fr }}</b-th>
            </b-tr>
          </template>
        </b-tbody>
      </b-table-simple>
      <!-- <div class="d-flex justify-content-center">
        <button class="btn btn-order" @click="generatePDF">Generate PDF</button>
      </div> -->
    </div>
  </b-modal>
</template>

<script>
import { ref } from "vue";
export default {
  props: {
    listeDeCourses: {
      type: Object,
      required: true,
    },
  },
  setup() {
    const rayons = [
      "Traiteur",
      "Fruits et légumes",
      "Epicerie",
      "Boulangerie",
      "Frais",
      "Boucherie",
      "Charcuterie",
      "Poissonnerie",
      "Œufs",
      "Produits laitiers",
      "Fromagerie",
      "Crèmerie",
      "Boissons",
      "Pâtisserie",
    ];
    const MaListeDeCourses = ref(null);
    const show = () => {
      MaListeDeCourses.value.show();
    };
    // const generatePDF = () => {
    //   const element = document.querySelector(".list-pdf");
    //   element.style.padding = "30px 20px 30px 20px"; // Apply padding
    //   html2pdf()
    //     .from(element)
    //     .save("table.pdf")
    //     .then(() => {
    //       element.style.padding = ""; // Remove padding instantly after saving PDF
    //     });
    // };

    return {
      MaListeDeCourses,
      rayons,
      show,
    };
  },
};
</script>

<style scoped>
.rayon {
  font-family: "Amanise";
  color: #004c40;
}

img {
  padding: 5px;
  height: 45px;
  widows: 45px;
}

.btn-order {
  color: white;
  background-color: #004c40;
  padding: 5px 10px 5px 10px;
  transition: 0.3s;
  font-family: "TangoSans";
}

.btn-order:hover {
  color: #004c40;
  background-color: white;
  border-color: #004c40;
}
</style>
