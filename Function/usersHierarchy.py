import role, user
import logging
#from dataclassess import dataclass
from dataclasses import dataclass
import copy
from role import Role
from user import User
@dataclass
class Hierarchy:
    """
    A class for setting users hierarchy
    """

    roles: list = None
    users: list = None

    def setRoles(self, roles):
        role_objs = []
        for role in roles:
            role_obj = Role(id=role['Id'], name=role['Name'], parent=role['Parent'])
            role_objs.append(role_obj)
        self.roles = role_objs

    def setUsers(self, users):
        user_objs = []
        for user in users:
            user_obj = User(id=user['Id'], name=user['Name'], role=user['Role'])
            user_objs.append(user_obj)
        self.users = user_objs

    def find_children_user_by_userid(self, user_id):
        user_objs = []
        # find child role
        for user_obj in self.users:
            if user_id == user_obj.getId():
                role_id = user_obj.getRole()
                children_roles = []

                for role_obj in self.roles:
                    if role_obj.getParent() == role_id:
                        children_roles.append(role_obj.getId())

        # find users belongs to these child roles
        for user_obj in self.users:
            if user_obj.getRole() in children_roles:
                user_objs.append(user_obj)
        all_arr = user_objs

        for user_obj in user_objs:
            arr = self.find_children_user_by_userid(user_obj.getId())
            for one in arr:
                if one not in all_arr:
                    all_arr.append(one)

        return all_arr


    def getSubOrdinates(self, user_id):

        user_objs = self.find_children_user_by_userid(user_id)

        user_objs = [user_obj.obj_2_dic() for user_obj in user_objs]

        return user_objs

