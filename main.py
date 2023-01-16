from utils import create_json
import argparse

#Example: python main.py --input=data_1 --output=output
 
# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument('--input', type=str, required=True)
parser.add_argument('--output', type=str, required=True)

args = parser.parse_args()





create_json(args.input, args.output)
