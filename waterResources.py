import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

year = []
water_level = []


def waterLevels(title, x_label, y_label):
    # Separating year and water levels to separate lists
    year0 = []
    water_level0 = []
    future_years = [2022, 2026, 2030]
    for row in year_water:
        year0.append(row[0])
        water_level0.append(row[1])

    plt.scatter(year0, water_level0, color='#00c0ff', label="Water Resource levels")

    slope, intercept, r, p, std_err = stats.linregress(year0, water_level0)

    # function of the line of best fit
    def myfunc(x):
        return slope * x + intercept

    # lineOfBestFit = list(map(myfunc, year))

    # plt.plot(year, lineOfBestFit, color='#01c243')

    for i in range(1962, 2019):
        year.append(i)
        water_level.append(myfunc(i))

    predictions = list(map(myfunc, future_years))

    # plt.plot(futureYearInc, extendedLineOfBestFit, color='#054a0d')
    plt.scatter(future_years, predictions, color='#00c0ff')

    # labelling predictions
    for i in range(0, len(future_years)):
        label = "(" + str(round(future_years[i], 2)) + ", " + str(round(predictions[i], 2)) + ")"
        plt.annotate(label, (future_years[i], predictions[i]))

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


def waterUsage(title, x_label, y_label):
    year1 = []
    water_level1 = []
    future_years = [2022, 2026, 2030]
    for row in year_water:
        year1.append(row[0])
        water_level1.append(row[1])

    index = 0
    for i in water_level1:
        j = year.index(year1[index])
        water_level1[index] = water_level[j] * (water_level1[index] / 100.0)
        index = index + 1

    plt.scatter(year1, water_level1, color='#66ddc0', label="Water Usage levels")

    slope, intercept, r, p, std_err = stats.linregress(year1, water_level1)

    # function of the line of best fit
    def myfunc(x):
        return slope * x + intercept

    predictions = list(map(myfunc, future_years))

    # plt.plot(futureYearInc, extendedLineOfBestFit, color='#054a0d')
    plt.scatter(future_years, predictions, color='#66ddc0')

    # labelling predictions
    for i in range(0, len(future_years)):
        label = "(" + str(round(future_years[i], 2)) + ", " + str(round(predictions[i], 2)) + ")"
        plt.annotate(label, (future_years[i], predictions[i]))

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


# Reading csv file with data on Syria's water levels
data = pd.read_csv("water-resource-levels.csv")
headings = data.columns.tolist()
# Converting data to manipulable list
year_water = data.values.tolist()

waterLevels("Water Resource levels", "Years", "Water in billion cubic meters")
# plt.show()

# Reading csv file with data on Syria's water Usage
data = pd.read_csv("water-usage.csv")
headings = data.columns.tolist()
# Converting data to manipulable list
year_water = data.values.tolist()

waterUsage("Water Usage levels", "Years", "Water in billion cubic meters")

# un-comment following lines if combined graph; and comment line 93
plt.title("")
plt.legend(loc="upper left")

plt.show()
