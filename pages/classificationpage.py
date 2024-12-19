import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set the title of the Streamlit app
st.title("Line Graph Example")

# Generate dummy data
x = np.linspace(0, 10, 100)  # X values (0 to 10, with 100 points)
y = np.sin(x)  # Y values (sine function)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y, label='Sine Wave', color='blue', linestyle='--', linewidth=2)

# Add labels, title, and legend
ax.set_title("Sine Wave Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)
