import { create } from "zustand";

interface UserSettings {
  theme: "dark" | "light";
  notifications: boolean;
  mapStyle: string;
}

interface UserStore {
  userId: string | null;
  username: string | null;
  email: string | null;
  tokens: number;
  settings: UserSettings;

  setUser: (user: { userId: string; username: string; email: string }) => void;
  setTokens: (tokens: number) => void;
  updateSettings: (settings: Partial<UserSettings>) => void;
  clearUser: () => void;
}

const defaultSettings: UserSettings = {
  theme: "dark",
  notifications: true,
  mapStyle: "default",
};

export const useUserStore = create<UserStore>((set) => ({
  userId: null,
  username: null,
  email: null,
  tokens: 0,
  settings: defaultSettings,

  setUser: (user) =>
    set({
      userId: user.userId,
      username: user.username,
      email: user.email,
    }),
  setTokens: (tokens) => set({ tokens }),
  updateSettings: (newSettings) =>
    set((state) => ({
      settings: { ...state.settings, ...newSettings },
    })),
  clearUser: () =>
    set({
      userId: null,
      username: null,
      email: null,
      tokens: 0,
      settings: defaultSettings,
    }),
}));
