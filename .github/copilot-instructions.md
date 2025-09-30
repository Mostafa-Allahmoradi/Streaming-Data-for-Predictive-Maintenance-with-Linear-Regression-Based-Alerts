# Copilot Instructions for Predictive Maintenance Streaming Data Project

## Project Architecture
- **Data Ingestion**: Raw robot axis data is streamed from CSV files in `data/` and visualized in `data_stream_visualization.ipynb`. Data is inserted into a Neon PostgreSQL database using `DataExtraction/DBManager.py`.
- **Data Management**: Use `DataExtraction/FileManager.py` for reading/writing CSVs and extracting columns. Data is loaded into pandas DataFrames for analysis.
- **Analysis & Modeling**: Predictive maintenance is performed in Jupyter notebooks (`predictive_maintenance.ipynb`, `Predictive_maintenance_attempt2.ipynb`) by training univariate linear regression models (one per axis) using time as input and axis current as output. Residuals and outliers are analyzed and visualized.
- **Results & Reporting**: Model outputs, alerts, errors, and plots are saved in the `results/` directory. Plots are organized by axis and type (e.g., regression, residuals, alerts).

## Key Workflows
- **Database Setup**: The DBManager class auto-creates the `robot_readings` table with columns for each axis and time. Connection details are hardcoded in `DBManager.py`.
- **Data Loading**: Use FileManager to load CSVs and extract relevant columns (excluding 'Trait').
- **Model Training**: For each axis (#1–#8), fit a linear regression (Time → Axis value) and record slope/intercept. Use synthetic data for testing and validation.
- **Residual Analysis**: Compute and plot residuals for each axis to identify outliers and alert conditions.
- **Event Logging**: Alerts and errors are annotated on plots and logged to CSVs in `results/`.

## Conventions & Patterns
- **Axis Naming**: Axis columns are named as 'Axis #1', 'Axis #2', ..., 'Axis #8'.
- **Time Handling**: Time is treated as seconds relative to the first timestamp.
- **Plot Storage**: All plots are saved in subfolders under `results/` by axis and type.
- **Error Handling**: FileManager and DBManager print status messages for success/failure.
- **Testing Data**: Synthetic test data is generated for model validation.

## Integration Points
- **Database**: Neon PostgreSQL, connection via psycopg2 (see `DBManager.py`).
- **DataFrames**: All analysis uses pandas DataFrames.
- **Visualization**: Matplotlib for plotting; plots are saved to disk, not displayed inline except in notebooks.

## Example: Adding a New Axis
- Update CSVs in `data/` to include new axis column (e.g., 'Axis #9').
- Update DBManager to include the new column in table creation and insertion logic.
- Update analysis notebooks to train and plot for the new axis.

## References
- See `README.md` for project motivation and architecture diagrams.
- See `DataExtraction/DBManager.py` and `FileManager.py` for data access patterns.
- See `results/` for output structure and naming conventions.

---
If any section is unclear or missing details, please provide feedback so instructions can be improved for future AI agents.
