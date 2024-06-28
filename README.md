# Book Recommendation Project

This project implements a book recommendation system using collaborative filtering with the Surprise library. The project includes data preparation, model training, evaluation, and visualizations.

## Project Structure

- `FinalProject.ipynb`: Jupyter Notebook for data preparation, model training, evaluation, and visualizations.
- `app.py`: Streamlit app for interactive book recommendations.
- `cleaned.csv`: Dataset containing book ratings and other relevant information.

## Requirements

- Python 3.7+
- pandas
- scikit-learn
- surprise
- matplotlib
- seaborn
- streamlit

## Installation

1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   cd BookRecommendationProject
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```sh
   pip install pandas scikit-learn surprise matplotlib seaborn streamlit
   ```

## Data Preparation and Visualization

The `FinalProject.ipynb` notebook performs the following steps:

1. **Data Preparation**:
   - Load the dataset from `cleaned.csv`.
   - Ensure correct data types for each column.
   - Drop rows with missing values in critical columns.

2. **Model Training**:
   - Use the Surprise library to train a collaborative filtering model with SVD (Singular Value Decomposition).

3. **Model Evaluation**:
   - Compute evaluation metrics: Mean Absolute Error (MAE), R-squared (R2), and Root Mean Squared Error (RMSE).

4. **Visualizations**:
   - Plot the distribution of ratings.
   - Display the top 10 most popular books.
   - Show a scatter plot of true ratings vs. predicted ratings.

To run the notebook, open it in Jupyter Notebook or Jupyter Lab and execute the cells.

## Interactive Streamlit App

The `app.py` file creates an interactive web application using Streamlit. It allows users to enter a user ID and get book recommendations based on the trained model.

### Running the Streamlit App

1. **Activate the virtual environment** (if not already activated):
   ```sh
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. **Run the Streamlit app**:
   ```sh
   streamlit run app.py
   ```

3. **Open the provided URL** in your web browser to interact with the app.

### Streamlit Interface

- **User ID Input**: Enter a user ID to get book recommendations.
- **Number of Recommendations Slider**: Select the number of recommendations to display.
- **Get Recommendations Button**: Click to get the recommendations.
- **Show Rating Distribution Checkbox**: Optionally display the distribution of ratings.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.