import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Function to calculate data rate based on given parameters
def calculate_data_rate(sf, bw_khz):
    # Constants
    cr = 4 / 5  # Coding Rate
    
    # Convert bandwidth from kHz to Hz for calculation
    bw_hz = bw_khz * 1e3
    
    # Calculate data rate using the formula provided
    data_rate = (bw_hz * np.log2(sf)) / sf * cr
    
    return data_rate

# Bandwidth values in kHz
bandwidths_khz = np.array([7.8, 10.4, 15.6, 20.8, 31.25, 41.7, 62.5, 125, 250, 500])

# Spreading Factors
spreading_factors = np.arange(7, 13)  # SF 7 to 12

# Initialize lists to store results
sf_list = []
bw_list_khz = []
data_rate_list = []

# Calculate data rate for each SF and bandwidth
for sf in spreading_factors:
    for bw_khz in bandwidths_khz:
        data_rate = calculate_data_rate(sf, bw_khz)
        
        sf_list.append(sf)
        bw_list_khz.append(bw_khz)
        data_rate_list.append(data_rate)

# Convert lists to pandas DataFrame
data = {
    'Spreading Factor': sf_list,
    'Bandwidth (kHz)': bw_list_khz,
    'Data Rate (bps)': data_rate_list
}

df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot for each spreading factor
for sf in spreading_factors:
    sf_data = df[df['Spreading Factor'] == sf]
    ax.plot(sf_data['Bandwidth (kHz)'], sf_data['Data Rate (bps)'], marker='o', label=f'SF {sf}')

ax.set_xscale('log')
ax.set_xlabel('Bandwidth (kHz)')
ax.set_ylabel('Data Rate (bps)')
ax.set_title('LoRa Data Rate vs Bandwidth for Different Spreading Factors')
ax.grid(True)
ax.legend(title='Spreading Factor')

plt.tight_layout()
plt.show()

# Print the DataFrame
print(df.to_string(index=False))
