/**
 * OpenRouter proxy service for frontend LLM calls.
 * Routes requests through OpenRouter to access various LLM providers.
 *
 * TODO: Set OPENROUTER_API_KEY in environment variables.
 */

const OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1";

export interface ChatMessage {
  role: "system" | "user" | "assistant";
  content: string;
}

export interface LLMRequestOptions {
  model?: string;
  messages: ChatMessage[];
  temperature?: number;
  maxTokens?: number;
  stream?: boolean;
}

export interface LLMResponse {
  id: string;
  model: string;
  content: string;
  usage: {
    promptTokens: number;
    completionTokens: number;
    totalTokens: number;
  };
}

/**
 * Send a chat completion request to OpenRouter.
 */
export async function chatCompletion(
  options: LLMRequestOptions
): Promise<LLMResponse> {
  const apiKey = process.env.OPENROUTER_API_KEY;
  if (!apiKey) {
    throw new Error("OPENROUTER_API_KEY is not configured");
  }

  const {
    model = "anthropic/claude-sonnet-4",
    messages,
    temperature = 0.7,
    maxTokens = 2048,
  } = options;

  const response = await fetch(`${OPENROUTER_BASE_URL}/chat/completions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
      "HTTP-Referer": process.env.FRONTEND_URL ?? "http://localhost:3000",
      "X-Title": "Project Nexus",
    },
    body: JSON.stringify({
      model,
      messages,
      temperature,
      max_tokens: maxTokens,
    }),
  });

  if (!response.ok) {
    const errorBody = await response.text();
    throw new Error(
      `OpenRouter API error (${response.status}): ${errorBody}`
    );
  }

  const data = (await response.json()) as {
    id: string;
    model: string;
    choices: Array<{ message: { content: string } }>;
    usage: {
      prompt_tokens: number;
      completion_tokens: number;
      total_tokens: number;
    };
  };

  const content = data.choices[0]?.message?.content ?? "";

  return {
    id: data.id,
    model: data.model,
    content,
    usage: {
      promptTokens: data.usage.prompt_tokens,
      completionTokens: data.usage.completion_tokens,
      totalTokens: data.usage.total_tokens,
    },
  };
}

/**
 * Stream a chat completion from OpenRouter.
 * Returns an async iterable of content chunks.
 *
 * TODO: Implement SSE streaming for real-time narrative generation.
 */
export async function* streamChatCompletion(
  options: LLMRequestOptions
): AsyncGenerator<string> {
  const apiKey = process.env.OPENROUTER_API_KEY;
  if (!apiKey) {
    throw new Error("OPENROUTER_API_KEY is not configured");
  }

  const {
    model = "anthropic/claude-sonnet-4",
    messages,
    temperature = 0.7,
    maxTokens = 2048,
  } = options;

  const response = await fetch(`${OPENROUTER_BASE_URL}/chat/completions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
      "HTTP-Referer": process.env.FRONTEND_URL ?? "http://localhost:3000",
      "X-Title": "Project Nexus",
    },
    body: JSON.stringify({
      model,
      messages,
      temperature,
      max_tokens: maxTokens,
      stream: true,
    }),
  });

  if (!response.ok) {
    const errorBody = await response.text();
    throw new Error(
      `OpenRouter API error (${response.status}): ${errorBody}`
    );
  }

  // TODO: Parse SSE stream from response.body
  // For now, fall back to non-streaming
  const data = (await response.json()) as {
    choices: Array<{ message: { content: string } }>;
  };
  yield data.choices[0]?.message?.content ?? "";
}

/**
 * Generate a game narrative based on world state and player action.
 * Convenience wrapper around chatCompletion for game-specific prompts.
 */
export async function generateGameNarrative(params: {
  scenarioTitle: string;
  scenarioType: string;
  universeRules: Record<string, unknown>;
  worldState: Record<string, unknown>;
  recentEvents: string[];
  playerAction: string;
}): Promise<LLMResponse> {
  const systemPrompt = `You are a game master for "${params.scenarioTitle}", a ${params.scenarioType} scenario.
You must follow these universe rules: ${JSON.stringify(params.universeRules)}

Current world state: ${JSON.stringify(params.worldState)}

Recent events:
${params.recentEvents.map((e, i) => `${i + 1}. ${e}`).join("\n")}

Respond to the player's action with:
1. A vivid narrative description (2-3 paragraphs)
2. A JSON block of quantitative changes to the world state

Format your response as:
NARRATIVE:
[your narrative here]

CHANGES:
[JSON object of world state changes]`;

  return chatCompletion({
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: params.playerAction },
    ],
    temperature: 0.8,
    maxTokens: 1024,
  });
}
