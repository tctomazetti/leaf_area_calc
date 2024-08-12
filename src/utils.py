import json
from paths import MODELS_FILE, BIBLIOGRAPHY_FILE, BIBLIOGRAPHY_DIR
from pathlib import Path


def load_model_info() -> dict[str, any]:
    with open(MODELS_FILE) as json_file:
        return json.load(json_file)


def load_bibliography_info() -> dict[str, any]:
    with open(BIBLIOGRAPHY_FILE) as json_file:
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


def mlr_calc(length: float, width: float, lv_right: float, lv_left: float, terms: list[dict[str, any]]) -> float:
    alv = (lv_right + lv_left) / 2
    result = 0
    for term in terms:
        ft = term.get("term")
        coef = term.get("coefficient")
        if ft == "l":
            result += coef * length
        elif ft == "l^2":
            result += coef * length**2
        elif ft == "w":
            result += coef * width
        elif ft == "w^2":
            result += coef * width**2
        elif ft == "alv":
            result += coef * alv
        elif ft == "alv^2":
            result += coef * alv**2
        elif ft == "constant":
            result += coef
        else:
            raise ValueError(f"coefficient {term} not valid")
    return round(result, 2) if result > 0 else 0


class Citation:
    def __init__(self, model_citation: str) -> None:
        bibliography = load_bibliography_info()
        citation = bibliography.get(model_citation, "No available bibliography")
        self.name = model_citation
        self.title = citation["title"]
        self.url = citation["url"]
        self.pdf_file = self._get_pdf_path(citation["file"])
    

    def _get_pdf_path(self, name: str) -> Path | None:
        if len(name) == 0:
            return None
        return BIBLIOGRAPHY_DIR / name
    