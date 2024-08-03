<template>
  <div>
    <section>
      <b-container fluid class="d-flex justify-content-center banner-conseils">
        <b-row>
          <b-col style="margin: 250px 0">
            <h1 class="text-center banner-text">
              Conseils aux Meilleurs Mangeurs
            </h1>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <section class="sec-back">
      <b-container>
        <b-row class="my-4">
          <b-card
            class="custom-card"
            style="background-color: rgba(133, 187, 47, 0.3)"
          >
            <b-row>
              <b-col
                cols="12"
                md="4"
                class="d-flex flex-column align-items-center"
              >
                <h1>1</h1>
                <img
                  src="../assets/conseils/conseils-meilleurs-mangeurs-removebg-preview-1.png"
                />
              </b-col>
              <b-col cols="12" md="8">
                <h4 class="conseil">Ne pas oublier d’où nous venons…</h4>
                <p>
                  Nous avons changé très vite nos habitudes alimentaires, ce qui
                  est à l’origine de l’apparition d’un grand nombre de
                  pathologies chroniques telles que les maladies
                  cardio-vasculaires.
                </p>
                <p>
                  Notre organisme est génétiquement programmé pour avoir une
                  alimentation très variée (fruits, plantes, graines, légumes),
                  une consommation faible en sucre rapide, un apport en protéine
                  végétale, mais aussi animale. C’est inscrit d’une certaine
                  manière dans notre patrimoine génétique…
                </p>
              </b-col>
            </b-row>
          </b-card>
        </b-row>

        <b-row class="my-4">
          <b-card class="custom-card">
            <b-row>
              <b-col
                cols="12"
                md="4"
                class="d-flex flex-column align-items-center"
              >
                <h1>2</h1>
                <img src="../assets/conseils/fat.png" alt="Image 2" />
              </b-col>
              <b-col cols="12" md="8">
                <h4 class="conseil">
                  … car sinon nous tombons dans différents pièges…
                </h4>
                <ul>
                  <li>
                    Nous avons tendance à faire le moins d’activité physique par
                    soucis d’économie d’énergie (survie) et pourtant notre
                    organisme en a besoin (par exemple pour fabriquer des
                    protéines musculaires et des molécules antioxydantes).
                  </li>
                  <li>
                    Nous restons stressés par nature, il nous faut donc
                    apprendre à relativiser…
                  </li>
                  <li>
                    Nous sommes attirés par des produits riches en sucres
                    ajoutés pour nous procurer du plaisir gustatif, mais fugace…
                    Les fruits mûrs de nos ancêtres ont été remplacés par des
                    produits artificiellement sucrés…
                  </li>
                </ul>
              </b-col>
            </b-row>
          </b-card>
        </b-row>

        <b-row class="my-4">
          <b-card
            class="custom-card"
            style="background-color: rgba(133, 187, 47, 0.3)"
          >
            <b-row>
              <b-col
                cols="12"
                md="4"
                class="d-flex flex-column align-items-center"
              >
                <h1>3</h1>
                <img src="../assets/conseils/fast_food-.png" alt="Image 3" />
              </b-col>
              <b-col cols="12" md="8">
                <h4 class="conseil">Limiter la fréquence des mauvais repas…</h4>
                <p>
                  Beaucoup de pièges nous tendent les bras, comme la
                  consommation de repas à la fois riches en graisses et sucres
                  rapides. Par exemple en consommant successivement des chips à
                  l’apéritif, du pain blanc pendant le repas. Une soupe
                  industrielle en entrée qui contient du sucre, puis en plat
                  principal un steak haché là encore industriel de provenance
                  douteuse en même temps qu’une purée « toute faite » là encore
                  remplie de sucres rapides. Le repas se fini par un autre
                  apport en graisse avec un fromage, suivi par un dessert
                  quasiment 100% sucre rapide. Il s’en suit un stockage des
                  lipides et une prise de poids assurée.
                </p>
              </b-col>
            </b-row>
          </b-card>
        </b-row>

        <b-row class="my-4">
          <b-card class="custom-card">
            <b-row>
              <b-col
                cols="12"
                md="4"
                class="d-flex flex-column align-items-center"
              >
                <h1>4</h1>
                <img src="../assets/conseils/salades.png" alt="Image 4" />
              </b-col>
              <b-col cols="12" md="8">
                <h4 class="conseil">Ne pas oublier d’où nous venons…</h4>
                <ul>
                  <li>
                    Évitez de prendre des apéritifs trop souvent car ils
                    contiennent généralement des sucres cachés associés à de la
                    graisse.
                  </li>
                  <li>
                    Commencez par une entrée à base de crudités, en privilégiant
                    les produits de saison (ex. mâches en hiver, tomates en
                    été).
                  </li>
                  <li>
                    Confectionnez-vous une bonne vinaigrette avec un jaune
                    d’œuf, un peu vinaigre de cidre, de l’huile d’olive, des
                    herbes divers et variées et des condiments de qualités.
                  </li>
                  <li>
                    Continuez par exemple avec une viande de volaille ou des
                    légumineuses accompagnées d’un légume de saison comme le
                    brocoli, le tout avec une sauce à base de crème et épices
                    (curry, sel).
                  </li>
                  <li>
                    Vous pouvez recouvrir les morceaux de légumes avec des
                    pignons de pin ou graines.
                  </li>
                  <li>
                    Pour finir ce repas, un morceau de fromage au lait de brebis
                    peut être le bienvenu, il vous apporte des minéraux,
                    protéines, mais généralement pas de lactose.
                  </li>
                  <li>Bien évidemment, l’eau accompagne votre repas…</li>
                </ul>
              </b-col>
            </b-row>
          </b-card>
        </b-row>

        <b-row class="my-4">
          <b-col cols="12" class="text-center">
            <a
              ><router-link to="/inscription"
                ><button class="btn sign-btn">
                  Je m'inscris gratuitement
                  <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
                </button>
              </router-link>
            </a>
          </b-col>
        </b-row>
      </b-container>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.banner-conseils {
  background-clip: border-box;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/conseils/conseils-mangeurs.jpg");
  width: 100%;
  height: 600px;
  background-attachment: fixed;
  background-size: cover;
  background-position: bottom 150px center;
  background-repeat: no-repeat;
}

/* Media query for phone-sized screens */
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

/* Media query for phone-sized screens */
@media only screen and (max-width: 991px) {
  .sec-back {
    padding-bottom: 250px;
  }
}

.custom-card {
  background-color: rgba(255, 228, 196, 0.3);
  border-radius: 20px;
  border: none;
  padding: 10px;
}

h1 {
  font-family: "TangoSans";
  font-size: 60px;
  font-weight: 700;
  color: rgb(0, 76, 64);
}

h4 {
  font-family: "Amanise";
  font-size: 32px;
  font-weight: 300;
  color: rgb(0, 76, 64);
}

p,
ul {
  font-family: "TangoSans";
  font-size: 18px;
  font-weight: 300;
  color: rgb(0, 0, 0);
  margin: 0 0 18px;
}

img {
  max-width: 100%;
  height: auto;
  max-height: 300px;
}

.sign-btn {
  font-family: "TangoSans";
  color: white;
  background-color: rgb(133, 187, 47);
  padding: 20px 40px;
}
</style>
