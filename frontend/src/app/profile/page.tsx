export default function ProfilePage() {
  return (
    <main className="min-h-screen p-8">
      <div className="mx-auto max-w-4xl">
        <h1 className="mb-2 text-4xl font-bold">Profile</h1>
        <p className="mb-8 text-neutral-400">
          Manage your account, view game history, and track statistics.
        </p>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          <div className="rounded-lg border border-neutral-800 p-6 text-center">
            <div className="mb-2 text-3xl font-bold">0</div>
            <div className="text-sm text-neutral-400">Games Played</div>
          </div>
          <div className="rounded-lg border border-neutral-800 p-6 text-center">
            <div className="mb-2 text-3xl font-bold">0</div>
            <div className="text-sm text-neutral-400">Scenarios Created</div>
          </div>
          <div className="rounded-lg border border-neutral-800 p-6 text-center">
            <div className="mb-2 text-3xl font-bold">0</div>
            <div className="text-sm text-neutral-400">Tokens Remaining</div>
          </div>
        </div>

        <section className="mt-8">
          <h2 className="mb-4 text-xl font-semibold">Recent Games</h2>
          <div className="rounded-lg border border-neutral-800 p-8 text-center text-neutral-500">
            No games played yet. Explore scenarios to get started.
          </div>
        </section>
      </div>
    </main>
  );
}
