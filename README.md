# E-Commerce Text Classification

## Overview

This project is a text classification model for categorizing e-commerce product descriptions into different categories such as Household, Books, Electronics, and Clothing & Accessories.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running Locally](#running-locally)
  - [Classifying Text](#classifying-text)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python (3.x recommended)
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/e-commerce-text-classification.git
   ```

2. Navigate to the project directory:

   ```bash
   cd e-commerce-text-classification
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Locally

To run the Streamlit app locally:

```bash
streamlit run stream_app.py
```

This will start the app, and you can access it in your browser at http://localhost:8501.

### Classifying Text

1. Enter the text you want to classify in the provided text area.
2. Click the "Classify" button.
3. The app will display the predicted category for the entered text.


## Model Details

The text classification model is trained using various algorithms, including Support Vector Classifier (SVC), k-Nearest Neighbors (KNN), Random Forest, and Multinomial Naive Bayes. Among these algorithms, the Support Vector Classifier performed well in terms of accuracy and generalization.

### Training Data

The training data for the model is sourced from the Kaggle E-commerce Text dataset. This dataset contains product descriptions from various e-commerce categories.

### Word to Vector Transformation

To convert words into numerical vectors, the TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer is employed. TF-IDF is a widely used technique in natural language processing that reflects the importance of words in a document relative to a collection of documents.

The model is trained to categorize product descriptions into different classes, including Household, Books, Electronics, and Clothing & Accessories.




## Contributing

If you would like to contribute to the project, please follow our Contribution Guidelines.

## License

This project is licensed under the MIT License.
