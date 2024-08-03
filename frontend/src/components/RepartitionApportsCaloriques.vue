<template>
  <b-modal
    size="xl"
    ref="RepartitionApportsCaloriques"
    centered
    hide-footer
    hide-header
  >
    <div>
      <div class="text-center">
        <h1>
          Répartition des apports caloriques de Mes Meilleurs Menus de la
          semaine (Kcal)
        </h1>
      </div>
      <div id="chart">
        <apexchart
          type="pie"
          height="480"
          width="480"
          :options="data.chartOptions"
          :series="data.series"
        ></apexchart>
      </div>
    </div>
  </b-modal>
</template>

<script>
import { ref } from "vue";
export default {
  name: "RepartitionApportsCaloriques",
  props: {
    infos: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const data = ref({
      series: [100],
      chartOptions: {
        chart: {
          height: 480,
          width: 480,
          type: "pie",
        },
        legend: {
          position: "bottom",
        },
        labels: ["User"],
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200,
              },
            },
          },
        ],
      },
    });
    const RepartitionApportsCaloriques = ref(null);
    const currentYear = new Date().getFullYear();
    // eslint-disable-next-line
    const bodyActivityMap = {"0 min": 0, "15 min": 0.25, "30 min": 0.5, "1 heure": 1, "1 heure 30 min": 1.5, "2 heures": 2, "3 heures": 3, "4 heures": 4};
    const NAP = (membre) => {
      // This function compute the "Niveau d'activité physique moyen"
      const sommeil = 8;
      const activiteLegere = bodyActivityMap[membre.activite_legere];
      const activiteMoyenne = bodyActivityMap[membre.activite_moyenne];
      const activiteElevee = bodyActivityMap[membre.activite_elevee];
      const activiteAssise =
        24 - (activiteLegere + activiteMoyenne + activiteElevee + sommeil);
      return (
        (sommeil +
          activiteAssise * 1.5 +
          activiteLegere * 2 +
          activiteMoyenne * 3 +
          activiteElevee * 3.5) /
        24
      );
    };
    const HarrisBenedictFormula = (member, NAP) => {
      const coefficients = {
        femme: { P: 9.74, T: 172.9, A: 4.737, C: 667.051 },
        homme: { P: 13.707, T: 492.3, A: 6.673, C: 77.607 },
      };

      const {
        P: poidsCoeff,
        T: tailleCoeff,
        A: ageCoeff,
        C: constanteCoeff,
      } = coefficients[member.genre];
      return (
        (poidsCoeff * member.poids +
          (tailleCoeff * member.taille) / 100 -
          ageCoeff * (currentYear - member.annee_naissance) +
          constanteCoeff) *
        NAP
      );
    };
    const computeApportsHebdomadaire = () => {
      // This function compute "L'apport calorique hebdomadaire" for each membre of Mes Meilleurs Menus
      // Main user is always present
      data.value.series = [
        Math.round(HarrisBenedictFormula(props.infos, NAP(props.infos)) * 7),
      ];
      data.value.chartOptions.labels = [props.infos.prenom];
      if (props.infos.membres_famille.length) {
        // If other members are present
        props.infos.membres_famille.forEach((membre) => {
          data.value.series.push(
            Math.round(HarrisBenedictFormula(membre, NAP(membre)) * 7)
          );
          data.value.chartOptions.labels.push(membre.prenom);
        });
      }
    };
    const show = () => {
      computeApportsHebdomadaire();
      RepartitionApportsCaloriques.value.show();
    };
    return {
      RepartitionApportsCaloriques,
      data,
      show,
      NAP,
      HarrisBenedictFormula,
      computeApportsHebdomadaire,
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

#chart {
  padding: 0;
  max-width: 480px;
  margin: 35px auto;
}
@media only screen and (max-width: 480px) {
  #chart {
    max-width: 200px;
    margin: 20px auto;
  }
}
</style>
