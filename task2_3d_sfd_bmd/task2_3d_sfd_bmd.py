# ===============================
# TASK 2: 3D SFD & BMD (MIDAS Style)
# ===============================

import os
import ast
import pandas as pd
import xarray as xr
import plotly.graph_objects as go

# -------------------------------
# Base directory
# -------------------------------
BASE_DIR = r"C:\Users\Dell\Desktop\FOSSEE_TASK\task2_3d_sfd_bmd"

# -------------------------------
# Helper function to load Python dict from .py file
# -------------------------------
def load_dict_from_pyfile(filename):
    """Read a Python dictionary from a .py file and return it as a dict."""
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {filename}")
    with open(path, "r") as f:
        content = f.read()
    # Extract the part after the '=' sign
    dict_str = content.strip().split("=", 1)[1].strip()
    return ast.literal_eval(dict_str)

# -------------------------------
# Step 1: Load nodes and elements
# -------------------------------
nodes_dict = load_dict_from_pyfile("node.py")
elements_dict = load_dict_from_pyfile("element.py")

# Convert to pandas DataFrame
nodes = pd.DataFrame([
    {"node": k, "x": v[0], "y": v[1], "z": v[2]} for k, v in nodes_dict.items()
])

elements = pd.DataFrame([
    {"element": k, "start_node": v[0], "end_node": v[1]} for k, v in elements_dict.items()
])

print("Node and element data loaded successfully")
print("First 5 nodes:\n", nodes.head())
print("First 5 elements:\n", elements.head())

# -------------------------------
# Step 2: Load NetCDF dataset
# -------------------------------
data = xr.open_dataset(os.path.join(BASE_DIR, "screening_task.nc"), engine="netcdf4")
print("NetCDF data loaded successfully")

# -------------------------------
# Step 3: Create lookup dictionaries
# -------------------------------
node_coords = {int(row["node"]): (row["x"], row["y"], row["z"]) for _, row in nodes.iterrows()}
elem_nodes = {int(row["element"]): (int(row["start_node"]), int(row["end_node"])) for _, row in elements.iterrows()}

# -------------------------------
# Step 4: Girder definitions
# -------------------------------
girders = {
    "Girder 1": [13, 22, 31, 40, 49, 58, 67, 76, 81],
    "Girder 2": [14, 23, 32, 41, 50, 59, 68, 77, 82],
    "Girder 3": [15, 24, 33, 42, 51, 60, 69, 78, 83],
    "Girder 4": [16, 25, 34, 43, 52, 61, 70, 79, 84],
    "Girder 5": [17, 26, 35, 44, 53, 62, 71, 80, 85],
}

# -------------------------------
# Step 5: Function to plot 3D diagram
# -------------------------------
def plot_3d_diagram(component_i, component_j, title, y_label):
    fig = go.Figure()

    for girder_name, elem_list in girders.items():
        for elem in elem_list:
            n1, n2 = elem_nodes[elem]

            # Node coordinates
            x1, y1, z1 = node_coords[n1]
            x2, y2, z2 = node_coords[n2]

            # Internal forces from Xarray
            val_i = data["forces"].sel(Element=elem, Component=component_i).item()
            val_j = data["forces"].sel(Element=elem, Component=component_j).item()

            # 3D line (MIDAS-style extrusion)
            fig.add_trace(go.Scatter3d(
                x=[x1, x2],
                y=[val_i, val_j],   # extrusion direction
                z=[z1, z2],
                mode="lines",
                line=dict(width=6),
                name=f"{girder_name} - E{elem}",
                showlegend=False
            ))

    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title="Bridge Length (X)",
            yaxis_title=y_label,
            zaxis_title="Bridge Width (Z)",
        ),
        height=700
    )

    fig.show()

# -------------------------------
# Step 6: Plot BMD (Mz)
# -------------------------------
plot_3d_diagram(
    component_i="Mz_i",
    component_j="Mz_j",
    title="3D Bending Moment Diagram (BMD)",
    y_label="Bending Moment (Mz)"
)

# -------------------------------
# Step 7: Plot SFD (Vy)
# -------------------------------
plot_3d_diagram(
    component_i="Vy_i",
    component_j="Vy_j",
    title="3D Shear Force Diagram (SFD)",
    y_label="Shear Force (Vy)"
)
