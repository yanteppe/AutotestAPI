correct_schema = {
    "properties": {
        "data": {
            "required": ["showcases"],
            "properties": {
                "showcases": {"type": "array"}
            },
            "showcases": {
                "required": ["items"],
                "properties": {
                    "items": {
                        "type": "array"
                    }
                },
                "items": {
                    "required": ["total", "type", "title"],
                    "properties": {
                        "total": {"type": "integer"},
                        "type": {"type": "string"},
                        "title": {"type": "string"},
                    }
                }
            }
        }
    }
}
