import pandas as pd
import os

class FileManager:

    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File not found: {file_path}")
        self.file_path = file_path
        self.data = self.read_csv()

    def read_csv(self):
        """Read data from a CSV file."""
        try:
            data = pd.read_csv(self.file_path)
            print(f"✅ Successfully loaded {len(data)} rows from {self.file_path}")
            return data
        except Exception as e:
            print(f"❌ Error reading {self.file_path}: {e}")
            return None
        
    def write_csv(self, output_path, data):
        """Write data to a CSV file."""
        try:
            data.to_csv(output_path, index=False)
            print(f"✅ Successfully wrote data to {output_path}")
        except Exception as e:
            print(f"❌ Error writing to {output_path}: {e}")
        
    def get_columns(self):
        """Read column names from the CSV file."""
        try:
            # self.columns = [col for col in self.data.columns if "Axis" in col]
            # self.columns = [col for col in self.data.columns if "Trait" not in col and "Time" not in col]
            columns = [col for col in self.data.columns if "Trait" not in col]
            return columns
        except Exception as e:
            print(f"❌ Error reading columns from {self.file_path}: {e}")
            return []
        
    def get_data(self):
        """Return the loaded DataFrame."""
        return self.data
    
    def write_plot(self, output_path, fig):
        """Save a plot to a file."""
        try:
            fig.savefig(output_path)
            print(f"✅ Successfully saved plot to {output_path}")
        except Exception as e:
            print(f"❌ Error saving plot to {output_path}: {e}")