#!/usr/bin/python
'''
this script is used to run commands in parallel

'''

import pp
import os
import argparse

def main():
   commandInput=raw_input('Specify the input text containing all the commands : ')
   mainTwo(commandInput)

def mainTwo(commandInput):
   f=open(commandInput,'r')
   commandText=f.readlines()
   print len(commandText)



   ppservers=()
   parallel=pp.Server()
   toDo=[]
   for line in commandText:
       toDo.append(line.split('\n')[0])

   jobs=[(item,parallel.submit(run,(item,),(),("os",))) for item in toDo]
   for item,job in jobs:
       print item
       job()


def run(toDo):
   print os.popen(toDo).read()

if __name__=='__main__':
   argparser = argparse.ArgumentParser(prog='parallel_Kevin.py',
   formatter_class=argparse.RawDescriptionHelpFormatter,
   description='''\
When this script is ran without argument,
it will ask you for the input file which contains the list of commands
you want to run in parallel

''',epilog="Kevin Cho 2013_03_23")
   argparser.add_argument("--command", "-c",nargs=1,
           help='''
           Specify the text file containing the commands
           that you want to run.
           Each command should be separated by a line.
           eg.
           parallel_Kevin.py -c commandList.txt
           parallel_Kevin.py --command commandList.txt
           ''')
   args = argparser.parse_args()
   if args.command:
       print args.command
       mainTwo(''.join(args.command))
   if not args.command:
       main()
