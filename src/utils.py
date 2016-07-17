def time_function(f, *args, **kwargs):
      """
        Call a function f with args and kwargs and return the time (in seconds) that it
        took to execute.
      """

      import time
      tic = time.time()
      f(*args, **kwargs)
      toc = time.time()

      return time.time() - tic

if __name__ == "__main__":
    def f(lst):
        """
            f(lst): return map(lambda x: x^2, lst)
        """
        return map(lambda x: x^2, lst)

    l = range(10)
    print "list: ", l
    print "func to time: ", f.__doc__
    print "Time to complete function: ", time_function(f, l)

