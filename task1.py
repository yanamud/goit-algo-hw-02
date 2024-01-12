from queue import Queue
import random

#Створити чергу заявок
queue = Queue()

def generate_request():
        item = random.randint(1, 100)
        queue.put(item)
        print(f"створено заяку: {item}")

def process_request():
    if queue.empty() == False:
        el = queue.get()
        print(f'Заяка {el} прийнята в роботу')
    else:
        print(f'Всі заявки оброблено')


user_input = input("Бажаєте створити нову заявку(y/n): ")

while user_input == 'y':
    generate_request()
    process_request()
    user_input = input("Бажаєте створити нову заявку(y/n): ")
else:
    print(F'Всього завок в роботі: {queue.qsize()}')


