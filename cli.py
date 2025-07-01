import argparse
import uvicorn
import os



def start():
    parser = argparse.ArgumentParser(description="A script that processes command-line arguments.")
    parser.add_argument('--port',type=int, required=True,help="Enter the port you want to listen")
    parser.add_argument('--origin',type=str,required=True, help="Enter the url you want to cache")
    args=parser.parse_args()
    os.environ['ALLOWED_ORIGIN'] =args.origin
    
    if  not args.orign:
        raise ReferenceError("Origin is required for the cache server to work")
    if not args.port:
        raise ReferenceError("Port is required for the cache server to work")

# now we pass the args to the server 
    uvicorn.run("main:app",  port=args.port, reload=True)


if __name__== "__main__":
    start()
