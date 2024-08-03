describe('Mes Preferences Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8080/mes-preferences');
    // Wait for the form to be visible before interacting
    cy.get('form').should('be.visible');
  });

  it('should exclude an ingredient', () => {
    cy.get('button').contains('Modifier').click();
    cy.get('input[list="search-input"]').clear().type('Tomate farcie');
    cy.get('button').contains('Exclure').click();
    cy.get('button').contains('Ingrédients exclus').click();
    cy.get('.ingredient-item').should('contain', 'Tomate farcie');
  });

  it('should add an ingredient to favorites', () => {
    cy.get('button').contains('Modifier').click();
    cy.get('input[list="search-input"]').clear().type('Pomme de terre, sans peau, rôtie/cuite au four');
    cy.get('button').contains('Favoris').click();
    cy.get('button').contains('Ingrédients favoris').click();
    cy.get('.ingredient-item').should('contain', 'Pomme de terre, sans peau, rôtie/cuite au four');
  });

//   it('should not add more than 10 excluded ingredients', à faire


  it('should submit the form with valid data', () => {
    cy.intercept('PUT', '**/mes-preferences', {
      statusCode: 200,
      body: { message: 'Success' },
    }).as('updateRequest');

    cy.get('button').contains('Modifier').click();

    // Fill in valid form data
    cy.get('select').first().select('Végétarienne', { force: true });
    cy.get('select').eq(1).select('Facile', { force: true });
    
    // Fill in "Temps maximum de préparation" for each day (Déjeuner and Diner)
    const days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'];
    let index = 2;
    days.forEach(day => {
      cy.get('select').eq(index).select('30 min', { force: true });
      index++;
      cy.get('select').eq(index).select('40 min', { force: true });
      index++;
    });

    // Fill in the same values for the mobile view (duplicated table)
    days.forEach(day => {
      cy.get('select').eq(index).select('30 min', { force: true });
      index++;
      cy.get('select').eq(index).select('40 min', { force: true });
      index++;
    });

    cy.get('select').eq(index).select('0', { force: true });
    cy.get('select').eq(index + 1).select('0', { force: true });
    cy.get('select').eq(index + 2).select('Midi', { force: true });
    cy.get('select').eq(index + 3).select('Sucré', { force: true });
    cy.get('select').eq(index + 4).select('Lundi', { force: true });
    cy.get('select').eq(index + 5).select('Mardi', { force: true });
    cy.get('select').eq(index + 6).select('Mercredi', { force: true });


    cy.get('button').contains('Sauvegarder').click();

    cy.wait('@updateRequest').its('response.statusCode').should('eq', 200);
    cy.get('.success').should('contain', 'Success');
  });

  it('should display error message on form submission failure', () => {
    cy.intercept('PUT', '**/mes-preferences', {
      statusCode: 400,
      body: { message: 'Error' },
    }).as('updateRequest');

    cy.get('button').contains('Modifier').click();

    // Fill in valid form data
    cy.get('select').first().select('Végétarienne', { force: true });
    cy.get('select').eq(1).select('Facile', { force: true });
    
   // Fill in "Temps maximum de préparation" for each day (Déjeuner and Diner)
    const days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'];
    let index = 2;
    days.forEach(day => {
      cy.get('select').eq(index).select('30 min', { force: true });
      index++;
      cy.get('select').eq(index).select('40 min', { force: true });
      index++;
    });

    // Fill in the same values for the mobile view (duplicated table)
    days.forEach(day => {
      cy.get('select').eq(index).select('30 min', { force: true });
      index++;
      cy.get('select').eq(index).select('40 min', { force: true });
      index++;
    });

    cy.get('select').eq(index).select('0', { force: true });
    cy.get('select').eq(index + 1).select('0', { force: true });
    cy.get('select').eq(index + 2).select('Midi', { force: true });
    cy.get('select').eq(index + 3).select('Sucré', { force: true });
    cy.get('select').eq(index + 4).select('Lundi', { force: true });
    cy.get('select').eq(index + 5).select('Mardi', { force: true });
    cy.get('select').eq(index + 6).select('Mercredi', { force: true });


    cy.get('button').contains('Sauvegarder').click();

    cy.wait('@updateRequest').its('response.statusCode').should('eq', 400);
    cy.get('.success').should('contain', 'Échec: Error');
  });
});