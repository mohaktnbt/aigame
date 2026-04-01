export default function ExplorePage() {
  return (
    <main className="min-h-screen p-8">
      <div className="mx-auto max-w-6xl">
        <h1 className="mb-2 text-4xl font-bold">Explore Scenarios</h1>
        <p className="mb-8 text-neutral-400">
          Browse community-created scenarios or start from a template.
        </p>

        <div className="mb-6 flex items-center gap-4">
          <input
            type="text"
            placeholder="Search scenarios..."
            className="flex-1 rounded-lg border border-neutral-700 bg-neutral-900 px-4 py-2 text-sm focus:border-neutral-500 focus:outline-none"
          />
          <select className="rounded-lg border border-neutral-700 bg-neutral-900 px-4 py-2 text-sm">
            <option>All Categories</option>
            <option>Historical</option>
            <option>Modern Geopolitics</option>
            <option>Alternate History</option>
            <option>Speculative Future</option>
          </select>
        </div>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {["Cold War Redux", "Pacific Century 2030", "European Realignment"].map(
            (title) => (
              <div
                key={title}
                className="rounded-lg border border-neutral-800 bg-neutral-900/50 p-6 transition hover:border-neutral-600"
              >
                <h3 className="mb-2 text-lg font-semibold">{title}</h3>
                <p className="mb-4 text-sm text-neutral-400">
                  A procedurally generated geopolitical simulation scenario.
                </p>
                <div className="flex items-center justify-between text-xs text-neutral-500">
                  <span>4-8 players</span>
                  <span>50 turns</span>
                </div>
              </div>
            )
          )}
        </div>
      </div>
    </main>
  );
}
