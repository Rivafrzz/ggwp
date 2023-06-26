import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(0)
X = np.random.rand(100, 1)
y = 2 + 3 * X + np.random.rand(100, 1)

df = pd.DataFrame(np.concatenate([X, y], axis=1), columns=['X', 'y'])
X = df[['X']]
y = df['y']
regression_model = LinearRegression()
regression_model.fit(X, y)
y_pred = regression_model.predict(X)
 
print('Intercept:', regression_model.intercept_)
print('Slope:', regression_model.coef_)
 
mse = mean_squared_error(y, y_pred)
print('Mean Squared Error:', mse)
