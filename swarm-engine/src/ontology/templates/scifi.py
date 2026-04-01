"""Sci-fi ontology template — planets, factions, species, technology."""

from typing import Any

SCIFI_TEMPLATE: dict[str, Any] = {
    "entity_types": [
        {
            "name": "Planet",
            "attributes": ["name", "system", "habitability", "population", "resources", "tech_level"],
        },
        {
            "name": "Faction",
            "attributes": ["name", "ideology", "military_power", "territory_count", "diplomatic_stance"],
        },
        {
            "name": "Species",
            "attributes": ["name", "homeworld", "lifespan", "traits", "population"],
        },
        {
            "name": "Technology",
            "attributes": ["name", "category", "tier", "inventor_faction", "proliferation"],
        },
        {
            "name": "Starship",
            "attributes": ["name", "class", "faction", "crew_size", "armament", "ftl_capable"],
        },
        {
            "name": "Station",
            "attributes": ["name", "type", "location", "faction", "capacity"],
        },
        {
            "name": "Agent",
            "attributes": ["name", "species", "faction", "role", "cybernetic_augments"],
        },
    ],
    "relationship_schemas": [
        {"type": "CONTROLS", "from": "Faction", "to": "Planet"},
        {"type": "HOMEWORLD_OF", "from": "Planet", "to": "Species"},
        {"type": "DEVELOPED_BY", "from": "Technology", "to": "Faction"},
        {"type": "ALLIED_WITH", "from": "Faction", "to": "Faction", "attributes": ["treaty", "since"]},
        {"type": "AT_WAR_WITH", "from": "Faction", "to": "Faction", "attributes": ["casus_belli"]},
        {"type": "ORBITS", "from": "Station", "to": "Planet"},
        {"type": "ASSIGNED_TO", "from": "Agent", "to": "Starship"},
        {"type": "MEMBER_OF", "from": "Agent", "to": "Faction"},
    ],
}
