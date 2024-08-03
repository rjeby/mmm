import { reactive } from "vue";

// Personal space state

export const personalSpaceState = reactive({
  show: false,
  enable() {
    this.show = true;
  },
  disable() {
    this.show = false;
  },
});

// User state
export const userState = reactive({
  token: "",
  role: "",
  isConfirmed: false,
  hasInfos: false,
  setUser(user) {
    this.token = user.access_token;
    this.role = user.role;
    this.isConfirmed = user.is_confirmed;
    this.hasInfos = user.has_infos;
    personalSpaceState.enable();
  },
  clearUser() {
    this.token = "";
    this.role = "";
    this.isConfirmed = false;
    this.hasInfos = false;
    personalSpaceState.disable();
  },
});
