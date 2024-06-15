class CourtCaseType:
  """
	A class to represent a type of court case.

	Attributes
	----------
	case_type : str
		The type of the court case.
	required_details : list
		A list of details required for the court case.

	Methods
	-------
	__init__(case_type, required_details):
		Initializes the CourtCaseType with the given parameters.
	"""

  def __init__(self, case_type, required_details):
    """
		Constructs all the necessary attributes for the CourtCaseType object.

		Parameters
		----------
		case_type : str
			The type of the court case.
		required_details : list
			A list of details required for the court case.
		"""
    self.case_type = case_type
    self.required_details = required_details
