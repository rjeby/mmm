<template>
  <div class="sec-back">
    <section class="banner d-flex justify-content-center">
      <b-container class="my-5 py-5">
        <b-row>
          <b-col class="text-center">
            <h1
              class="amanise text-capitalize py-3 banner-descr"
              style="margin-top: 250px"
            >
              Ma Communauté des Meilleurs Mangeurs
            </h1>
          </b-col>
        </b-row>
      </b-container>
    </section>
    <section class="container-fluid banner2 py-4">
      <b-container>
        <b-row>
          <b-col cols="12" class="mb-4 p-5">
            <div class="text-center tangosans">
              <h2
                class="amanise"
                style="color: #004c40; font-size: clamp(32px, 2vw + 25px, 48px)"
              >
                Mieux Manger pour ma santé et le climat
              </h2>
              <p class="lead">
                De plus en plus de personnes veulent mieux manger pour leur
                santé et pour préserver le climat et ils s'inscrivent à Mes
                Meilleurs Menus. Voici des témoignages des meilleurs mangeurs
              </p>
            </div>
          </b-col>

          <b-col
            v-for="(person, index) in testimonials"
            :key="index"
            cols="12"
            class="mb-4"
          >
            <b-card
              class="card-testimony"
              :style="
                index % 2 !== 0 ? { backgroundColor: 'rgba(0,0,0,0)' } : {}
              "
            >
              <b-row no-gutters>
                <b-col
                  cols="12"
                  md="2"
                  class="d-flex justify-content-center align-items-center order-1 order-md-1 mb-3 mb-md-0"
                >
                  <b-img
                    :src="person.image"
                    :alt="person.name"
                    fluid
                    class="rounded-circle img-fluid img-size"
                  ></b-img>
                </b-col>
                <b-col cols="12" md="10" class="order-2 order-md-2">
                  <b-card-body>
                    <h5 class="card-title">{{ person.name }}</h5>
                    <p class="card-text">{{ person.text }}</p>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </section>
  </div>
</template>

<script>
export default {
  name: "Testimonials",
  data() {
    return {
      testimonials: [
        {
          name: "Isabelle, 50 ans, du Haut-Rhin",
          text: "Mère de famille, je souhaite améliorer ma santé et celle de mes enfants et participer activement à la réduction des émissions de gaz à effet de serre. \nJ'apprécie Mes Meilleurs Menus pour les idées de menus sans viande et pour le calcul des apports nécessaires en fibres, en vitamines et en minéraux.",
          image: require("@/assets/meilleurs-mangeurs/Isabelle-scaled.jpg"),
        },
        {
          name: "Reine-Marie, 75 ans, du Jura",
          text: "Grand-mère active, je souhaite préserver ma santé et mon porte-monnaie. Pour bien vieillir, je fais attention à mon alimentation. J'apprécie Mes Meilleurs Menus pour les recettes faciles et équilibrées et la sélection de bons produits qui vont avec.",
          image: require("@/assets/meilleurs-mangeurs/Reine-Marie.jpg"),
        },
        {
          name: "Sébastien, 42 ans, de Lozère",
          text: "Je suis un inconditionnel des longues ballades et même de treks en montagne sur plusieurs jours. C'est pourquoi, ce que je mange, c'est essentiel pour garder la forme et pour ne pas trop m'éloigner de mon poids idéal, ce qui n'est pas simple car j'ai tendance à en prendre facilement… Avec Mes Meilleurs Menus, je suis sûr de trouver des menus équilibrés qui m'aideront à atteindre ces objectifs. Étant proche de la nature, il est évident que si je peux diminuer « mon impact carbone », je me dois de le faire. Là encore Mes Meilleurs Menus va me guider afin d'y arriver.",
          image: require("@/assets/meilleurs-mangeurs/Seb-photo.jpg"),
        },
        {
          name: "Sophie, 34 ans, Bas-Rhin",
          text: "Mère de famille, je souhaite améliorer ma digestion, trouver un bon petit déjeuner et manger de meilleurs sucres. Les problèmes qui touchent la planète me tiennent à cœur, j'aimerai agir pour le climat en baissant ma consommation de viande.",
          image: require("@/assets/meilleurs-mangeurs/Photo-Sophie.jpg"),
        },
        {
          name: "Etienne, 35 ans, Seine-et-Marne",
          text: "Père de famille, je souhaite reprendre le sport et atteindre mon poids de forme. Je sais que l'alimentation est primordiale et je tiens particulièrement à montrer l'exemple pour mes enfants. J'ai envie de leur inculquer les bonnes habitudes alimentaires dès les premières années. Les futures générations devront trouver une alimentation moins couteuse pour la planète, c'est pourquoi je tiens à commencer dès aujourd'hui.",
          image: require("@/assets/meilleurs-mangeurs/Photo-Etienne.jpg"),
        },
      ],
    };
  },
};
</script>

<style scoped>
.banner {
  background-clip: border-box;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/meilleurs-mangeurs/couple-souriant-passer-du-temps-ensemble-dans-cuisine-1-1-scaled.jpg");
  /* top 150px center fixed no-repeat; */
  width: 100%;
  height: 600px;
  background-size: cover;

  background-position: top 150px center;
  background-repeat: no-repeat;
}

.banner2 {
  background: url("../assets/meilleurs-mangeurs/forks.png");
  /* top 150px center fixed no-repeat; */
  width: auto;
  height: 100%;

  background-position: center right;
  background-repeat: no-repeat;
}

/* Media query for phone-sized screens */
@media only screen and (max-width: 991px) {
  .sec-back {
    padding-bottom: 250px;
  }
}

.card-testimony {
  padding: 80px 0 80px 0;
  font-family: "TangoSans";
  background-color: rgba(133, 187, 47, 0.28);
  border-color: rgba(133, 187, 47, 0.28);
}

.banner-descr {
  font-size: clamp(36px, 2vw + 29px, 84px);
  font-weight: 400;
  color: white;
}

.img-fluid {
  max-width: 100%;
  height: auto;
}

.rounded-circle {
  border-radius: 50%;
  width: 100px;
  /* Adjust size as needed */
  height: 100px;
  /* Adjust size as needed */
  object-fit: cover;
}

.card-title {
  color: rgb(0, 128, 62);
  font-size: 18px;
  /* Increase the title size */
}

.card-text {
  font-size: 18px;
  /* Increase the text size */
}

.img-size {
  height: 150px;
  /* Ensure consistent size */
  width: 150px;
  /* Ensure consistent size */
  object-fit: cover;
  /* Ensure the image fits the container */
}
</style>
