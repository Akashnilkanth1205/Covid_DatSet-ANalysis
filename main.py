import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def f1(df, continent):

    bool_df = df[df["Continent"] == continent] #selecting the continent details
    max_total_cases = bool_df.iloc[bool_df['TotalCases'].argmax(), 0] #maximum  cases in country of given continent
    min_total_cases = bool_df.iloc[bool_df['TotalCases'].argmin(), 0]#min cases in country of given continent
    print(f'Most number of Total cases: {max_total_cases} \nLeast number of Total cases: {min_total_cases}') # displaying the min max countries
    columns = (bool_df[['Country/Region', 'TotalCases', 'TotalRecovered', 'TotalDeaths']])  #selecting columns for displaying graph

    plt.figure(figsize=(15, 7))  # defining figure size

    #took the 3 columns for stack barplot
    plt.bar(columns['Country/Region'], columns['TotalCases'], label='TotalCases')
    plt.bar(columns['Country/Region'], columns['TotalRecovered'], label='TotalRecovered')
    plt.bar(columns['Country/Region'], columns['TotalDeaths'], label='TotalDeaths')
    plt.legend()   #displaying legends
    plt.xticks(rotation=45, ha = 'right')
    # plt.bar(x, y2, bottom=y1, color='b')
    plt.show() #displaying plot


def f2(df, continent):
    boolContinent = df["Continent"] == continent
    # boolCountry= df["Country/Region"]==country
    bool = df.loc[boolContinent]
    columns = (bool[['TotalRecovered', 'TotalDeaths']])
    sns.lmplot(x='TotalDeaths', y='TotalRecovered', data=columns)  #showing relationship between total deaths per total recovery
    plt.show()


def f3(df):
    # First prints the number of entries in the dataset for each continent.
    bar_df = df.groupby(['Continent', 'Country/Region']).agg({'Tot Cases/1M pop': 'mean'}).reset_index()
    print('Number of Entries in the dataset for each continent :\n', df['Continent'].value_counts())

    # Generates a barplot per continent containing the number of tests/1M per continent.
    for i in bar_df["Continent"].unique():
        plt.figure(figsize=(20, 10))
        temp_df = bar_df.loc[bar_df["Continent"] == i]
        temp_df['Tot Cases/1M pop'] = temp_df['Tot Cases/1M pop'] / \
                                      df.loc[df['Continent'] == i, 'Country/Region'].shape[0]
        sns.barplot(data=temp_df, x=temp_df['Country/Region'], y='Tot Cases/1M pop', hue=temp_df["Continent"])
        plt.xticks(rotation=45, ha='right')
        plt.show()


def f4(df1,country_name):  # create a line plot of Daily Vaccinations on the y-axis and date on the x-axis of a particular country
    fun1 = df1.loc[df1["country"] == country_name][::4]  # To avoid the messy graph and for beautification using date step as 4
    plt.figure(figsize=(20, 10))
    sns.lineplot(data=fun1, x=fun1["date"], y=fun1['daily_vaccinations'], hue=fun1["country"])
    plt.xticks(rotation=90, ha='right')
    plt.show()


def main():
    # importing the csv files
    df = pd.read_csv('worldometer_data.csv')
    df1 = pd.read_csv('country_vaccinations.csv')

    while (True):
        print('Welcome to our Analysis pipeline of Covid-19 data')
        print('Please select one of the following option :\n'
              '1 - Display cases per country specific continent.\n'
              '2 - Calculate the recovered and death percentages per country in a specific  Contient.\n'
              '3 - Display number of test per continent.\n'
              '4 - Display the daily vaccination of the Specific country.\n'
              '5 - Exit.')

        option = int(input("Please select option : "))

        # generate a stacked barplot with the following data, Total cases, Total recovered and
        # Total Death (in this order) for countries in a specific continent.
        if (option == 1):
            continent = input("Please, enter one of the following continent names : "
                              "North America, South America, Asia, Europe,Africa, Australia : \n")
            f1(df, continent)

        # A function to define the relationship between the Total Recovered and Total Deaths of patients in a specific continent
        elif (option == 2):
            continent = input("Please enter one of the following continent name : "
                              "North America, South America, Asia, Europe, Africa, Australia : \n")
            f2(df, continent)

        elif (option == 3):
            f3(df)  #calling the f3

        elif (option == 4):
            country = input("Please enter the name of country : \n"
                            "Ireland, USA, India, Brazil, Japan, Australia : ")
            f4(df1, country)

        elif (option == 5):
            break  # exit loop

        else:  # if wrong input from user
            print("**********Please Select the valid option from the given menu*********")


main()
