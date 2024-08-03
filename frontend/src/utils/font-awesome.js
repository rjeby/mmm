import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faHandHoldingHeart,
  faRightFromBracket,
  fas,
} from "@fortawesome/free-solid-svg-icons";
import { faArrowRightToBracket } from "@fortawesome/free-solid-svg-icons";
import { faRightToBracket } from "@fortawesome/free-solid-svg-icons";
import { faAnglesRight } from "@fortawesome/free-solid-svg-icons";
import { faCogs, faUser, faUsers } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faCogs, faUser, faUsers, fas);
library.add(faHandHoldingHeart, faAnglesRight);
library.add(faArrowRightToBracket);
library.add(faRightToBracket);
library.add(faRightFromBracket);

export default FontAwesomeIcon;
