describe('Inscription Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8080/inscription');
    // Wait for the form to be visible before interacting
    cy.get('form').should('be.visible');
  });

  it('should display validation error for invalid email', () => {
    cy.get('#email').clear().type('invalid-email');
    cy.get('#email').blur();
    cy.get('.error').should('contain', 'Adresse email non valide');
  });

  it('should display validation error for invalid password', () => {
    cy.get('#password').clear().type('weakpassword');
    cy.get('#password').blur();
    cy.get('.error').should('contain', 'Le mot de passe doit contenir au moins 8 caractères, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial parmi !@#$%^&*');
  });

  it('should display validation error for non-matching passwords', () => {
    cy.get('#password').clear().type('ValidPassword1!');
    cy.get('#confirmPassword').clear().type('DifferentPassword1!');
    cy.get('#confirmPassword').blur();
    cy.get('.error').should('contain', 'Les mots de passe ne correspondent pas');
  });

  it('should submit the form with valid data', () => {
    cy.intercept('POST', '**/api/register', {
      statusCode: 200,
      body: { message: 'Success' },
    }).as('registerRequest');

    // Fill in valid form data
    cy.get('#email').clear().type('test@example.com');
    cy.get('#password').clear().type('ValidPassword1!');
    cy.get('#confirmPassword').clear().type('ValidPassword1!');

    cy.get('form').submit();

    cy.wait('@registerRequest').its('response.statusCode').should('eq', 200);
    cy.url().should('include', '/connection');
  });

  it('should display error message on form submission failure', () => {
    cy.intercept('POST', '**/api/register', {
      statusCode: 400,
      body: { message: 'Error' },
    }).as('registerRequest');

    // Fill in valid form data
    cy.get('#email').clear().type('test@example.com');
    cy.get('#password').clear().type('ValidPassword1!');
    cy.get('#confirmPassword').clear().type('ValidPassword1!');

    cy.get('form').submit();

    cy.wait('@registerRequest').its('response.statusCode').should('eq', 400);
    cy.get('.success').should('contain', "Échec de l'inscription: Error");
  });
});
