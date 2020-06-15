import time
import calendar
import pandas as pd

CSV_PATH = './csvs/'
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
SEPARATOR = '-' * 40

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data.')

    # Get user input for city.
    while True:
        try:
            city = input("Choose a city (Chicago, New York City, Washington): ").lower()
            if CITY_DATA[city]:
                break
        except KeyError:
            print('Unknown city, please try again: ')
            
    # Get user input for month.
    while True:
        try:
            month = input('Enter a month (January-June), or enter "all" for all months: ')
            if month.capitalize() in calendar.month_name[:7] or month == 'all':
                break
            else:
                raise ValueError
        except ValueError:
            print('Please enter a valid month, or "all" for all months: ')

    # Get user input for day of the week.
    while True:
        try:
            day = input('Enter a day of the week (e.g, Tuesday), or "all" for all days: ')
            if day.capitalize() in calendar.day_name or day == 'all':
                break
            else:
                raise ValueError
        except ValueError:
            print('Please enter a valid weekday, or "all" for all days: ')

    print(SEPARATOR)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # Load data file into a dataframe.
    df = pd.read_csv(CSV_PATH + CITY_DATA[city])

    # Convert the Start Time column to datetime.
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week, and hour from Start Time to create new columns.
    df['month'] = df['Start Time'].dt.month
    df['day_of_the_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable.
    if month != 'all':
        # Get month number from month name.
        months = list(calendar.month_name)
        month = months.index(month.capitalize())
    
        # Filter by month to create the new dataframe.
        df = df[df['month'] == month]

    # Filter by day of week if applicable.
    if day != 'all':
        # Filter by day of week to create the new dataframe.
        df = df[df['day_of_the_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Get most popular months, days, and hours.
    popular_stats = ['month', 'day_of_the_week', 'hour']
    for stat in popular_stats:
        print(get_most_popular(df, stat))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(SEPARATOR)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Add a new column to the dateframe for combined start/end stations.
    df['Station Combination'] = df['Start Station'] + ' to ' + df['End Station']

    # Get most popular stations.
    popular_stats = ['Start Station', 'End Station', 'Station Combination']
    for stat in popular_stats:
        print(get_most_popular(df, stat))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(SEPARATOR)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: {} seconds'.format(total_travel_time))

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(SEPARATOR)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('--- User types ---')
    print(user_types.to_string())
    print()
    
    # Washington does not include Gender or Birth Year data.
    if city in ['new york city', 'chicago']:

        gender_counts = df['Gender'].value_counts()
        print('--- Gender ---')
        print(gender_counts.to_string())
        print()

        print('--- Birth year ---')
        earliest_birth_year = int(df['Birth Year'].min())
        latest_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])

        print('Earliest birth year: ', earliest_birth_year)
        print('Latest birth year: ', latest_birth_year)
        print('Most common birth year: ', common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(SEPARATOR)


def get_most_popular(df, stat):
    """Returns the most popular value for a given column."""

    most_popular = df[stat].mode()[0]
    stat_label = stat.replace("_", " ")

    # For the month, return the month name instead of the integer.
    if stat == 'month':
        most_popular = calendar.month_name[most_popular]

    return 'Most frequent ' + stat_label + ': ' + str(most_popular)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
