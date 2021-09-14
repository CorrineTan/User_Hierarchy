from . import users, roles, usersHierarchy
import logging
import json
from pathlib import Path

def load_roles_config(args):
	roles_config = None
	try:
		config_path = Path(args.roles).resolve(strict=True)
		with open(config_path) as json_file:
			roles_config = json.load(json_file)
	except FileNotFoundError:
		logging.error(f"\n\nTable config file could not be found: {args.roles}")
		parser.print_help(sys.stderr)
		sys.exit(2)
	return roles_config

def load_users_config(args):
	users_config = None
	try:
		config_path = Path(args.users).resolve(strict=True)
		with open(users_path) as json_file:
			users_config = json.load(json_file)
	except FileNotFoundError:
		logging.error(f"\n\nTable config file could not be found: {args.users}")
		parser.print_help(sys.stderr)
		sys.exit(2)
	return users_config

def main(args):
	roles = load_roles_config(args)
	users = load_roles_config(users)
	usersHierarchy.Hierarchy.setRoles(roles)
	usersHierarchy.Hierarchy.setUsers(users)

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

	logging.info("Hierarchy for User 3: ")
	usersHierarchy.Hierarchy.getSubOrdinates(3)

	logging.info("Hierarchy for User 1: ")
	usersHierarchy.Hierarchy.getSubOrdinates(1)
