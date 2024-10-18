from datetime import datetime, timezone

# Get current time in UTC
current_time_utc = datetime.now(timezone.utc)
dtstamp = current_time_utc.strftime('%Y%m%dT%H%M%SZ')

print(f'DTSTAMP:{dtstamp}')