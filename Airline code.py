#11 Flight status distribution
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("merge_flights.csv")
status = df["flight_status"].value_counts()
status.plot(kind="bar")
plt.title("Flight Status Distribution")
plt.xlabel("Flight Status")
plt.ylabel("Count")
plt.show()



#12 Top 10 airlines by flights
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('merge_flights.csv')

top_airlines = df['airline_id'].value_counts().head(10)

top_airlines.plot(kind='bar')
plt.title('Top 10 Airlines by Number of Flights')
plt.xlabel('Airline ID')
plt.ylabel('Number of Flights')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Top 10 Airlines by Number of Flights:")
print(top_airlines)




#13 Delay minutes distribution
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('merge_flights.csv')

print("Columns:", df.columns.tolist())

delay_data = df['delay_minutes'].dropna()

plt.figure(figsize=(10, 6))
plt.hist(delay_data, bins=20, edgecolor='black', color='skyblue')
plt.title('Distribution of Flight Delay Minutes')
plt.xlabel('Delay Minutes')
plt.ylabel('Number of Flights')
plt.grid(True, alpha=0.3)
plt.show()

print(f"\nTotal flights: {len(delay_data)}")
print(f"Average delay: {delay_data.mean():.1f} minutes")
print(f"Median delay: {delay_data.median():.1f} minutes")
print(f"Maximum delay: {delay_data.max():.1f} minutes")







#14 Monthly flight trend
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("merge_flights.csv")

df["scheduled_departure_date"] = pd.to_datetime(df["scheduled_departure_date"])

monthly = df.groupby(df["scheduled_departure_date"].dt.month)["flight_id"].count()

monthly.plot(kind="line", marker='o', color='blue')
plt.title("Monthly Flight Trend")
plt.xlabel("Month")
plt.ylabel("Number of Flights")
plt.grid(True, alpha=0.3)
plt.xticks(range(1, 13))
plt.show()

print("\nMonthly Flight Counts:")
print(monthly)







#15 Weather condition frequency
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("weather.csv")


df["conditions"].value_counts().plot(kind="bar", color='skyblue', edgecolor='black')

plt.title("Weather Conditions Frequency")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Days")
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


print("\nWeather Condition Frequencies:")
print(df["conditions"].value_counts())



















































































































