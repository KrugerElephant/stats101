import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timedelta as td
from random import randint


def extract_start_year(row):
    return row['start_date'].year

def get_active_cases_cumulative_count_by_year(df):

    min_year = min(df['start_date']).year
    max_year = max(df['start_date']).year

    print(f'{min_year} to {max_year}')
    df['start_year'] = df.apply(extract_start_year, axis=1)

    number_of_active_cases_by_year = []

    for year in range(min_year, max_year):
        
        active_cases = df.loc[(df['end_date'].isnull()) & (df['start_year'] <= year)]

        new_row = {
            "year":  year,
            "count": len(active_cases),
            "active_cases_tabular_data": active_cases
        }

        number_of_active_cases_by_year.append(new_row)

    df_active_cases = pd.DataFrame(number_of_active_cases_by_year)

    return df_active_cases

# --------------------------------------------------
   
data = []

for case_id in range(1, 100):

    start_date = dt.now() - td(randint(1, 6000))
    end_date = np.nan

    if randint(1, 3) == 1:
        end_date = start_date + td(randint(1, 700))

    gender = "M" if case_id % 2 == 0 else "F"

    new_row = {
        "start_date": start_date,
        "end_date": end_date,
        "case_id": case_id,
        "gender": gender       
    }
    
    data.append(new_row)

df = pd.DataFrame(data)

print(df.head(15))

aggregated_data = get_active_cases_cumulative_count_by_year(df)
print(aggregated_data.head(3))
