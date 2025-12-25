import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs basic data cleaning steps:
    - Removes duplicate rows
    - Optimizes data types to reduce memory usage
    """
    df = df.copy()

    df = df.drop_duplicates()

    cols_to_int = [
    'Diabetes_binary', 'HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke',
    'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump',
    'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'DiffWalk', 'Sex', 'Age', 'Education',
    'Income']
    df[cols_to_int] = df[cols_to_int].astype('int8')

    df[['BMI', 'MentHlth', 'PhysHlth']] = df[['BMI', 'MentHlth', 'PhysHlth']].astype('int16')

    return df

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies domain-informed feature engineering:
    - Caps extreme BMI values
    - Creates composite health indicators
    """
    df = df.copy()

    df['BMI'] = df['BMI'].clip(upper=70) # Capping

    df['Difficult_Health'] = (df['PhysHlth'] > 15).astype(int)

    return df

def prepare_train_test_split(
    df: pd.DataFrame,
    target: str,
    test_size: float = 0.2,
    random_state: int = 42
):
    """
    Splits the dataset into stratified train/test sets and applies feature scaling.
    Returns scaled features along with the fitted scaler for reproducibility.
    """
    X = df.drop(target, axis=1)
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state, stratify=y)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler