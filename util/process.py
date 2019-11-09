import sys

def get_command_prop(prop: str) -> str:
    result = list(filter(lambda element: prop in  element ,sys.argv))
    return result[0] if len(result) > 0 else None
