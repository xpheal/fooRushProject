#!/usr/bin/env python3
import csv
import sys

def main():
	with open(sys.argv[1], 'r') as in_f:
		with open(sys.argv[2], 'w') as out_f:
			csv_r = csv.reader(in_f)
			csv_w = csv.writer(out_f)
			id_p = -1
			for row in csv_r:
				if id_p == -1:
					csv_w.writerow(["id"] + row)
					id_p = id_p + 1
				else:
					csv_w.writerow([id_p] + row)
					id_p = id_p + 1



if __name__ == '__main__':
	main()
