import json
from dataclasses import dataclass

@dataclass
class User:
	"""
	A class for Users
	"""

	id: int
	name: str
	role: int


	def getId(self):
		return self.id


	def getName(self):
		"""
		Getter for name
		"""
		return self.name


	def getRole(self):
		"""
		Getter for role
		"""
		return self.role


	def __str__(self):
		"""
		Overider the output with string json format
		"""
		output = {
			"Id": self.getId(),
			"Name": self.getName(),
			"Role": self.getRole()
		}
		return json.dumps(output)


	def objtToDict(self):
		"""
		Convert object to dict
		"""
		output = {
			"Id": self.getId(),
			"Name": self.getName(),
			"Role": self.getRole()
		}
		return output
		