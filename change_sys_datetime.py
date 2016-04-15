#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime
import click

date_command_template = ("date %(month)02d%(day)02d%(hour)02d"
                         "%(minute)02d%(year)d.%(second)02d")

__now = datetime.datetime.now()
__year = __now.year
__month = __now.month
__day = __now.day
__hour = __now.hour
__minute = __now.minute
__second = __now.second


@click.command()
@click.option('--year', '-Y', type=int, default=__year,
              help='year with 4 digital')
@click.option('--month', '-m', type=int, default=__month,
              help='month range in 1-12')
@click.option('--day', '-d', type=int, default=__day,
              help='day range in 1-31')
@click.option('--hour', '-H', type=int, default=__hour,
              help='year range in 0-23')
@click.option('--minute', '-M', type=int, default=__minute,
              help='year range in 0-59')
@click.option('--second', '-S', type=int, default=__second,
              help='year range in 0-59')
def change_with_detail(year, month, day, hour, minute, second):
    """
    Quick python script to change system date and time.\n
    More friendly compare to Unix `date` command
    """

    table = {
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': minute,
        'second': second,
    }

    date_str = date_command_template % table
    do_change_sys_datetime(date_str)


def do_change_sys_datetime(date_str):
    click.secho("change system datetime with: ### %s ###" % date_str,
                bold=True, fg="yellow")
    os.system(date_str)


if __name__ == '__main__':
    change_with_detail()
