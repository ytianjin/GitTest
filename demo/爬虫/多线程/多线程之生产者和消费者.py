from json.tool import main
import threading,random

# 定义银行存款
g_money = 1000
g_times = 0

lock = threading.Lock
# 定义生产者
class Productor(threading.Thread):
    def run(self):
        global g_money
        global g_times
        while True:
            
            lock.acquire()
            if g_times > 10:
                lock.release()
                break
            money = random.randint(100,1000)
            g_money += money
            g_times += 1
            print('{}谁挣了{}钱'.format(threading.current_thread(), money))
            lock.release()

# 定义消费者者
class Consumer(threading.Thread):
    def run(self):
        global g_money
        global g_times
        while True:
            lock.acquire()
            money = random.randint(100,1000)
            if g_money >= money:
                g_money -= money
                print('{}消费{}块钱,还剩{}块钱'.format(threading.current_thread(),money,g_money))
            else:
                if g_times > 10:
                    lock.release()
                    break
                print('{}谁准备消费{},余额不足'.format(threading.current_thread(),money))
            lock.release()

if __name__ == '__main__':
    # 定义三个生产者
    for i in range(3):
        # 实例化对象
        p = Productor()
        p.start()
    # 定义五个消费者者
    for j in range(3):
        c = Consumer()
        c.start()
    pass