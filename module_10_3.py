import threading
import random
import time

lock = threading.Lock()

class Bank():
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            random_num = random.randint(50, 500)
            self.balance += random_num
            print(f'Пополнение: {random_num}. Баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and lock.locked() == True:
                lock.release()


    def take(self):
        for i in range(100):
            random_num = random.randint(50, 500)
            print(f"Запрос на {random_num}")
            if self.balance >= random_num:
                self.balance -= random_num
                print(f"Снятие: {random_num}. Баланс: {self.balance}")
                time.sleep(0.001)
            else:
                print("Запрос отклонён, недостаточно средств")
                lock.locked()
                time.sleep(0.001)



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
