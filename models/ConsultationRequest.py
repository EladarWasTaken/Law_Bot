class ConsultationRequest:
	"""
	A class to represent a consultation request.

	Attributes
	----------
	user_id : str
		The ID of the user making the request.
	case_type : str
		The type of the court case.
	details : dict
		The details required for the court case.
	selected_firm : str
		The law firm selected for the consultation.
	provided_documents : list
		The list of documents provided for the consultation.

	Methods
	-------
	__init__(user_id, case_type, details, selected_firm, provided_documents):
		Initializes the ConsultationRequest with the given parameters.
	"""

	def __init__(self, user_id, case_type, details, selected_firm,
	             provided_documents):
		"""
		Constructs all the necessary attributes for the ConsultationRequest object.

		Parameters
		----------
		user_id : str
			The ID of the user making the request.
		case_type : str
			The type of the court case.
		details : dict
			The details required for the court case.
		selected_firm : str
			The law firm selected for the consultation.
		provided_documents : list
			The list of documents provided for the consultation.
		"""
		self.user_id = user_id
		self.case_type = case_type
		self.details = details
		self.selected_firm = selected_firm
		self.provided_documents = provided_documents
