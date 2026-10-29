import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sem = threading.Semaphore(1)
        self.bar_sem = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.foo_sem.acquire()
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.bar_sem.acquire()
            printBar()
            self.foo_sem.release()