import argparse
import csv
from Bio import SeqIO
from Bio.Seq import Seq

def get_args():
    #create an argumentparser object
    parser= argparse.ArgumentParser(description='This script parses and does some \
        neat stuff with a GFF file')
    parser.add_argument("gff", help="name of gff file")
    parser.add_argument("fasta", help= "name of fasta file")
    return parser.parse_args()

    

def parse_fasta():
    #read and parse the FASTA file
    #read() assumes one seq only in the fasta file
    return SeqIO.read(args.fasta, 'fasta')
def revcomp(seq):
    return seq.reverse_compliment()

def parse_gff(genome_object):
    genome_sequence= genome_object.seq

    #read the gff file line by line
    with open(args.gff, 'r') as gff_file:
        #create a csv csv reader object 
        reader= csv.reader(gff_file, delimiter="\t")
        #read the actual lines
        for line in reader:
            organism        = line[0]
            feature_type    = line[2]
            start           = int(line[3])
            end             = int(line[4])
            strand          = line[6]
            attributes      = line[-1]
            if feature_type == 'CDS':
                print(feature_type)
                #extract the sequence of this feature from the genome
                feature_seq= genome_sequence [start-1:end]
                if strand == '-':
                    feature_seq= revcomp(feature_seq)
                #print fasta nucleotide sequence for this gene 
                #print(len(feature_seq))

def main():
    genome_sequence= parse_fasta()
    parse_gff(genome_sequence)



#get the command line arguments
args= get_args()


#set the env for this script
if __name__ == "__main__":
    main()