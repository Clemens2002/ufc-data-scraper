from ufc_data_scraper.data_models.event.result import Result
from ufc_data_scraper.data_models.event.weight_class import WeightClass
from ufc_data_scraper.data_models.event.accolade import Accolade
from ufc_data_scraper.data_models.event.rule_set import RuleSet

from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Fight:
    fight_order: int
    referee_name: str
    fighters_stats: list
    result: Result
    weight_class: WeightClass
    accolades: Accolade
    rule_set: RuleSet
    fight_scores: list
