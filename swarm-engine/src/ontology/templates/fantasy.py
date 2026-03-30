"""Fantasy ontology template — kingdoms, magic users, guilds, creatures."""

from typing import Any

FANTASY_TEMPLATE: dict[str, Any] = {
    "entity_types": [
        {
            "name": "Kingdom",
            "attributes": ["name", "ruler", "population", "wealth", "military_strength", "magic_affinity"],
        },
        {
            "name": "MagicUser",
            "attributes": ["name", "school", "power_level", "allegiance", "artifacts_held"],
        },
        {
            "name": "Guild",
            "attributes": ["name", "type", "influence", "headquarters", "member_count"],
        },
        {
            "name": "Creature",
            "attributes": ["name", "species", "threat_level", "habitat", "intelligence", "tameable"],
        },
        {
            "name": "Artifact",
            "attributes": ["name", "power", "origin", "current_holder", "corruption_level"],
        },
        {
            "name": "Region",
            "attributes": ["name", "terrain", "magic_density", "resources", "danger_level"],
        },
        {
            "name": "Deity",
            "attributes": ["name", "domain", "follower_count", "alignment", "active"],
        },
    ],
    "relationship_schemas": [
        {"type": "RULES", "from": "MagicUser", "to": "Kingdom"},
        {"type": "MEMBER_OF", "from": "MagicUser", "to": "Guild"},
        {"type": "INHABITS", "from": "Creature", "to": "Region"},
        {"type": "ALLIED_WITH", "from": "Kingdom", "to": "Kingdom", "attributes": ["treaty_type"]},
        {"type": "AT_WAR_WITH", "from": "Kingdom", "to": "Kingdom"},
        {"type": "WORSHIPS", "from": "MagicUser", "to": "Deity"},
        {"type": "POSSESSES", "from": "MagicUser", "to": "Artifact"},
        {"type": "LOCATED_IN", "from": "Kingdom", "to": "Region"},
        {"type": "GUARDS", "from": "Creature", "to": "Artifact"},
    ],
}
