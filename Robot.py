from ctypes import *


class NRC_RobotDHConfig(Structure):
    _fields_ = [("L1", c_double),
                ("L2", c_double),
                ("L3", c_double),
                ("L4", c_double),
                ("L5", c_double),
                ("L6", c_double),
                ("L7", c_double),
                ("theta", c_double),  # <5轴方向，仅对六轴机器人有效，参数可选：0、90
                ("CoupleCoe12", c_double),  # <1/2轴耦合比
                ("CoupleCoe23", c_double),  # <2/3轴耦合比
                ("CoupleCoe32", c_double),  # <3/2轴耦合比
                ("CoupleCoe45", c_double),  # <3/4轴耦合比
                ("CoupleCoe46", c_double),  # <4/5轴耦合比
                ("CoupleCoe56", c_double)  # <5/6轴耦合比
                ]


def createRobotInstance(name):
    dll = cdll.LoadLibrary("D:\Project\Repos\libtest\out\LIBTEST.dll")
    cr = dll.createRobot
    cr.restype = POINTER(Robot)
    return cr(name)


class Robot(Structure):
    _fields_ = [("id", c_double),
                ("name", c_wchar_p),
                ("dhConfig", POINTER(NRC_RobotDHConfig))]

    dh_config = NRC_RobotDHConfig(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    name = 'nobody'

    def __init__(self, n="nobody"):
        super(Robot, self).__init__()
        print(b"robot create")
        self.name = n
        self.dll = cdll.LoadLibrary("D:\Project\Repos\libtest\out\LIBTEST.dll")

    def setRobotConfig(self, L1, L2):
        self.dll = cdll.LoadLibrary("D:\Project\Repos\libtest\out\LIBTEST.dll")
        createRobotConfig = self.dll.createRobotConfig
        createRobotConfig.argtypes = [c_double, c_double, c_double]
        createRobotConfig.restype = NRC_RobotDHConfig
        L1 = c_double(L1)
        L2 = c_double(L2)
        L3 = c_double(3.9)
        config = createRobotConfig(L1, L2, L3)
        self.dll.setRobotConfig(byref(self),config)

    # def createRobot(self, n):
    #     cr = self.dll.createRobot
    #     cr.restype = POINTER(Robot)
    #     a = cr(n)
    #     print(a.contents)
    #     b = a.contents
    #     print(b.name)
    #     print(b)
    def move(self):
        self.dll.move()