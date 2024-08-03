describe('Formulaire Inscription Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8080/formulaire-inscription');
    // Wait for the form to be visible before interacting
    cy.get('form').should('be.visible');
  });

  it('should display validation error for invalid prenom', () => {
    cy.get('input[type="text"]').first().clear().type('123');
    cy.get('form').submit();
    cy.get('span').should('contain', 'Prénom invalide');
  });

  it('should display validation error for invalid taille', () => {
    cy.get('input[type="number"]').eq(1).clear().type('300');
    cy.get('form').submit();
    cy.get('span').should('contain', 'Taille invalide. La taille doit être un nombre entre 50 et 220 cm');
  });

  it('should display validation error for invalid poids', () => {
    cy.get('input[type="number"]').eq(2).clear().type('2');
    cy.get('form').submit();
    cy.get('span').should('contain', 'Poids invalide. Le poids doit être un nombre entre 5 et 150 kg');
  });

  it('should display validation error for invalid année de naissance', () => {
    cy.get('input[type="number"]').eq(0).clear().type('1900');
    cy.get('form').submit();
    cy.get('span').should('contain', `L'année de naissance doit être un nombre entre ${new Date().getFullYear() - 114} et ${new Date().getFullYear() - 3}`);
  });

  it('should display validation error for invalid code postal', () => {
    cy.get('input[list="search-input"]').clear().type('00000');
    cy.get('form').submit();
    cy.get('span').should('contain', 'Veuillez entrer un code postal valide');
  });

  it('should add and remove a family member', () => {
    cy.get('button').contains('Ajouter un membre').click();
    cy.get('.associated-member').should('have.length', 1);
    cy.get('button').contains('Supprimer ce membre').click();
    cy.get('.associated-member').should('have.length', 0);
  });
});

describe('Formulaire Inscription Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8080/formulaire-inscription');
    // Wait for the form to be visible before interacting
    cy.get('form').should('be.visible');
  });

  it('should display validation error for invalid prenom', () => {
    cy.get('input[type="text"]').first().clear().type('123');
    cy.get('form').submit();
    cy.get('span').should('contain', 'Prénom invalide');
  });

  it('should display validation error for invalid taille', () => {
    cy.get('input[type="number"]').eq(1).clear().type('300');
    cy.get('form').submit();
    cy.get('span').should('contain', 'Taille invalide. La taille doit être un nombre entre 50 et 220 cm');
  });

  it('should display validation error for invalid poids', () => {
    cy.get('input[type="number"]').eq(2).clear().type('2');
    cy.get('form').submit();
    cy.get('span').should('contain', 'Poids invalide. Le poids doit être un nombre entre 5 et 150 kg');
  });

  it('should display validation error for invalid année de naissance', () => {
    cy.get('input[type="number"]').eq(0).clear().type('1900');
    cy.get('form').submit();
    cy.get('span').should('contain', `L'année de naissance doit être un nombre entre ${new Date().getFullYear() - 114} et ${new Date().getFullYear() - 3}`);
  });

  it('should display validation error for invalid code postal', () => {
    cy.get('input[list="search-input"]').clear().type('00000');
    cy.get('form').submit();
    cy.get('span').should('contain', 'Veuillez entrer un code postal valide');
  });

  it('should add and remove a family member', () => {
    cy.get('button').contains('Ajouter un membre').click();
    cy.get('.associated-member').should('have.length', 1);
    cy.get('button').contains('Supprimer ce membre').click();
    cy.get('.associated-member').should('have.length', 0);
  });
});

describe('Formulaire Inscription Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8080/formulaire-inscription');
    // Wait for the form to be visible before interacting
    cy.get('form').should('be.visible');
  });

  // Existing tests...

  it('should only allow adding up to 5 family members', () => {
    const addButton = cy.get('button').contains('Ajouter un membre');

    // Add 5 family members
    for (let i = 0; i < 5; i++) {
      addButton.click();
    }

    // Check that 5 members have been added
    cy.get('.associated-member').should('have.length', 5);

    // Ensure the add button is not visible after adding 5 members
    cy.get('button').contains('Ajouter un membre').should('not.exist');
  });
});