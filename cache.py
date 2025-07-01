cache_store={}

def set_cache(key:str,value:dict):
    # set cache in the cache store obj
    cache_store[key]=value
    print("cache is set")
    return 

def get_cache(key):
    # retrive the stored cache
    return cache_store.get(key)

def clear_cache():
    print("cache Cleared")
    cache_store.clear()
    return
