#!/usr/bin/env python3  # Use Python 3 interpreter to run this script
import sys  # Import sys module to access command-line arguments

# Define valid ranges for each cron field
RANGES = {
    "minute": (0, 59),
    "hour": (0, 23),
    "day": (1, 31),
    "month": (1, 12),
    "weekday": (0, 6),
}

# Function to expand a cron field expression into a list of values
def expand(expr, field):
    start, end = RANGES[field]  # Get valid range for the field
    if expr == "*":  # '*' means all possible values in the range
        return list(range(start, end + 1))
    
    vals = set()  # Use a set to avoid duplicate values
    for part in expr.split(","):  # Split expression by comma for multiple values
        if part.startswith("*/"):  # Handle step values like '*/15'
            step = int(part[2:])
            vals.update(range(start, end + 1, step))  # Add values with step
        elif "-" in part:  # Handle ranges like '5-10'
            s, e = map(int, part.split("-"))
            vals.update(range(s, e + 1))  # Add all numbers in range
        else:  # Single numeric value
            vals.add(int(part))
    return sorted(vals)  # Return sorted list of values

# Function to parse a full cron expression
def parse(expr):
    m, h, d, mo, w, cmd = expr.split(maxsplit=5)  # Split into 6 parts (minute, hour, day, month, weekday, command)
    # Expand each field using the expand function
    data = {f: expand(v, f) for f, v in zip(["minute","hour","day","month","weekday"], [m,h,d,mo,w])}
    data["command"] = cmd  # Store the command separately
    return data  # Return parsed data as dictionary

# Function to display parsed cron fields in readable format
def show(data):
    for k in ["minute","hour","day","month","weekday"]:  # Iterate through fields
        print(f"{k:<8}{' '.join(map(str, data[k]))}")  # Print field name and its values
    print(f"command {data['command']}")  # Print the command

# Main entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:  # Ensure exactly one argument is provided
        print('Usage: cron_parser.py "<cron expression>"')  # Print usage message
        sys.exit(1)  # Exit with error code 1
    show(parse(sys.argv[1]))  # Parse and display the cron expression
