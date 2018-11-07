channels = {
    "additionalProperties": False,
    "properties": {
        "id": {"type": "integer"},
        "type": {"type": "string"},
        "urn": {"type": "string"},
        "title": {"type": "string"},
        "adult": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object"
        },
        "resources": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "integer"},
                    "type": {"type": "string"},
                    "drm": {"type": "string"},
                    "evenKey": {"type": "string"},
                    "oddKey": {"type": "string"},
                    "source": {"type": "string"}
                },
                "required": ["id", "type"],
                "type": "object"
            },
            "type": "array"
        },
        "description": {"type": "string"},
        "lcn": {"type": "integer"},
        "style": {
            "additionalProperties": False,
            "properties": {
                "backgroundColor": {"type": "string"}
            },
            "required": ["backgroundColor"],
            "type": "object"
        },
        "offersUrn": {"type": "null"},
        "available": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",

        },
        "rating": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "quality": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object"
        },
        "services": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "type": {"type": "string"},
                    "state": {
                        "additionalProperties": False,
                        "properties": {
                            "type": {"type": "string"}
                        },
                        "required": ["type"],
                        "type": "object"
                    }

                },
                "required": ["type", "state"],
                "type": "object"

            },
            "type": "array",
        },
        "schedules": {
            "additionalProperties": False,
            "properties": {
                "showcases": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "items": {
                                "additionalItems": False,
                                "items": {
                                    "additionalProperties": False,
                                    "properties": {
                                        "id": {"type": "integer"},
                                        "type": {"type": "string"},
                                        "urn": {"type": "string"},
                                        "startAt": {"type": "string"},
                                        "endAt": {"type": "string"},
                                        "position": {"type": "integer"},
                                        "global": {
                                            "additionalProperties": False,
                                            "properties": {
                                                "id": {"type": "integer"},
                                                "title": {"type": "string"},
                                                "adult": {
                                                    "additionalProperties": False,
                                                    "properties": {
                                                        "type": {"type": "string"}
                                                    },
                                                    "required": ["type"],
                                                    "type": "object"
                                                },
                                                "rating": {
                                                    "additionalProperties": False,
                                                    "properties": {
                                                        "type": {"type": "string"}
                                                    },
                                                    "required": ["type"],
                                                    "type": "object"
                                                },
                                                "locals": {
                                                    "additionalItems": False,
                                                    "items": {
                                                        "additionalProperties": False,
                                                        "properties": {
                                                            "id": {"type": "integer"},
                                                            "title": {"type": "string"},
                                                            "available": {
                                                                "additionalProperties": False,
                                                                "properties": {
                                                                    "type": {"type": "string"}
                                                                },
                                                                "required": ["type"],
                                                                "type": "object"
                                                            },
                                                            "quality": {
                                                                "additionalProperties": False,
                                                                "properties": {
                                                                    "type": {"type": "string"}
                                                                },
                                                                "required": ["type"],
                                                                "type": "object"
                                                            },
                                                            "services": {
                                                                "additionalItems": False,
                                                                "items": {
                                                                    "additionalProperties": False,
                                                                    "properties": {
                                                                        "type": {"type": "string"},
                                                                        "state": {
                                                                            "additionalProperties": False,
                                                                            "properties": {
                                                                                "type": {"type": "string"}
                                                                            },
                                                                            "required": ["type"],
                                                                            "type": "object"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "type",
                                                                        "state"],
                                                                    "type": "object"

                                                                },
                                                                "type": "array",
                                                            },
                                                            "resources": {
                                                                "additionalItems": False,
                                                                "items": {
                                                                    "additionalProperties": False,
                                                                    "properties": {
                                                                        "id": {"type": "integer"},
                                                                        "type": {"type": "string"},
                                                                        "drm": {"type": "string"},
                                                                        "evenKey": {"type": "string"},
                                                                        "oddKey": {"type": "string"},
                                                                        "source": {"type": "string"}
                                                                    },
                                                                    "required": ["id", "type"],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            },
                                                            "urn": {"type": "string"}
                                                        },
                                                        "required": [
                                                            "id", "title", "available",
                                                            "quality", "services", "resources", "urn"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    "type": "array"
                                                }
                                            },
                                            "required": [
                                                "id", "title",
                                                "adult", "rating", "locals"
                                            ],
                                            "type": "object",
                                        },
                                        "data": {
                                            "additionalProperties": False,
                                            "properties": {
                                                "id": {"type": "integer"},
                                                "type": {"type": "string"},
                                                "urn": {"type": "string"},
                                                "title": {"type": "string"},
                                                "adult": {
                                                    "additionalProperties": False,
                                                    "properties": {
                                                        "type": {"type": "string"}},
                                                    "type": "object",
                                                },
                                                "resources": {
                                                    "additionalItems": False,
                                                    "items": {
                                                        "additionalProperties": False,
                                                        "properties": {
                                                            "id": {"type": "integer"},
                                                            "type": {"type": "string"}
                                                        },
                                                        "required": ["id", "type"],
                                                        "type": "object",
                                                    },
                                                    "type": "array"
                                                },
                                                "releasedAt": {"type": ["null", "string"]},
                                                "rating": {
                                                    "additionalProperties": False,
                                                    "properties": {
                                                        "type": {"type": "string"}
                                                    },
                                                    "required": ["type"],
                                                    "type": "object",
                                                },
                                                "favorite": {
                                                    "additionalProperties": False,
                                                    "properties": {
                                                        "type": {"type": "string"}
                                                    },
                                                    "required": ["type"],
                                                    "type": "object",
                                                },
                                                "personsUrn": {"type": ["null", "string"]},
                                                "categories": {
                                                    "additionalItems": False,
                                                    "items": {
                                                        "additionalProperties": False,
                                                        "properties": {
                                                            "id": {"type": "integer"},
                                                            "title": {"type": "string"}
                                                        },
                                                        "required": ["id", "title"],
                                                        "type": "object",
                                                    },
                                                    "type": "array",
                                                },
                                                "description": {"type": "string"},
                                                "duration": {"type": "integer"},
                                                "episodeNumber": {"type": "integer"},
                                                "seasonNumber": {"type": "integer"},
                                                "countries": {"type": "array"},
                                                "genres": {
                                                    "additionalItems": False,
                                                    "items": {
                                                        "additionalProperties": False,
                                                        "properties": {
                                                            "id": {"type": "integer"},
                                                            "title": {"type": "string"}
                                                        },
                                                        "required": ["id", "title"],
                                                        "type": "object",
                                                    },
                                                    "type": "array",
                                                },
                                                "awards": {"type": "array"},
                                                "estimate": {
                                                    "additionalProperties": False,
                                                    "properties": {
                                                        "type": {"type": "string"}
                                                    },
                                                    "required": ["type"],
                                                    "type": "object",
                                                },
                                                "vod": {
                                                    "additionalProperties": False,
                                                    "properties": {
                                                        "id": {"type": "integer"},
                                                        "type": {"type": "null"},
                                                        "urn": {"type": "null"},
                                                        "available": {
                                                            "additionalProperties": False,
                                                            "properties": {
                                                                "type": {"type": "string"}
                                                            },
                                                            "required": ["type"],
                                                            "type": "object",
                                                        },
                                                    },
                                                    "required": ["id", "type", "urn"],
                                                    "type": "object",
                                                },
                                            },
                                            "required": [
                                                "id", "type", "urn", "title", "adult",
                                                "resources", "releasedAt", "rating", "favorite", "personsUrn",
                                                "categories", "description", "duration", "episodeNumber",
                                                "seasonNumber", "countries", "genres", "awards", "estimate", "vod"
                                            ],
                                            "type": "object",

                                        },
                                        "available": {
                                            "additionalProperties": False,
                                            "properties": {
                                                "type": {"type": "string"}
                                            },
                                            "required": ["type"],
                                            "type": "object",
                                        },
                                    },
                                    "required": [
                                        "id", "type", "urn",
                                        "startAt", "endAt", "position",
                                        "global", "data", "available"
                                    ],
                                    "type": "object"
                                },
                                "type": "array"
                            },
                            "total": {"type": "integer"},
                            "links": {"type": "array"},
                            "type": {"type": "string"},
                            "urn": {"type": "string"},
                            "title": {"type": "string"},
                            "recommendationId": {"type": "string"}

                        },
                        "required": [
                            "items", "total",
                            "links", "type",
                            "urn", "title", "recommendationId"
                        ],
                        "type": "object",
                    },
                    "type": "array"

                },
                "total": {"type": "integer"},
                "links": {"type": "array"},
                "type": {"type": "string"},
                "urn": {"type": "string"},
                "title": {"type": "string"},
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
                "showcases", "total",
                "links", "type",
                "urn", "title", "references"
            ],
            "type": "object"
        },
        "offer": {"type": "null"},
        "favorite": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        }
    },
    "required": [
        "id", "type", "urn", "title",
        "adult", "resources", "description",
        "lcn", "style", "offersUrn", "available",
        "rating", "quality", "services", "schedules",
        "offer", "favorite"
    ],
    "type": "object"
}

catchup = {
    "additionalProperties": False,
    "properties": {
        "id": {"type": "integer"},
        "type": {"type": "string"},
        "urn": {"type": "string"},
        "startAt": {"type": "string"},
        "endAt": {"type": "string"},
        "position": {"type": "integer"},
        "global": {
            "additionalProperties": False,
            "properties": {
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "adult": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "rating": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "locals": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "string"},
                            "available": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"}
                                },
                                "required": ["type"],
                                "type": "object"
                            },
                            "quality": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"}
                                },
                                "required": ["type"],
                                "type": "object"
                            },
                            "services": {
                                "additionalItems": False,
                                "items": {
                                    "additionalProperties": False,
                                    "properties": {
                                        "type": {"type": "string"},
                                        "state": {
                                            "additionalProperties": False,
                                            "properties": {
                                                "type": {"type": "string"}
                                            },
                                            "required": ["type"],
                                            "type": "object"
                                        }
                                    },
                                    "required": ["type", "state"],
                                    "type": "object"

                                },
                                "type": "array",
                            },
                            "resources": {
                                "additionalItems": False,
                                "items": {
                                    "additionalProperties": False,
                                    "properties": {
                                        "id": {"type": "integer"},
                                        "type": {"type": "string"},
                                        "drm": {"type": "string"},
                                        "evenKey": {"type": "string"},
                                        "oddKey": {"type": "string"},
                                        "source": {"type": "string"}
                                    },
                                    "required": ["id", "type"],
                                    "type": "object"
                                },
                                "type": "array"
                            },
                            "urn": {"type": "string"}
                        },
                        "required": [
                            "id",
                            "title",
                            "available",
                            "quality",
                            "services",
                            "resources",
                            "urn"
                        ],
                        "type": "object"
                    },
                    "type": "array",
                },
            },
            "required": [
                "id", "title",
                "adult", "rating", "locals"
            ],
            "type": "object"
        },
        "data": {
            "additionalProperties": False,
            "properties": {
                "id": {},
                "type": {},
                "urn": {},
                "title": {},
                "adult": {},
                "resources": {  # <<< array
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "id": {"type": "integer"},
                            "type": {"type": "string"}
                        },
                        "required": ["id", "type"],
                        "type": "object"
                    },
                    "type": "array",
                },
                "releasedAt": {"type": ["null", "string"]},
                "rating": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "favorite": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "personsUrn": {"type": ["null", "string"]},
                "categories": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "string"}
                        },
                        "required": ["id", "title"],
                        "type": "object"
                    },
                    "type": "array",
                },
                "description": {"type": "string"},
                "duration": {"type": "integer"},
                "episodeNumber": {"type": "integer"},
                "seasonNumber": {"type": "integer"},
                "countries": {"type": "array"},
                "genres": {
                    "addittionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"title": "string"}
                        },
                        "required": ["id", "title"],
                        "type": "object"
                    },
                },
                "awards": {"type": "array"},
                "estimate": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "vod": {
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "integer"},
                        "type": {"type": "null"},
                        "urn": {"type": "null"},
                        "available": {
                            "additionalProperties": False,
                            "properties": {
                                "type": {"type": "string"}
                            },
                            "required": ["type"],
                            "type": "object"
                        },
                    },
                    "required": [
                        "id", "type",
                        "urn", "available"
                    ],
                    "type": "object"
                },
            },
            "required": [
                "id", "type", "urn", "title", "adult",
                "resources", "releasedAt", "rating", "favorite", "personsUrn",
                "categories", "description", "duration", "episodeNumber", "seasonNumber",
                "countries", "genres", "awards", "estimate", "vod"
            ],
            "type": "object"
        },
        "available": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object"
        }
    },
    "required": [
        "id", "type", "urn",
        "startAt", "endAt", "position",
        "global", "data", "available"
    ],
    "type": "object"
}

channel_packages = {
    "additionalProperties": False,
    "properties": {
        "id": {"type": "integer"},
        "type": {"type": "string"},
        "urn": {"type": "string"},
        "title": {"type": "string"},
        "adult": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "resources": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "integer"},
                    "type": {"type": "string"},
                },
                "required": ["id", "type"],
                "type": "object"
            },
            "type": "array"
        },
        "description": {"type": "string"},
        "offersUrn": {"type": "string"},
        "childrenUrn": {"type": "string"},
        "rating": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "available": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",

        },
        "offer": {
            "additionalProperties": False,
            "properties": {
                "id": {"type": "integer"},
                "type": {"type": "string"},
                "urn": {"type": "string"},
                "price": {"type": "integer"},
                "purchaseAt": {"type": "null"},
                "expireAt": {"type": "null"},
                "ivod": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "status": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "provider": {"type": "null"},
                "period": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"},
                        "value": {"type": "integer"}
                    },
                    "required": ["type", "value"],
                    "type": "object",
                },
                "adult": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "root": {
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "integer"},
                        "type": {"type": "string"},
                        "urn": {"type": "string"},
                        "resources": {
                            "additionalItems": False,
                            "items": {
                                "additionalItems": False,
                                "type": "array"
                            },
                            "type": "array"
                        },
                    },
                    "required": ["id", "type", "urn", "resources"],
                    "type": "object",

                },
                "stocks": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "endAt": {"type": "string"},
                            "discount": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                    "value": {"type": "string"}
                                },
                                "required": ["type", "value"],
                                "type": "object",
                            },
                            "startAt": {"type": "string"},
                            "type": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                },
                                "required": ["type"],
                                "type": "object",
                            },
                            "oldPrice": {"type": "integer"},
                            "status": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                    "value": {"type": "string"}
                                },
                                "required": ["type", "value"],
                                "type": "object",
                            }
                        },
                        "required": [
                            "endAt", "discount", "startAt",
                            "type", "oldPrice", "status"
                        ],
                        "type": "object",
                    },
                    "type": "array",
                },
                "quality": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "type": {"type": ["string", "null"]}
                        },
                        "required": ["type"],
                        "type": "object"
                    }
                },
                "store": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "source": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "null"},
                        "name": {"type": "null"}
                    },
                    "required": ["type", "name"],
                    "type": "object"
                }
            },
            "required": [
                "id", "type", "urn", "price",
                "purchaseAt", "expireAt", "ivod", "status",
                "provider", "period", "adult", "root"
            ],
            "type": "object"
        },
        "quality": {"type": ["null", "array"]},
    },
    "required": [
        "id", "type", "urn",
        "title", "adult", "resources",
        "description", "offersUrn", "rating",
        "available", "offer", "quality"
    ],
    "type": "object"
}

movies = {
    "additionalProperties": False,
    "properties": {
        "id": {"type": "integer"},
        "type": {"type": "string"},
        "urn": {"type": "string"},
        "title": {"type": "string"},
        "adult": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object"
        },
        "resources": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "integer"},
                    "type": {"type": "string"},
                    "drm": {"type": "string"}
                },
                "required": ["id", "type"],
                "type": "object"
            },
            "type": "array"
        },
        "releasedAt": {"type": "string"},
        "rating": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "favorite": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "personsUrn": {"type": "null"},
        "categories": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "id": {"type": ["integer", "null"]},
                    "title": {"type": ["string", "null"]}
                },
                "required": ["id", "title"],
                "type": "object",
            },
            "type": "array",
        },
        "offersUrn": {"type": "string"},
        "available": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",

        },
        "offer": {
            "additionalProperties": False,
            "properties": {
                "id": {"type": "integer"},
                "type": {"type": "string"},
                "urn": {"type": "string"},
                "price": {"type": "integer"},
                "purchaseAt": {"type": "null"},
                "expireAt": {"type": "null"},
                "ivod": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "status": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "provider": {
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "integer"},
                        "title": {"title": "string"},
                        "resources": {
                            "additionalItems": False,
                            "items": {
                                "additionalProperties": False,
                                "properties": {
                                    "id": {"type": "integer"},
                                    "type": {"type": "string"},
                                },
                                "required": ["id", "type"],
                                "type": "object"
                            },
                            "type": ["null", "array"],
                        },
                    },
                    "required": ["id", "title", "resources"],
                    "type": "object",
                },
                "period": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"},
                        "value": {"type": "integer"}
                    },
                    "required": ["type", "value"],
                    "type": "object",
                },
                "adult": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "root": {
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "integer"},
                        "type": {"type": "string"},
                        "urn": {"type": "string"},
                        "resources": {
                            "additionalItems": False,
                            "items": {
                                "additionalProperties": False,
                                "properties": {
                                    "id": {"type": ["null", "integer"]},
                                    "type": {"type": ["null", "string"]},
                                },
                                "required": ["id", "type"],
                                "type": "object"
                            },
                            "type": "array",
                        },
                    },
                    "required": ["id", "type", "urn", "resources"],
                    "type": "object"
                },
                "stocks": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "endAt": {"type": "string"},
                            "discount": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                    "value": {"type": "string"}
                                },
                                "required": ["type", "value"],
                                "type": "object",
                            },
                            "startAt": {"type": "string"},
                            "type": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                },
                                "required": ["type"],
                                "type": "object",
                            },
                            "oldPrice": {"type": "integer"},
                            "status": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                    "value": {"type": "string"}
                                },
                                "required": ["type", "value"],
                                "type": "object",
                            }
                        },
                        "required": [
                            "endAt", "discount", "startAt",
                            "type", "oldPrice", "status"
                        ],
                        "type": "object",
                    },
                    "type": "array",
                },
                "quality": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "type": {"type": "string"}
                        },
                        "required": ["type"],
                        "type": "object"
                    },
                    "type": "array"
                },
                "store": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "source": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "null"},
                        "name": {"type": "null"}
                    },
                    "required": ["type", "name"],
                    "type": "object",
                }
            },
            "required": [
                "id", "type", "urn", "price", "purchaseAt", "expireAt",
                "ivod", "status", "provider", "period", "adult", "root",
                "stocks", "quality", "store", "source"
            ],
            "type": "object",
        },
        "description": {"type": "string"},
        "duration": {"type": "integer"},
        "position": {"type": "integer"},
        "estimate": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",

        },
    },
    "required": [
        "id", "type", "urn", "title", "adult", "resources",
        "releasedAt", "rating", "favorite", "personsUrn", "categories", "offersUrn",
        "available", "offer", "description", "duration", "position", "estimate",
    ],
    "type": "object",
}

packages = {
    "additionalProperties": False,
    "properties": {
        "id": {"type": "integer"},
        "type": {"type": "string"},
        "urn": {"type": "string"},
        "title": {"type": "string"},
        "adult": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object"
        },
        "resources": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "integer"},
                    "type": {"type": "string"},
                },
                "required": ["id", "type"],
                "type": "object"
            },
            "type": "array"
        },
        "description": {"type": "string"},
        "offersUrn": {"type": ["string", "null"]},
        "childrenUrn": {"type": "string"},
        "rating": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "available": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "offer": {"type": "null"}
    },
    "required": [
        "id", "type", "urn",
        "title", "adult", "resources",
        "description", "offersUrn", "childrenUrn",
        "rating", "available", "offer"
    ],
    "type": "object",
}

subscriptions = {
    "additionalProperties": False,
    "properties": {
        "id": {"type": "integer"},
        "type": {"type": "string"},
        "urn": {"type": "string"},
        "title": {"type": "string"},
        "adult": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object"
        },
        "resources": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "integer"},
                    "type": {"type": "string"},
                },
                "required": ["id", "type"],
                "type": "object"
            },
            "type": "array"
        },
        "description": {"type": "string"},
        "offersUrn": {"type": ["object", "string"]},
        "childrenUrn": {"type": "string"},
        "rating": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "available": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "offer": {
            "additionalProperties": False,
            "properties": {
                "id": {"type": "integer"},
                "type": {"type": "string"},
                "urn": {"type": "string"},
                "price": {"type": "integer"},
                "purchaseAt": {"type": "null"},
                "expireAt": {"type": "null"},
                "ivod": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "status": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "provider": {
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "integer"},
                        "title": {"type": "string"},
                        "resources": {
                            "additionalItems": False,
                            "items": {
                                "additionalProperties": False,
                                "properties": {
                                    "id": {"type": "integer"},
                                    "type": {"type": "string"},
                                },
                                "required": ["id", "type"],
                                "type": "object"
                            },
                            "type": ["null", "array"],
                        },
                    },
                    "required": ["id", "title"],
                    "type": "object"
                },
                "period": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"},
                        "value": {"type": "integer"}
                    },
                    "required": ["type", "value"],
                    "type": "object",
                },
                "adult": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "root": {
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "integer"},
                        "type": {"type": "string"},
                        "urn": {"type": "string"},
                        "resources": {
                            "additionalItems": False,
                            "items": {
                                "additionalProperties": False,
                                "properties": {
                                    "id": {"type": "integer"},
                                    "type": {"type": "string"}
                                },
                                "required": ["id", "type"],
                                "type": "object",
                            },
                            "type": "array",
                        },
                    },
                    "required": ["id", "type", "urn", "resources"],
                    "type": "object",

                },
                "stocks": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "endAt": {"type": "string"},
                            "discount": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                    "value": {"type": "string"}
                                },
                                "required": ["type", "value"],
                                "type": "object",
                            },
                            "startAt": {"type": "string"},
                            "type": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                },
                                "required": ["type"],
                                "type": "object",
                            },
                            "oldPrice": {"type": "integer"},
                            "status": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                    "value": {"type": "string"}
                                },
                                "required": ["type", "value"],
                                "type": "object",
                            }
                        },
                        "required": [
                            "endAt", "discount", "startAt",
                            "type", "oldPrice", "status"
                        ],
                        "type": "object",
                    },
                    "type": "array",
                },
                "quality": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "type": {"type": ["string", "null"]}
                        },
                        "required": ["type"],
                        "type": "object"
                    }
                },
                "store": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "source": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "null"},
                        "name": {"type": "null"}
                    },
                    "required": ["type", "name"],
                    "type": "object"
                }
            },
            "required": [
                "id", "type", "urn", "price",
                "purchaseAt", "expireAt", "ivod", "status",
                "provider", "period", "adult", "root",
                "stocks", "quality", "store", "source"
            ],
            "type": "object",
        },
    },
    "required": [
        "id", "type", "urn", "title",
        "adult", "resources", "description", "offersUrn",
        "childrenUrn", "rating", "available", "offer",
    ],
    "type": "object",
}

genres = {
    "additionalProperties": False,
    "properties": {
        "id": {"type": "integer"},
        "type": {"type": "string"},
        "urn": {"type": "string"},
        "title": {"type": "string"},
        "adult": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object"
        },
        "resources": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "integer"},
                    "type": {"type": "string"},
                },
                "required": ["id", "type"],
                "type": "object"
            },
            "type": "array"
        },
        "description": {"type": "string"}
    },
    "required": [
        "id", "type", "urn",
        "title", "adult", "resources", "description"
    ],
    "type": "object",
}

serials = {
    "additionalProperties": False,
    "properties": {
        "id": {"type": "integer"},
        "type": {"type": "string"},
        "urn": {"type": "string"},
        "title": {"type": "string"},
        "adult": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object"
        },
        "resources": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "integer"},
                    "type": {"type": "string"},
                },
                "required": ["id", "type"],
                "type": "object"
            },
            "type": "array"
        },
        "releasedAt": {"type": "string"},
        "rating": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "favorite": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "personsUrn": {"type": ["null", "string"]},
        "categories": {
            "additionalItems": False,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "id": {"type": ["integer", "null"]},
                    "title": {"type": ["string", "null"]}
                },
                "required": ["id", "title"],
                "type": "object",
            },
            "type": "array",
        },
        "offersUrn": {"type": "string"},
        "available": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        },
        "offer": {
            "additionalProperties": False,
            "properties": {
                "id": {"type": "integer"},
                "type": {"type": "string"},
                "urn": {"type": "string"},
                "price": {"type": "integer"},
                "purchaseAt": {"type": "null"},
                "expireAt": {"type": "null"},
                "ivod": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "status": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "provider": {
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "integer"},
                        "title": {"type": "string"},
                        "resources": {"type": ["null", "array"]}
                    },
                    "required": ["id", "title", "resources"],
                    "type": "object"
                },
                "period": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"},
                        "value": {"type": "integer"}
                    },
                    "required": ["type", "value"],
                    "type": "object",
                },
                "adult": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object",
                },
                "root": {
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "integer"},
                        "type": {"type": "string"},
                        "urn": {"type": "string"},
                        "resources": {
                            "additionalItems": False,
                            "items": {
                                "additionalProperties": False,
                                "properties": {
                                    "id": {"type": "integer"},
                                    "type": {"type": "string"}
                                },
                                "required": ["id", "type"],
                                "type": "object",
                            },
                            "type": "array",
                        },
                    },
                    "required": ["id", "type", "urn", "resources"],
                    "type": "object",

                },
                "stocks": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "endAt": {"type": "string"},
                            "discount": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                    "value": {"type": "string"}
                                },
                                "required": ["type", "value"],
                                "type": "object",
                            },
                            "startAt": {"type": "string"},
                            "type": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                },
                                "required": ["type"],
                                "type": "object",
                            },
                            "oldPrice": {"type": "integer"},
                            "status": {
                                "additionalProperties": False,
                                "properties": {
                                    "type": {"type": "string"},
                                    "value": {"type": "string"}
                                },
                                "required": ["type", "value"],
                                "type": "object",
                            }
                        },
                        "required": [
                            "endAt", "discount", "startAt",
                            "type", "oldPrice", "status"
                        ],
                        "type": "object",
                    },
                    "type": "array",
                },
                "quality": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "type": {"type": ["string", "null"]}
                        },
                        "required": ["type"],
                        "type": "object"
                    }
                },
                "store": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "string"}
                    },
                    "required": ["type"],
                    "type": "object"
                },
                "source": {
                    "additionalProperties": False,
                    "properties": {
                        "type": {"type": "null"},
                        "name": {"type": "null"}
                    },
                    "required": ["type", "name"],
                    "type": "object"
                }
            },
            "required": [
                "id", "type", "urn", "price",
                "purchaseAt", "expireAt", "ivod", "status",
                "provider", "period", "adult", "root",
                "stocks", "quality", "store", "source"
            ],
            "type": "object",
        },
        "description": {"type": "string"},
        "seasonsUrn": {"type": "null"},
        "continues": {"type": "null"},
        "estimate": {
            "additionalProperties": False,
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"],
            "type": "object",
        }
    },
    "required": [
        "id", "type", "urn", "title",
        "adult", "resources", "releasedAt", "rating",
        "favorite", "personsUrn", "categories", "offersUrn",
        "available",  # "offer",
        "description", "seasonsUrn",
        "continues", "estimate"
    ],
    "type": "object",
}

mixed = {
    "additionalItems": False,
    "items": {"type": ["array", "null"]}
}

correct_schema = {
    "additionalProperties": False,
    "properties": {
        "data": {
            "additionalProperties": False,
            "properties": {
                "showcases": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "items": {
                                "items": {
                                    "anyOf": [
                                        channels,
                                        catchup,
                                        channel_packages,
                                        movies,
                                        packages,
                                        subscriptions,
                                        genres,
                                        serials,
                                        mixed
                                    ]
                                },
                                "type": "array"
                            },
                            "total": {"type": "integer"},
                            "links": {"type": "array"},
                            "type": {"type": "string"},
                            "urn": {"type": "string"},
                            "title": {"type": "string"},
                            "recommendationId": {"type": "string"}
                        },
                        "required": [
                            "items", "total", "links",
                            "type", "urn", "title"
                        ],
                        "type": "object"
                    },
                    "type": "array",

                },
                "total": {"type": "integer"},
                "links": {"type": "array"},
                "type": {"type": "string"},
                "urn": {"type": "string"},
                "title": {"type": "string"},
                "references": {
                    "additionalItems": False,
                    "items": {
                        "additionalProperties": False,
                        "properties": {
                            "title": {"type": "string"},
                            "urn": {"type": "string"},
                            "type": {"type": "string"},
                        },
                        "required": ["title", "urn", "type"],
                        "type": "object"
                    },
                    "type": "array"
                }
            },
            "required": [
                "showcases",
                "total",
                "links",
                "type",
                "urn",
                "title",
                "references"
            ],
            "type": "object"
        }
    },
    "type": "object"
}

# correct_schema_1 = {
#     "additionalProperties": False,
#     "properties": {
#         "data": {
#             "additionalProperties": False,
#             "properties": {
#
#                 "showcases": {
#                     "additionalItems": False,
#                     "items": {
#                         "additionalProperties": False,
#                         "properties": {
#                             "items": {
#                                 "additionalItems": False,
#                                 "items": {
#                                     "additionalProperties": False,
#                                     "properties": {
#                                         "additionalProperties": False,
#                                         "properties": {
#                                             "id": {"type": "string"},
#                                             "type": {"type": "string"},
#                                             "urn": {"type": "string"},
#                                             "title": {"type": "string"},
#                                             "adult": {
#                                                 "additionalProperties": False,
#                                                 "properties": {
#                                                     "title": {"type": "string"},
#                                                     "type": {"type": "string"}
#                                                 },
#                                                 "required": ["title", "type"],
#                                                 "type": "object"
#                                             },
#                                             "resources": {
#                                                 "additionalItems": False,
#                                                 "items": {
#                                                     "additionalProperties": False,
#                                                     "properties": {
#                                                         "id": {"type": "integer"},
#                                                         "type": {"type": "string"},
#                                                         "drm": {"type": "string"},
#                                                         "evenKey": {"type": "string"},
#                                                         "oddKey": {"type": "string"},
#                                                         "source": {"type": "string"}
#                                                     },
#                                                     "required": ["id", "type"],
#                                                     "type": "object"
#                                                 },
#                                                 "type": "array"
#                                             },
#                                             "description": {"type": "string"},
#                                             "lcn": {"type": "integer"},
#                                             "style": {
#                                                 "additionalProperties": False,
#                                                 "properties": {
#                                                     "backgroundColor": {"type": "string"}
#                                                 },
#                                                 "required": ["backgroundColor"],
#                                                 "type": "object"
#                                             },
#                                             "offersUrn": "null",
#                                             "available": {
#                                                 "additionalProperties": False,
#                                                 "properties": {
#                                                     "type": {"type": "string"}
#                                                 },
#                                                 "required": ["type"],
#                                                 "type": "object",
#
#                                             },
#                                             "rating": {
#                                                 "additionalProperties": False,
#                                                 "properties": {
#                                                     "type": {"type": "string"}
#                                                 },
#                                                 "required": ["type"],
#                                                 "type": "object",
#                                             },
#                                             "quality": {
#                                                 "additionalProperties": False,
#                                                 "properties": {
#                                                     "type": {"type": "string"}
#                                                 },
#                                                 "required": ["type"],
#                                                 "type": "object,"
#                                             },
#                                             "services": {
#                                                 "additionalItems": False,
#                                                 "items": {
#                                                     "additionalProperties": False,
#                                                     "properties": {
#                                                         "type": {"type": "string"},
#                                                         "state": {
#                                                             "additionalProperties": False,
#                                                             "properties": {
#                                                                 "type": {"type": "string"}
#                                                             },
#                                                             "required": ["type"],
#                                                             "type": "object"
#                                                         }
#
#                                                     },
#                                                     "required": ["type", "state"],
#                                                     "type": "object"
#
#                                                 },
#                                                 "type": "array",
#                                             },
#                                             "schedules": {
#                                                 "additionalProperties": False,
#                                                 "properties": {
#                                                     "showcases": {
#                                                         "additionalItems": False,
#                                                         "items": {
#                                                             "additionalProperties": False,
#                                                             "properties": {
#                                                                 "items": {
#                                                                     "additionalItems": False,
#                                                                     "items": {
#                                                                         "additionalProperties": False,
#                                                                         "properties": {
#                                                                             "id": {"type": "integer"},
#                                                                             "type": {"type": "string"},
#                                                                             "urn": {"type": "string"},
#                                                                             "startAt": {"type": "string"},
#                                                                             "endAt": {"type": "string"},
#                                                                             "position": {"type": "integer"},
#                                                                             "global": {
#                                                                                 "additionalProperties": False,
#                                                                                 "properties": {
#                                                                                     "id": {"type": "integer"},
#                                                                                     "title": {"type": "string"},
#                                                                                     "adult": {
#                                                                                         "additionalProperties": False,
#                                                                                         "properties": {
#                                                                                             "type": {"type": "string"}
#                                                                                         },
#                                                                                         "required": ["type"],
#                                                                                         "type": "object"
#                                                                                     },
#                                                                                     "rating": {
#                                                                                         "additionalProperties": False,
#                                                                                         "properties": {
#                                                                                             "type": {"type": "string"}
#                                                                                         },
#                                                                                         "required": ["type"],
#                                                                                         "type": "object"
#                                                                                     },
#                                                                                     "locals": {
#                                                                                         "additionalItems": False,
#                                                                                         "items": {
#                                                                                             "additionalProperties": False,
#                                                                                             "properties": {
#                                                                                                 "id": {
#                                                                                                     "type": "integer"},
#                                                                                                 "title": {
#                                                                                                     "type": "string"},
#                                                                                                 "available": {
#                                                                                                     "additionalProperties": False,
#                                                                                                     "properties": {
#                                                                                                         "type": {
#                                                                                                             "type": "string"}
#                                                                                                     },
#                                                                                                     "required": [
#                                                                                                         "type"],
#                                                                                                     "type": "object"
#                                                                                                 },
#                                                                                                 "quality": {
#                                                                                                     "additionalProperties": False,
#                                                                                                     "properties": {
#                                                                                                         "type": {
#                                                                                                             "type": "string"}
#                                                                                                     },
#                                                                                                     "required": [
#                                                                                                         "type"],
#                                                                                                     "type": "object,"
#                                                                                                 },
#                                                                                                 "services": {
#                                                                                                     "additionalItems": False,
#                                                                                                     "items": {
#                                                                                                         "additionalProperties": False,
#                                                                                                         "properties": {
#                                                                                                             "type": {
#                                                                                                                 "type": "string"},
#                                                                                                             "state": {
#                                                                                                                 "additionalProperties": False,
#                                                                                                                 "properties": {
#                                                                                                                     "type": {
#                                                                                                                         "type": "string"}
#                                                                                                                 },
#                                                                                                                 "required": [
#                                                                                                                     "type"],
#                                                                                                                 "type": "object"
#                                                                                                             }
#                                                                                                         },
#                                                                                                         "required": [
#                                                                                                             "type",
#                                                                                                             "state"],
#                                                                                                         "type": "object"
#
#                                                                                                     },
#                                                                                                     "type": "array",
#                                                                                                 },
#                                                                                                 "resources": {
#                                                                                                     "additionalItems": False,
#                                                                                                     "items": {
#                                                                                                         "additionalProperties": False,
#                                                                                                         "properties": {
#                                                                                                             "id": {
#                                                                                                                 "type": "integer"},
#                                                                                                             "type": {
#                                                                                                                 "type": "string"},
#                                                                                                             "drm": {
#                                                                                                                 "type": "string"},
#                                                                                                             "evenKey": {
#                                                                                                                 "type": "string"},
#                                                                                                             "oddKey": {
#                                                                                                                 "type": "string"},
#                                                                                                             "source": {
#                                                                                                                 "type": "string"}
#                                                                                                         },
#                                                                                                         "required": [
#                                                                                                             "id",
#                                                                                                             "type"],
#                                                                                                         "type": "object"
#                                                                                                     },
#                                                                                                     "type": "array"
#                                                                                                 },
#                                                                                                 "urn": {
#                                                                                                     "type": "string"}
#                                                                                             },
#                                                                                             "required": [
#                                                                                                 "id", "title",
#                                                                                                 "available",
#                                                                                                 "quality", "services",
#                                                                                                 "resources", "urn"
#                                                                                             ],
#                                                                                             "type": "object"
#                                                                                         },
#                                                                                         "type": "array"
#                                                                                     }
#                                                                                 },
#                                                                                 "required": [
#                                                                                     "id", "title",
#                                                                                     "adult", "reting", "locals"
#                                                                                 ],
#                                                                                 "type": "object",
#                                                                             },
#                                                                             "data": {
#                                                                                 "additionalProperties": False,
#                                                                                 "properties": {
#                                                                                     "id": {"type": "integer"},
#                                                                                     "type": {"type": "string"},
#                                                                                     "urn": {"type": "string"},
#                                                                                     "title": {"type": "string"},
#                                                                                     "adult": {
#                                                                                         "additionalProperties": False,
#                                                                                         "properties": {
#                                                                                             "type": {"type": "string"}},
#                                                                                         "type": "object",
#                                                                                     },
#                                                                                     "resources": {
#                                                                                         "additionalItems": False,
#                                                                                         "items": {
#                                                                                             "additionalProperties": False,
#                                                                                             "properties": {
#                                                                                                 "id": {
#                                                                                                     "type": "integer"},
#                                                                                                 "type": {
#                                                                                                     "type": "string"}
#                                                                                             },
#                                                                                             "required": ["id", "type"],
#                                                                                             "type": "object",
#                                                                                         },
#                                                                                         "type": "array"
#                                                                                     },
#                                                                                     "releasedAt": {"type", "null"},
#                                                                                     "rating": {
#                                                                                         "additionalProperties": False,
#                                                                                         "properties": {
#                                                                                             "type": {"type", "string"}
#                                                                                         },
#                                                                                         "required": ["type"],
#                                                                                         "type": "object",
#                                                                                     },
#                                                                                     "favorite": {
#                                                                                         "additionalProperties": False,
#                                                                                         "properties": {
#                                                                                             "type": {"type", "string"}
#                                                                                         },
#                                                                                         "required": ["type"],
#                                                                                         "type": "object",
#                                                                                     },
#                                                                                     "personsUrn": {"type", "string"},
#                                                                                     "categories": {
#                                                                                         "additionalItems": False,
#                                                                                         "items": {
#                                                                                             "additionalProperties": False,
#                                                                                             "properties": {
#                                                                                                 "id": {
#                                                                                                     "type": "integer"},
#                                                                                                 "title": {"type",
#                                                                                                           "string"}
#                                                                                             },
#                                                                                             "required": ["id", "title"],
#                                                                                             "type": "object",
#                                                                                         },
#                                                                                         "type": "array",
#                                                                                     },
#                                                                                     "description": {"type": "string"},
#                                                                                     "duration": {"type": "integer"},
#                                                                                     "episodeNumber": {
#                                                                                         "type": "integer"},
#                                                                                     "seasonNumber": {"type": "integer"},
#                                                                                     # "countries": {
#                                                                                     #     "additionalItems": False,
#                                                                                     #     "items": {
#                                                                                     #         "additionalProperties": False,
#                                                                                     #         "properties": {
#                                                                                     #             "id": {"type": "integer"},
#                                                                                     #             "title": {"type", "string"}
#                                                                                     #         },
#                                                                                     #         "required": ["id", "title"],
#                                                                                     #         "type": "object",
#                                                                                     #     },
#                                                                                     #     "type": ["null", "array"],
#                                                                                     # },
#                                                                                     "countries": {
#                                                                                         "additionalItems": False,
#                                                                                         "type": "array"
#                                                                                     },
#                                                                                     "genres": {
#                                                                                         "additionalItems": False,
#                                                                                         "items": {
#                                                                                             "additionalProperties": False,
#                                                                                             "properties": {
#                                                                                                 "id": {
#                                                                                                     "type": "integer"},
#                                                                                                 "title": {"type",
#                                                                                                           "string"}
#                                                                                             },
#                                                                                             "required": ["id", "title"],
#                                                                                             "type": "object",
#                                                                                         },
#                                                                                         "type": "array",
#                                                                                     },
#                                                                                     # "awards": {
#                                                                                     #     "additionalItems": False,
#                                                                                     #     "items": {
#                                                                                     #         "additionalProperties": False,
#                                                                                     #         "properties": {
#                                                                                     #             "id": {"type": "integer"},
#                                                                                     #             "title": {"type", "string"}
#                                                                                     #         },
#                                                                                     #         "required": ["id", "title"],
#                                                                                     #         "type": "object",
#                                                                                     #     },
#                                                                                     #     "type": ["null", "array"],
#                                                                                     # },
#                                                                                     "awards": {
#                                                                                         "additionalItems": False,
#                                                                                         "type": "array"
#                                                                                     },
#                                                                                     "estimate": {
#                                                                                         "additionalProperties": False,
#                                                                                         "properties": {
#                                                                                             "type": {"type": "string"}
#                                                                                         },
#                                                                                         "required": ["type"],
#                                                                                         "type": "object",
#                                                                                     },
#                                                                                     "vod": {
#                                                                                         "additionalProperties": False,
#                                                                                         "properties": {
#                                                                                             "id": {"type", "integer"},
#                                                                                             "type": {"type", "null"},
#                                                                                             "urn": {"type", "null"},
#                                                                                             "available": {
#                                                                                                 "additionalProperties": False,
#                                                                                                 "properties": {
#                                                                                                     "type": {"type",
#                                                                                                              "string"}
#                                                                                                 },
#                                                                                                 "required": ["type"],
#                                                                                                 "type": "object",
#                                                                                             },
#                                                                                         },
#                                                                                         "required": [
#                                                                                             "id", "type",
#                                                                                             "urn", "available"
#                                                                                         ],
#                                                                                         "type": "object",
#                                                                                     },
#                                                                                 },
#                                                                                 "required": [
#                                                                                     "id", "type", "urn", "title",
#                                                                                     "adult",
#                                                                                     "resources", "releasedAt", "rating",
#                                                                                     "favorite", "personsUrn",
#                                                                                     "categories", "description",
#                                                                                     "duration", "episodeNumber",
#                                                                                     "seasonNumber", "countries",
#                                                                                     "genres", "awards", "estimate",
#                                                                                     "vod"
#                                                                                 ],
#                                                                                 "type": "object",
#
#                                                                             },
#                                                                             "available": {
#                                                                                 "additionalProperties": False,
#                                                                                 "properties": {
#                                                                                     "type": {"type": "string"}
#                                                                                 },
#                                                                                 "required": ["type"],
#                                                                                 "type": "object",
#                                                                             },
#                                                                         },
#                                                                         "required": [
#                                                                             "id", "type", "urn",
#                                                                             "startAt", "endAt", "position",
#                                                                             "global", "data", "available"
#                                                                         ],
#                                                                         "type": "object"
#                                                                     },
#                                                                     "type": "array"
#                                                                 },
#                                                                 "total": {"type": "integer"},
#                                                                 "links": {},  # !
#                                                                 "type": {"type": "string"},
#                                                                 "urn": {"type": "string"},
#                                                                 "title": {"type": "string"},
#                                                                 "recommendationId": {"type": "string"}
#
#                                                             },
#                                                             "required": [
#                                                                 "items", "total",
#                                                                 "links", "type",
#                                                                 "urn", "title", "recommendationId"
#                                                             ],
#                                                             "type": "object",
#                                                         },
#                                                         "type": "array"
#
#                                                     },
#                                                     "total": {"type": "integer"},
#                                                     "links": {
#                                                         "additionalItems": False,
#                                                         "type": "array"
#                                                     },
#                                                     "type": {"type": "string"},
#                                                     "urn": {"type": "string"},
#                                                     "title": {"type": "string"},
#                                                     "references": {
#                                                         "additionalItems": False,
#                                                         "items": {
#                                                             "additionalProperties": False,
#                                                             "properties": {
#                                                                 "title": {"type": "string"},
#                                                                 "urn": {"type": "string"},
#                                                                 "type": {"type": "string"}
#                                                             },
#                                                             "required": ["title", "urn", "type"],
#                                                             "type": "object"
#                                                         },
#                                                         "type": "array"
#                                                     }
#                                                 },
#                                                 "required": [
#                                                     "showcases", "total",
#                                                     "links", "type",
#                                                     "urn", "title", "references"
#                                                 ],
#                                                 "type": "object"
#                                             },
#                                             "offer": {"type": "null"},
#                                             "favorite": {
#                                                 "additionalProperties": False,
#                                                 "properties": {
#                                                     "type": {"type": "string"}
#                                                 },
#                                                 "required": ["type"],
#                                                 "type": "object",
#                                             }
#                                         },
#                                         "required": [
#                                             "id", "type", "urn", "title",
#                                             "adult", "resources", "description",
#                                             "lcn", "style", "offersUrn", "available",
#                                             "rating", "quality", "services", "schedules",
#                                             "offer", "favorite"
#                                         ],
#                                         "type": "object"
#                                     }
#                                 },
#                                 "type": "array"
#                             },
#                             "total": {"type": "integer"},
#                             "links": {"type": "array"},
#                             "type": {"type": "string"},
#                             "urn": {"type": "string"},
#                             "title": {"type": "string"},
#                             "recommendationId": "string"
#                         },
#                         "required": [
#                             "items", "total", "links",
#                             "type", "urn", "title"
#                         ],
#                         "type": "object"
#                     },
#                     "type": "array",
#
#                 },
#                 "total": {"type": "integer"},
#                 "links": {"type": "array"},
#                 "type": {"type": "string"},
#                 "urn": {"type": "string"},
#                 "title": {"type": "string"},
#                 "references": {
#                     "additionalItems": False,
#                     "items": {
#                         "additionalProperties": False,
#                         "properties": {
#                             "title": {"type": "string"},
#                             "urn": {"type": "string"},
#                             "type": {"type": "string"},
#                         },
#                         "required": ["title", "urn", "type"],
#                         "type": "object"
#                     },
#                     "type": "array"
#                 }
#             },
#             "required": [
#                 "showcases", "total", "links",
#                 "type", "urn", "title", "references"
#             ],
#             "type": "object"
#         }
#     },
#     "required": ["data"],
#     "type": "object"
# }
