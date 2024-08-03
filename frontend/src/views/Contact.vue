<template>
  <div>
    <section>
      <b-container fluid class="d-flex justify-content-center banner-contact">
        <b-row align-v="center">
          <b-col>
            <h1 class="banner-text">Contactez-nous</h1>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <section class="sec-back">
      <b-container>
        <b-row class="text-center">
          <p>
            Si vous avez des questions, des commentaires, propositions ou des
            remarques concernant Mes Meilleurs Menus, n’hésitez pas à nous
            contacter.
          </p>
        </b-row>
        <b-form>
          <b-input type="text" placeholder="Votre nom et prénom" class="m-3" />
          <b-input type="text" placeholder="Votre adresse mail" class="m-3" />
          <b-form-textarea
            type="text"
            placeholder="Votre message"
            class="m-3"
          />
          <button class="btn env-btn">ENVOYER</button>
        </b-form>
      </b-container>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.banner-contact {
  background-clip: border-box;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/Contact/olives.png");
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

p {
  font-family: "TangoSans";
  font-size: 18px;
  font-weight: 300;
  color: rgb(0, 0, 0);
  margin: 0 0 18px;
}

.env-btn {
  color: white;
  background-color: rgb(0, 76, 64);
  font-family: "TangoSans";
  font-weight: 200;
  border: none;
  border-radius: 10px;
  padding: 10px 20px 10px 20px;
  margin: 10px;
}
</style>
