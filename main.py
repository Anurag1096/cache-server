#This is the main server file which will be started by cli at user specified port and url
#Then it will cache the data coming at that url into the cache server.
from cache import set_cache,get_cache,clear_cache
from fastapi import FastAPI,Request,Response
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx

app = FastAPI()

allowed_origin = os.getenv("ALLOWED_ORIGIN", "").rstrip("/")

app.add_middleware(
CORSMiddleware,
allow_origins=[allowed_origin],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"]
)


@app.api_route("{path:path}",methods=["GET"])
async def proxy(path:str, request:Request):
    
    query=request.url.query
    full_path= f"/{path}?{query}" if query else f"{path}"
    cache_key=f"{request.method}:{full_path}"
   
    cached= get_cache(cache_key)
    if cached:
        return Response(
            content=cached['content'],
            status_code=200,
            media_type='application/json',
            headers={"X-Cache":"HIT"}
        )
        
    #Now to add it to cache map
    target_url = f"{allowed_origin}{path}"
   
    if query:
        target_url += f'?{query}'
    
    
    # Now to forward the request to the proxy server
    
    async with httpx.AsyncClient(follow_redirects=True) as client:
        origin_response=await client.request(method=request.method, url=target_url)
        
    
    set_cache(
        cache_key,{'content':origin_response.content}
    )
        
    return Response(
        content=origin_response.content,
        status_code=origin_response.status_code,
        headers={"X-Cache":"MISS"},
        media_type=origin_response.headers.get("content-type","application/json")
    )
            