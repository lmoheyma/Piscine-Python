def callLimit(limit: int):
    """
    This function takes an limiter in argument
    and return a decorator to limit the call's
    number of a function
    """
    count = 0

    def callLimiter(function):
        """
        Intern function created by 'callLimit'
        It's the decorator used to limit the call's number
        """
        def limit_function(*args: any, **kwds: any):
            """
            Intern function created by 'callLimiter' to survey
            the number of call, if the number of call is more than
            the 'limit', its raises an AssertionError
            """
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"Error: {function} call too \
many times")
            except Exception as e:
                print(e)
        return limit_function
    return callLimiter
