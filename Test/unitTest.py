from usersHierarchy import usersHierarchy
import pytest

roles = [
	{
		"Id": 1,
		"Name": "System Administrator",
		"Parent": 0
	},
	{
		"Id": 2,
		"Name": "Location Manager",
		"Parent": 1,
	},
	{
		"Id": 3,
		"Name": "Supervisor",
		"Parent": 2,
	},
	{
		"Id": 4,
		"Name": "Employee",
		"Parent": 3,
	},
	{
		"Id": 5,
		"Name": "Trainer",
		"Parent": 3,
	}
]
users = [
	{
		"Id": 1,
		"Name": "Adam Admin",
		"Role": 1
	},
	{
		"Id": 2,
		"Name": "Emily Employee",
		"Role": 4
	},
	{
		"Id": 3,
		"Name": "Sam Supervisor",
		"Role": 3
	},
	{
		"Id": 4,
		"Name": "Mary Manager",
		"Role": 2
	},
	{
		"Id": 5,
		"Name": "Steve Trainer",
		"Role": 5
	}
]
uh = usersHierarchy()
uh.setRoles(roles)
uh.setUsers(users)

def test_case1():
	got = [{'Id': 5, 'Name': 'Steve Trainer', 'Role': 5}, {'Id': 2, 'Name': 'Emily Employee', 'Role': 4}]
	assert (uh.getSubOrdinates(3) == got)


def test_case2():
	got = [{'Id': 4, 'Name': 'Mary Manager', 'Role': 2}, {'Id': 3, 'Name': 'Sam Supervisor', 'Role': 3},
		   {'Id': 5, 'Name': 'Steve Trainer', 'Role': 5}, {'Id': 2, 'Name': 'Emily Employee', 'Role': 4}]
	assert (uh.getSubOrdinates(1) == got)


if __name__ == '__main__':
	pytest.main(['unitTest.py', '-s'])
