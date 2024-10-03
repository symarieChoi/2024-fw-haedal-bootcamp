from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))

seoul_time = datetime.now(KST)

print(seoul_time.strftime("%Y-%m-%d"))