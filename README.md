# NBA Career Longevity Prediction API :basketball:

## Overview

This project contains a machine learning model that predicts whether NBA players will last more than 5 years in the league based on their performance statistics. It includes a REST API that serves the predictions of the model. :smile:

## Features

- Predictive modeling using logistic regression.
- Evaluation of model performance with precision-recall curves and cross-validation.
- A REST API to provide predictions on player longevity.

## Getting Started

### Prerequisites

- Python 3.8+
- Pip for Python package installation

### Installation

Download the repository

Install the required Python packages:
```
pip install -r requirements.txt
```


## Project Structure

The project directory is structured as follows:

- `app/` - Contains the Flask application files, including routes, views, and templates for the API.
- `data/` - Houses the dataset files and related images, such as feature correlations and distributions.
- `models/` - Stores the serialized model file.
- `notebooks/` - Includes Jupyter notebooks for data analysis, exploration, preprocessing, and model exploration.
- `src/` - Contains utility scripts for data processing and model operations.
- `tests/` - Includes api json collection for postman.
- `test.py` - A Python script that was initially here to start on the project.
- `requirements.txt` - Lists the Python dependencies for the project.
- `README.md` - The top-level README for developers using this project.
- `test_junior_ds[1].pdf` - The rules for this project and insight about data structure.


### Notebooks

The `notebooks/` directory contains several Jupyter notebooks that detail different stages of the data science workflow:

- `data_analysis.md` - Markdown file summarizing the data analysis findings.
- `data_exploration.ipynb` - Notebook for initial exploration of the data, understanding the distributions, and identifying patterns.
- `data_preprocessing.ipynb` - Notebook for preprocessing the data, including cleaning and feature engineering.
- `model_exploration.ipynb` - Notebook for exploring different models, tuning parameters, and selecting the best model.

These notebooks are integral for documenting the iterative process of building and evaluating the machine learning model.

## Development

### Usage

To start the API server, run:
```
python app/routes.py
```

The API endpoints will be available at `http://localhost:5000/`.

#### Endpoints

The API provides the following endpoints:

- `/` - Home endpoint providing information about the API.
- `/predict` - Endpoint to submit player statistics for predictions.
- `/documentation` - Endpoint to access detailed API documentation.


### Examples

To predict the career longevity of a player, send a POST request to the `/predict` endpoint with the player's statistics:

```
POST /predict
Host: localhost:5000
Content-Type: application/json

{
    "GP": 82,
    "FTM": 150,
    "OREB": 55,
    "STL": 60,
    "BLK": 20,
    "AST": 250
}
```

## Training the Model

To train or retrain the model using the notebooks, ensure you have Jupyter installed and navigate to the notebooks/ directory and open the desired notebook.


## Contact

For any queries, you can reach out to [Julien.DELAVANDE@student-isae.supaero.fr](mailto:Julien.DELAVANDE@student-isae.supaero.f).
