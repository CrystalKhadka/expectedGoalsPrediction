#%%
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Load the dataset
data = pd.read_csv('../data/model/haaland_shots_with_match_id.csv')

#%%
# Select relevant features and target
features = ['X', 'Y', 'shotType', 'lastAction', 'situation']
target = 'xG'
data = data[features + [target]].dropna()  # Drop rows with missing values

# Preprocess the data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['X', 'Y']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['shotType', 'lastAction', 'situation'])
    ]
)

#%%
data
#%%
X = data[features]
y = data[target]

# Transform features
X_processed = preprocessor.fit_transform(X)
#%%
X_processed
#%%
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
#%%
from sklearn.metrics import r2_score

X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)


# Define the neural network model
nn_model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1, activation='linear')  # Output layer for regression
])

# Compile the model
nn_model.compile(optimizer='adam', loss='mse', metrics=['mse'])

# Train the model
history = nn_model.fit(X_train, y_train, epochs=50, batch_size=16, validation_split=0.2, verbose=1)

# Evaluate the model
loss, mse = nn_model.evaluate(X_test, y_test, verbose=1)
print(f"Test Loss: {loss}, Test MSE: {mse}")

y_pred = nn_model.predict(X_test).flatten()
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2:.4f}")

# Define a function to predict xG for new inputs
def predict_xg(x, y, shot_type, last_action, situation):
    input_data = pd.DataFrame([[x, y, shot_type, last_action, situation]], columns=['X', 'Y', 'shotType', 'lastAction', 'situation'])
    input_processed = preprocessor.transform(input_data)
    predicted_xg = nn_model.predict(input_processed)
    return predicted_xg[0][0]
#%%
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Evaluate the model
loss, mse = nn_model.evaluate(X_test, y_test, verbose=1)
print(f"Test Loss: {loss:.4f}, Test MSE: {mse:.4f}")

# Calculate R² Score
y_pred = nn_model.predict(X_test).flatten()
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2:.4f}")

# Plot training history
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training vs Validation Loss')
plt.legend()
plt.show()

#%%
example_xg = predict_xg(0.885, 0.5, 'LeftFoot', 'Standard', 'Penalty')
print(f"Predicted xG: {example_xg:.4f}")
#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

haaland_shots_data = pd.read_csv('../data/model/haaland_shots_with_match_id.csv')

# Select relevant features and target
features = ['X', 'Y', 'shotType', 'lastAction', 'situation']
target = 'xG'
data = haaland_shots_data[features + [target]].dropna()

# Preprocess data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['X', 'Y']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['shotType', 'lastAction', 'situation'])
    ]
)
X = data[features]
y = data[target]
X_processed = preprocessor.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

# Define models
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "Support Vector Regressor": SVR(kernel='rbf', C=1.0, epsilon=0.1)
}

# Train and evaluate each model
results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results.append({"Model": name, "MSE": mse, "R²": r2})

# Convert results to a DataFrame for better readability
results_df = pd.DataFrame(results)
print(results_df)
#%%
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Load the dataset
file_path = '../data/model/haaland_shots_with_match_id.csv'  # Adjust to your file path
haaland_data = pd.read_csv(file_path)

# Create the target: 1 for 'Goal', 0 for other results
haaland_data['goal'] = (haaland_data['result'] == 'Goal').astype(int)

# Select relevant features
features = ['X', 'Y', 'xG', 'situation', 'shotType', 'lastAction', 'opponent', 'venue']
target = 'goal'

# Encode categorical features
categorical_features = ['situation', 'shotType', 'lastAction', 'opponent', 'venue']
label_encoders = {col: LabelEncoder() for col in categorical_features}

for col in categorical_features:
    haaland_data[col] = label_encoders[col].fit_transform(haaland_data[col])

# Scale numerical features
scaler = StandardScaler()
haaland_data[['X', 'Y', 'xG']] = scaler.fit_transform(haaland_data[['X', 'Y', 'xG']])

# Split the dataset into features and target
X = haaland_data[features]
y = haaland_data[target]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Define the binary classification model
binary_model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # Sigmoid activation for binary classification
])

# Compile the model
binary_model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = binary_model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)

# Evaluate the model
loss, accuracy = binary_model.evaluate(X_test, y_test, verbose=1)
print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")


# Prediction Function
def predict_goal(x, y, xg, situation, shot_type, last_action, opponent, venue):
    input_data = pd.DataFrame([[x, y, xg, situation, shot_type, last_action, opponent, venue]],
                              columns=['X', 'Y', 'xG', 'situation', 'shotType', 'lastAction', 'opponent', 'venue'])

    # Encode and scale the input data
    for col in categorical_features:
        input_data[col] = label_encoders[col].transform(input_data[col])
    input_data[['X', 'Y', 'xG']] = scaler.transform(input_data[['X', 'Y', 'xG']])

    # Predict
    prediction = binary_model.predict(input_data)
    return prediction[0][0]


# Example Prediction
example_prediction = predict_goal(0.8357, 0.4913, 0.7, 'OpenPlay', 'LeftFoot', 'Pass', 'Burnley', 'Away')
print(f"Predicted Probability of Goal: {example_prediction:.4f}")


#%%
