class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        # Perform some analysis on the data
        summary = self.data.describe()
        return summary
    
    def handle_missing_values(self, method='interpolate'):
        missing_report = self.data.isna().sum()

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