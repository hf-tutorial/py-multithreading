import single_thread_crawler
from model import UrlList
import threading
from timeit import timeit


@timeit
def single_thread():
    for each in UrlList:
        single_thread_crawler.craw(each)

@timeit
def multi_thread():
    threads = []
    for url in UrlList:
        threads.append(
            threading.Thread(target=single_thread_crawler.craw, args=(url,))
        )

    for each in threads:
        each.start()

    for each in threads:
        each.join()


if __name__ == "__main__":
    single_thread()
    multi_thread()