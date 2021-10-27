import random

from threading import Thread, Barrier


LIST_LEN = random.randint(5, 10)

def find_end(idx):
    end[idx] = link[idx]
    pass
        

if __name__ == "__main__":
    link = list(range(1, LIST_LEN + 1))
    link[-1] = None
    end = [None] * LIST_LEN

    threads = [Thread(target=find_end, args=(idx,)) for idx in range(LIST_LEN)]

    print(end)

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

    print(end)



