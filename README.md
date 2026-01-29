# fossee-osdag-sfd-bmd
# SFD & BMD Visualization using Xarray (Osdag – FOSSEE Internship)

## Project Overview
This repository contains the implementation and visualization of **Shear Force Diagrams (SFD)** and  
**Bending Moment Diagrams (BMD)** as part of the **FOSSEE / Osdag internship tasks**.

The objective is to extract structural analysis data from an **Xarray (NetCDF) dataset** and visualize
the results in both **2D** and **3D (MIDAS-style)** formats using Python.

---

## Tasks Performed

### Task 1: SFD & BMD from Xarray (Central Girder)
- Loaded structural analysis data from a NetCDF file using Xarray
- Identified central girder elements
- Extracted shear force and bending moment values
- Generated 2D SFD and BMD plots using Matplotlib (PyPlot)

### Task 2: 3D MIDAS-Style SFD & BMD
- Used node and element connectivity data
- Mapped force and moment values in 3D space
- Generated MIDAS-style 3D SFD and BMD visualizations using Plotly

---

## Technologies Used
- Python
- Xarray
- NumPy
- Pandas
- Matplotlib (PyPlot)
- Plotly

---

## How to Run the Code

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/fossee-osdag-sfd-bmd.git


2. Install required libraries:
    pip install xarray numpy pandas matplotlib plotly netCDF4


3. Run the scripts for Task 1 and Task 2 using Python:
    python task1_sfd_bmd.py
    python task2_3d_sfd_bmd.py

   
   git clone https://github.com/YOUR_USERNAME/fossee-osdag-sfd-bmd.git
