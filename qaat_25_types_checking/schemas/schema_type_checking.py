correct_schema = {
    "additionalProperties": False,
    "properties": {
        "data": {
            "additionalProperties": False,
            "properties": {
                "links": {
                    "additionalItems": False,
                    "type": "array"
                },
                "showcases": {
                    "additionalItems": False,
                    # "items": showcase,
                    "type": "array"
                },
                "items": {
                    "additionalItems": False,
                    # "items": schedule,
                    # "items": {
                    #     "anyOf": [
                            # channel,
                            # channel_package,
                            # episode,
                            # genre,
                            # gift,
                            # movie,
                            # offer,
                            # package,
                            # person,
                            # program,
                            # schedule,
                            # season,
                            # serial,
                            # subscription,
                            # provider,
                            # promotion
                        # ]
                    # },
                    "type": "array"
                },
                "title": {
                    "type": "string"
                },
                "total": {
                    "type": "integer"
                },
                "type": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "urn": {
                    "type": "string"
                },
                "references": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "title": {"type": "string"},
                            "urn": {"type": "string"},
                            "type": {"type": "string"}
                        },
                        "required": ["title", "urn", "type"],
                        "type": "object"
                    },
                    "type": "array"
                }
            },
            "required": [
                "links",
                "title",
                "total",
                "type",
                "urn"
            ],
            "type": "object"
        }
    },
    "required": [
        "data"
    ],
    "type": "object"
}