from sklearn.linear_model import LinearRegression

class ModelTrainer:
    def __init__(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
        self.trained_model = None

    def train_model(self, method='linear_regression'):
        model = LinearRegression()
        self.trained_model = model.fit(self.x_train, self.y_train)
        return self.trained_model