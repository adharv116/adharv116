import argparse
import csv

def main():

    parser = argparse.ArgumentParser(description="Calculate statistics for unemployment rates")
    parser.add_argument("input_file", help="Input CSV file containing unemployment data")
    parser.add_argument("--country", required=True, help="Country to perform the operation for")
    parser.add_argument("-o", choices=['avg', 'min', 'max'], default='avg', help="Operation to perform on rates (default: avg)")
    parser.add_argument("--from", dest="from_year", type=int, help="Starting year (inclusive)")
    parser.add_argument("--to", dest="to_year", type=int, help="Ending year (inclusive)")
    args = parser.parse_args()

    total_rate = 0
    count = 0
    min_rate = float('inf')
    max_rate = float('-inf')

    with open(args.input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            country, _, year, rate = row
            if country == args.country:
                year = int(year)
                if (not args.from_year or year >= args.from_year) and (not args.to_year or year <= args.to_year):
                    rate = float(rate)
                    total_rate += rate
                    count += 1
                    min_rate = min(min_rate, rate)
                    max_rate = max(max_rate, rate)

    if count > 0:
        if args.o == 'avg':
            result = total_rate / count
            message = f"Average for all years for {args.country}: {result}"
        elif args.o == 'min':
            result = min_rate
            if args.from_year and args.to_year:
                message = f"Minimum for years between {args.from_year} and {args.to_year} for {args.country}: {result}"
            else:
                message = f"Minimum for all years for {args.country}: {result}"
        elif args.o == 'max':
            result = max_rate
            if args.from_year and args.to_year:
                message = f"Maximum for years between {args.from_year} and {args.to_year} for {args.country}: {result}"
            else:
                message = f"Maximum for all years for {args.country}: {result}"
        print(message)
    else:
        print(f"No data available for {args.country} in the specified date range.")

if __name__ == "__main__":
    main()
