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


def simple_reg_calc(x_value: float, terms: list[dict[str, any]]) -> float:
    result = 0
    for term in terms:
        if term["term"] == "x":
            result += term["coefficient"] * x_value
        elif term["term"] == "x^2":
            result += term["coefficient"] * (x_value ** 2)
        elif term["term"] == "constant":
            result += term["coefficient"]
    return round(result, 2) if result > 0 else 0


class Leaf:
    def __init__(self, length: float | None, width: float | None, right_lv: float | None, left_lv: float | None) -> None:
        self.length = length
        self.width = width
        self.right_lv = right_lv
        self.left_lv = left_lv
        self.alv = self._calc_alv()

    def _calc_alv(self) -> float | None:
        if self.right_lv is None or self.left_lv is None:
            return None
        return round((self.right_lv + self.left_lv) / 2, 2)
    
    def calc_ldi(self) -> float | None:
        if self.alv is None or self.alv == 0:
            return None
        return round((abs(self.right_lv - self.left_lv) / self.alv) * 10, 2)


def mlr_calc(leaf: Leaf, terms: list[dict[str, any]]) -> float:
    result = 0
    for term in terms:
        ft = term.get("term")
        coef = term.get("coefficient")
        if ft == "l":
            result += coef * leaf.length
        elif ft == "l^2":
            result += coef * leaf.length**2
        elif ft == "w":
            result += coef * leaf.width
        elif ft == "w^2":
            result += coef * leaf.width**2
        elif ft == "alv":
            result += coef * leaf.alv
        elif ft == "alv^2":
            result += coef * leaf.alv**2
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
