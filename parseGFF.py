import argparse

def get_args():
    #create an argumentparser object
    parser= argparse.ArgumentParser(description='This script return the two fileand read line by line')
    #making three functions for getting input, calculating fibonacci and printing:
    #add positional arguments(these are the ones that are absoultely essential/required)
    parser.add_argument("filegff", help= "the gff file you want to open")
    parser.add_argument("filefasta", help= "the fasta file you want to open")
    args= parser.parse_args()
    return args
def main():
    args = get_args()

    with open(args.filegff, "r") as filegff:
        for line in filegff:
            line = line.strip()  # Strip newlines
            parts = line.split('\t')  # Split the line into columns based on tabs
            # Extract the start and end positions
            start = int(parts[3])
            end = int(parts[4])
            feature_length = end - start + 1  # Calculate feature length
            print(f'Feature Length: {feature_length}')  # Print the length of the feature

    # Open the FASTA file
    with open(args.filefasta, "r") as filefasta:
        pass

if __name__ == "__main__":
    main()