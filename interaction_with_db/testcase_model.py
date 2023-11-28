from dataclasses import dataclass


@dataclass
class TestCaseModel:
    tc_description: str
    tc_author_id: int
    tc_name: str
    new_description: str



