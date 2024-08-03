<template>
  <div class="sec-back">
    <!-- Header Section -->
    <section>
      <b-container
        fluid
        class="d-flex justify-content-center banner-engagement"
      >
        <b-row align-v="center">
          <b-col>
            <h1 class="text-center banner-text" style="margin-top: 100px">
              Nos 9 engagements
            </h1>
          </b-col>
        </b-row>
      </b-container>
    </section>
    <!-- Engagements Sections -->
    <section class="sec-back p-1">
      <b-container>
        <b-row v-for="(defi, index) in Defis.part1" :key="index" class="my-4">
          <b-col>
            <b-card
              class="p-3"
              style="
                background-color: bisque;
                border-radius: 20px;
                border: none;
              "
              :style="
                index % 2 !== 0
                  ? { backgroundColor: 'rgba(133, 187, 47, 0.3)' }
                  : { backgroundColor: 'rgba(255, 228, 196, 0.3)' }
              "
            >
              <b-row>
                <b-col
                  cols="12"
                  md="4"
                  class="d-flex flex-column align-items-center"
                >
                  <h3 class="text-center defi">{{ defi.defi }}</h3>
                  <b-img
                    :src="defi.image"
                    alt="css-mask"
                    class="mask-leaf1 mt-3"
                  ></b-img>
                </b-col>
                <b-col cols="12" md="8">
                  <h4>{{ defi.engagement }}</h4>
                  <p>{{ defi.details }}</p>
                </b-col>
              </b-row>
            </b-card>
          </b-col>
        </b-row>

        <b-row
          v-for="(defi, index) in Defis.part2"
          :key="2 + index"
          class="my-4"
        >
          <b-col>
            <b-card
              class="p-3"
              style="border-radius: 20px; border: none"
              :style="
                index % 2 !== 0
                  ? { backgroundColor: 'rgba(133, 187, 47, 0.3)' }
                  : { backgroundColor: 'rgba(255, 228, 196, 0.30)' }
              "
            >
              <b-row>
                <b-col
                  cols="12"
                  md="4"
                  class="d-flex flex-column align-items-center"
                >
                  <h3 class="text-center defi">{{ defi.defi }}</h3>
                  <b-img
                    :src="defi.image"
                    alt="css-mask"
                    class="mask-leaf2 mt-3"
                  ></b-img>
                </b-col>
                <b-col cols="12" md="8">
                  <h4>{{ defi.engagement }}</h4>
                  <p>{{ defi.details }}</p>
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
import img1 from "../assets/nos-9-engagements/courses.jpg";
import img2 from "../assets/nos-9-engagements/enfant.jpg";
import img3 from "../assets/nos-9-engagements/sphere-with-trees-scaled.jpg";
import img4 from "../assets/nos-9-engagements/courses3.png";

export default {
  data() {
    return {
      Defis: {
        part1: [
          {
            id: 1,
            defi: "Défi : Changer nos habitudes tous ensemble",
            engagement:
              "Engagement 1 : Des menus entièrement gratuits dès l’inscription",
            details:
              "Parce que tout le monde doit pouvoir mieux manger pour améliorer sa santé et le climat sans augmenter ses dépenses. L’épidemie de Covid 19 nous a montré la fragilité de nos organismes et chaque jour l’urgence de la crise climatique devient plus pressante. C’est pour cela qu’il est urgent que TOUS ENSEMBLE nous changions notre façon de nous alimenter. C’est l’objectif de Mes Meilleurs Menus, notamment en rendant ce service gratuit dès l’inscription et semaine après semaine aussi longtemps que vous le souhaitez.",
            image: img1,
          },
          {
            id: 2,
            defi: "Défi : Garder le plaisir de manger",
            engagement: "Engagement 2 : Des menus savoureux et de saison",
            details:
              "Parce que manger doit d’abord être un plaisir, Mes Meilleurs Menus vous proposent de découvrir chaque jour des repas différents, simples à confectionner et toujours savoureux. Tout au long des mois et des saisons, nos plats et nos recettes sauront utiliser le meilleur de la cuisine méditerranéenne pour ravir vos papilles et faire du bien à votre corps.",
            image: img2,
          },
        ],
        part2: [
          {
            id: 3,
            defi: "Défi : Se baser sur les résultats de la science",
            engagement:
              "Engagement 3 : Des menus à faible indice glycémique basés sur l’alimentation méditerranéenne",
            details:
              "L’alimentation méditerranéenne a été scientifiquement démontrée comme étant l’une des meilleures au monde en ce qui concerne notamment la prévention des maladies cardiovasculaires. La mise en place de nos menus s’est faite après une synthèse des études scientifiques publiés dans des revues internationales sérieuses qui ont démontrées les nombreux bienfaits de l’alimentation méditerranéenne ainsi que les bienfaits des repas à indice glycémique bas avec peu de sucres rapides. Nos menus combinent ces deux approches afin d’optimiser les effets bénéfiques.",
            image: img3,
          },
          {
            id: 4,
            defi: "Défi : Lutter contre la crise climatique",
            engagement: "Engagement 4 : Des menus bas-carbone",
            details:
              "Mes Meilleurs Menus participent à la réduction des émissions de gaz à effet de serre en :Proposant un remplacement partiel (menu flexitarien) des protéines animales par des protéines végétales. D’après le WWF et Eco2 Initiative, l’empreinte carbone du repas flexitarien est 38% plus faible que celle du repas “classique”. Dans une famille française, cela correspond à environ 10 kg d’équivalent CO2 en moins par personne par semaine, c’est-à-dire aux émissions de CO2 de 93kms parcourus en Peugeot 208 BlueHDI (sur la base d’émissions officielles de 107g/km)! Privilégiant des viandes à plus faibles émissions carbone (poulet, dinde, …) plutôt que les viandes de ruminants dont l’élevage émet du méthane. Vous guidant vers des produits bas carbone issus de filières et de fabricants engagés dans une réduction des émissions de gaz à effet de serre.",
            image: img4,
          },
          {
            id: 5,
            defi: "Défi : Satisfaire mes besoins nutritionnels",
            engagement:
              "Engagement 5 : Des menus riches en vitamines, minéraux et fibres",
            details:
              "En plus d’un apport énergétique adapté à vos besoins, Mes Meilleurs Menus sont conçus pour vous apporter chaque semaine 24 nutriments essentiels (vitamines, minéraux, fibres) et les protéines, lipides et glucides dont votre corps a besoin à hauteur des valeurs nutritionnelles de référence recommandées par l’ANSES (Agence nationale de sécurité sanitaire, de l’alimentation, de l’environnement et du travail). Mes Meilleurs Menus apportent également des fibres et des aliments contenants des probiotiques qui aident à maintenir l’équilibre de votre microbiote.",
            image: img4,
          },
          {
            id: 6,
            defi: "Défi : Atteindre nos objectifs individuels",
            engagement: "Engagement 6 : Des menus personnalisés",
            details:
              "Nous souhaitons tous mieux manger pour notre santé et préserver le climat de notre planète mais nos besoins alimentaires sont différents. C’est pour cela que Mes Meilleurs Menus sont personnalisés en fonction de vos besoins alimentaires sur la base de votre genre, de votre âge, de votre taille, de votre poids et de votre niveau d’activité physique. Si vous avez besoin d’aller plus loin dans la personnalisation, des professionnelles de santé vous aident à mettre Mes Meilleurs Menus en pratique.",
            image: img4,
          },
          {
            id: 7,
            defi: "Défi : Choisir les bons produits",
            engagement:
              "Engagement 7 : Les bons produits rigoureusement sélectionnés par Mes Meilleurs Menus",
            details:
              "Mes Meilleurs Menus a développé un cahier des charges précis pour sélectionner les produits que nous incluons dans nos repas. Les produits que nous incluons dans nos recettes sont sélectionnés pour leurs qualités nutritionnelles, leurs qualités gustatives, leurs bénéfices environnementaux et leur accessibilité par les Meilleurs Mangeurs. Pour plus de détail sur notre méthodologie de sélection de produit, c’est par ici",
            image: img4,
          },
          {
            id: 8,
            defi: "Défi : Préserver son porte-monnaie",
            engagement: "Engagement 8 : Des menus abordables",
            details:
              "Au quotidien, Mes Meilleurs Menus ne coutent pas plus cher : par rapport à un régime occidental riche en viande, le budget pour Mes Meilleurs Menus sera équivalent. Vous ferez des économies sur la viande, sur les produits (hyper) transformés et sur les éventuels grignotages entre les repas et vous dépenserez sans doute un peu plus de poissons, de fruits et de légumes. Privilégier l’eau plutôt que les jus ou d’autres boissons revient également moins cher. Mes Meilleurs Menus privilégient la qualité plutôt que la quantité.",
            image: img4,
          },
          {
            id: 9,
            defi: "Défi : Se rassembler",
            engagement: "Engagement 9 : Des menus qui nous réunissent",
            details:
              "Nous souhaitons que Mes Meilleurs Menus, ce soit aussi la possibilité de rencontrer d’autres Meilleurs Mangeurs de votre région dans un cadre convivial pour améliorer ensemble notre alimentation et inspirer d’autres personnes à devenir des Meilleurs Mangeurs eux aussi. C’est ainsi que collectivement, nous pourrons avoir un impact significatif pour lutter contre la crise climatique.",
            image: img4,
          },
        ],
      },
    };
  },
};
</script>

<style scoped>
.banner-engagement {
  background-clip: border-box;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/nos-9-engagements/repas.png");
  width: 100%;
  height: 600px;
  background-attachment: fixed;
  background-size: cover;
  background-position: bottom 150px center;
  background-repeat: no-repeat;
}

@media only screen and (max-width: 991px) {
  .sec-back {
    padding-bottom: 250px;
  }
}

.banner-text {
  font-family: "Amanise";
  font-size: clamp(36px, 4vw + 29px, 84px);
  font-weight: 400;
  color: white;
}

.sec-back {
  background: url("../assets/meilleure-menus.png");
  background-attachment: fixed;
  background-size: cover;
  background-position: center center;
}

.defi {
  font-family: "TangoSans";
  font-size: 30px;
  font-weight: 700;
  color: rgb(0, 76, 64);
}

h4 {
  font-family: "Amanise";
  font-size: 32px;
  font-weight: 300;
  color: rgb(0, 76, 64);
}

p {
  font-family: "TangoSans";
  font-size: 18px;
  font-weight: 300;
  color: rgb(0, 0, 0);
  margin: 0 0 18px;
}

img {
  width: 300px;
  height: 300px;
  object-fit: cover;
}

.mask-leaf1 {
  width: 100%;
  height: 200%;
  max-width: 300px;
  max-height: 300px;
  -webkit-mask-image: url("../assets/nos-9-engagements/leaf.svg");
  mask-image: url("../assets/nos-9-engagements/leaf.svg");
  -webkit-mask-size: contain;
  mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
}

.mask-leaf2 {
  width: 100%;
  height: auto;
  max-width: 300px;
  max-height: 300px;
  object-fit: contain;
  -webkit-mask-image: url("../assets/nos-9-engagements/leaf.svg");
  mask-image: url("../assets/nos-9-engagements/leaf.svg");
  -webkit-mask-size: contain;
  mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
}
</style>
