import getopt
import sys


def operation():
    try:
        option, args = getopt.getopt(sys.argv[1:], ":p", ["project"])
    except getopt.GetoptError as e:
        print("not support the arg:" + str(e))
        exit(0)
    else:
        return create_operation(option)


def create_operation(options):
    operation_dict = {}
    try:
        for k,v in options:
            if k in ("-p", "--project"):
                operation_dict["project"] = v
    except Exception as e:
        print("do not support arg: " + str(e))
    return operation_dict
