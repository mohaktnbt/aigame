"use client";

import type { ProbabilityDistribution } from "@/lib/types";

interface ProbabilityDisplayProps {
  distributions: ProbabilityDistribution[];
  title?: string;
}

export default function ProbabilityDisplay({
  distributions,
  title = "Outcome Probabilities",
}: ProbabilityDisplayProps) {
  const sorted = [...distributions].sort((a, b) => b.probability - a.probability);

  return (
    <div className="rounded-lg border border-neutral-800 p-4">
      <h4 className="mb-3 text-sm font-semibold text-neutral-400">{title}</h4>
      {sorted.length === 0 ? (
        <p className="text-sm text-neutral-600">No probability data available.</p>
      ) : (
        <ul className="space-y-2">
          {sorted.map((dist) => (
            <li key={dist.outcome}>
              <div className="mb-1 flex items-center justify-between text-sm">
                <span>{dist.outcome}</span>
                <span className="font-mono text-neutral-400">
                  {(dist.probability * 100).toFixed(1)}%
                </span>
              </div>
              <div className="h-2 overflow-hidden rounded-full bg-neutral-800">
                <div
                  className="h-full rounded-full bg-blue-500 transition-all"
                  style={{ width: `${dist.probability * 100}%` }}
                />
              </div>
              <div className="mt-0.5 text-right text-xs text-neutral-600">
                confidence: {(dist.confidence * 100).toFixed(0)}%
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
