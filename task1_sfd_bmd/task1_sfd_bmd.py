# Step 0: Import libraries
import xarray as xr
import numpy as np
import plotly.graph_objects as go

# Step 1: Load the dataset
data = xr.open_dataset("screening_task.nc",  engine="netcdf4")
print(data)

# Central girder elements
central_elements = [15, 24, 33, 42, 51, 60, 69, 78, 83]

# Initialize lists
Mz = []
Vy = []

# Extract values
for elem in central_elements:
    # Bending Moment
    Mz.append(
        data["forces"].sel(Element=elem, Component="Mz_i").item()
    )
    Mz.append(
        data["forces"].sel(Element=elem, Component="Mz_j").item()
    )

    # Shear Force
    Vy.append(
        data["forces"].sel(Element=elem, Component="Vy_i").item()
    )
    Vy.append(
        data["forces"].sel(Element=elem, Component="Vy_j").item()
    )

# Convert to numpy arrays
Mz = np.array(Mz)
Vy = np.array(Vy)

print("Bending Moment (Mz):", Mz)
print("Shear Force (Vy):", Vy)

# X-axis
x = np.arange(len(Mz))

# Bending Moment Diagram
fig_bmd = go.Figure()
fig_bmd.add_trace(go.Scatter(
    x=x,
    y=Mz,
    mode="lines+markers",
    name="Bending Moment (Mz)"
))
fig_bmd.update_layout(
    title="Bending Moment Diagram (Central Girder)",
    xaxis_title="Node Index along Girder",
    yaxis_title="Bending Moment (kNm)"
)
fig_bmd.show()

# Shear Force Diagram
fig_sfd = go.Figure()
fig_sfd.add_trace(go.Scatter(
    x=x,
    y=Vy,
    mode="lines+markers",
    name="Shear Force (Vy)"
))
fig_sfd.update_layout(
    title="Shear Force Diagram (Central Girder)",
    xaxis_title="Node Index along Girder",
    yaxis_title="Shear Force (kN)"
)
fig_sfd.show()
