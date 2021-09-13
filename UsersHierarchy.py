# use bfs to to solve this problem
# the eligible roll and user will be removed from the rolls and users, improving program efficiency
import copy


class UsersHierarchy(object):
    def __init__(self):
        self.roles = None
        self.users = None

    def setRoles(self, roles):
        self.roles = roles

    def setUsers(self, users):
        self.users = users

    def getSubOrdinates(self, user_id):
        result = []
        users = copy.deepcopy(self.users)
        roles = copy.deepcopy(self.roles)
        for user in users:
            if user_id == user["Id"]:
                role_id = user["Role"]
                stack = [role_id]
                while len(stack) != 0:
                    role_id = stack.pop(0)
                    # Traversal in reverse order to remove eligible data
                    for i in range(len(roles) - 1, -1, -1):
                        role = roles[i]
                        if role["Parent"] == role_id:
                            stack.append(role["Id"])
                            roles.remove(role)
                            # Traversal in reverse order to remove eligible data
                            for j in range(len(users) - 1, -1, -1):
                                user = users[j]
                                if user["Role"] == role["Id"]:
                                    result.append(user)
                                    users.remove(user)
    return result
