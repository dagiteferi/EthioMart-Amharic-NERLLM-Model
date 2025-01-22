# Amharic Named Entity Recognition (NER) System for EthioMart

## Overview
This repository contains the implementation of a Named Entity Recognition (NER) system tailored for the Amharic language. The system is built using XLM-RoBERTa, a state-of-the-art multilingual transformer model, and is designed to extract key entities such as product names, prices, and locations from Amharic text data. The primary application of this system is for EthioMart, leveraging insights from Telegram messages.

## Features
- **Amharic Text Segmentation**: Utilizes the amseg library for accurate tokenization of Amharic text.
- **Data Cleaning and Preprocessing**: Handles morphological complexities, removes unnecessary characters, and aligns tokens with labels.
- **Fine-Tuned Transformer Model**: Employs XLM-RoBERTa for robust multilingual NER tasks.
- **Performance Metrics**: Evaluates model performance using precision, recall, and F1-score.

## Dataset
The dataset consists of Amharic text messages scraped from Telegram channels such as @MerttEka. These messages provide a rich source of information for identifying products, prices, and locations.

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/your_username/dagiteferi-ethiomart-amharic-nerllm-model.git
    cd dagiteferi-ethiomart-amharic-nerllm-model
    ```
2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
### Data Preparation
- Run the `scrapper.py` script located in the `scripts/` directory to scrape data.
- Use the provided preprocessing scripts to clean and label the data:
    ```sh
    python scripts/preprocessing.py
    ```

### Model Training
- Fine-tune the model using the notebook:
    ```sh
    notebooks/XLM_Fine-tune.ipynb
    ```

### Evaluation
- Evaluate the model’s performance:
    ```sh
    python scripts/evaluate_model.py
    ```

## Results
The fine-tuned model achieved the following performance metrics:
- **Precision**: 99.9%
- **Recall**:1.00
- **F1-Score**: 1.00

## Folder Structure
Directory structure:
 ```sh
└── dagiteferi-ethiomart-amharic-nerllm-model/
    ├── README.md
    ├── requirements.txt
    ├── scraping_session.session
    ├── notebooks/
    │   ├── README.md
    │   ├── XLM_Fine-tune.ipynb
    │   ├── __init__.py
    │   ├── label.ipynb
    │   ├── preprocessing.ipynb
    │   └── token.ipynb
    ├── scripts/
    │   ├── README.md
    │   ├── __init__.py
    │   ├── labeling.py
    │   ├── preprocessing.py
    │   ├── scrapper.py
    │   └── __pycache__/
    ├── src/
    │   ├── __init__.py
    │   └── file_structure.py
    ├── tests/
    │   └── __init__.py
    └── .github/
        └── workflows/
            └── unittests.yml
```
## Limitations and Future Work
- **Incomplete Coverage**: Expand on tasks such as model comparison and interpretability.
- **Dataset Diversity**: Incorporate more diverse sources to improve generalization.
- **Documentation**: Enhance inline comments and examples for better clarity.



## Acknowledgements
- 10 Academy Team

- Telegram Channels for Data Collection

