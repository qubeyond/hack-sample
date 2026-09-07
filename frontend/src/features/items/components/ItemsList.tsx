import { useEffect, useState } from "react";

import { Button } from "@/shared/ui/button";

import { listItems } from "../api";
import { Item } from "../types";

export function ItemsList() {
  const [items, setItems] = useState<Item[]>([]);

  const refresh = () => listItems().then(setItems).catch(console.error);

  useEffect(() => {
    refresh();
  }, []);

  return (
    <div>
      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
      <Button variant="outline" size="sm" onClick={refresh}>
        Refresh
      </Button>
    </div>
  );
}
