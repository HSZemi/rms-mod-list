import {Writable, writable} from "svelte/store";
import {getSingleModId} from "./helpers";

export const filter: Writable<string> = writable('');
export const sortMethod: Writable<string> = writable('created');
export const sortDirection: Writable<string> = writable('DESC');
export const singleModId: Writable<number | null> = writable(getSingleModId());
