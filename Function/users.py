import json
from dataclasses import dataclass

@dataclass
class Users:
	"""
	A class for Users
	"""

	id: int
	name: str
	role: int


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


   	def getRole(self):
   		"""
   		Getter for role
   		"""
   		return self.role


   	def __str__(self):
   		"""
   		Overide the output with string json format
   		"""
   		output = {
   			"Id": getId,
   			"Name": getName,
   			"Role": getParent
   		}

   		return json.dumps(output)