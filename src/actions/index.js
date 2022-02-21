import { DEVICE_READY } from "./types";
import api from "../apis/api";

export const deviceReady = (id) => async (dispatch) => {
  const response = await api.get(`/device/${id}`);
  dispatch({ type: DEVICE_READY, payload: response.data });
};
