import { DEVICE_READY } from "../actions/types";

export default (state = {}, action) => {
  switch (action.type) {
    case DEVICE_READY:
      return { ...state, [action.payload.id]: action.payload };
    default:
      return state;
  }
};
