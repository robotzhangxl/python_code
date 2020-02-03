import sys
import test_case
import numpy as np
from ctypes import *
import robot


def main():
    print('this message is from main function')

    r = robot.createRobotInstance(b"TestRobot").contents
    r.setRobotConfig(88, 99)
    r.move()

    # np.test()
    # test_case.ctypes_test()
    # test_case.module_class_test()
    # test_case.time_test()
    # test_case.list_test()
    # test_case.tuple_test()
    # test_case.dictory_test()
    # test_case.fibonacci_test(1,2)
    pass
    return


if __name__ == '__main__':
    print("name  is main")
    main()
