from datetime import datetime
date="Aug 13 2001 9:45AM"
date_time=datetime.strptime(date,"%b %d %Y %I:%M%p")
print(date_time)