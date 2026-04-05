
import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv", skipinitialspace=True)

    race_count = df['race'].value_counts()

    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(), 1
    )

    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )

    higher_edu = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )
    lower_edu = ~higher_edu

    higher_education_rich = round(
        (df[higher_edu]['salary'] == '>50K').mean() * 100, 1
    )

    lower_education_rich = round(
        (df[lower_edu]['salary'] == '>50K').mean() * 100, 1
    )

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[
        df['hours-per-week'] == min_work_hours
    ]

    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    country_stats = (
        df.groupby('native-country')['salary']
        .value_counts(normalize=True)
    )

    highest_country = (
        country_stats.loc[:, '>50K'] * 100
    ).idxmax()

    highest_country_percentage = round(
        country_stats.loc[highest_country, '>50K'] * 100, 1
    )

    india_rich = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]

    top_IN_occupation = (
        india_rich['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Average age of men:", average_age_men)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_country,
        'highest_earning_country_percentage': highest_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
