"""
Problem Statement:

You are given a list of bus departure times as strings in "HH:MM" 24-hour format (e.g., ["08:00", "09:15", "10:30"]) and a current time in the same format (e.g., "10:00"). 
Find the most recent bus departure time that occurred before the current time and return the number of minutes that have elapsed since that departure until the current time.

Assumptions:
- All times are on the same day (no midnight wrap-around).
- The departure list may not be sorted.
- There is at least one departure before the current time; if not, the function raises a ValueError.
- Times are valid and properly formatted.

Example:
departures = ["08:00", "09:15", "10:30", "11:45"]
current_time = "10:00"
Output: 45  (since last departure was at 09:15, and 10:00 - 09:15 = 45 minutes)
"""

def minutes_since_last_departure(departures, current_time):
    def to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    current_min = to_minutes(current_time)
    max_dep_min = -1  # Sentinel for no valid departure
    
    for dep in departures:
        dep_min = to_minutes(dep)
        if dep_min < current_min:
            max_dep_min = max(max_dep_min, dep_min)
    
    if max_dep_min == -1:
        raise ValueError("No departures before current time")
    
    return current_min - max_dep_min

# Example usage (for testing):
if __name__ == "__main__":
    departures = ["08:00", "09:15", "10:30", "11:45"]
    current_time = "10:00"
    result = minutes_since_last_departure(departures, current_time)
    print(result)  # Output: 45
