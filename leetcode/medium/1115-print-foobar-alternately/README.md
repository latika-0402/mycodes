# Print FooBar Alternately

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Suppose you are given the following code:

```
class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}

```

The same instance of `FooBar` will be passed to two different threads:

- thread A will call foo(), while
- thread B will call bar().

Modify the given program to output `"foobar"` `n` times.

 

 **Example 1:** 

```
Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.

```

 **Example 2:** 

```
Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.

```

 

 **Constraints:** 

- 1 <= n <= 1000

## Solution

**Language:** Python  
**Runtime:** 86 ms (beats 35.06%)  
**Memory:** 19.8 MB (beats 75.86%)  
**Submitted:** 2026-10-29T02:49:26.527Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/print-foobar-alternately/)