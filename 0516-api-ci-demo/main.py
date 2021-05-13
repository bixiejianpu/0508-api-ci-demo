import pytest
from command_line import operation


def run():
    opt = operation()
    print(opt)
    project_name = opt.get("project")
    if project_name is None:
        print("project_name can not be None")
        exit(-1)
    start_command = [project_name]
    pytest.main(start_command)


if __name__ == "__main__":
    run()