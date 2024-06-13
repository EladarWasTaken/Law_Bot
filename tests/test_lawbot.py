import pytest
from models.LawBot import LawBot


@pytest.fixture
def lawbot():
	return LawBot('test_data.json')


def test_load_data(lawbot):
	assert len(lawbot.court_case_types) > 0
	assert len(lawbot.law_firms) > 0


def test_find_law_firms_and_documents_divorce(lawbot):
	case_type = "Divorce"
	details = {"Date of Marriage": "01-01-2010", "Children Involved": "2"}
	firms, documents = lawbot.find_law_firms_and_documents(case_type, details)

	assert any("firm a" == firm.lower() for firm in firms)
	assert any("marriage certificate" == document.lower()
	           for document in documents)


def test_find_law_firms_and_documents_theft(lawbot):
	case_type = "Theft"
	details = {
	    "Date of Incident": "01-01-2022",
	    "Location of Incident": "Street"
	}
	firms, documents = lawbot.find_law_firms_and_documents(case_type, details)

	assert any("firm a" == firm.lower() for firm in firms)
	assert any("theft report" == document.lower() for document in documents)


def test_find_law_firms_and_documents_no_case(lawbot):
	case_type = "Fraud"
	details = {
	    "Date of Incident": "01-01-2022",
	    "Location of Incident": "Street"
	}
	firms, documents = lawbot.find_law_firms_and_documents(case_type, details)

	assert len(firms) == 0
	assert len(documents) == 0


def test_request_consultation_missing_details(lawbot):
	case_type = "Car Accident"
	details = {"Date of Incident": "01-01-2022"}
	result = lawbot.request_consultation(case_type, details)

	assert "missing details" in result.lower()


def test_request_consultation_success(lawbot):
	case_type = "Car Accident"
	details = {
	    "Date of Incident": "01-01-2022",
	    "Location of Incident": "Street",
	    "Driver's Condition": "Sober"
	}
	result = lawbot.request_consultation(case_type, details)

	assert isinstance(result, dict)
	assert any("firm b" == firm.lower() for firm in result["firms"])
	assert any("accident report" == document.lower()
	           for document in result["required_documents"])
