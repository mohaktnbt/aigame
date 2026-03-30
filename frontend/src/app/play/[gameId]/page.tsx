import GameMap from "@/components/map/GameMap";
import ActionPanel from "@/components/game/ActionPanel";
import EventsFeed from "@/components/game/EventsFeed";

interface PlayPageProps {
  params: Promise<{ gameId: string }>;
}

export default async function PlayPage({ params }: PlayPageProps) {
  const { gameId } = await params;

  return (
    <div className="flex h-screen flex-col">
      {/* Top bar */}
      <header className="flex items-center justify-between border-b border-neutral-800 px-4 py-2">
        <h1 className="text-lg font-semibold">Game: {gameId}</h1>
        <div className="flex items-center gap-4">
          <span className="text-sm text-neutral-400">Turn 1 / 50</span>
          <button className="rounded bg-neutral-800 px-3 py-1 text-sm hover:bg-neutral-700">
            Pause
          </button>
        </div>
      </header>

      {/* Main content */}
      <div className="flex flex-1 overflow-hidden">
        {/* Map area */}
        <div className="flex-1 relative">
          <GameMap />
        </div>

        {/* Right sidebar */}
        <aside className="flex w-96 flex-col border-l border-neutral-800">
          <div className="flex-1 overflow-hidden">
            <EventsFeed />
          </div>
          <div className="border-t border-neutral-800">
            <ActionPanel />
          </div>
        </aside>
      </div>
    </div>
  );
}
