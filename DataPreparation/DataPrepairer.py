import pandas as pd

class DataPrepairer:
    def __init__(self, data):
        self.data = data
    
    def handle_missing_values(self, method='interpolate'):
        missing_report = self.data.isna().sum()
        print(f" Missing values per column report: {missing_report.to_dict()}")

        if missing_report.sum() > 0:
            # self.data = self.data.fillna(method='ffill').fillna(method='bfill')
            print(f"❌ Missing values detected. Applying linear interpolation...")
            self.data.iloc[:, 1:] = self.data.iloc[:, 1:].interpolate(
                method='linear', limit_direction='both'
            )
            print(f"✅ Successfully applied linear interpolation.")
            missing_after = self.data.isna().sum()
            print(f" Missing values per column after interpolation: {missing_after.to_dict()}")
        else:
            print(f"✅ No missing values detected. Moving on...")
        
        return self.data
    
    def handle_duplicates(self, subset_cols):
        duplicate_count = self.data.duplicated(subset=subset_cols).sum()
        if duplicate_count > 0:
            print(f"❌ Detected {duplicate_count} duplicate rows based on columns {subset_cols}. Removing duplicates...")
            self.data = self.data.drop_duplicates(subset=subset_cols)
            print(f"✅ Successfully removed duplicates.")
        else:
            print(f"✅ No duplicate rows detected based on columns {subset_cols}. Moving on...")
        return self.data
    
    def parse_timestamps(self, time_col):
        try:
            # Convert 'time' column to timezone-aware datetimes (UTC)
            self.data[time_col] = pd.to_datetime(self.data[time_col], utc=True, errors='coerce')
            print(f"✅ Successfully parsed '{time_col}' to timezone-aware datetime (UTC).")
        except Exception as e:
            print(f"❌ Error parsing '{time_col}': {e}")
        return self.data
    
    def sort_chronologically(self, col_name):
        self.data = self.data.sort_values(col_name).reset_index(drop=True)
        print(f"✅ Successfully sorted data chronologically by '{col_name}'.")
        return self.data