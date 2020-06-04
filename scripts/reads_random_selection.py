import argparse
# Create arguments for command line
parser = argparse.ArgumentParser(description="Fastq filtering")
# Filtering too short reads
parser.add_argument('--min_length', help="minimal length of read",
                    dest="min_length", type=int, action="store", default=1)
# A number how many times we would like to reduce our library
parser.add_argument('--reduce-level', help="integer how many times reduce reads number", nargs=1, type=int,
                    action="store", dest="reduce_level", default=10)
# Name for output
parser.add_argument('--output_base_name', help="common name`s start for output files",
                    action="store", dest='output_base_name')
# Set a random number for generator
parser.add_argument('--set_seed', dest="seed", action="store", help = "set seeds for random generation")
# File that we would like to filtered and reduce
parser.add_argument("file", help="fastq file")

args = parser.parse_args()

from random import randint as randint
import random
# set a random number
random.seed(args.seed)

#function for filtering too short reads
def min_len(seq):
    if len(seq) >= args.min_length:
        return True
    else:
        return False

# function that decided safe sequence or not
def checking_parametrs(name_s, seq, rev_name, rev_seq):
    if args.output_base_name:
        output_name = args.output_base_name
    else:
        o_n = args.file.split('.')
        output_name = o_n[0]
    if min_len(seq):
        if randint(0, (args.reduce_level[0]*10000000+1)) % args.reduce_level[0] == 0:
            output_name = output_name + "_passed.fasta"
            with open(output_name, 'a') as output:
                output.write(name_s + '\r\n')
                output.write(seq + '\r\n')
                output.write(rev_name + '\r\n')
                output.write(rev_seq + '\r\n')
        return

#open fasta file
with open(args.file, "r") as in_f:
    for element in in_f:
        name_s = element.rstrip('\n')  # 1
        seq = next(in_f).rstrip('\n')  # 2
        rev_name = next(in_f).rstrip('\n') #3
        rev_seq = next(in_f).rstrip('\n') #4
        checking_parametrs(name_s, seq, rev_name, rev_seq)