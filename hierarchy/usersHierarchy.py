from . import role, user
import logging
from dataclasses import dataclass

@dataclass
class Hierarchy:
	"""
	A class for setting users hierarchy (i.e. connection between user and role)
	"""

	roles: list = None
	users: list = None


	def setRoles(self, roles):
		"""
		Setter for roles. Convert json to list of role obejcts.
		"""
		role_objs = []
		for role_elem in roles:
			role_obj = role.Role(id=role_elem['Id'], name=role_elem['Name'], parent=role_elem['Parent'])
			role_objs.append(role_obj)
		self.roles = role_objs


	def setUsers(self, users):
		"""
		Setter for users. Convert json to list of user obejcts.
		"""
		user_objs = []
		for user_elem in users:
			user_obj = user.User(id=user_elem['Id'], name=user_elem['Name'], role=user_elem['Role'])
			user_objs.append(user_obj)
		self.users = user_objs


	def findChild(self, user_id):
		"""
		Find hierarchy between roles and users. Return a list of matched user objects.
		"""
		user_objs = []
		# find child role
		for user_obj in self.users:
			if user_id == user_obj.getId():
				role_id = user_obj.getRole()
				children_roles = []

				for role_obj in self.roles:
					if role_obj.getParent() == role_id:
						children_roles.append(role_obj.getId())

		# find users belongs to the child roles
		for user_obj in self.users:
			if user_obj.getRole() in children_roles:
				user_objs.append(user_obj)

		all_arr = user_objs
		for user_obj in user_objs:
			arr = self.findChild(user_obj.getId())
			for one in arr:
				if one not in all_arr:
					all_arr.append(one)

		return all_arr


	def getSubOrdinates(self, user_id):
		"""
		Convert hierarchy result from list of user objects to list of dicts
		"""
		user_objs = self.findChild(user_id)
		user_objs = [user_obj.objtToDict() for user_obj in user_objs]
		
		return user_objs
