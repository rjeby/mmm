<template>
  <b-modal
    size="xl"
    ref="MesApportsNutritionnels"
    centered
    hide-footer
    hide-header
  >
    <div>
      <div class="text-center">
        <h1>
          Pourcentage de couverture des Valeurs Nutritionnelles de Référence par
          les apports de Mes Meilleurs Menus
        </h1>
      </div>
      <apexchart
        height="700"
        type="bar"
        :options="options"
        :series="[
          {
            name: 'Pourcentage',
            data: apportsNutritionnels,
          },
        ]"
      ></apexchart>
    </div>
  </b-modal>
</template>

<script>
import { ref } from "vue";
export default {
  name: "MesApportsNutritionnels",
  props: {
    apportsNutritionnels: {
      type: Array,
      required: true,
    },
  },
  setup() {
    const MesApportsNutritionnels = ref(null);
    const show = () => {
      MesApportsNutritionnels.value.show();
    };
    return {
      MesApportsNutritionnels,
      show,
      options: {
        chart: {
          id: "Apport Nutritionnel",
        },
        plotOptions: {
          bar: {
            borderRadius: 4,
            borderRadiusApplication: "end",
            horizontal: true,
            colors: {
              ranges: [
                {
                  from: 0,
                  to: 70,
                  color: "#FFFF00",
                },
                {
                  from: 71,
                  to: 10000,
                  color: "#004c40",
                },
              ],
            },
          },
        },
        dataLabels: {
          enabled: false,
        },
        xaxis: {
          forceNiceScale: false,
          max: 500,
          categories: [
            "Fibres (g)",
            "Iode (µg)",
            "Magnésium (mg)",
            "Fer (mg)",
            "Cuivre (mg)",
            "Sodium (mg)",
            "Sélénium (µg)",
            "Zinc (mg)",
            "Phosphore (mg)",
            "Kalcium (mg)",
            "Manganèse (mg)",
            "Potassium (mg)",
            "Vitamine K1 (µg)",
            "Vitamine E (mg)",
            "Vitamine D (µg)",
            "Vitamine C (mg)",
            "Vitamine B12 (µg)",
            "Vitamine B9 (µg)",
            "Vitamine B6 (mg)",
            "Vitamine B5 (mg)",
            "Vitamine B3 (mg)",
            "Vitamine B2 (mg)",
            "Vitamine B1 (mg)",
            "Vitamine A (µg)",
          ],
          labels: {
            style: {
              fontFamily: "TangoSans",
              fontSize: "15px",
              fontWeight: "bold",
              color: "#263238",
            },
            formatter: function (val) {
              return val + "%";
            },
          },
        },
        yaxis: {
          labels: {
            style: {
              fontFamily: "TangoSans",
              fontSize: "15px",
              fontWeight: "bold",
              color: "#263238",
            },
          },
        },
      },
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
</style>
