"""Subplots"""
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1,2)

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 5, 6, 7, 9, 21, 22, 23]
z = [22, 19, 15, 12, 11, 9, 4, 1]

ax1.plot(x, y, color='r', label="Y Values")
ax1.plot(x, z)
ax2.plot(x, z, color='g', label="Z Values")

ax1.legend()
ax1.set_title('Y')
ax2.legend()
ax2.set_title('Z')

plt.tight_layout()

plt.show()

"""SheCodes Advanced Homework Week 3"""

fig, (ax1, ax2) = plt.subplots(1, 2)

years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

ax1.plot(years,
         temp_anomalies,
         color='b',
         alpha=0.5,
         marker='o',
         linestyle='-')
ax2.bar(years, co2_emissions, color='g', alpha=0.5)

ax1.set_title('Global Temperature Anomalies')
ax2.set_title('Global CO2 Emissions')

ax1.set_ylabel('Temperature Anomaly in Celsius')
ax2.set_ylabel('CO2 emissions (in billions of metric tons)')

ax1.set_xlabel('Year')
ax2.set_xlabel('Year')

ax1.set_xticks(years)
ax2.set_xticks(years)

ax1.grid(True)
ax2.grid(True)

plt.tight_layout()
plt.savefig("output.png")
plt.show()
