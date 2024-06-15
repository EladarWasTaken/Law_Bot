import pytest

from models.ConsultationRequest import ConsultationRequest


@pytest.fixture
def test_consultation_request_initialization():
  user_id = "user123"
  case_type = "criminal"
  details = {"case_id": "case123", "description": "Description of the case"}
  selected_firm = "Law Firm ABC"
  provided_documents = ["doc1.pdf", "doc2.pdf"]

  consultation_request = ConsultationRequest(user_id, case_type, details, selected_firm, 
                                             provided_documents)

  assert consultation_request.user_id == user_id
  assert consultation_request.case_type == case_type
  assert consultation_request.details == details
  assert consultation_request.selected_firm == selected_firm
  assert consultation_request.provided_documents == provided_documents


def test_consultation_request_initialization_empty():
  user_id = ""
  case_type = ""
  details = {}
  selected_firm = ""
  provided_documents = []

  consultation_request = ConsultationRequest(user_id, case_type, details, selected_firm,
                                             provided_documents)

  assert consultation_request.user_id == user_id
  assert consultation_request.case_type == case_type
  assert consultation_request.details == details
  assert consultation_request.selected_firm == selected_firm
  assert consultation_request.provided_documents == provided_documents


def test_consultation_request_initialization_with_none():
  user_id = None
  case_type = None
  details = None
  selected_firm = None
  provided_documents = None

  consultation_request = ConsultationRequest(user_id, case_type, details, selected_firm, 
                                             provided_documents)

  assert consultation_request.user_id == user_id
  assert consultation_request.case_type == case_type
  assert consultation_request.details == details
  assert consultation_request.selected_firm == selected_firm
  assert consultation_request.provided_documents == provided_documents