describe('Home Page', () => {
  it('should load the home page', () => {
    cy.visit('http://localhost:8080');
    cy.contains('p', 'Mes Meilleurs Menus');
  });
});