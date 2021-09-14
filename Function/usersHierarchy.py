from . import roles, users
import logging
from dataclassess import dataclass

@dataclass
class Hierarchy:
    """
    A class for setting users hierarchy
    """

    roles: roles.Roles
    users: users.Users

    def setRoles(self, roles):
    """
    Setters for Roles
    ""H
        self.roles = roles

    def setUsers(self, users):
    """
    Setters for Users
    """
        self.users = users

    def getSubOrdinates(self, user_id):
    """
    Getter for subordinates for users
    """
        result = []
        users = copy.deepcopy(self.users)
        roles = copy.deepcopy(self.roles)
        for user in users:
            if user_id == user["Id"]:
                role_id = user["Role"]
                stack = [role_id]
                while len(stack) != 0:
                    role_id = stack.pop(0)
                    for i in range(len(roles) - 1, -1, -1):
                        role = roles[i]
                        if role["Parent"] == role_id:
                            stack.append(role["Id"])
                            roles.remove(role)
                            for j in range(len(users) - 1, -1, -1):
                                user = users[j]
                                if user["Role"] == role["Id"]:
                                    result.append(user)
                                    users.remove(user)
        return result
