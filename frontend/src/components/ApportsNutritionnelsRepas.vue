<template>
  <b-modal
    size="xl"
    ref="ApportsNutritionnelsRepas"
    centered
    hide-footer
    hide-header
  >
    <div class="text-center">
      <h1>Apports Nutritionnelles du Menu</h1>
    </div>
    <div id="chart">
      <apexchart
        type="bar"
        height="500"
        :options="data.chartOptions"
        :series="data.series"
      ></apexchart>
    </div>
  </b-modal>
</template>
<script>
import { ref } from "vue";
export default {
  props: {
    repas: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const data = ref({
      series: [
        {
          name: "Entrée",
          data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0,
          ],
        },
        {
          name: "Plat",
          data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0,
          ],
        },
        {
          name: "Dessert",
          data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0,
          ],
        },
      ],
      chartOptions: {
        chart: {
          type: "bar",
          height: 500,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: "60%",
            endingShape: "rounded",
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          show: true,
          width: 1,
          colors: ["transparent"],
        },
        xaxis: {
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
        },
        yaxis: {},
        fill: {
          opacity: 1,
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return val;
            },
          },
        },
      },
    });
    const ApportsNutritionnelsRepas = ref(null);
    const show = () => {
      if (props.repas.plat) {
        data.value.series = [
          {
            name: "Entrée",
            data: [
              Math.round(props.repas.apportsNutritionnelsEntree.fibres / 100),
              Math.round(props.repas.apportsNutritionnelsEntree.iode / 100),
              Math.round(
                props.repas.apportsNutritionnelsEntree.magnesium / 100
              ),
              Math.round(props.repas.apportsNutritionnelsEntree.fer / 100),
              Math.round(props.repas.apportsNutritionnelsEntree.cuivre / 100),
              Math.round(props.repas.apportsNutritionnelsEntree.sodium / 100),
              Math.round(props.repas.apportsNutritionnelsEntree.selenium / 100),
              Math.round(props.repas.apportsNutritionnelsEntree.zinc / 100),
              Math.round(
                props.repas.apportsNutritionnelsEntree.phosphore / 100
              ),
              Math.round(props.repas.apportsNutritionnelsEntree.calcium / 100),
              Math.round(
                props.repas.apportsNutritionnelsEntree.manganese / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.potassium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineK1 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineE / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineD / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineC / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineB12 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineB9 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineB6 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineB5 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineB3 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineB2 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineB1 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsEntree.vitamineA / 100
              ),
            ],
          },
          {
            name: "Plat",
            data: [
              Math.round(props.repas.apportsNutritionnelsPlat.fibres / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.iode / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.magnesium / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.fer / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.cuivre / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.sodium / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.selenium / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.zinc / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.phosphore / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.calcium / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.manganese / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.potassium / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineK1 / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineE / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineD / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineC / 100),
              Math.round(
                props.repas.apportsNutritionnelsPlat.vitamineB12 / 100
              ),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineB9 / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineB6 / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineB5 / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineB3 / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineB2 / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineB1 / 100),
              Math.round(props.repas.apportsNutritionnelsPlat.vitamineA / 100),
            ],
          },
          {
            name: "Dessert",
            data: [
              Math.round(props.repas.apportsNutritionnelsDessert.fibres / 100),
              Math.round(props.repas.apportsNutritionnelsDessert.iode / 100),
              Math.round(
                props.repas.apportsNutritionnelsDessert.magnesium / 100
              ),
              Math.round(props.repas.apportsNutritionnelsDessert.fer / 100),
              Math.round(props.repas.apportsNutritionnelsDessert.cuivre / 100),
              Math.round(props.repas.apportsNutritionnelsDessert.sodium / 100),
              Math.round(
                props.repas.apportsNutritionnelsDessert.selenium / 100
              ),
              Math.round(props.repas.apportsNutritionnelsDessert.zinc / 100),
              Math.round(
                props.repas.apportsNutritionnelsDessert.phosphore / 100
              ),
              Math.round(props.repas.apportsNutritionnelsDessert.calcium / 100),
              Math.round(
                props.repas.apportsNutritionnelsDessert.manganese / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.potassium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineK1 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineE / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineD / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineC / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineB12 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineB9 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineB6 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineB5 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineB3 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineB2 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineB1 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsDessert.vitamineA / 100
              ),
            ],
          },
        ];
      } else if (props.repas.petitDejeuner) {
        data.value.series = [
          {
            name: "Petit Déjeuner",
            data: [
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.fibres / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.iode / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.magnesium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.fer / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.cuivre / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.sodium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.selenium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.zinc / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.phosphore / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.calcium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.manganese / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.potassium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineK1 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineE / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineD / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineC / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineB12 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineB9 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineB6 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineB5 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineB3 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineB2 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineB1 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsPetitDejeuner.vitamineA / 100
              ),
            ],
          },
        ];
      } else if (props.repas.vinaigrette) {
        data.value.series = [
          {
            name: "Vinaigrette",
            data: [
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.fibres / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.iode / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.magnesium / 100
              ),
              Math.round(props.repas.apportsNutritionnelsVinaigrette.fer / 100),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.cuivre / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.sodium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.selenium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.zinc / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.phosphore / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.calcium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.manganese / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.potassium / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineK1 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineE / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineD / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineC / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineB12 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineB9 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineB6 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineB5 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineB3 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineB2 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineB1 / 100
              ),
              Math.round(
                props.repas.apportsNutritionnelsVinaigrette.vitamineA / 100
              ),
            ],
          },
        ];
      }
      ApportsNutritionnelsRepas.value.show();
    };
    return {
      ApportsNutritionnelsRepas,
      data,
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
</style>
