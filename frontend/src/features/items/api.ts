import { apiFetch } from "../../shared/api/client";
import { Item } from "./types";

export function listItems() {
  return apiFetch<Item[]>("/api/v1/items");
}

export function createItem(name: string) {
  return apiFetch<Item>("/api/v1/items", {
    method: "POST",
    body: JSON.stringify({ name }),
  });
}
