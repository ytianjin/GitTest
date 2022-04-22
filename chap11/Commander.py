# 带标识值的武将类 

class Commander:
    """武将类"""

    __counter = 0   # 赋予的最后一个标识值是多少

    def __init__(self, name: str) -> None:
        """构造函数"""
        self.__name = name
        Commander.__counter += 1
        self.__id = Commander.__counter

    def id(self) -> int:
        """"获取标识值"""
        return self.__id

    @classmethod
    def max_id(cls) -> int:
        """"当前赋予的最后一个标识值"""
        return cls.__counter

    def print(self) -> None:
        """打印输出数据"""
        print('{}:标识值是{}'.format(self.__name, self.__id))

oda = Commander('织田信长')      # 标识值为1 
toyotomi = Commander('丰臣秀吉') # 标识值为2 
tokugawa = Commander('德川家康') # 标识值为3 

print('oda.id() = {}'.format(oda.id()))
print('toyotomi.id() = {}'.format(toyotomi.id()))
print('tokugawa.id() = {}'.format(tokugawa.id()))

print('Commander.max_id() = {}'.format(Commander.max_id()))
print('oda.max_id() = {}'.format(oda.max_id()))
