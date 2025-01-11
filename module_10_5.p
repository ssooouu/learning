import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while file.readline() != '':
            all_data.append(file.readline())



start_time = time.time()
filenames = [f'file {number}.txt' for number in range(1, 5)]

for i in filenames:
    read_info(i)

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Время работы: {elapsed_time}')

if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(5) as p:
        p.map(read_info, ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt'])
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Время работы: {elapsed_time}')
