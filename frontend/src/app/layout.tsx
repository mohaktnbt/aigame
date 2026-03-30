import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Project Nexus",
  description: "Universal Scenario Simulation - Shape history, influence nations, and explore alternate realities",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-[var(--color-background)] text-[var(--color-foreground)] antialiased">
        {children}
      </body>
    </html>
  );
}
