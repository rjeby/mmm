<template>
  <div>
    <section>
      <b-container fluid class="d-flex justify-content-center banner-actualite">
        <b-row align-v="center">
          <b-col>
            <h1 class="text-center banner-text">
              Actualités : la santé par l’alimentation
            </h1>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <section class="banner">
      <b-container>
        <h2 class="text-center">
          Voici nos derniers articles scientifiques en direction du grand public
        </h2>

        <b-row class="justify-content-center m-5 custom-card">
          <b-col>
            <div class="video-header text-center">
              <h2 class="video-title text-left">
                Mes Meilleurs Menus en direct sur France Bleu et France 3 Alsace
              </h2>
              <hr class="title-divider" />
              <div class="video-date">15 Janvier 2024</div>
            </div>
            <div class="video-container text-center">
              <iframe
                src="https://www.facebook.com/plugins/video.php?height=316&href=https%3A%2F%2Fwww.facebook.com%2F100087745325261%2Fvideos%2F917260553401991%2F&show_text=false&width=560&t=0"
                width="100%"
                height="550px"
                style="border: none; overflow: hidden"
                scrolling="no"
                frameborder="0"
                allowfullscreen="true"
                allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"
              >
              </iframe>
            </div>
          </b-col>
        </b-row>

        <b-row>
          <b-col
            v-for="article in Articles"
            :key="article.titre"
            cols="12"
            md="6"
          >
            <b-card class="mb-4 custom-card">
              <b-row no-gutters>
                <!-- <b-col cols="4" class="d-flex justify-content-center align-items-center">
                                    <img :src="article.editeurImage" class="img-fluid" alt="Editor Image">
                                </b-col> -->
                <b-col cols="12">
                  <b-card-body
                    :style="{
                      backgroundImage: `url(${article.editeurImage})`,
                      backgroundPosition: 'top left',
                      backgroundRepeat: 'no-repeat',
                      backgroundSize: '100px auto',
                    }"
                  >
                    <div class="d-flex justify-content-center">
                      <img
                        :src="article.image"
                        style="min-height: 216px; width: auto"
                        class="img-fluid mb-2"
                        alt="Article Image"
                      />
                    </div>
                    <hr class="title-divider" />
                    <h3 class="card-title">{{ article.titre }}</h3>
                    <p class="text-muted">{{ article.date }}</p>
                    <p class="card-text">{{ article.intro }}</p>
                    <b-button class="btn btn-order" :href="article.lien"
                      >Lire plus</b-button
                    >
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
  setup() {
    return {
      Articles: [
        {
          editeurImage: require("../assets/actualites/image_1570192079_26fb85a6e3780598be62e05803cab9b3.png"),
          image: require("../assets/actualites/6625396D-DCD7-4C10-B82B-9CBB391C3C32.jpg"),
          titre: "RÉDUIRE SA CONSOMMATION DE VIANDE, C’EST PARTI !",
          date: "Janvier 2020",
          intro:
            "Vous savez que manger beaucoup de viande est néfaste pour la santé, en plus de poser de sérieux problèmes écologiques, mais vous vous posez de nombreuses questions : comment réduire sa consommation sans souffrir de carences ? À quelle fréquence est-il conseillé d’en manger ? STOP ! Grâce aux explications et conseils délivrés dans ce livre, vous trouverez enfin une réponse claire à toutes vos interrogations.",
          lien: "https://www.fnac.com/a13906757/Veronique-Beck-Reduire-sa-consommation-de-viande-c-est-parti",
        },
        {
          editeurImage: require("../assets/actualites/image_1570192079_26fb85a6e3780598be62e05803cab9b3.png"),
          image: require("../assets/actualites/6625396D-DCD7-4C10-B82B-9CBB391C3C32.jpg"),
          titre: "MES ASTUCES ANTI-GRIGNOTAGE, C’EST PARTI !",
          date: "Septembre 2019",
          intro:
            "Vous êtes un éternel grignoteur et vous avez le sentiment que vous ne prenez plus de plaisir à manger ? Vous avez des addictions à certains aliments ? Vous avez perdu la notion des quantités, bref, vous ne maîtrisez plus ce que vous mangez ? STOP ! Il est temps de vous prendre en main et de réagir. Il s’agit d’en finir avec cette mauvaise habitude qui peut avoir de lourdes répercussions sur votre santé.",
          lien: "https://www.fnac.com/a13445475/Veronique-Beck-Mes-astuces-anti-grignotage-c-est-parti",
        },
        {
          editeurImage: require("../assets/actualites/logo-1.png"),
          image: require("../assets/actualites/oeufs.png"),
          titre: "L’œuf, injustement victime de son cholestérol ?",
          date: "Novembre 2022",
          intro:
            "Cet aliment, riche en cholestérol, a longtemps été étiqueté « mauvais pour la santé ». Ce n’est plus le cas, d’autant que l’œuf possède de nombreux atouts nutritionnels.",
          lien: "https://www.quechoisir.org/actualite-alimentation-l-oeuf-injustement-victime-de-son-cholesterol-n104399/",
        },
        {
          editeurImage: require("../assets/actualites/logo-en-b159aca2598f351db37072c75294e4c8.png"),
          image: require("../assets/actualites/horloge-humaine.png"),
          titre: "Mieux respecter son horloge interne pour une meilleure santé",
          date: "Novembre 2022",
          intro:
            "Nos vies, celle de tous les êtres vivants, sont scandées par divers rythmes biologiques, fondamentaux pour leur bon fonctionnement. Ils peuvent être de trois types, selon leur durée.",
          lien: "https://theconversation.com/mieux-respecter-son-horloge-interne-pour-une-meilleure-sante-194196",
        },
        {
          editeurImage: require("../assets/actualites/logo-en-b159aca2598f351db37072c75294e4c8.png"),
          image: require("../assets/actualites/probleme-cardiaque.png"),
          titre:
            "Insuffisance cardiaque : comment la prévenir, comment la traiter",
          date: "Novembre 2021",
          intro:
            "Ce qu’est l’insuffisance cardiaque, son origine et ses symptômes. Même si la prise en charge médicamenteuse s’améliore, il n’y aura régression du nombre de patients concernés que par de nouvelles habitudes hygiéno-diététiques",
          lien: "https://theconversation.com/insuffisance-cardiaque-comment-la-prevenir-comment-la-traiter-170822",
        },
        {
          editeurImage: require("../assets/actualites/logo-en-b159aca2598f351db37072c75294e4c8.png"),
          image: require("../assets/actualites/chocolat.png"),
          titre:
            "Acides gras « trans » limités par l’UE : que se passe-t-il au niveau moléculaire pour qu’ils soient nocifs ?",
          date: "Avril 2021",
          intro:
            "En 2021, la consommation de graisses de type acides gras trans reste encore très importante dans nos pays occidentaux et de plus en plus de preuves indiquent que cette consommation accrue est un important facteur de risque de développement de maladies cardio-vasculaires.",
          lien: "https://theconversation.com/acides-gras-trans-limites-par-lue-que-se-passe-t-il-au-niveau-moleculaire-pour-quils-soient-nocifs-157791",
        },
      ],
    };
  },
};
</script>

<style scoped>
.banner-actualite {
  background-clip: border-box;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/actualites/actualite-scaled.jpg");
  /*linear-gradient(rgba(0, 0, 0, .5), rgba(0, 0, 0, .5)), top 150px center fixed no-repeat; */
  margin: 50px 0;

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

/* Media query for phone-sized screens */
@media only screen and (max-width: 991px) {
  .banner {
    padding-bottom: 250px;
  }
}

h2 {
  font-family: "TangoSans";
  font-style: italic;
  font-size: clamp(23px, 2vw + 15px, 36px);
  color: rgb(0, 76, 64);
}

.video-section {
  background-color: rgba(241, 140, 46, 0.11);
  /* Light background color */
  padding: 20px;
  border-radius: 10px;
}

.video-title {
  font-family: "TangoSans", sans-serif;
  color: #004c40;
  font-size: 22px;
  margin-bottom: 10px;
}

.title-divider {
  width: 200px;
  border: 1px solid #e57373;
  margin: 10px auto;
  /* Center the line */
}

.video-date {
  font-family: "TangoSans", sans-serif;
  color: #e57373;
  font-size: 1em;
}

.video-container {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.img-fluid {
  max-height: 100px;
  object-fit: cover;
}

.card-title {
  font-family: "TangoSans", sans-serif;
  color: #004c40;
  font-size: 1.2em;
}

.text-muted {
  font-family: "TangoSans", sans-serif;
  color: #e57373;
  font-size: 0.9em;
}

.card-text {
  font-family: "TangoSans", sans-serif;
  font-size: 1em;
}

.custom-card {
  background-color: rgba(241, 140, 46, 0.11);
  border: none;
  border-radius: 20px;
  padding: 25px;
}

.btn-order {
  color: white;
  background-color: rgb(133, 187, 47);
  transition: 0.3s;
  font-family: "TangoSans";
  border: none;
}

.btn-order:hover {
  color: white;
  background-color: #004c40;
  border-color: #004c40;
}
</style>
