<template>
  <div>
    <section>
      <b-container fluid class="d-flex justify-content-center banner-mmm">
        <b-row align-v="center">
          <b-col>
            <h1></h1>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <section class="sec-back">
      <b-container>
        <div class="text-center">
          <h1>Qui sommes-nous ?</h1>
          <p>
            Mes Meilleurs Menus sont produits et diffusés par l’Association des
            Meilleurs Mangeurs. Cette association a été fondée par Jean-Noel
            Talabardon et Joffrey Zoll :
          </p>
        </div>

        <b-row>
          <b-card class="custom-card">
            <b-row>
              <b-col cols="12" md="6" order="2" order-md="1">
                <h2>Jean-Noel Talabraon</h2>
                <p>
                  est diplomé d’HEC Paris et du Master de Marketing
                  Pharmaceutique de la Faculté de Pharmacie de Chatenay-Malabry
                  (Université de Paris-Saclay). Il travaille depuis plus de 20
                  ans dans l’industrie pharmaceutique et a eu la fierté de
                  participer à la commercialisation de plusieurs nouveaux
                  médicaments, notamment pour le traitement de l’hypertension,
                  du diabète, de la bronchite chronique obstructive (BPCO), de
                  la migraine et de la sclérose en plaques. Jean-Noel constate
                  que de plus en plus de pathologies chroniques sont la
                  conséquence d’un style de vie trop sédentaire, d’une
                  alimentation trop riche en sucre et trop pauvre en vitamine D
                  et en fibres. Notamment les carences en fibres entrainent avec
                  le temps un déséquilibre du microbiote dont de nombreuses
                  études ont montré les influences néfastes sur notre systeme
                  immunitaire et la survenue de pathologies auto-immunes.
                  Jean-Noel est aussi très sensible aux conséquences
                  désastreuses de la crise climatique, d’où son engagement pour
                  la création de l’Association des Meilleurs Mangeurs et le
                  développement de Mes Meilleurs Menus pour aider concrètement
                  le grand public à Mieux Manger, pour une meilleure santé et un
                  meilleur climat sur notre unique planète.
                </p>
              </b-col>
              <b-col cols="12" md="6" class="col-image1" order="1" order-md="2">
              </b-col>
            </b-row>
          </b-card>
        </b-row>

        <b-row>
          <b-card class="custom-card">
            <b-row>
              <b-col cols="12" md="6" class="col-image2">
                <div></div>
              </b-col>
              <b-col cols="12" md="6">
                <h2>Joffrey Zoll</h2>
                <p>
                  est Enseignant-Chercheur – Praticien Hospitalier en
                  physiologie à la faculté de médecine de Strasbourg. Il est
                  spécialiste des effets de l’exercice physique et de la
                  nutrition. Il travaille depuis 20 ans dans le domaine du
                  métabolisme, chez l’homme sain et malade (maladies
                  cardiovasculaires et métaboliques). Il est plus
                  particulièrement spécialiste de la fonction mitochondriale et
                  des différentes filières énergétiques associés (voies glucides
                  et lipidiques). Depuis plusieurs années il s’intéresse aux
                  effets délétères de la prise de sucre associée à la prise de
                  lipides dans des modèles d’obésité/diabète et il caractérise
                  au niveau mitochondriale hépatique et musculaire, les effets
                  bénéfiques de la prise d’acides gras à chaines moyennes ainsi
                  que les effets bénéfiques du régime cétogène. Concernant sa
                  pratique Hospitalière, il s’est engagé dans la prévention du
                  développement des maladies métaboliques par des actions dans
                  le domaine de l’alimentation et de l’activité physique. Ainsi,
                  il travaille notamment avec la Maison pour la Science de
                  Strasbourg en participant à la formation des professeurs dans
                  le domaine de la nutrition et en se rendant dans des collèges
                  pilotes pour discuter avec les élèves du second degré de ces
                  problèmes concernant l’alimentation/activité physique. Il
                  travaille également avec le Jardin des sciences de Strasbourg
                  et donne des conférences sur des sujets variés tel que les
                  méfaits du sucre, les pièges du chocolat ou les bienfaits de
                  l’activité physique. Joffrey Zoll publie régulièrement des
                  articles scientifiques à destination du grand public, là
                  encore pour aider les citoyens à se sortir des différents
                  pièges de la société de consommation
                </p>
              </b-col>
            </b-row>
          </b-card>
        </b-row>
      </b-container>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.banner-mmm {
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/qui-sommes-nous/equipe-scaled.jpg");
  margin: 50px 0;
  width: 100%;
  height: 700px;
  background-attachment: fixed;
  background-clip: border-box;
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
}

.sec-back {
  background: url("../assets/meilleure-menus.png");
  background-attachment: fixed;
  background-size: cover;
  background-position: center center;
}

@media only screen and (max-width: 991px) {
  .sec-back {
    padding-bottom: 250px;
  }
}

.col-image1 {
  background-image: url("../assets/qui-sommes-nous/1631808822068.jpg");
  background-attachment: scroll;
  background-position: top center;
  background-size: cover;
  min-height: 800px;
}

.col-image2 {
  background-image: url("../assets/qui-sommes-nous/Photo-Joffrey.jpg");
  background-attachment: scroll;
  background-position: top center;
  background-size: cover;
  min-height: 700px;
}

.card-body {
  padding: 0;

  border: none;
}

.custom-card {
  padding: 0;
  margin-bottom: 30px;
  background-color: rgba(133, 187, 47, 0.28);
  border-radius: 20px;
  border: none;
}

p {
  font-family: "TangoSans";
  font-size: 18px;
  font-weight: 300;
  color: rgb(0, 0, 0);
  margin: 18px;
}

img {
  min-height: 990px;
  height: 100%;
  width: auto;
}

h2 {
  font-family: "Amanise";
  font-size: clamp(32px, 2vw + 25px, 48px);
  font-weight: 400;
  color: #004c40;
  padding: 15px;
}

h1 {
  font-family: "Amanise";
  font-size: clamp(36px, 4vw + 29px, 84px);
  font-weight: 400;
  color: #004c40;
}
</style>
