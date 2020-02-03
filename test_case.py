import sys
import time  # 引入time模块
from robot import *
from ctypes import *
import platform


def module_class_test():
    """Module  test for robot class"""
    r = Robot('TR')
    print(r)
    return


def time_test():
    ticks = time.time()
    print("当前时间戳为:", ticks)

    return


def list_test():
    """list test"""
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday']
    print(days)  # 输出完整列表
    print(days[0])  # 输出列表的第一个元素
    print(days[1:3])  # 输出第二个至第三个元素
    print(days[2:])  # 输出从第三个开始至列表末尾的所有元素
    t = 'Thursday'
    if (t in days):
        print("变量  ", t, "在给定的列表中 list 中")
    else:
        print("1 - 变量", t, "不在给定的列表中 list 中")
    for l in days:  # 第一个实例
        print(l)
    return


def tuple_test():
    """tuple test. Read only"""
    tuple = ('runoob', 786, 2.23, 'john', 70.2)
    print(tuple)


def dictory_test():
    """dictory test """
    # dictionary的作用如同map
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"

    tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

    print(dict['one'])  # 输出键为'one' 的值
    print(dict[2])  # 输出键为 2 的值
    print(tinydict)  # 输出完整的字典
    print(tinydict.keys())  # 输出所有键
    print(tinydict.values())  # 输出所有值
    x = 'runoob'
    sys.stdout.write(x + '\n')


def ctypes_test():
    """ctypes usage test"""
    # 提取标准libc实现. 注意不同平台的调用方法
    if platform.system() == 'Windows':
        libc = cdll.LoadLibrary('msvcrt.dll')
    # libc = windll.LoadLibrary('msvcrt.dll')  # Windows only
    # libc = oledll.LoadLibrary('msvcrt.dll')  # Windows only
    # libc = pydll.LoadLibrary('msvcrt.dll')

    # libc = CDLL('msvcrt.dll')
    # libc = WinDLL('msvcrt.dll')  # Windows only
    # libc = OleDLL('msvcrt.dll')  # Windows only
    # libc = PyDLL('msvcrt.dll')
    elif platform.system() == 'Linux':
        libc = cdll.LoadLibrary('libc.so.6')
        # libc = pydll.LoadLibrary('libc.so.6')
        # libc = CDLL('libc.so.6')
        # libc = PyDLL('libc.so.6')
        # libc.argtypes = [c_char_p]
        # Python3的默认编码为unicode,需要加上encode
        libc.printf('Hello ctypes!\n'.encode())


# mylib = CDLL("libtest.so")
# add = mylib.add
# add.argtypes = [c_int, c_int]  # 参数类型，两个int（c_int是ctypes类型，见上表）
# add.restype = c_int # 返回值类型，int (c_int 是ctypes类型，见上表）
# sum = add(3, 6)


def fibonacci_test(first, second):
    mydll = cdll.LoadLibrary("D:\Project\Repos\libtest\out\LIBTEST.dll")
    # dll.show()
    print(mydll.add(first, second))
    mydll.fibonacci_init(first, second)
    # Write out the sequence values until overflow.
    for i in range(1, 10):
        print(mydll.fibonacci_index(), ": ", mydll.fibonacci_current())
    mydll.fibonacci_next()
