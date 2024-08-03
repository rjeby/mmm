<template>
  <div class="sec-back">
    <section>
      <b-container fluid class="d-flex justify-content-center banner-conseils">
        <b-row align-v="center">
          <b-col>
            <h1 class="text-center banner-text">Les Micro-Nutriments</h1>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <section class="sec-back">
      <b-container>
        <div class="text-center py-3">
          <h2>Les micro-nutriments ça sert à quoi ?</h2>
          <p>
            A la différence des protides, lipides ou glucides, les
            micro-nutriments n’apportent pas d’énergie. Cependant ils sont
            indispensables au bon fonctionnement et développement du corps. Et
            c’est pour cela que Mes Meilleurs Menus sont conçus de façon à vous
            apporter notamment les micro-nutriments dont votre corps a besoin.
          </p>
          <p>
            Voici un aperçu des principaux minéraux et vitamines dont le corps a
            besoin&nbsp;:
          </p>
        </div>

        <b-row>
          <b-col
            cols="12"
            v-for="(nutriment, index) in nutriments"
            :key="index"
          >
            <b-card
              class="nutriment-card"
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
                  class="d-flex justify-content-center align-items-center"
                >
                  <h3>{{ nutriment.symbol }}</h3>
                </b-col>
                <b-col cols="12" md="8">
                  <h4>{{ nutriment.nom }}</h4>
                  <p>{{ nutriment.definition }}</p>
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
  data() {
    return {
      nutriments: [
        {
          symbol: "Mg",
          nom: "Le Magnésium",
          definition:
            "Le magnésium aide à la solidification des os et des dents. Il aide aussi les muscles et le cœur à bien faire leur travail en plus de participer au contrôle de la tension artérielle, à la production des protéines et à l’utilisation de l’énergie provenant des aliments.",
        },
        {
          symbol: "Zn",
          nom: "Le zinc",
          definition:
            "Le zinc joue un rôle important dans la croissance, la réponse immunitaire, les fonctions neurologiques et reproductives. Il participe à la synthèse de l’ADN et des protéines. Il joue également un rôle dans la modulation de l’humeur et dans l’apprentissage, ainsi que dans la vision, le goût et l’odorat. Enfin, il intervient dans le processus de la coagulation sanguine, dans les fonctions de l’hormone thyroïdienne, ainsi que dans le métabolisme de l’insuline.",
        },
        {
          symbol: "Fe",
          nom: "Le fer",
          definition:
            "Le fer a un rôle fondamental dans la constitution de l’hémoglobine, dans la constitution de la myoglobine contenue dans les muscles et dans celle de nombreux enzymes indispensables au fonctionnement de l’organisme. Il est présent en très petite quantité dans l’organisme et une partie de ce fer est éliminée chaque jour.",
        },
        {
          symbol: "Ca",
          nom: "Le calcium",
          definition:
            "Le calcium aide à bâtir et à maintenir des os et des dents solides. Le calcium est indispensable pour les enfants, car leurs os sont en période de croissance et de développement. Le calcium est aussi essentiel aux contractions musculaires, dont celles du coeur. En plus, il contribue à régulariser la pression sanguine, il favorise la cicatrisation et il permet au cerveau d’envoyer des messages aux autres parties du corps.",
        },
        {
          symbol: "P",
          nom: "Le phosphore",
          definition:
            "Le phosphore participe à la minéralisation du squelette et est nécessaire au fonctionnement des nerfs et des muscles. Il intervient dans de nombreuses réactions énergétiques sous forme de phosphates, et dans l’absorption et la transformation de certains nutriments.",
        },
        {
          symbol: "K",
          nom: "Le potassium",
          definition:
            "Le potassium joue un rôle important dans la transmission de l’influx nerveux et dans la contraction musculaire, il est utile au maintien de l’automatisme cardiaque et favorise la digestion et l’assimilation.",
        },
        {
          symbol: "Se",
          nom: "Le sélénium",
          definition:
            "Présent essentiellement dans l’organisme au niveau du foie, le sélénium possède un rôle d’antioxydant qui assure la protection des défenses naturelles de l’organisme. En synergie avec d’autres enzymes du corps, il renforce ainsi notre système immunitaire et aide à lutter contre la propagation des radicaux libres.",
        },
        {
          symbol: "Na",
          nom: "Le sodium",
          definition:
            "Le sodium est l’élément prépondérant dans le sang et dans les liquides extra-cellulaires du corps. Il détermine l’équilibre hydrique de l’organisme et l’hydratation des cellules (avec le potassium). Son élimination ou sa rétention, au niveau rénal, sont l’un des mécanismes de la régulation de la pression artérielle. Il joue un rôle essentiel dans la contraction musculaire, dans le maintien de l’équilibre acido-basique et dans l’excitabilité normale des muscles.",
        },
        {
          symbol: "Mn",
          nom: "Le manganèse",
          definition:
            "Le manganèse participe à l’utilisation des glucides et des lipides par l’organisme. Il entre en jeu également dans la lutte contre les radicaux libres. Il peut même parfois remplacer le magnésium chez certaines enzymes qui en ont besoin.",
        },
        {
          symbol: "Cu",
          nom: "Le cuivre",
          definition:
            "Le cuivre contribue à la pigmentation de la peau et des cheveux. Il intervient aussi dans le transport du fer dans l’organisme et il aide au bon fonctionnement du système nerveux. Le cuivre contribue au bon fonctionnement du système immunitaire. Le cuivre agit comme un antioxydant et contribue à protéger les cellules contre le stress oxydatif.",
        },
        {
          symbol: "Vit A",
          nom: "Vitamines A",
          definition:
            "La vitamine A est importante pour la santé des yeux, le système immunitaire et la reproduction. La vitamine A permet également la croissance des os et des tissus recouvrant les diverses parties du corps (cornée, bronches, intestin, peau, etc.).",
        },
        {
          symbol: "Vit B1",
          nom: "Vitamines B1",
          definition:
            "La vitamine B1 contribue à un métabolisme énergétique normal. La vitamine B1 est impliquée, en tant que co-enzyme, dans le métabolisme et l’assimilation des glucides, lipides et protéines apportés par les aliments consommés. Dans le système nerveux, elle intervient dans la transmission de l’influx nerveux. La vitamine B1 (ou thiamine) contribue à des fonctions psychologiques normales comme la mémoire, le raisonnement ou encore la concentration.",
        },
        {
          symbol: "Vit B2",
          nom: "Vitamine B2",
          definition:
            "La vitamine B2 contribue au maintien d’une peau normale. Les rôles de la vitamine B2 (ou riboflavine) dans l’organisme sont nombreux: la vitamine B2 intervient dans le métabolisme général des glucides, lipides et protéines et plus particulièrement dans l’oxydation du glucose, responsable de la libération d’énergie. Elle joue aussi un rôle dans la respiration cellulaire : la riboflavine intervient au niveau de la cellule (mitochondrie) dans la dégradation des éléments de l’alimentation. Cette dégradation aboutit à la production de produit utilisable pour le fonctionnement cellulaire.",
        },
        {
          symbol: "Vit B3",
          nom: "Vitamine B3",
          definition:
            "La vitamine B3 contribue au métabolisme énergétique normal et à des fonctions comme la mémoire, le raisonnement ou encore la concentration. La vitamine B3 contribue aussi au maintien d’une peau normale.",
        },
        {
          symbol: "Vit B5",
          nom: "Vitamine B5",
          definition:
            "La vitamine B5 contribue à la synthèse normale et au métabolisme normal des hormones stéroïdes, de la vitamine D et de certains neurotransmetteurs. La vitamine B5 joue un rôle dans le bon fonctionnement du système nerveux, dans la biosynthèse de l’acétylcholine, neuromédiateur chimique du système nerveux central. Elle contribue à des fonctions psychologiques normales comme la mémoire, le raisonnement ou encore la concentration.",
        },
        {
          symbol: "Vit B6",
          nom: "Vitamine B6",
          definition:
            "La vitamine B6 joue un rôle dans la libération d’énergie. Elle intervient dans la synthèse des globules rouges et la formation de l’hémoglobine, associée aux vitamines B9 et B12. Elle contribue également à réguler l’activité hormonale. La vitamine B6 aide à réduire la fatigue et contribue au fonctionnement normal du système immunitaire.",
        },
        {
          symbol: "Vit B9",
          nom: "Vitamine B9",
          definition:
            "La vitamine B9 contribue à la croissance des tissus maternels durant la grossesse et participe à la formation normale du sang. Elle aide à réduire la fatigue, participe au bon fonctionnement du système immunitaire et contribue à des fonctions psychologiques normales (mémoire, raisonnement, concentration).",
        },
        {
          symbol: "Vit B12",
          nom: "Vitamine B12",
          definition:
            "La vitamine B12 contribue à la formation des globules sanguins et au bon fonctionnement des nerfs. Les végétariens et végétaliens sont fortement à risque de carence en vitamine B12, la prise d’un complément alimentaire de vitamine B12 leur est recommandée.",
        },
        {
          symbol: "Vit C",
          nom: "Vitamine C",
          definition:
            "La vitamine C augmente l’absorption du fer provenant des produits céréaliers, des légumineuses, des œufs et des légumes. Elle aide au bon fonctionnement du système immunitaire, à cicatriser les plaies ainsi qu’à fabriquer et à régénérer le sang, la peau, les os et les ligaments. Comme la vitamine C a des propriétés antioxydantes, elle contribue aussi à protéger les cellules du corps.",
        },
        {
          symbol: "Vit D",
          nom: "Vitamine D",
          definition:
            "La vitamine D intervient dans l’absorption du calcium et du phosphore par les intestins, puis dans la réabsorption par les reins. Indispensable à la croissance durant la petite enfance, elle assure le maintien du capital osseux à l’âge adulte. Les symptômes d’une carence en vitamine D sont la fatigue, la faiblesse musculaire, la peau sèche, des douleurs osseuses ou des crampes. Près de 80 % de la population occidentale et presque toutes les personnes âgées seraient déficientes en vitamine D car passé un certain âge, l’organisme ne synthétise plus la vitamine D aussi facilement.",
        },
        {
          symbol: "Vit E",
          nom: "Vitamine E",
          definition:
            "La vitamine E est un puissant anti-oxydant qui neutralise les radicaux libres, protégeant ainsi les membranes cellulaires de notre organisme du stress oxydatif.",
        },
        {
          symbol: "Vit K",
          nom: "Vitamine K",
          definition:
            "La vitamine K est essentielle à la coagulation du sang et au métabolisme des os.",
        },
        {
          symbol: "Fibres",
          nom: "Les fibres",
          definition:
            "Les fibres ne sont pas des micro-nutriments mais des macronutriments et sont indispensables au bon développement de notre microbiote intestinal qui joue un rôle capital dans le fonctionnement du corps humain. Les fibres sont des glucides qui ne peuvent être digérés et absorbés par l’organisme. Elles parviennent donc intactes dans le gros intestin où elles nourrissent les bactéries et participent à la santé du microbiote intestinal. Peu caloriques, elles permettent de réguler le transit, en augmentant le volume des selles en cas de constipation et en captant l’eau du tube digestif en cas de diarrhée. Enfin, elles diminuent l’absorption des toxines et mauvaises graisses et ralentissent l’assimilation des glucides. Surtout elles nous aident à nous sentir rassasiés et à mieux contrôler notre appétit.",
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

h2 {
  font-family: "Amanise";
  color: #004c40;
  font-size: clamp(28px, 2vw + 21px, 42px);
  padding: 5px;
  margin: 5px;
}

h3 {
  font-family: "TangoSans";
  font-size: clamp(28px, 2vw + 21px, 42px);
  font-weight: 700;
  color: rgb(0, 128, 62);
  margin: 0 0 25px;
}

h4 {
  font-family: "Amanise";
  color: #004c40;
  font-size: 30px;
  padding: 5px;
  margin: 5px;
}

p {
  font-family: "TangoSans";
  font-size: 18px;
  font-weight: 300;
  color: rgb(0, 0, 0);
  margin: 0 0 18px;
}

.nutriment-card {
  border-radius: 20px;
  border: none;
  margin: 10px;
  padding: 5px;
}
</style>
