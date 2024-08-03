describe('Form Validation Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8080/connection');
    // Wait for the form to be visible before interacting
    cy.get('form').should('be.visible');
  });

  it('should show email error for invalid email', () => {
    cy.get('#email').type('invalid-email', { force: true });
    cy.get('form').submit();
    cy.get('.error').should('contain', 'Adresse email non valide');
  });

  it('should show password error for invalid password', () => {
    cy.get('#password').type('invalidpass', { force: true });
    cy.get('form').submit();
    cy.get('.error').should('contain', 'Le mot de passe doit contenir au moins 8 caractères, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial parmi !@#$%^&*');
  });

  it('should not show errors for valid email and password', () => {
    cy.get('#email').type('test@example.com', { force: true });
    cy.get('#password').type('ValidPassword1!', { force: true });
    cy.get('form').submit();
    cy.get('.error').should('not.exist');
  });
});


// must run both frontend and backend servers to run the following test, be wary of that
describe('Form Submission Test', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8080/connection');
    // Wait for the form to be visible before interacting
    cy.get('form').should('be.visible');
  });

  it('should submit the form with valid credentials', () => {
    cy.intercept('POST', '**/api/login', {
      statusCode: 200,
      body: { access_token: 'fakeToken', is_confirmed: true, has_infos: true },
    }).as('loginRequest');

    cy.get('#email').should('be.visible').type('test@example.com', { force: true });
    cy.get('#password').should('be.visible').type('ValidPassword1!', { force: true });
    cy.get('form').submit();

    cy.wait('@loginRequest').its('response.statusCode').should('eq', 200);
    cy.get('.success').should('not.exist');
  });

  it('should show error message on login failure', () => {
    cy.intercept('POST', '**/api/login', {
      statusCode: 401,
      body: { message: 'Unauthorized' },
    }).as('loginRequest');

    cy.get('#email').should('be.visible').type('test@example.com', { force: true });
    cy.get('#password').should('be.visible').type('WrongPassword1!', { force: true });
    cy.get('form').submit();

    cy.wait('@loginRequest').its('response.statusCode').should('eq', 401);
    cy.get('.success').should('contain', 'Connection échoué: Unauthorized');
  });
});

describe('Modal Interaction Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8080/connection');
    // Wait for the form to be visible before interacting
    cy.get('form').should('be.visible');
  });

  it('should open the forget password modal', () => {
    cy.get('.forget-password a').click();
    cy.get('.modal').should('be.visible');
    cy.get('.modal-content h2').should('contain', 'Mot de passe oublié ?');
  });

  it('should validate reset email in forget password modal', () => {
    cy.get('.forget-password a').click();
    cy.get('.modal').should('be.visible');
    cy.get('#forget-email').type('invalid-email', { force: true });
    cy.get('.modal-content form').submit();
    cy.get('.modal .error').should('contain', 'Adresse email non valide');
  });

  it('should submit the forget password form with valid email', () => {
    cy.intercept('POST', '**/api/forgot-password', {
      statusCode: 200,
      body: { message: 'Reset email sent' },
    }).as('forgotPasswordRequest');

    cy.get('.forget-password a').click();
    cy.get('.modal').should('be.visible');
    cy.get('#forget-email').type('test@example.com', { force: true });
    cy.get('.modal-content form').submit();

    cy.wait('@forgotPasswordRequest').its('response.statusCode').should('eq', 200);
    cy.get('.modal .success').should('contain', 'Un email de réinitialisation a été envoyé à votre adresse');
  });

  it('should close the forget password modal', () => {
    cy.get('.forget-password a').click();
    cy.get('.modal').should('be.visible');
    cy.get('.modal .close').click({ force: true }); // Use force: true to ensure the click happens
    cy.get('.modal').should('not.exist');
  });
});
