import sys;
import test_case;
import numpy as np
from ctypes import *


# class mytype(Structure):
#     _fields_ = [("number", c_int32),
#                 ("longnum", c_long),
#                 ("art", c_char),


def main():

    print('this message is from main function')

    dll = cdll.LoadLibrary("D:\Project\Repos\libtest\out\LIBTEST.dll")
    print(dll.add(1,2))
    #dll.show()

    createRobotConfig = dll.createRobotConfig
    createRobotConfig.argtypes = [c_double,c_double,c_double]
    L1 = c_double(1.6)
    L2 = c_double(2.8)
    L3 = c_double(3.9)
    createRobotConfig(L1,L2,L3)
    dll.fibonacci_init(1,1)
    #Write out the sequence values until overflow.
    for i in range(1,10):
        print(dll.fibonacci_index(),": ",dll.fibonacci_current())
        dll.fibonacci_next()



    #libtest = CDLL('libtest.pyd')
    #print(libtest)
    #libtest = cdll.libtest
    #np.test()
    # test_case.ctypes_test()
    # test_case.module_class_test()
    # test_case.time_test()
    # test_case.list_test()
    # test_case.tuple_test()
    # test_case.dictory_test()
    pass
    return

if __name__ == '__main__':
    print("name  is main")
    main()



