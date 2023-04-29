import threading
import csv

class PrimeFinder(threading.Thread):
    """A class that generates prime numbers in a given range using multithreading"""
    def __init__(self, start, end, numbers_list):
        threading.Thread.__init__(self)
        self.start = start
        self.end = end
        self.list = numbers_list

    def run(self):
        for num in range(self.start, self.end + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    self.list.append(num)
        
        with open('primes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.primes)