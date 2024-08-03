const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents() {
      // implement node event listeners here
    },
    viewportWidth: 1280, // Set the viewport width
    viewportHeight: 720, // Set the viewport height
  },
});
