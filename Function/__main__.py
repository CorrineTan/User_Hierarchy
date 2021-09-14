import user, role, usersHierarchy
from user import User
from role import Role
import json
from pathlib import Path
import sys
import argparse

def load_roles_config(args):
	roles_config = None
	try:
		config_path = Path(args.roles).resolve(strict=True)
		with open(config_path) as json_file:
			roles_config = json.load(json_file)
	except FileNotFoundError:
		print(f"\n\nTable config file could not be found: {args.roles}")
		parser.print_help(sys.stderr)
		sys.exit(2)
	return roles_config

def load_users_config(args):
	users_config = None
	try:
		config_path = Path(args.users).resolve(strict=True)
		with open(config_path) as json_file:
			users_config = json.load(json_file)
	except FileNotFoundError:
		print(f"\n\nTable config file could not be found: {args.users}")
		parser.print_help(sys.stderr)
		sys.exit(2)
	return users_config

def process(args):
	roles = load_roles_config(args)
	users = load_users_config(args)

	hierarchy = usersHierarchy.Hierarchy()

	hierarchy.setRoles(roles)
	hierarchy.setUsers(users)

	return hierarchy

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-r",
		"--roles",
		help="the path to the roles json file",
	)
	parser.add_argument(
		"-u",
		"--users",
		help="the path to the users json file",
	)    
	args = parser.parse_args()

	hierarchy = process(args)


	print("Hierarchy for User 3: ")
	res = hierarchy.getSubOrdinates(3)
	print(res)

	print("Hierarchy for User 1: ")
	res = hierarchy.getSubOrdinates(1)
	print(res)

	print("Hierarchy for User 1: ")
	res = hierarchy.getSubOrdinates(5)
	print(res)
