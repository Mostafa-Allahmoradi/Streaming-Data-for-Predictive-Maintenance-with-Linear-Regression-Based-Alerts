class DataAnalyzer:
    def __init__(self, data):
        self.data = data.dropna()
        self.Q1 = self.data.quantile(0.25)
        self.Q3 = self.data.quantile(0.75)
        self.IQR = self.Q3 - self.Q1
        self.Upperbound = self.Q3 + 1.5 * self.IQR
        self.Lowerbound = self.Q1 - 1.5 * self.IQR
        self.Mask_outliers = (self.data < self.Lowerbound) | (self.data > self.Upperbound)
        self.Outlier_Indices = self.data[self.Mask_outliers].index.tolist()
        self.Outlier_Report = {
            "Q1": self.Q1,
            "Q3": self.Q3,
            "IQR": self.IQR,
            "Lowerbound": self.Lowerbound,
            "Upperbound": self.Upperbound,
            "outlier_count": len(self.Outlier_Indices),
            "outlier_indices": self.Outlier_Indices,
        }

    def analyze(self):
        # Perform some analysis on the data
        summary = self.data.describe()
        return summary

    def print_outlier_report(self):
        print(f"    Q1: {self.Q1}")
        print(f"    Q3: {self.Q3}")
        print(f"    IQR: {self.IQR}")
        print(f"    Bounds: [{self.Lowerbound:.2f}, {self.Upperbound:.2f}]")
        # print(f"  Lower Bound: {self.Lowerbound}")
        # print(f"  Upper Bound: {self.Upperbound}")
        print(f"    Number of Outliers detected: {len(self.Outlier_Indices)}")
        print(f"    Outlier Indices: {self.Outlier_Indices[:10]}")  # show sample of indices
    