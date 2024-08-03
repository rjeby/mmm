<template>
  <div>
    <section>
      <b-container fluid class="d-flex justify-content-center banner-faq">
        <b-row align-v="center">
          <b-col>
            <h1 class="banner-text">Questions les plus fréquentes</h1>
          </b-col>
        </b-row>
      </b-container>
    </section>
    <section>
      <h1></h1>
    </section>
    <section class="sec-back">
      <b-container>
        <b-row class="justify-content-center" style="margin: 100px 0 100px 0">
          <b-col cols="12" md="12" lg="12">
            <b-card v-for="(faq, index) in faqs" :key="index" class="faq-card">
              <b-row align-v="center" @click="toggle(index)" class="faq-header">
                <b-col cols="10">
                  <h5 class="faq-question">
                    {{ faq.question }}
                  </h5>
                </b-col>
                <b-col cols="2" class="text-right">
                  <b-button v-b-toggle="'faq-collapse-' + index" variant="link">
                    <b-icon
                      :icon="isCollapsed[index] ? 'plus' : 'dash'"
                      aria-hidden="true"
                    ></b-icon>
                  </b-button>
                </b-col>
              </b-row>
              <b-collapse :id="'faq-collapse-' + index">
                <b-card-body>
                  <p class="faq-answer">{{ faq.answer }}</p>
                </b-card-body>
              </b-collapse>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      faqs: [
        {
          question: "Est-ce que Mes Meilleurs Menus est vraiment gratuit ?",
          answer:
            "Oui ! Mes Meilleurs Menus est un service entièrement gratuit. Mes Meilleurs Menus permet au plus grand nombre de participer à la lutte contre la crise climatique tout en prenant soin de sa santé. Mes Meilleurs Menus sont produits et diffusés par l’Association des Meilleurs Mangeurs, cette association est financée par des dons. Pour soutenir Mes Meilleurs Menus, faites un don.",
        },
        {
          question:
            "Est-ce que Mes Meilleurs Menus vont faire augmenter mon budget alimentation ?",
          answer:
            "Non, par rapport à un régime riche en viande, le budget pour Mes Meilleurs Menus sera équivalent : vous ferez des économies sur la viande, sur les produits (hyper) transformés et sur les grignotages entre les repas et vous dépenserez sans doute un peu plus en poissons, en fruits et en légumes.",
        },
        {
          question:
            "Comment est-ce que Mes Meilleurs Menus participent à la lutte contre la crise climatique ?",
          answer:
            "Par rapport à un régime riche en viande, Mes Meilleurs Menus correspondent à un régime de type flexitarien qui permet une réduction de la consommation de viande sans risque de carence alimentaire par insuffisance des apports. Comme l’élevage des animaux dégage d’importantes quantités de gaz à effet de serre, Mes Meilleurs Menus permet une économie significative d’émissions de gaz à effet de serre, de l’ordre de 38% d’après une étude du WWF et de ECO2 initiatives. Ainsi par rapport à des repas « classiques », Mes Meilleurs Menus permettent d’éviter chaque semaine 10kg d’équivalent CO2, cela correspond aux émissions de 112kms parcourus en Peugeot 208 BlueHDI (sur la base d’émissions officielles de 107g/km).",
        },
        {
          question:
            "A quelle fréquence est-ce que on peut recevoir Mes Meilleurs Menus ?",
          answer:
            "Une fois inscrit.e on reçoit Mes Meilleurs Menus chaque semaine et on peut se désinscrire quand on veut.",
        },
        {
          question:
            "Est-il possible de se faire livrer les produits nécessaires pour préparer Mes Meilleurs Menus sur une semaine ?",
          answer: "Cela n’est pas encore possible mais nous y réfléchissons.",
        },
        {
          question:
            "Est-ce que je peux perdre du poids avec Mes Meilleurs Menus?",
          answer:
            "Oui, si vous le souhaitez, les apports en calories de Mes Meilleurs Menus peuvent être réduits pour vous aider à retrouver votre poids de forme en perdant jusqu’à 1kg par mois. Pour cela, dans le formulaire d’inscription, en réponse à la question « Est-ce que je souhaite perdre du poids ? », répondez « Oui, je souhaite perdre jusqu’à un kilo par mois ».",
        },
        {
          question:
            "Est-ce que Mes Meilleurs Menus convient aussi aux Musulmans?",
          answer:
            "Oui, Mes Meilleurs Menus a pour ambition de rassembler le plus grand nombre pour que chacun puisse mieux manger pour sa santé et pour le climat et donc bien sûr Mes Meilleurs Menus convient également aux Musulmans. De façon générale, Mes Meilleurs Menus proposent une recette à base de poisson, de viande ou d’œufs une fois par jour et lorsqu’une recette inclut du porc, une viande alternative est systématiquement proposée.",
        },
        {
          question:
            "Est-ce que je peux également faire bénéficier mon conjoint de Mes Meilleurs Menus?",
          answer:
            "Oui, il est possible de recevoir Mes Meilleurs Menus avec les quantités ajustées pour 2 personnes. Pour cela dans le formulaire d’inscription, dans la seconde partie après vous être inscrit, vous avez la possibilité d’inscrire une deuxième personne avec qui vous partagez habituellement vos repas.",
        },
      ],
      isCollapsed: [],
    };
  },
  mounted() {
    this.isCollapsed = this.faqs.map(() => true);
  },
  methods: {
    toggle(index) {
      this.$set(this.isCollapsed, index, !this.isCollapsed[index]);
    },
  },
};
</script>

<style scoped>
.banner-faq {
  background-clip: border-box;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/healthy-scaled.jpg");
  /*linear-gradient(rgba(0, 0, 0, .5), rgba(0, 0, 0, .5)), top 150px center fixed no-repeat; */
  margin: 50px 0;

  width: 100%;
  height: 700px;
  background-attachment: fixed;
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
}

.banner-text {
  font-family: "Amanise";
  font-size: clamp(36px, 4vw + 29px, 84px);
  font-weight: 400;
  color: white;
}

.faq-container {
  background-color: #edf4d9;
  padding: 20px;
  border-radius: 15px;
}

/* Media query for phone-sized screens */
@media only screen and (max-width: 991px) {
  .sec-back {
    padding-bottom: 250px;
  }
}

.faq-card {
  margin-bottom: 10px;
  border: none;
  /* background-color: rgba(133, 187, 47, 0.28); */
  border-radius: 10px;
}

.faq-question {
  cursor: pointer;
  /* color: #004C40; */
}

.faq-answer {
  font-size: 16px;
  /* color: #333; */
}
</style>
