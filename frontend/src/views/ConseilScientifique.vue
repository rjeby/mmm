<template>
  <div>
    <section>
      <b-container fluid class="d-flex justify-content-center banner-conseils">
        <b-row align-v="center">
          <b-col>
            <h1 class="text-center banner-text">Conseil Scientifique</h1>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <section class="sec-back">
      <b-container>
        <div class="text-center py-3">
          <h2>Conseil scientifique de Mes Meilleurs Menus</h2>
          <p>
            Présidé par Joffrey Zoll, le Conseil scientifique de Mes Meilleurs
            Menus rassemble des spécialistes de la santé, de la nutrition et de
            la lutte contre la crise climatique.
          </p>
          <p>
            Le Conseil scientifique de Mes Meilleurs Menus apporte son expertise
            dans la composition des menus et le développement de nouveaux
            services pour aider le grand public à mieux manger. Il est composé
            de:
          </p>
        </div>

        <b-row v-for="(expert, index) in Experts" :key="index" class="my-4">
          <b-card class="expert-card">
            <b-row>
              <b-col
                cols="12"
                md="5"
                class="d-flex flex-column align-items-center"
              >
                <div>
                  <img :src="expert.image" />
                </div>
              </b-col>
              <b-col cols="12" md="7">
                <h3>{{ expert.nom }}</h3>
                <p>{{ expert.propos }}</p>
              </b-col>
            </b-row>
          </b-card>
        </b-row>
        <div v-for="expert in Experts" :key="expert.id"></div>
      </b-container>
    </section>
  </div>
</template>

<script>
import img1 from "../assets/conseils-scientifique/joffrey.jpg";
import img2 from "../assets/conseils-scientifique/Katia-Befort-e1701528354709.jpeg";
import img3 from "../assets/conseils-scientifique/Eleonore.png";

export default {
  data() {
    return {
      Experts: [
        {
          nom: "Joffrey ZOLL",
          propos:
            "Enseignant-Chercheur – Praticien Hospitalier en physiologie à la faculté de médecine de Strasbourg. Il est spécialiste des effets de l’exercice physique et de la nutrition. Il travaille depuis 20 ans dans le domaine du métabolisme.",
          image: img1,
        },
        {
          nom: "Katia Befort",
          propos:
            "Chercheur en Neurosciences (CNRS et Université de Strasbourg). Elle est spécialiste des comportements addictifs et s’intéresse aux conséquences d’une prise excessive de nourriture riche en gras et/ou en sucre sur le fonctionnement du cerveau.",
          image: img2,
        },
        {
          nom: "Dr Eléonore Djikeussi",
          propos:
            "Médecin cancérologue hématologue et micronutritionniste,  elle a développé une expertise dans l’accompagnement nutrithérapeutique des malades atteints de cancer.",
          image: img3,
        },
      ],
    };
  },
};
</script>

<style scoped>
.banner-conseils {
  background-clip: border-box;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/lalimentation-positive-et-durable/courses.png");
  /*linear-gradient(rgba(0, 0, 0, .5), rgba(0, 0, 0, .5)), top 150px center fixed no-repeat; */
  padding: 50px 0;
  width: 100%;
  height: 700px;
  background-attachment: fixed;
  background-size: cover;
  background-position: bottom 200px center;
  background-repeat: no-repeat;
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

.expert-card {
  background-color: none;
  padding: 80px 0 80px 0;
  border-radius: 20px;
}

h2 {
  font-family: "Amanise";
  color: #004c40;
  font-size: clamp(28px, 2vw + 21px, 42px);
  padding: 5px;
  margin: 5px;
}

h3 {
  font-family: "TangoSans";
  font-size: 18px;
  font-weight: 700;
  color: rgb(0, 128, 62);
  margin: 0 0 25px;
}

p {
  font-family: "TangoSans";
  font-size: 18px;
  font-weight: 300;
  color: rgb(0, 0, 0);
  margin: 0 0 18px;
}

img {
  border-radius: 50%;
  height: 200px;
  width: 200px;
}
</style>
