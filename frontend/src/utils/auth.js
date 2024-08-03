import { jwtDecode } from "jwt-decode";
import { userState } from "./store";

// const AUTH_TOKEN_KEY = "token";
// const USER_INFO_KEY = "user";

export function logoutUser() {
  clearAuthToken();
  clearUser();
}

export function clearAuthToken() {
  userState.token = "";
}

export function clearUser() {
  userState.role = "";
  userState.isConfirmed = false;
  userState.hasInfos = false;
}

export function getAuthToken() {
  return userState.token;
}

export function isLoggedIn() {
  let authToken = getAuthToken();
  return !!authToken && !isTokenExpired(authToken);
}

function getTokenExpirationDate(encodedToken) {
  let token = jwtDecode(encodedToken);
  if (!token.exp) {
    return null;
  }

  let date = new Date(0);
  date.setUTCSeconds(token.exp);

  return date;
}

function isTokenExpired(token) {
  let expirationDate = getTokenExpirationDate(token);
  return expirationDate < new Date();
}
