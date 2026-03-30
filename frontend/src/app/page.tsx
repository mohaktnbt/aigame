import Link from "next/link";

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8">
      <div className="max-w-3xl text-center">
        <h1 className="mb-4 text-6xl font-bold tracking-tight">
          Project Nexus
        </h1>
        <p className="mb-2 text-xl text-neutral-400">
          Universal Scenario Simulation
        </p>
        <p className="mb-12 text-lg text-neutral-500">
          Shape history, influence nations, and explore alternate realities
          powered by AI-driven geopolitical modeling.
        </p>

        <div className="flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
          <Link
            href="/explore"
            className="rounded-lg bg-white px-8 py-3 text-lg font-semibold text-black transition hover:bg-neutral-200"
          >
            Explore Scenarios
          </Link>
          <Link
            href="/create"
            className="rounded-lg border border-neutral-700 px-8 py-3 text-lg font-semibold transition hover:border-neutral-500 hover:bg-neutral-900"
          >
            Create Scenario
          </Link>
        </div>
      </div>
    </main>
  );
}
