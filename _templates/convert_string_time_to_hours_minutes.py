def convert_time_to_minutes(time: str):
   hours, minutes = map(int, time.split(':'))
   return hours, minutes
