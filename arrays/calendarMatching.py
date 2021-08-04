"""
Calendar Matching

Imagine that you want to schedule a meeting
of a certain duration with a co-worker. You
have access to your calendar and your coworker's calendar (both of which contain
your respective meetings for the day, in the
form of [startTime, endTime] ), as well
as both of your daily bounds (i.e., the earliest
and latest times at which you're available for
meetings every day, in the form of
[earliestTime, latestTime] ).
Write a function that takes in your calendar,
your daily bounds, your co-worker's
calendar, your co-worker's daily bounds, and
the duration of the meeting that you want to
schedule, and that returns a list of all the
time blocks (in the form of
[startTime, endTime] ) during which
you could schedule the meeting, ordered
from earliest time block to latest.
Note that times will be given and should be
returned in military time. For example:
8:30 , 9:01 , and 23:56 .
Also note that the given calendar times will
be sorted by start time in ascending order,
as you would expect them to appear in a
calendar application like Google Calendar.

Sample Input:

calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
dailyBounds1 = ["9:00", "20:00"]
calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30

Sample Output
[["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
"""


