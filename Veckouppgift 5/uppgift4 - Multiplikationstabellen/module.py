
def muliplication_table(n, limit):
    if not isinstance(n, int):
        raise TypeError(f"muliplication_table: parameter n '{n}' is of type '{type(n)}' instead of 'int'")
    
    if not isinstance(limit, int):
        raise TypeError(f"muliplication_table: parameter limit '{limit}' is of type '{type(limit)}' instead of 'int'")
    
    if limit <= 0:
        return None
    return [n*(i+1) for i in range(limit)]
