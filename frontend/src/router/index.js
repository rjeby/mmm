import Vue from "vue";
import VueRouter from "vue-router";

import Accueil from "@/views/Accueil.vue";
import NosEngagements from "@/views/NosEngagements.vue";
import MeilleursMangeurs from "@/views/MeilleursMangeurs.vue";
import Conseils from "@/views/Conseils.vue";
import AlimentationPositiveDurable from "@/views/AlimentationPositiveDurable.vue";
import ConseilScientifique from "@/views/ConseilScientifique.vue";
import Actualites from "@/views/Actualites.vue";
import QuiSommesNous from "@/views/QuiSommesNous.vue";
import Contact from "@/views/Contact.vue";
import PolitiqueDeConfidentialite from "@/views/PolitiqueDeConfidentialite.vue";
import Faq from "@/views/Faq.vue";
import PageIntrouvable from "@/views/PageIntrouvable.vue";
import MmmEnPratique from "@/views/MmmEnPratique.vue";
import LesMicroNutriments from "@/views/LesMicroNutriments.vue";
import Inscription from "@/views/Inscription.vue";
import Connection from "@/views/Connection.vue";
import Deconnection from "@/views/Deconnection.vue";
import Inactive from "@/views/Inactive.vue";
import FormulaireInscription from "@/views/FormulaireInscription.vue";
import MaFamille from "@/views/MaFamille.vue";
import MesInfos from "@/views/MesInfos.vue";
import MesPreferences from "@/views/MesPreferences.vue";
import MesMeilleursMenus from "@/views/MesMeilleursMenus.vue";

import { isLoggedIn } from "@/utils/auth";
import { userState } from "@/utils/store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "accueil",
    component: Accueil,
  },
  {
    path: "/meilleurs-mangeurs",
    name: "meilleurs-mangeurs",
    component: MeilleursMangeurs,
  },
  {
    path: "/lalimentation-positive-et-durable",
    name: "lalimentation-positive-et-durable",
    component: AlimentationPositiveDurable,
  },
  {
    path: "/nos-9-engagements",
    name: "nos-9-engagements",
    component: NosEngagements,
  },
  {
    path: "/conseils",
    name: "conseils",
    component: Conseils,
  },
  {
    path: "/conseils-scientifique",
    name: "conseils-scientifique",
    component: ConseilScientifique,
  },
  {
    path: "/actualites",
    name: "actualites",
    component: Actualites,
  },
  {
    path: "/qui-sommes-nous",
    name: "qui-sommes-nous",
    component: QuiSommesNous,
  },
  {
    path: "/contact",
    name: "contact",
    component: Contact,
  },
  {
    path: "/politique-de-confidentialite",
    name: "politique-de-confidentialite",
    component: PolitiqueDeConfidentialite,
  },
  {
    path: "/faq",
    name: "faq",
    component: Faq,
  },
  {
    path: "/mmm-en-pratique",
    name: "mmm-en-pratique",
    component: MmmEnPratique,
  },
  {
    path: "/les-micro-nutriments",
    name: "les-micro-nutriments",
    component: LesMicroNutriments,
  },
  {
    path: "/inscription",
    name: "inscription",
    component: Inscription,
    beforeEnter: (to, from, next) => {
      if (isLoggedIn()) {
        next("/");
      } else {
        next();
      }
    },
  },
  {
    path: "/connection",
    name: "connection",
    component: Connection,
    beforeEnter: (to, from, next) => {
      if (isLoggedIn()) {
        if (
          userState.role === "USER" &&
          !userState.isConfirmed & !userState.hasInfos
        ) {
          next("/inactive");
        } else if (
          userState.role === "USER" &&
          userState.isConfirmed & !userState.hasInfos
        ) {
          next("/formulaire-inscription");
        } else if (
          userState.role === "USER" &&
          userState.isConfirmed & userState.hasInfos
        ) {
          next("/mes-meilleurs-menus");
        }
      } else {
        next();
      }
    },
  },
  {
    path: "/deconnection",
    name: "deconnection",
    component: Deconnection,
    beforeEnter: (to, from, next) => {
      if (isLoggedIn()) {
        next();
      } else {
        next("/");
      }
    },
  },
  {
    path: "/inactive",
    name: "inactive",
    component: Inactive,
    beforeEnter: (to, from, next) => {
      if (
        isLoggedIn() &&
        userState.role === "USER" &&
        !userState.isConfirmed &&
        !userState.hasInfos
      ) {
        next();
      } else {
        next("/");
      }
    },
  },
  {
    path: "/formulaire-inscription",
    name: "formulaire-inscription",
    component: FormulaireInscription,
    beforeEnter: (to, from, next) => {
      if (
        isLoggedIn() &&
        userState.role === "USER" &&
        userState.isConfirmed &&
        !userState.hasInfos
      ) {
        next();
      } else {
        next("/");
      }
    },
  },
  {
    path: "/mes-infos",
    name: "mes-infos",
    component: MesInfos,
    beforeEnter: (to, from, next) => {
      if (
        isLoggedIn() &&
        userState.role === "USER" &&
        userState.isConfirmed &&
        userState.hasInfos
      ) {
        next();
      } else {
        next("/");
      }
    },
  },
  {
    path: "/mes-preferences",
    name: "mes-preferences",
    component: MesPreferences,
    beforeEnter: (to, from, next) => {
      if (
        isLoggedIn() &&
        userState.role === "USER" &&
        userState.isConfirmed &&
        userState.hasInfos
      ) {
        next();
      } else {
        next("/");
      }
    },
  },
  {
    path: "/ma-famille",
    name: "ma-famille",
    component: MaFamille,
    beforeEnter: (to, from, next) => {
      if (
        isLoggedIn() &&
        userState.role === "USER" &&
        userState.isConfirmed &&
        userState.hasInfos
      ) {
        next();
      } else {
        next("/");
      }
    },
  },
  {
    path: "/mes-meilleurs-menus",
    name: "mes-meilleurs-menus",
    component: MesMeilleursMenus,
    beforeEnter: (to, from, next) => {
      if (
        isLoggedIn() &&
        userState.role === "USER" &&
        userState.isConfirmed &&
        userState.hasInfos
      ) {
        next();
      } else {
        next("/");
      }
    },
  },
  {
    path: "/:catchAll(.*)",
    name: "PageIntrouvable",
    component: PageIntrouvable,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    // Always scroll to top when navigating to a new page
    return { x: 0, y: 0 };
  },
});

export default router;
