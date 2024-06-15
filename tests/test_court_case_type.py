import pytest

from models.CourtCaseType import CourtCaseType


@pytest.fixture
def test_court_case_type_initialization():
  case_type = "Divorce"
  required_details = ["Date of Marriage", "Children Involved"]
  court_case = CourtCaseType(case_type, required_details)

  assert court_case.case_type == case_type
  assert court_case.required_details == required_details


def test_court_case_type_initialization_empty_details():
  case_type = "Theft"
  required_details = []
  court_case = CourtCaseType(case_type, required_details)

  assert court_case.case_type == case_type
  assert court_case.required_details == required_details


def test_court_case_type_initialization_with_none():
  case_type = "Car Accident"
  required_details = None
  court_case = CourtCaseType(case_type, required_details)

  assert court_case.case_type == case_type
  assert court_case.required_details is None
