"""Historical ontology template — nations, leaders, citizens, military, economy."""

from typing import Any

HISTORICAL_TEMPLATE: dict[str, Any] = {
    "entity_types": [
        {
            "name": "Nation",
            "attributes": ["name", "government_type", "gdp", "population", "stability_index"],
        },
        {
            "name": "Leader",
            "attributes": ["name", "title", "ideology", "approval_rating", "tenure_years"],
        },
        {
            "name": "Citizen",
            "attributes": ["name", "age", "occupation", "region", "loyalty", "grievances"],
        },
        {
            "name": "MilitaryUnit",
            "attributes": ["name", "branch", "strength", "morale", "deployment_region"],
        },
        {
            "name": "EconomicSector",
            "attributes": ["name", "output", "employment", "growth_rate", "sanctions_impact"],
        },
        {
            "name": "PoliticalParty",
            "attributes": ["name", "ideology", "seats", "popularity", "coalition_partners"],
        },
        {
            "name": "MediaOutlet",
            "attributes": ["name", "bias", "reach", "credibility", "owner"],
        },
    ],
    "relationship_schemas": [
        {"type": "LEADS", "from": "Leader", "to": "Nation"},
        {"type": "CITIZEN_OF", "from": "Citizen", "to": "Nation"},
        {"type": "SERVES_IN", "from": "Citizen", "to": "MilitaryUnit"},
        {"type": "ALLIED_WITH", "from": "Nation", "to": "Nation", "attributes": ["strength", "since"]},
        {"type": "HOSTILE_TO", "from": "Nation", "to": "Nation", "attributes": ["severity"]},
        {"type": "TRADES_WITH", "from": "Nation", "to": "Nation", "attributes": ["volume", "goods"]},
        {"type": "MEMBER_OF", "from": "Leader", "to": "PoliticalParty"},
        {"type": "INFLUENCES", "from": "MediaOutlet", "to": "Citizen", "attributes": ["reach"]},
    ],
}
