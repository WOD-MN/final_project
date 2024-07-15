import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Bandwidth values in kHz
bandwidths_khz = np.array([7.8, 10.4, 15.6, 20.8, 31.25, 41.7, 62.5, 125, 250, 500])

# Spreading Factors
spreading_factors = np.arange(7, 13)  # SF 7 to 12

# Coding Rate (assuming constant for simplicity)
cr = 4 / 5  # Coding Rate
payload_size = 20  # in bytes

# Initialize lists to store results
sf_list = []
bw_list_khz = []
airtime_list = []

# Calculate airtime for each SF and bandwidth
for sf in spreading_factors:
    for bw_khz in bandwidths_khz:
        # Convert bandwidth from kHz to Hz for calculation
        bw_hz = bw_khz * 1e3
        # Simplified airtime calculation (this is a placeholder for the actual LoRa airtime formula)
        airtime = (8 * payload_size) / (bw_hz / (2**sf))
        
        sf_list.append(sf)
        bw_list_khz.append(bw_khz)
        airtime_list.append(airtime)

# Convert to pandas DataFrame
data = {
    'Spreading Factor': sf_list,
    'Bandwidth (kHz)': bw_list_khz,
    'Airtime (ms)': airtime_list
}

df = pd.DataFrame(data)

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))  # Increase figure size

colors = plt.cm.viridis(np.linspace(0, 1, len(spreading_factors)))
for i, sf in enumerate(spreading_factors):
    sf_data = df[df['Spreading Factor'] == sf]
    ax1.plot(sf_data['Bandwidth (kHz)'], sf_data['Airtime (ms)'], 'o-', color=colors[i], label=f'SF {sf}')

ax1.set_xlabel('Bandwidth (kHz)')
ax1.set_xscale('log')
ax1.set_ylabel('Airtime (ms)', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Set custom ticks for x and y axes
ax1.set_xticks(bandwidths_khz)
ax1.get_xaxis().set_major_formatter(plt.ScalarFormatter())
ax1.set_yticks(np.arange(0, max(airtime_list) + 1, 50))

# Add custom legend
for i, sf in enumerate(spreading_factors):
    ax1.text(1.02, 0.95 - i * 0.05, f'SF {sf}', color=colors[i], transform=ax1.transAxes, fontsize=12, fontweight='bold')

fig.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust layout to make space for the custom legend
plt.title('LoRa Bandwidth vs Airtime for Different Spreading Factors')
plt.grid(True)
plt.show()

# Print the table
print(df.to_string(index=False))
