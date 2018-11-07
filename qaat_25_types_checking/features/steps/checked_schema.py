from jsonschema import validate

"""
Модуль для проверки схем
"""

# Проверяемая схема
checked_schema = {}


def debug_schema():
    '''Валидатор схемы'''

    # Проверяемый json
    json_response = {}

    validate(json_response, checked_schema)


debug_schema()
