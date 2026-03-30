"use client";

import { useEffect } from "react";
import type { SentimentData } from "@/lib/types";

interface SentimentOverlayProps {
  data: SentimentData[];
  visible: boolean;
}

export default function SentimentOverlay({ data, visible }: SentimentOverlayProps) {
  useEffect(() => {
    if (!visible || data.length === 0) return;

    // deck.gl HeatmapLayer integration will go here
    // Uses @deck.gl/layers HeatmapLayer with mapbox overlay
    // Data points mapped from SentimentData coordinates and sentiment values
  }, [data, visible]);

  if (!visible) return null;

  return (
    <div className="pointer-events-none absolute inset-0">
      {/* deck.gl overlay canvas renders here */}
      <div className="absolute bottom-4 left-4 rounded bg-black/70 px-3 py-2 text-xs text-white">
        <div className="mb-1 font-semibold">Sentiment Overlay</div>
        <div className="flex items-center gap-2">
          <span className="inline-block h-2 w-4 rounded bg-red-500" /> Hostile
          <span className="inline-block h-2 w-4 rounded bg-yellow-500" /> Neutral
          <span className="inline-block h-2 w-4 rounded bg-green-500" /> Friendly
        </div>
      </div>
    </div>
  );
}
