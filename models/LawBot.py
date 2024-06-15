import json


class LawBot:
	"""
	A class to represent a bot that helps users find law firms and required documents
	for specific court cases.

	Attributes
	----------
	data_file : str
		The path to the JSON file containing the data.
	court_case_types : list
		A list of court case types.
	law_firms : list
		A list of law firms and their supported case types.
	consultation_requests : list
		A list of consultation requests.

	Methods
	-------
	load_data():
		Loads data from the JSON file into the class attributes.
	find_law_firms_and_documents(case_type, details):
		Finds law firms and required documents for a given case type and details.
	request_consultation(case_type, details):
		Requests a consultation for a given case type and details.
	"""

	def __init__(self, data_file):
		"""
		Constructs all the necessary attributes for the LawBot object.

		Parameters
		----------
		data_file : str
			The path to the JSON file containing the data.
		"""
		self.data_file = data_file
		self.court_case_types = []
		self.law_firms = []
		self.consultation_requests = []
		self.load_data()

	def load_data(self):
		"""
		Loads data from the JSON file into the class attributes.
		"""
		with open(self.data_file, "r", encoding="utf-8") as f:
			data = json.load(f)
			self.court_case_types = data["court_case_types"]
			self.law_firms = data["law_firms"]
			self.consultation_requests = data["consultation_requests"]

	def find_law_firms_and_documents(self, case_type, details):
		"""
		Finds law firms and required documents for a given case type and details.

		Parameters
		----------
		case_type : str
			The type of the court case.
		details : dict
			The details required for the court case.

		Returns
		-------
		tuple
			A tuple containing a list of matching law firms and a list of required
			documents.
		"""
		matching_firms = []
		required_documents = []

		for firm in self.law_firms:
			if any(case_type.lower() in case.lower()
			       for case in firm["supported_cases"]):
				matching_firms.append(firm["name"])
				required_documents.extend(firm["required_documents"].get(
				    case_type, []))

		return matching_firms, required_documents

	def request_consultation(self, case_type, details):
		"""
		Requests a consultation for a given case type and details.

		Parameters
		----------
		case_type : str
			The type of the court case.
		details : dict
			The details required for the court case.

		Returns
		-------
		str or dict
			A message indicating an error or a dictionary containing the matching law
			firms and required documents.
		"""
		case_type_info = next(
		    (item for item in self.court_case_types
		     if case_type.lower() in item["case_type"].lower()), None)
		if not case_type_info:
			return "Case type not found"

		firms, documents = self.find_law_firms_and_documents(
		    case_type, details)

		if not firms:
			return "There are no law firms for this case type."

		response = {"firms": firms, "required_documents": documents}

		return response
