"use client";

import { useGameStore } from "@/stores/gameStore";
import { AlertTriangle, Globe, Swords, TrendingUp, MessageCircle } from "lucide-react";
import type { Event } from "@/lib/types";

const eventIcons: Record<Event["type"], React.ReactNode> = {
  political: <Globe size={14} />,
  military: <Swords size={14} />,
  economic: <TrendingUp size={14} />,
  diplomatic: <MessageCircle size={14} />,
  social: <AlertTriangle size={14} />,
};

const severityColors: Record<Event["severity"], string> = {
  low: "text-neutral-400",
  medium: "text-yellow-400",
  high: "text-orange-400",
  critical: "text-red-400",
};

export default function EventsFeed() {
  const events = useGameStore((state) => state.events);

  return (
    <div className="flex h-full flex-col">
      <div className="border-b border-neutral-800 px-4 py-2">
        <h3 className="text-sm font-semibold text-neutral-400">Events Feed</h3>
      </div>
      <div className="flex-1 overflow-y-auto p-2">
        {events.length === 0 ? (
          <div className="p-4 text-center text-sm text-neutral-600">
            No events yet. The simulation will generate events as turns progress.
          </div>
        ) : (
          <ul className="space-y-2">
            {events.map((event) => (
              <li
                key={event.id}
                className="rounded-lg border border-neutral-800 bg-neutral-900/50 p-3"
              >
                <div className="mb-1 flex items-center gap-2">
                  <span className={severityColors[event.severity]}>
                    {eventIcons[event.type]}
                  </span>
                  <span className="text-sm font-medium">{event.title}</span>
                </div>
                <p className="text-xs text-neutral-500">{event.description}</p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
