"use client";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from "recharts";

interface QuantDashboardProps {
  gdpData?: { turn: number; value: number }[];
  militaryData?: { turn: number; value: number }[];
  sentimentData?: { turn: number; value: number }[];
}

export default function QuantDashboard({
  gdpData = [],
  militaryData = [],
  sentimentData = [],
}: QuantDashboardProps) {
  const chartData = gdpData.map((point, i) => ({
    turn: point.turn,
    gdp: point.value,
    military: militaryData[i]?.value ?? 0,
    sentiment: sentimentData[i]?.value ?? 0,
  }));

  return (
    <div className="space-y-4 p-4">
      <h3 className="text-sm font-semibold text-neutral-400">
        Quantitative Dashboard
      </h3>

      {chartData.length === 0 ? (
        <div className="flex h-48 items-center justify-center rounded-lg border border-neutral-800 text-sm text-neutral-600">
          Charts will appear as the simulation progresses.
        </div>
      ) : (
        <div className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#333" />
              <XAxis dataKey="turn" stroke="#666" fontSize={12} />
              <YAxis stroke="#666" fontSize={12} />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#1a1a1a",
                  border: "1px solid #333",
                  borderRadius: "8px",
                }}
              />
              <Legend />
              <Line type="monotone" dataKey="gdp" stroke="#22c55e" name="GDP" />
              <Line type="monotone" dataKey="military" stroke="#ef4444" name="Military" />
              <Line type="monotone" dataKey="sentiment" stroke="#3b82f6" name="Sentiment" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  );
}
