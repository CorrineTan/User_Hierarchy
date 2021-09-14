import json
from dataclasses import dataclass

@dataclass
class Role:
	"""
	A class for Roles
	"""

	id: int
	name: str
	parent: int

	def getId(self):
		"""
		Getter for id
		"""
		return self.id


	def getName(self):
		"""
		Getter for name
		"""
		return self.name


	def getParent(self):
		"""
		Getter for parent
		"""
		return self.parent


	def __str__(self):
		"""
		Overide the output with string json format
		"""
		output = {
			"Id": self.getId(),
			"Name": self.getName(),
			"Parent": self.getParent()
		}
		return json.dumps(output)