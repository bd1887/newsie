import datetime
from django.utils import timezone

def get_date_or_default(date, default="today_min"):

    date_format_url = "%Y_%m_%d"

    date_or_default = None

    try:
        date = datetime.datetime.strptime(date, date_format_url)
        date_or_default = datetime.datetime.combine(date, datetime.time.min, timezone.utc)
    except Exception as e:
        date_or_default = datetime.datetime.combine(datetime.date.today(), datetime.time.min, timezone.utc)

    return date_or_default