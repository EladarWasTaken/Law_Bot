import pytest

from models.LawFirm import LawFirm


@pytest.fixture
def test_law_firm_initialization():
  name = "Firm A"
  supported_cases = ["Divorce"]
  required_documents = ["Marriage Certificate", "Children's Documents"]
  law_firm = LawFirm(name, supported_cases, required_documents)

  assert law_firm.name == name
  assert law_firm.supported_cases == supported_cases
  assert law_firm.required_documents == required_documents


def test_law_firm_initialization_empty_details():
  name = "Firm B"
  supported_cases = []
  required_documents = []
  law_firm = LawFirm(name, supported_cases, required_documents)

  assert law_firm.name == name
  assert law_firm.supported_cases == supported_cases
  assert law_firm.required_documents == required_documents


def test_law_firm_initialization_with_none():
  name = "Firm A"
  supported_cases = None
  required_documents = None
  law_firm = LawFirm(name, supported_cases, required_documents)

  assert law_firm.name == name
  assert law_firm.supported_cases is None
  assert law_firm.required_documents is None
