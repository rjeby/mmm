<template>
  <b-modal size="xl" ref="Legend" centered hide-footer hide-header>
    <div class="container tangosans">
      <div>
        <p>
          <img src="../assets/icons/shopping-basket.png" />: Remplacer par un
          plat avec un ingrédient que j’ai déjà ou que je vais acheter (car il
          est en promotion) et que je saisis dans une case avec une recherche
          automatique à mesure que je saisis le nom de l’ingrédient
        </p>
        <p>
          <img src="../assets/icons/iconmonstr-checkbox-14.png" />
          <img src="../assets/icons/box.png" /> : Garder (ou pas) le menu pour
          la liste de course
        </p>
        <p>
          <img src="../assets/icons/heart.png" /> : Remplacer par un menu favori
          : sur un clic le menu est remplacé par un menu favori
        </p>
        <p>
          <img
            src="../assets/icons/circle-of-two-clockwise-arrows-rotation.png"
          />
          : Remplacer par un autre menu au hasard
        </p>
        <p>
          <img src="../assets/icons/magic-wand.png" /> : Remplacer par un menu
          amélioré, si encore un clic, remplacer par un menu de fête : Chaque
          menu est soit « bon marché », «menu amélioré » ou « menu de fête ».
          Par défaut l’application ne propose que des recettes « bon marché »,
          que l’utilisateur peut remplacer par un «menu amélioré » ou un « menu
          de fête » à une date donnée par le bouton sur l’interface.
        </p>
        <p>
          <img src="../assets/icons/fork-and-knife-in-cross.png" /> Sortie au
          restaurant : saisir ce que l’on a mangé au restaurant l’application
          compense les apports nutritionnels sur les 4 jours suivants
        </p>
        <p>
          <img src="../assets/icons/cloche.png" /> Faire des restes pour le
          prochain menu, clic et le même menu apparait pour le menu suivant,
          reclic et l’utilisation des restes est déplacée au menu suivant,
          reclic et c’est au menu encore après. Ainsi si je fais un double clic
          sur ce pictogramme à côté du menu du mardi midi, alors les quantités
          sont doublées et le menu apparait le mercredi midi. Si je fais 3 clics
          alors les quantités sont doublées et apparaissent le mercredi soir.
        </p>
        <p class="paragraph-style">
          <img src="../assets/icons/info.png" />
          Pour modifier Mes Meilleurs Menus de la semaine, cliquez sur le bouton
          modifier. Pour persister les changements, cliquez sur le bouton
          sauvegarder, sinon cliquez sur le bouton annuler. En cliquant sur
          "programme par défaut", le système appliquera automatiquement la
          proposition recommandée par défaut.
        </p>
      </div>
    </div>
  </b-modal>
</template>

<script>
import { ref } from "vue";
export default {
  setup() {
    const Legend = ref(null);
    const show = () => {
      Legend.value.show();
    };
    return {
      show,
      Legend,
    };
  },
};
</script>

<style scoped>
img {
  width: 40px;
  height: 40px;
  padding: 5px;
}

.paragraph-style {
  color: #004c40;
}
</style>
