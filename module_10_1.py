import threading
import time


def write_words(word_count, file_name):
    i = 1
    while i != word_count + 1:
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"Какое-то слово №{i}\n")
            time.sleep(0.1)
            i += 1
    print(f"Завершилась запись в файл {file_name}")
start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Время работы потоков: {elapsed_time}')

start_time_2 = time.time()

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_1.start()

thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_2.start()

thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_4.start()

thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_3.start()
thread_3.join()



end_time_2 = time.time()
elapsed_time_2 = end_time_2 - start_time_2
print(f'Время работы потоков: {elapsed_time_2}')
