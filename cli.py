import argparse


parser = argparse.ArgumentParser(description="A script that processes command-line arguments.")


parser.add_argument('--port',type=int, required=True,help="Enter the port you want to listen")

parser.add_argument('--origin',type=str,required=True, help="Enter the url you want to cache")

args=parser.parse_args()


# now we pass the args to the server 