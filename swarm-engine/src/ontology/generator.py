"""
OntologyGenerator — Dynamically creates entity types and relationship
schemas adapted to the genre of a seed document.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from src.ontology.templates.historical import HISTORICAL_TEMPLATE
from src.ontology.templates.scifi import SCIFI_TEMPLATE
from src.ontology.templates.fantasy import FANTASY_TEMPLATE

router = APIRouter()


class OntologyRequest(BaseModel):
    """Request body for ontology generation."""
    seed_document: str
    genre_hint: str | None = None  # "historical", "scifi", "fantasy", or None for auto-detect


class OntologySchema(BaseModel):
    """Generated ontology schema."""
    genre: str
    entity_types: list[dict[str, Any]]
    relationship_schemas: list[dict[str, Any]]


GENRE_TEMPLATES: dict[str, dict[str, Any]] = {
    "historical": HISTORICAL_TEMPLATE,
    "scifi": SCIFI_TEMPLATE,
    "fantasy": FANTASY_TEMPLATE,
}


class OntologyGenerator:
    """Generates world ontologies from seed documents.

    The generator inspects the seed document (or uses a genre hint) to select
    the best template, then adapts entity types and relationship schemas to
    the specific setting described in the document.
    """

    def detect_genre(self, seed_document: str) -> str:
        """Classify the seed document into a genre.

        TODO: Use an LLM or keyword heuristic to auto-detect genre.
        """
        lowered = seed_document.lower()
        if any(kw in lowered for kw in ("planet", "starship", "galaxy", "alien")):
            return "scifi"
        if any(kw in lowered for kw in ("magic", "dragon", "kingdom", "wizard")):
            return "fantasy"
        return "historical"

    def generate_ontology(
        self,
        seed_document: str,
        genre_hint: str | None = None,
    ) -> OntologySchema:
        """Generate an ontology from a seed document.

        Args:
            seed_document: Free-text description of the world setting.
            genre_hint: Optional genre override. If None, auto-detected.

        Returns:
            OntologySchema with entity types and relationship schemas.

        TODO: Enrich the base template with entities extracted from the seed
              document via LLM parsing.
        TODO: Support hybrid genres (e.g., sci-fi + fantasy).
        """
        genre = genre_hint or self.detect_genre(seed_document)
        template = GENRE_TEMPLATES.get(genre, GENRE_TEMPLATES["historical"])

        return OntologySchema(
            genre=genre,
            entity_types=template["entity_types"],
            relationship_schemas=template["relationship_schemas"],
        )


_generator = OntologyGenerator()


@router.post("/generate", response_model=OntologySchema)
async def generate_ontology(request: OntologyRequest) -> OntologySchema:
    """Generate a world ontology from a seed document."""
    return _generator.generate_ontology(
        seed_document=request.seed_document,
        genre_hint=request.genre_hint,
    )
