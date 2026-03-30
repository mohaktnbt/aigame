"use client";

import { useState } from "react";
import { Send } from "lucide-react";

interface ChatMessage {
  id: string;
  sender: string;
  senderFaction: string;
  content: string;
  timestamp: number;
  isPlayer: boolean;
}

export default function DiplomacyChat() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<ChatMessage[]>([]);

  const handleSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim()) return;

    const newMessage: ChatMessage = {
      id: Date.now().toString(),
      sender: "Player",
      senderFaction: "player-faction",
      content: message,
      timestamp: Date.now(),
      isPlayer: true,
    };

    setMessages((prev) => [...prev, newMessage]);
    setMessage("");
  };

  return (
    <div className="flex h-full flex-col">
      <div className="border-b border-neutral-800 px-4 py-2">
        <h3 className="text-sm font-semibold text-neutral-400">
          Diplomatic Channel
        </h3>
      </div>

      <div className="flex-1 overflow-y-auto p-3">
        {messages.length === 0 ? (
          <div className="flex h-full items-center justify-center text-sm text-neutral-600">
            Begin diplomatic negotiations with other factions.
          </div>
        ) : (
          <ul className="space-y-3">
            {messages.map((msg) => (
              <li
                key={msg.id}
                className={`flex ${msg.isPlayer ? "justify-end" : "justify-start"}`}
              >
                <div
                  className={`max-w-[80%] rounded-lg px-3 py-2 text-sm ${
                    msg.isPlayer
                      ? "bg-blue-600 text-white"
                      : "bg-neutral-800 text-neutral-200"
                  }`}
                >
                  {!msg.isPlayer && (
                    <div className="mb-1 text-xs font-semibold text-neutral-400">
                      {msg.sender}
                    </div>
                  )}
                  {msg.content}
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>

      <form onSubmit={handleSend} className="border-t border-neutral-800 p-3">
        <div className="flex gap-2">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Send a diplomatic message..."
            className="flex-1 rounded-lg border border-neutral-700 bg-neutral-900 px-3 py-2 text-sm focus:border-neutral-500 focus:outline-none"
          />
          <button
            type="submit"
            disabled={!message.trim()}
            className="rounded-lg bg-blue-600 p-2 text-white transition hover:bg-blue-500 disabled:opacity-50"
          >
            <Send size={16} />
          </button>
        </div>
      </form>
    </div>
  );
}
