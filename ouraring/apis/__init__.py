
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from ouraring.api.daily_activity_api import DailyActivityApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from ouraring.api.daily_activity_api import DailyActivityApi
from ouraring.api.daily_readiness_api import DailyReadinessApi
from ouraring.api.daily_sleep_api import DailySleepApi
from ouraring.api.heart_rate_api import HeartRateApi
from ouraring.api.personal_info_api import PersonalInfoApi
from ouraring.api.sessions_api import SessionsApi
from ouraring.api.sleep_periods_api import SleepPeriodsApi
from ouraring.api.tags_api import TagsApi
from ouraring.api.workouts_api import WorkoutsApi
