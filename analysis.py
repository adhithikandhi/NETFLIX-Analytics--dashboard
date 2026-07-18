import pandas as pd

def total_users(df):

    return len(df)


def average_watch(df):

    return round(df["Watch_Time"].mean(),2)


def completion_rate(df):

    return round(
        (df["Watch_Time"]>=60).mean()*100,
        2
    )


def dropout(df):

    return round(
        (df["Watch_Time"]<15).mean()*100,
        2
    )