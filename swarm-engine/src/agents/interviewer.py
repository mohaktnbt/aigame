"""
AgentInterviewer — Conducts in-character interviews with any simulated agent.

Given an agent_id and a question, the interviewer constructs a prompt from
the agent's persona, memories, and current world context, then returns an
in-character response.
"""

from __future__ import annotations

from pydantic import BaseModel

from src.agents.persona_generator import AgentPersona


class InterviewRequest(BaseModel):
    """Payload for an interview question."""
    agent_id: str
    question: str
    context: str | None = None  # optional extra world-state context


class InterviewResponse(BaseModel):
    """In-character reply from an agent."""
    agent_id: str
    agent_name: str
    archetype: str
    response: str
    confidence: float  # 0-1 how certain the agent is of their answer


class AgentInterviewer:
    """Generates in-character responses from simulated agents.

    The interviewer pulls the agent's persona, retrieves relevant memories
    from the memory backend, and synthesizes a prompt for the LLM to produce
    a first-person, in-character reply.

    TODO: Integrate with LLM backend (httpx call to inference API).
    TODO: Inject GraphRAG context for world-aware answers.
    TODO: Pull agent memories via ZepMemoryClient.
    """

    def _build_system_prompt(self, agent: AgentPersona, context: str | None) -> str:
        """Construct the system prompt for the interview.

        TODO: Include memory retrieval results and graph context.
        """
        personality = agent.personality
        lines = [
            f"You are {agent.name}, a {agent.archetype.lower()} from {agent.region}.",
            f"You are aligned with the {agent.faction} faction.",
            f"Personality (OCEAN): O={personality.openness} C={personality.conscientiousness} "
            f"E={personality.extraversion} A={personality.agreeableness} N={personality.neuroticism}",
            f"Backstory: {agent.backstory}",
        ]
        if context:
            lines.append(f"Current situation: {context}")
        lines.append("Respond in first person, staying fully in character.")
        return "\n".join(lines)

    async def interview(
        self,
        agent: AgentPersona,
        question: str,
        context: str | None = None,
    ) -> InterviewResponse:
        """Conduct an in-character interview with the given agent.

        Args:
            agent: The agent persona to interview.
            question: The question to ask.
            context: Optional additional world-state context.

        Returns:
            InterviewResponse with the agent's in-character reply.

        TODO: Replace stub response with actual LLM inference call.
        """
        system_prompt = self._build_system_prompt(agent, context)

        # --- STUB: Replace with real LLM call ---
        stub_response = (
            f"[In character as {agent.name}] "
            f"That is an interesting question. As a {agent.archetype.lower()} "
            f"from {agent.region}, I would say this matter is complex. "
            f"My loyalty to {agent.faction} shapes my view considerably."
        )

        return InterviewResponse(
            agent_id=agent.agent_id,
            agent_name=agent.name,
            archetype=agent.archetype,
            response=stub_response,
            confidence=0.5,  # TODO: derive from personality traits
        )
