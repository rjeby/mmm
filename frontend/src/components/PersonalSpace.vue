<template>
  <div>
    <div class="dropdown" @click.stop="toggleDropdown">
      <button
        class="btn btn-order2 dropdown-toggle"
        type="button"
        id="userDropdown"
        aria-haspopup="true"
        aria-expanded="false"
      >
        <font-awesome-icon :icon="['fas', 'user']" /> Mon Espace Personnel
      </button>
      <div
        class="dropdown-menu"
        :class="{ show: isDropdownVisible }"
        aria-labelledby="userDropdown"
      >
        <div v-if="personalSpaceState.show">
          <a
            class="dropdown-item"
            @click.stop="navigateTo('mes-meilleurs-menus')"
          >
            <font-awesome-icon class="icon" icon="fa-solid fa-utensils" /> Mes
            Meilleurs Menus
          </a>
          <a class="dropdown-item" @click.stop="navigateTo('mes-infos')">
            <font-awesome-icon class="icon" :icon="['fas', 'user']" /> Mes
            informations
          </a>
          <a class="dropdown-item" @click.stop="navigateTo('mes-preferences')">
            <font-awesome-icon class="icon" :icon="['fas', 'cogs']" /> Mes
            préférences
          </a>
          <a class="dropdown-item" @click.stop="navigateTo('ma-famille')">
            <font-awesome-icon class="icon" :icon="['fas', 'users']" /> Ma
            famille
          </a>
          <a class="dropdown-item" @click.stop="navigateTo('deconnection')">
            <font-awesome-icon
              class="icon"
              :icon="['fas', 'right-from-bracket']"
            />
            Se déconnecter
          </a>
        </div>
        <div v-else>
          <a class="dropdown-item" @click.stop="navigateTo('connection')">
            <font-awesome-icon
              class="icon"
              :icon="['fas', 'right-from-bracket']"
            />
            Se connecter
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router/composables";
import { ref, onMounted, onBeforeUnmount } from "vue";
import { personalSpaceState } from "@/utils/store";

export default {
  setup() {
    const isDropdownVisible = ref(false);
    const router = useRouter();

    const toggleDropdown = () => {
      isDropdownVisible.value = !isDropdownVisible.value;
    };

    const closeDropdown = (event) => {
      if (isDropdownVisible.value && !event.target.closest(".dropdown")) {
        isDropdownVisible.value = false;
      }
    };

    const navigateTo = (routeName) => {
      isDropdownVisible.value = !isDropdownVisible.value;
      router.push({ name: routeName }).catch(() => {});
    };

    onMounted(() => {
      document.addEventListener("click", closeDropdown);
    });

    onBeforeUnmount(() => {
      document.removeEventListener("click", closeDropdown);
    });

    return {
      personalSpaceState,
      isDropdownVisible,
      toggleDropdown,
      navigateTo,
    };
  },
};
</script>

<style scoped>
.btn-order {
  color: white;
  background-color: #004c40;
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
}

.btn-order2:hover {
  color: white;
  background-color: #004c40;
  border-color: #004c40;
}

.dropdown-menu {
  width: 233px;
}

.dropdown-item {
  cursor: pointer;
}

.dropdown-item:hover {
  color: white;
  background-color: #004c40;
}

.dropdown-item .icon {
  width: 35px;
}
</style>
