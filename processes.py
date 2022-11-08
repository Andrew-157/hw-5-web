from multiprocessing import Pool
import os
from time import time, sleep


def factorize(*number):

    to_return = []

    for num in number:
        inner_list = []
        for div_num in range(1, num+1):
            if num % div_num == 0:
                inner_list.append(div_num)
        to_return.append(inner_list)
    sleep(1)
    return to_return


if __name__ == "__main__":
    start = time()
    with Pool(4) as pool:
        results = pool.map(factorize, (128, 255, 99999, 10651060))
    finish = time()
    a = results[0][0]
    b = results[1][0]
    c = results[2][0]
    d = results[3][0]
    print(finish - start)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
