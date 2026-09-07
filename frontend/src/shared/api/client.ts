const baseUrl = import.meta.env.VITE_API_URL as string;

export async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${baseUrl}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...init,
  });

  if (!res.ok) {
    throw new Error(`request to ${path} failed with ${res.status}`);
  }

  return res.json() as Promise<T>;
}
