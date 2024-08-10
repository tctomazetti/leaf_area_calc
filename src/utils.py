import json
from paths import MODELS_FILE


def load_model_info() -> dict[str, any]:
    with open(MODELS_FILE) as json_file:
        return json.load(json_file)


def get_model_parameters(model_info: dict[str, any], specie: str, variety: str, feature: str, model_cod: str) -> dict[str, any]:
    return model_info[specie][variety][feature][model_cod]


def get_terms(parameters: dict[str, any]) -> list[dict[str, any]]:
    return parameters["model"]["terms"]


def calculate_leaf_area(value: float, terms: list[dict[str, any]]) -> float:
    result = 0
    for term in terms:
        if term["term"] == "x":
            result += term["coefficient"] * value
        elif term["term"] == "x^2":
            result += term["coefficient"] * (value ** 2)
        elif term["term"] == "constant":
            result += term["coefficient"]
    return round(result, 2) if result > 0 else 0
