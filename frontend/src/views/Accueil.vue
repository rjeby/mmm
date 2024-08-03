<template>
  <div>
    <!-- Main Card Section -->
    <section
      class="banner d-flex justify-content-center align-items-center pt-5"
    >
      <b-container class="my-5 py-5">
        <b-row>
          <b-col
            cols="12"
            lg="6"
            class="text-center"
            style="
              background-color: rgba(0, 76, 64, 0.83);
              border-radius: 15px;
              padding: 10px;
              margin-top: 100px;
            "
          >
            <p
              class="text-nowrap amanise text-capitalize py-3 banner-descr text-larger"
            >
              Mes Meilleurs Menus
            </p>
            <p class="tangosans">
              M'aide à Mieux Manger pour ma santé et climat
            </p>
            <p class="tangosans">
              Je reçois chaque semaine mon programme de savoureux menus
              méditerranéens, équilibrés et durables, avec des recettes
              détaillées et la liste de courses qui va bien.
            </p>

            <a
              ><router-link to="/inscription"
                ><button class="btn btn-lg btn-order2">
                  Je m'inscris gratuitement
                  <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
                </button>
              </router-link>
            </a>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <!-- Program Description Section -->
    <section class="banner-2">
      <b-container>
        <b-row>
          <b-col>
            <h1
              class="text-center my-4 amanise"
              style="color: #004c40; font-size: clamp(32px, 2vw + 25px, 48px)"
            >
              Mes Meilleurs Menus, c'est un programme de menus:
            </h1>
          </b-col>
        </b-row>
        <b-row>
          <b-col
            cols="12"
            md="4"
            class="mb-4 tangosans"
            v-for="(item, index) in programItems"
            :key="index"
          >
            <b-card
              class="h-100 text-center"
              style="border: none"
              :style="
                index % 2 != 0
                  ? { backgroundColor: 'rgba(255,255,255,0)' }
                  : { backgroundColor: 'rgba(133, 187, 47, 0.28)' }
              "
            >
              <div
                class="d-flex justify-content-center align-items-center mb-3"
                style="height: 125px"
              >
                <b-card-img
                  :src="item.imgSrc"
                  alt="Image"
                  class="img-fluids"
                ></b-card-img>
              </div>
              <b-card-text>{{ item.text }}</b-card-text>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </section>
    <section style="background-color: rgba(133, 187, 47, 0.28)">
      <div>
        <svg
          class="svg-container"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 283.5 27.8"
          preserveAspectRatio="none"
        >
          <path
            class="elementor-shape-fill-1"
            d="M283.5,9.7c0,0-7.3,4.3-14,4.6c-6.8,0.3-12.6,0-20.9-1.5c-11.3-2-33.1-10.1-44.7-5.7
          s-12.1,4.6-18,7.4c-6.6,3.2-20,9.6-36.6,9.3C131.6,23.5,99.5,7.2,86.3,8c-1.4,0.1-6.6,0.8-10.5,2c-3.8,1.2-9.4,3.8-17,4.7
          c-3.2,0.4-8.3,1.1-14.2,0.9c-1.5-0.1-6.3-0.4-12-1.6c-5.7-1.2-11-3.1-15.8-3.7C6.5,9.2,0,10.8,0,10.8V0h283.5V9.7z M260.8,11.3
          c-0.7-1-2-0.4-4.3-0.4c-2.3,0-6.1-1.2-5.8-1.1c0.3,0.1,3.1,1.5,6,1.9C259.7,12.2,261.4,12.3,260.8,11.3z M242.4,8.6
          c0,0-2.4-0.2-5.6-0.9c-3.2-0.8-10.3-2.8-15.1-3.5c-8.2-1.1-15.8,0-15.1,0.1c0.8,0.1,9.6-0.6,17.6,1.1c3.3,0.7,9.3,2.2,12.4,2.7
          C239.9,8.7,242.4,8.6,242.4,8.6z M185.2,8.5c1.7-0.7-13.3,4.7-18.5,6.1c-2.1,0.6-6.2,1.6-10,2c-3.9,0.4-8.9,0.4-8.8,0.5
          c0,0.2,5.8,0.8,11.2,0c5.4-0.8,5.2-1.1,7.6-1.6C170.5,14.7,183.5,9.2,185.2,8.5z M199.1,6.9c0.2,0-0.8-0.4-4.8,1.1
          c-4,1.5-6.7,3.5-6.9,3.7c-0.2,0.1,3.5-1.8,6.6-3C197,7.5,199,6.9,199.1,6.9z M283,6c-0.1,0.1-1.9,1.1-4.8,2.5s-6.9,2.8-6.7,2.7
          c0.2,0,3.5-0.6,7.4-2.5C282.8,6.8,283.1,5.9,283,6z M31.3,11.6c0.1-0.2-1.9-0.2-4.5-1.2s-5.4-1.6-7.8-2C15,7.6,7.3,8.5,7.7,8.6
          C8,8.7,15.9,8.3,20.2,9.3c2.2,0.5,2.4,0.5,5.7,1.6S31.2,11.9,31.3,11.6z M73,9.2c0.4-0.1,3.5-1.6,8.4-2.6c4.9-1.1,8.9-0.5,8.9-0.8
          c0-0.3-1-0.9-6.2-0.3S72.6,9.3,73,9.2z M71.6,6.7C71.8,6.8,75,5.4,77.3,5c2.3-0.3,1.9-0.5,1.9-0.6c0-0.1-1.1-0.2-2.7,0.2
          C74.8,5.1,71.4,6.6,71.6,6.7z M93.6,4.4c0.1,0.2,3.5,0.8,5.6,1.8c2.1,1,1.8,0.6,1.9,0.5c0.1-0.1-0.8-0.8-2.4-1.3
          C97.1,4.8,93.5,4.2,93.6,4.4z M65.4,11.1c-0.1,0.3,0.3,0.5,1.9-0.2s2.6-1.3,2.2-1.2s-0.9,0.4-2.5,0.8C65.3,10.9,65.5,10.8,65.4,11.1
          z M34.5,12.4c-0.2,0,2.1,0.8,3.3,0.9c1.2,0.1,2,0.1,2-0.2c0-0.3-0.1-0.5-1.6-0.4C36.6,12.8,34.7,12.4,34.5,12.4z M152.2,21.1
          c-0.1,0.1-2.4-0.3-7.5-0.3c-5,0-13.6-2.4-17.2-3.5c-3.6-1.1,10,3.9,16.5,4.1C150.5,21.6,152.3,21,152.2,21.1z"
          />
          <path
            class="elementor-shape-fill-1"
            d="M269.6,18c-0.1-0.1-4.6,0.3-7.2,0c-7.3-0.7-17-3.2-16.6-2.9c0.4,0.3,13.7,3.1,17,3.3
          C267.7,18.8,269.7,18,269.6,18z"
          />
          <path
            class="elementor-shape-fill-1"
            d="M227.4,9.8c-0.2-0.1-4.5-1-9.5-1.2c-5-0.2-12.7,0.6-12.3,0.5c0.3-0.1,5.9-1.8,13.3-1.2
          S227.6,9.9,227.4,9.8z"
          />
          <path
            class="elementor-shape-fill-1"
            d="M204.5,13.4c-0.1-0.1,2-1,3.2-1.1c1.2-0.1,2,0,2,0.3c0,0.3-0.1,0.5-1.6,0.4
          C206.4,12.9,204.6,13.5,204.5,13.4z"
          />
          <path
            class="elementor-shape-fill-1"
            d="M201,10.6c0-0.1-4.4,1.2-6.3,2.2c-1.9,0.9-6.2,3.1-6.1,3.1c0.1,0.1,4.2-1.6,6.3-2.6
          S201,10.7,201,10.6z"
          />
          <path
            class="elementor-shape-fill-1"
            d="M154.5,26.7c-0.1-0.1-4.6,0.3-7.2,0c-7.3-0.7-17-3.2-16.6-2.9c0.4,0.3,13.7,3.1,17,3.3
          C152.6,27.5,154.6,26.8,154.5,26.7z"
          />
          <path
            class="elementor-shape-fill-1"
            d="M41.9,19.3c0,0,1.2-0.3,2.9-0.1c1.7,0.2,5.8,0.9,8.2,0.7c4.2-0.4,7.4-2.7,7-2.6
          c-0.4,0-4.3,2.2-8.6,1.9c-1.8-0.1-5.1-0.5-6.7-0.4S41.9,19.3,41.9,19.3z"
          />
          <path
            class="elementor-shape-fill-1"
            d="M75.5,12.6c0.2,0.1,2-0.8,4.3-1.1c2.3-0.2,2.1-0.3,2.1-0.5c0-0.1-1.8-0.4-3.4,0
          C76.9,11.5,75.3,12.5,75.5,12.6z"
          />
          <path
            class="elementor-shape-fill-1"
            d="M15.6,13.2c0-0.1,4.3,0,6.7,0.5c2.4,0.5,5,1.9,5,2c0,0.1-2.7-0.8-5.1-1.4
          C19.9,13.7,15.7,13.3,15.6,13.2z"
          />
        </svg>
      </div>
      <!-- Climate Impact Section -->
      <b-container>
        <b-row class="justify-content-center">
          <b-col>
            <h2
              class="text-center my-4 amanise"
              style="color: #004c40; font-size: clamp(32px, 2vw + 25px, 48px)"
            >
              Réduire son impact sur le climat
            </h2>
            <p class="text-center tangosans text-dark">
              D'après
              <a
                style="color: #004c40; font-size: clamp(14px, 2vw + 5px, 18px)"
                href="https://www.wwf.fr/vous-informer/actualites/pour-le-meme-prix-manger-mieux-tout-en-reduisant-notre-impact-sur-la-planete-cest-possible"
                target="_blank"
                >WWF et Eco2 Initiative</a
              >, l'empreinte carbone du repas flexitarien est 38% plus faible
              que celle du repas "classique".
            </p>
            <h3
              class="text-center my-4 tangosans"
              style="
                color: #004c40;
                font-weight: 700;
                font-size: clamp(14px, 2vw + 10px, 25px);
              "
            >
              Émissions de gaz à effet de serre associées à la production de 1
              kg de nourriture:
            </h3>
            <div class="d-flex justify-content-center my-4">
              <b-img
                :src="require('@/assets/accueil/35963672089.png')"
                alt="Carbon emissions"
                fluid
                class="mb-3"
                style="max-height: 400px; border-radius: 15px"
              ></b-img>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </section>
    <section style="background-color: rgba(255, 255, 255, 1)">
      <div>
        <svg
          class="svg-container"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 283.5 27.8"
          preserveAspectRatio="none"
        >
          <path
            class="elementor-shape-fill-2"
            d="M283.5,9.7c0,0-7.3,4.3-14,4.6c-6.8,0.3-12.6,0-20.9-1.5c-11.3-2-33.1-10.1-44.7-5.7
          s-12.1,4.6-18,7.4c-6.6,3.2-20,9.6-36.6,9.3C131.6,23.5,99.5,7.2,86.3,8c-1.4,0.1-6.6,0.8-10.5,2c-3.8,1.2-9.4,3.8-17,4.7
          c-3.2,0.4-8.3,1.1-14.2,0.9c-1.5-0.1-6.3-0.4-12-1.6c-5.7-1.2-11-3.1-15.8-3.7C6.5,9.2,0,10.8,0,10.8V0h283.5V9.7z M260.8,11.3
          c-0.7-1-2-0.4-4.3-0.4c-2.3,0-6.1-1.2-5.8-1.1c0.3,0.1,3.1,1.5,6,1.9C259.7,12.2,261.4,12.3,260.8,11.3z M242.4,8.6
          c0,0-2.4-0.2-5.6-0.9c-3.2-0.8-10.3-2.8-15.1-3.5c-8.2-1.1-15.8,0-15.1,0.1c0.8,0.1,9.6-0.6,17.6,1.1c3.3,0.7,9.3,2.2,12.4,2.7
          C239.9,8.7,242.4,8.6,242.4,8.6z M185.2,8.5c1.7-0.7-13.3,4.7-18.5,6.1c-2.1,0.6-6.2,1.6-10,2c-3.9,0.4-8.9,0.4-8.8,0.5
          c0,0.2,5.8,0.8,11.2,0c5.4-0.8,5.2-1.1,7.6-1.6C170.5,14.7,183.5,9.2,185.2,8.5z M199.1,6.9c0.2,0-0.8-0.4-4.8,1.1
          c-4,1.5-6.7,3.5-6.9,3.7c-0.2,0.1,3.5-1.8,6.6-3C197,7.5,199,6.9,199.1,6.9z M283,6c-0.1,0.1-1.9,1.1-4.8,2.5s-6.9,2.8-6.7,2.7
          c0.2,0,3.5-0.6,7.4-2.5C282.8,6.8,283.1,5.9,283,6z M31.3,11.6c0.1-0.2-1.9-0.2-4.5-1.2s-5.4-1.6-7.8-2C15,7.6,7.3,8.5,7.7,8.6
          C8,8.7,15.9,8.3,20.2,9.3c2.2,0.5,2.4,0.5,5.7,1.6S31.2,11.9,31.3,11.6z M73,9.2c0.4-0.1,3.5-1.6,8.4-2.6c4.9-1.1,8.9-0.5,8.9-0.8
          c0-0.3-1-0.9-6.2-0.3S72.6,9.3,73,9.2z M71.6,6.7C71.8,6.8,75,5.4,77.3,5c2.3-0.3,1.9-0.5,1.9-0.6c0-0.1-1.1-0.2-2.7,0.2
          C74.8,5.1,71.4,6.6,71.6,6.7z M93.6,4.4c0.1,0.2,3.5,0.8,5.6,1.8c2.1,1,1.8,0.6,1.9,0.5c0.1-0.1-0.8-0.8-2.4-1.3
          C97.1,4.8,93.5,4.2,93.6,4.4z M65.4,11.1c-0.1,0.3,0.3,0.5,1.9-0.2s2.6-1.3,2.2-1.2s-0.9,0.4-2.5,0.8C65.3,10.9,65.5,10.8,65.4,11.1
          z M34.5,12.4c-0.2,0,2.1,0.8,3.3,0.9c1.2,0.1,2,0.1,2-0.2c0-0.3-0.1-0.5-1.6-0.4C36.6,12.8,34.7,12.4,34.5,12.4z M152.2,21.1
          c-0.1,0.1-2.4-0.3-7.5-0.3c-5,0-13.6-2.4-17.2-3.5c-3.6-1.1,10,3.9,16.5,4.1C150.5,21.6,152.3,21,152.2,21.1z"
          />
          <path
            class="elementor-shape-fill-2"
            d="M269.6,18c-0.1-0.1-4.6,0.3-7.2,0c-7.3-0.7-17-3.2-16.6-2.9c0.4,0.3,13.7,3.1,17,3.3
          C267.7,18.8,269.7,18,269.6,18z"
          />
          <path
            class="elementor-shape-fill-2"
            d="M227.4,9.8c-0.2-0.1-4.5-1-9.5-1.2c-5-0.2-12.7,0.6-12.3,0.5c0.3-0.1,5.9-1.8,13.3-1.2
          S227.6,9.9,227.4,9.8z"
          />
          <path
            class="elementor-shape-fill-2"
            d="M204.5,13.4c-0.1-0.1,2-1,3.2-1.1c1.2-0.1,2,0,2,0.3c0,0.3-0.1,0.5-1.6,0.4
          C206.4,12.9,204.6,13.5,204.5,13.4z"
          />
          <path
            class="elementor-shape-fill-2"
            d="M201,10.6c0-0.1-4.4,1.2-6.3,2.2c-1.9,0.9-6.2,3.1-6.1,3.1c0.1,0.1,4.2-1.6,6.3-2.6
          S201,10.7,201,10.6z"
          />
          <path
            class="elementor-shape-fill-2"
            d="M154.5,26.7c-0.1-0.1-4.6,0.3-7.2,0c-7.3-0.7-17-3.2-16.6-2.9c0.4,0.3,13.7,3.1,17,3.3
          C152.6,27.5,154.6,26.8,154.5,26.7z"
          />
          <path
            class="elementor-shape-fill-2"
            d="M41.9,19.3c0,0,1.2-0.3,2.9-0.1c1.7,0.2,5.8,0.9,8.2,0.7c4.2-0.4,7.4-2.7,7-2.6
          c-0.4,0-4.3,2.2-8.6,1.9c-1.8-0.1-5.1-0.5-6.7-0.4S41.9,19.3,41.9,19.3z"
          />
          <path
            class="elementor-shape-fill-2"
            d="M75.5,12.6c0.2,0.1,2-0.8,4.3-1.1c2.3-0.2,2.1-0.3,2.1-0.5c0-0.1-1.8-0.4-3.4,0
          C76.9,11.5,75.3,12.5,75.5,12.6z"
          />
          <path
            class="elementor-shape-fill-2"
            d="M15.6,13.2c0-0.1,4.3,0,6.7,0.5c2.4,0.5,5,1.9,5,2c0,0.1-2.7-0.8-5.1-1.4
          C19.9,13.7,15.7,13.3,15.6,13.2z"
          />
        </svg>
      </div>

      <b-container>
        <b-row>
          <div class="text-center text-dark my-4">
            <h1
              class="amanise"
              style="
                color: #004c40;
                font-size: clamp(32px, 2vw + 25px, 48px);
                margin-bottom: 20px;
              "
            >
              Extrait du programme de menus hebdomadaires
            </h1>
          </div>
        </b-row>

        <b-row class="justify-content-center">
          <div
            id="carouselExampleIndicators"
            class="carousel slide"
            data-bs-ride="carousel"
            style="max-width: 800px"
          >
            <div class="carousel-indicators">
              <button
                v-for="(image, index) in images"
                :key="index"
                type="button"
                :data-bs-target="'#carouselExampleIndicators'"
                :data-bs-slide-to="index"
                :class="['indicator-button', { active: index === 0 }]"
                :aria-current="index === 0 ? 'true' : undefined"
                :aria-label="'Slide ' + (index + 1)"
              ></button>
            </div>
            <div class="carousel-inner">
              <div
                v-for="(image, index) in images"
                :key="index"
                :class="['carousel-item', { active: index === 0 }]"
              >
                <img :src="image.src" class="d-block w-100" alt="..." />
              </div>
            </div>
            <button
              class="carousel-control-prev custom-control-prev"
              type="button"
              data-bs-target="#carouselExampleIndicators"
              data-bs-slide="prev"
            >
              <span
                class="carousel-control-prev-icon custom-control-icon"
                aria-hidden="true"
              ></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button
              class="carousel-control-next custom-control-next"
              type="button"
              data-bs-target="#carouselExampleIndicators"
              data-bs-slide="next"
            >
              <span
                class="carousel-control-next-icon custom-control-icon"
                aria-hidden="true"
              ></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </b-row>
      </b-container>

      <div class="d-flex justify-content-center my-5">
        <b-button
          class="btn btn-order"
          href="../assets/Exemple-1.pdf"
          target="_blank"
          type="button"
          >Voir le programme complet</b-button
        >
      </div>
    </section>

    <!-- Additional Links Section -->
    <section
      class="banner-3"
      style="background-color: rgba(241, 140, 46, 0.22)"
    >
      <div>
        <svg
          class="svg-container"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 283.5 27.8"
          preserveAspectRatio="none"
        >
          <path
            class="elementor-shape-fill-3"
            d="M283.5,9.7c0,0-7.3,4.3-14,4.6c-6.8,0.3-12.6,0-20.9-1.5c-11.3-2-33.1-10.1-44.7-5.7
          s-12.1,4.6-18,7.4c-6.6,3.2-20,9.6-36.6,9.3C131.6,23.5,99.5,7.2,86.3,8c-1.4,0.1-6.6,0.8-10.5,2c-3.8,1.2-9.4,3.8-17,4.7
          c-3.2,0.4-8.3,1.1-14.2,0.9c-1.5-0.1-6.3-0.4-12-1.6c-5.7-1.2-11-3.1-15.8-3.7C6.5,9.2,0,10.8,0,10.8V0h283.5V9.7z M260.8,11.3
          c-0.7-1-2-0.4-4.3-0.4c-2.3,0-6.1-1.2-5.8-1.1c0.3,0.1,3.1,1.5,6,1.9C259.7,12.2,261.4,12.3,260.8,11.3z M242.4,8.6
          c0,0-2.4-0.2-5.6-0.9c-3.2-0.8-10.3-2.8-15.1-3.5c-8.2-1.1-15.8,0-15.1,0.1c0.8,0.1,9.6-0.6,17.6,1.1c3.3,0.7,9.3,2.2,12.4,2.7
          C239.9,8.7,242.4,8.6,242.4,8.6z M185.2,8.5c1.7-0.7-13.3,4.7-18.5,6.1c-2.1,0.6-6.2,1.6-10,2c-3.9,0.4-8.9,0.4-8.8,0.5
          c0,0.2,5.8,0.8,11.2,0c5.4-0.8,5.2-1.1,7.6-1.6C170.5,14.7,183.5,9.2,185.2,8.5z M199.1,6.9c0.2,0-0.8-0.4-4.8,1.1
          c-4,1.5-6.7,3.5-6.9,3.7c-0.2,0.1,3.5-1.8,6.6-3C197,7.5,199,6.9,199.1,6.9z M283,6c-0.1,0.1-1.9,1.1-4.8,2.5s-6.9,2.8-6.7,2.7
          c0.2,0,3.5-0.6,7.4-2.5C282.8,6.8,283.1,5.9,283,6z M31.3,11.6c0.1-0.2-1.9-0.2-4.5-1.2s-5.4-1.6-7.8-2C15,7.6,7.3,8.5,7.7,8.6
          C8,8.7,15.9,8.3,20.2,9.3c2.2,0.5,2.4,0.5,5.7,1.6S31.2,11.9,31.3,11.6z M73,9.2c0.4-0.1,3.5-1.6,8.4-2.6c4.9-1.1,8.9-0.5,8.9-0.8
          c0-0.3-1-0.9-6.2-0.3S72.6,9.3,73,9.2z M71.6,6.7C71.8,6.8,75,5.4,77.3,5c2.3-0.3,1.9-0.5,1.9-0.6c0-0.1-1.1-0.2-2.7,0.2
          C74.8,5.1,71.4,6.6,71.6,6.7z M93.6,4.4c0.1,0.2,3.5,0.8,5.6,1.8c2.1,1,1.8,0.6,1.9,0.5c0.1-0.1-0.8-0.8-2.4-1.3
          C97.1,4.8,93.5,4.2,93.6,4.4z M65.4,11.1c-0.1,0.3,0.3,0.5,1.9-0.2s2.6-1.3,2.2-1.2s-0.9,0.4-2.5,0.8C65.3,10.9,65.5,10.8,65.4,11.1
          z M34.5,12.4c-0.2,0,2.1,0.8,3.3,0.9c1.2,0.1,2,0.1,2-0.2c0-0.3-0.1-0.5-1.6-0.4C36.6,12.8,34.7,12.4,34.5,12.4z M152.2,21.1
          c-0.1,0.1-2.4-0.3-7.5-0.3c-5,0-13.6-2.4-17.2-3.5c-3.6-1.1,10,3.9,16.5,4.1C150.5,21.6,152.3,21,152.2,21.1z"
          />
          <path
            class="elementor-shape-fill-3"
            d="M269.6,18c-0.1-0.1-4.6,0.3-7.2,0c-7.3-0.7-17-3.2-16.6-2.9c0.4,0.3,13.7,3.1,17,3.3
          C267.7,18.8,269.7,18,269.6,18z"
          />
          <path
            class="elementor-shape-fill-3"
            d="M227.4,9.8c-0.2-0.1-4.5-1-9.5-1.2c-5-0.2-12.7,0.6-12.3,0.5c0.3-0.1,5.9-1.8,13.3-1.2
          S227.6,9.9,227.4,9.8z"
          />
          <path
            class="elementor-shape-fill-3"
            d="M204.5,13.4c-0.1-0.1,2-1,3.2-1.1c1.2-0.1,2,0,2,0.3c0,0.3-0.1,0.5-1.6,0.4
          C206.4,12.9,204.6,13.5,204.5,13.4z"
          />
          <path
            class="elementor-shape-fill-3"
            d="M201,10.6c0-0.1-4.4,1.2-6.3,2.2c-1.9,0.9-6.2,3.1-6.1,3.1c0.1,0.1,4.2-1.6,6.3-2.6
          S201,10.7,201,10.6z"
          />
          <path
            class="elementor-shape-fill-3"
            d="M154.5,26.7c-0.1-0.1-4.6,0.3-7.2,0c-7.3-0.7-17-3.2-16.6-2.9c0.4,0.3,13.7,3.1,17,3.3
          C152.6,27.5,154.6,26.8,154.5,26.7z"
          />
          <path
            class="elementor-shape-fill-3"
            d="M41.9,19.3c0,0,1.2-0.3,2.9-0.1c1.7,0.2,5.8,0.9,8.2,0.7c4.2-0.4,7.4-2.7,7-2.6
          c-0.4,0-4.3,2.2-8.6,1.9c-1.8-0.1-5.1-0.5-6.7-0.4S41.9,19.3,41.9,19.3z"
          />
          <path
            class="elementor-shape-fill-3"
            d="M75.5,12.6c0.2,0.1,2-0.8,4.3-1.1c2.3-0.2,2.1-0.3,2.1-0.5c0-0.1-1.8-0.4-3.4,0
          C76.9,11.5,75.3,12.5,75.5,12.6z"
          />
          <path
            class="elementor-shape-fill-3"
            d="M15.6,13.2c0-0.1,4.3,0,6.7,0.5c2.4,0.5,5,1.9,5,2c0,0.1-2.7-0.8-5.1-1.4
          C19.9,13.7,15.7,13.3,15.6,13.2z"
          />
        </svg>
      </div>
      <b-container>
        <h1
          class="amanise text-center"
          style="color: #004c40; font-size: clamp(32px, 2vw + 25px, 48px)"
        >
          Découvrez aussi ...
        </h1>

        <b-row>
          <b-col
            cols="12"
            md="4"
            v-for="(link, index) in additionalLinks"
            :key="index"
            class="mb-3"
          >
            <div class="cards h-100">
              <div class="image-wrapper">
                <img
                  :src="link.image"
                  class="card-img-top image-hover"
                  alt="Card image cap"
                />
                <div class="overlay">
                  <div class="overlay-text">
                    <router-link :to="link.route" class="text-overlay">
                      <p>{{ link.text }}</p>
                    </router-link>
                    <router-link
                      :to="link.route"
                      class="btn btn-order2 btn-lg mt-2"
                      >Voir Plus</router-link
                    >
                  </div>
                </div>
              </div>
            </div>
          </b-col>
        </b-row>

        <b-row>
          <b-col class="text-center my-4">
            <router-link to="/inscription"
              ><button class="btn btn-order">
                Je m'inscris gratuitement
                <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
              </button>
            </router-link>
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
      programItems: [
        {
          imgSrc: require("../assets/accueil/MMMFichier-14x-8.png"),
          text: "Entièrement gratuits, car TOUT LE MONDE doit pouvoir améliorer son alimentation tout en protégeant le climat",
        },
        {
          imgSrc: require("../assets/accueil/MMMFichier-24x-8.png"),
          text: "De saison, savoureux avec des produits rigoureusement sélectionnés",
        },
        {
          imgSrc: require("../assets/accueil/MMMFichier-34x-8.png"),
          text: "Avec moins de viande et moins d'émissions de gaz à effet de serre",
        },
        {
          imgSrc: require("../assets/accueil/MMMFichier-44x-8.png"),
          text: "De type méditerranéen à faible indice glycémique conçu sur la base des derniers résultats scientifiques",
        },
        {
          imgSrc: require("../assets/accueil/MMMFichier-54x-8.png"),
          text: "Avec tous les apports nécessaires en 24 nutriments (fibres, vitamines et minéraux)",
        },
        {
          imgSrc: require("../assets/accueil/MMMFichier-74x-8-1.png"),
          text: "Personnalisés qui permettent des apports ajustés aux besoins nutritionnels et qui permettent une perte de poids",
        },
      ],
      additionalLinks: [
        {
          route: "/mmm-en-pratique",
          text: "Des professionelles de santé à votre écoute",
          image: require("@/assets/accueil/professionnels-scaled.jpg"),
        },
        {
          route: "/nos-9-engagements",
          text: "Nos 9 Engagements",
          image: require("@/assets/accueil/young-woman-cafe-dines-traditional-shakshuka-ayran-scaled.jpg"),
        },
        {
          route: "/les-micro-nutriments",
          text: "Micro-nutriments",
          image: require("@/assets/accueil/courses.png"),
        },
      ],
      images: [
        {
          src: require("@/assets/accueil/Capture-decran-2024-01-15-a-13.43.27.png"),
        },
        {
          src: require("@/assets/accueil/Capture-decran-2024-01-15-a-13.44.07.png"),
        },
        {
          src: require("@/assets/accueil/Capture-decran-2024-01-15-a-13.44.46.png"),
        },
        {
          src: require("@/assets/accueil/Capture-decran-2024-01-15-a-13.45.28.png"),
        },
      ],
    };
  },
};
</script>

<style scoped>
section {
  color: white;
}

/* Custom styles for carousel controls and indicators */
.custom-control-prev,
.custom-control-next {
  filter: invert(1);
  /* Invert colors to make the controls black */
}

.custom-control-icon {
  background-color: black;
  /* Ensure the background color of controls is black */
}

.carousel-indicators .indicator-button {
  background-color: black;
  /* Make indicators black */
}

.carousel-indicators .indicator-button.active {
  background-color: rgba(0, 0, 0, 0.75);
  /* Slightly transparent for active indicator */
}

.carousel {
  max-width: 800px;
}

.carousel-item img {
  height: 100%;

  object-fit: contain;
}

.amanise {
  font-size: 150%;
}

.cards {
  background-color: rgba(133, 187, 47, 0.28);
  border: none;
  border-radius: 25px;
}

.card-title {
  color: #ffffff;
  font-family: "Amanise", Sans-serif;
  font-size: 50px;
  font-weight: 500;
}

.img-fluids {
  width: 100%;
  height: 125px;
  height: auto;
  max-width: 125px;
  max-height: 120px;
}

.banner {
  background: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),
    url("../assets/accueil/repas-dehors.png") center center fixed no-repeat;
  background-size: cover;
  height: 700px;
  font-size: larger;
  padding-top: 250px;

  /* height: 700px; */
  /* background-attachment: fixed; */
}

.banner-descr {
  font-size: 300%;
  font-weight: 400;
  color: white;
}

.banner-2 {
  background: url("../assets/meilleure-menus.png") center center fixed no-repeat;
  background-size: cover;

  color: black;
}

/* Media query for phone-sized screens */
@media only screen and (max-width: 991px) {
  .banner-3 {
    padding-bottom: 250px;
  }
}

.btn-order {
  color: white;
  background-color: #004c40;
  padding: 5px 10px 5px 10px;
  transition: 0.3s;
  font-family: "TangoSans";
}

.btn-order:hover {
  color: #004c40;
  background-color: white;
  border-color: #004c40;
}

.btn-order2 {
  color: white;
  background-color: rgb(133, 187, 47);
  transition: 0.3s;
  font-family: "TangoSans";
  border: none;
}

.btn-order2:hover {
  color: white;
  background-color: #004c40;
  border-color: #004c40;
}

/*  SVG container */
.elementor-shape-fill-1 {
  fill: #fff;
}

.elementor-shape-fill-2 {
  fill: rgba(133, 187, 47, 0.28);
}

.elementor-shape-fill-3 {
  fill: #fff;
}

/* svg {
    height: 70px;
    width: 100%
} */

.svg-container {
  height: 70px;
  width: 100%;
}

/* A découvrir section */
.image-wrapper {
  position: relative;
  height: 510px;
  overflow: hidden;
  transition: 0.3s;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: box-shadow 0.3s ease;
}

.image-wrapper:hover img {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  width: 100%;
  transition: 0.5s;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  transition: 0.3s;
}

.overlay:hover {
  background-image: linear-gradient(
    rgba(133, 187, 47, 0.28) 0%,
    rgb(0, 0, 0) 99%
  );
}

.overlay-text {
  color: white;
  font-size: 30px;
  font-family: "Tangosans";
}

.text-overlay {
  color: white;
  text-decoration: none;
}
</style>
