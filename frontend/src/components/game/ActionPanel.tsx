"use client";

import { useState } from "react";
import { Send } from "lucide-react";

export default function ActionPanel() {
  const [action, setAction] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!action.trim() || isSubmitting) return;

    setIsSubmitting(true);
    try {
      // Submit action to game engine via API
      console.log("Submitting action:", action);
      setAction("");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="p-4">
      <h3 className="mb-2 text-sm font-semibold text-neutral-400">
        Issue Command
      </h3>
      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="text"
          value={action}
          onChange={(e) => setAction(e.target.value)}
          placeholder="Enter a diplomatic, military, or economic action..."
          className="flex-1 rounded-lg border border-neutral-700 bg-neutral-900 px-3 py-2 text-sm focus:border-neutral-500 focus:outline-none"
          disabled={isSubmitting}
        />
        <button
          type="submit"
          disabled={isSubmitting || !action.trim()}
          className="rounded-lg bg-white p-2 text-black transition hover:bg-neutral-200 disabled:opacity-50"
        >
          <Send size={16} />
        </button>
      </form>
    </div>
  );
}
