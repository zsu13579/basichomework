# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# own scirpt not done yet
# from django import template
# from datetime import datetime
# from django.utils.timesince import timesince
#
# register = template.Library()
#
# @register.filter
# def todolistdate(value):
#     interval = datetime.now() - value
#     timesince()
#     return interval

# revise from timesince.py from django.utils.timesince
import datetime

from django.utils.html import avoid_wrapping
from django.utils.timezone import is_aware, utc
from django.utils.translation import ugettext, ungettext_lazy
from django import template

TIMESINCE_CHUNKS = (
    (60 * 60 * 24 * 365, ungettext_lazy('%d 年', '%d 年')),
    (60 * 60 * 24 * 30, ungettext_lazy('%d 月', '%d 月')),
    (60 * 60 * 24 * 7, ungettext_lazy('%d 周', '%d 周')),
    (60 * 60 * 24, ungettext_lazy('%d 日', '%d 日')),
    (60 * 60, ungettext_lazy('%d 小时', '%d 小时')),
    (60, ungettext_lazy('%d 分钟', '%d 分钟'))
)

register = template.Library()

@register.filter
def todolistdate(d, now=None, reversed=False):
    """
    Takes two datetime objects and returns the time between d and now
    as a nicely formatted string, e.g. "10 minutes".  If d occurs after now,
    then "0 minutes" is returned.

    Units used are years, months, weeks, days, hours, and minutes.
    Seconds and microseconds are ignored.  Up to 1 adjacent units will be
    displayed.  For example, "2 weeks" and "1 year" are
    possible outputs, but "2 weeks, 3 hours" and "1 year, 5 days" are not.

    Adapted from
    http://web.archive.org/web/20060617175230/http://blog.natbat.co.uk/archive/2003/Jun/14/time_since
    """
    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if now and not isinstance(now, datetime.datetime):
        now = datetime.datetime(now.year, now.month, now.day)

    if not now:
        now = datetime.datetime.now(utc if is_aware(d) else None)

    delta = (d - now) if reversed else (now - d)
    # ignore microseconds
    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since <= 0:
        # d is in the future compared to now, stop processing.
        return avoid_wrapping(ugettext('0 分钟'))
    for i, (seconds, name) in enumerate(TIMESINCE_CHUNKS):
        count = since // seconds
        if count != 0:
            break
    result = avoid_wrapping(name % count)
    # if i + 1 < len(TIMESINCE_CHUNKS):
    #     # Now get the second item
    #     seconds2, name2 = TIMESINCE_CHUNKS[i + 1]
    #     count2 = (since - (seconds * count)) // seconds2
    #     if count2 != 0:
    #         result += ugettext(', ') + avoid_wrapping(name2 % count2)
    return result