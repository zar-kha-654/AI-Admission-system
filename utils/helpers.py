import json


def format_programs(programs):
    return json.dumps(programs, indent=2)


def format_student(student):
    return json.dumps(student, indent=2)
