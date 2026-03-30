export default function CreatePage() {
  return (
    <main className="min-h-screen p-8">
      <div className="mx-auto max-w-4xl">
        <h1 className="mb-2 text-4xl font-bold">Create Scenario</h1>
        <p className="mb-8 text-neutral-400">
          Define the world, factions, and rules for your simulation.
        </p>

        <div className="space-y-6">
          <section className="rounded-lg border border-neutral-800 p-6">
            <h2 className="mb-4 text-xl font-semibold">Scenario Details</h2>
            <div className="space-y-4">
              <div>
                <label className="mb-1 block text-sm text-neutral-400">
                  Scenario Name
                </label>
                <input
                  type="text"
                  placeholder="Enter scenario name..."
                  className="w-full rounded-lg border border-neutral-700 bg-neutral-900 px-4 py-2 text-sm focus:border-neutral-500 focus:outline-none"
                />
              </div>
              <div>
                <label className="mb-1 block text-sm text-neutral-400">
                  Description
                </label>
                <textarea
                  placeholder="Describe your scenario..."
                  rows={4}
                  className="w-full rounded-lg border border-neutral-700 bg-neutral-900 px-4 py-2 text-sm focus:border-neutral-500 focus:outline-none"
                />
              </div>
            </div>
          </section>

          <section className="rounded-lg border border-neutral-800 p-6">
            <h2 className="mb-4 text-xl font-semibold">Factions</h2>
            <p className="text-sm text-neutral-500">
              Faction editor coming soon. Define nations, alliances, and AI agent
              personalities.
            </p>
          </section>

          <section className="rounded-lg border border-neutral-800 p-6">
            <h2 className="mb-4 text-xl font-semibold">World Parameters</h2>
            <p className="text-sm text-neutral-500">
              Configure economic models, military balance, and diplomatic
              relationships.
            </p>
          </section>

          <button className="w-full rounded-lg bg-white px-6 py-3 font-semibold text-black transition hover:bg-neutral-200">
            Create Scenario
          </button>
        </div>
      </div>
    </main>
  );
}
