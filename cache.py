cache_store={}

def set_cache(args):
    # set cache in the cache store obj
    print("cache is set")
    return

def get_cache(args):
    # retrive the stored cache
    if not cache_store[args]:
        print("cache Miss")
        return
    return cache_store[args]

def clear_cache():
    print("cache Cleared")
    cache_store={}
    return
