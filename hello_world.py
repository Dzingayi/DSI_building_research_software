import argparse 
 
parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('name')
parser.add_argument('-r', type=int, default=1)
args = parser.parse_args()
 
for _ in range(args.r):
  print('Hello ' + args.name + '!')