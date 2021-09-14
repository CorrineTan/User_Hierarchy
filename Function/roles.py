import json
from dataclasses import dataclass

@dataclass
class Roles:
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
   			"Id": getId,
   			"Name": getName,
   			"Parent": getParent
   		}

   		return json.dumps(output)