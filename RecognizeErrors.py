import re

MAX_VAR_NAME_LENGTH = 79

snake_case_regex = re.compile(r'^[a-z_][a-z0-9_]*$')
upper_snake_regex = re.compile(r'^[A-Z][A-Z0-9_]*$')


def recognizeErrors(list):
    returnList = []
    for item in list:
        name = item["name"]
        scope = item["scope"]
        line = item["line"]
        core_name = name.lstrip("_")

        if scope == "local":
            if "global" in name.lower():
                returnList.append({
                    "name": name,
                    "line": line,
                    "scope": scope,
                    "issue": "Suspicious: name includes 'global', but is local"
                })
            elif len(core_name) > 1 and not core_name.islower():
                if any(c.isupper() for c in core_name[1:]):
                    returnList.append({
                        "name": name,
                        "line": line,
                        "scope": scope,
                        "issue": "Naming Violation: Use snake_case"
                    })
        else:
            if not upper_snake_regex.match(name):
                returnList.append({
                    "name": name,
                    "line": line,
                    "scope": scope,
                    "issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES"
                })
        if len(name) > MAX_VAR_NAME_LENGTH:
            returnList.append({
                    "name": name,
                    "line": line,
                    "scope": scope,
                    "issue": "Naming Violation: Variable name too long"
            })
    return returnList
