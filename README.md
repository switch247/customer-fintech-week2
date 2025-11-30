# Customer Experience Analytics

## Overview
This project analyzes customer experience through reviews from banking apps. It involves data collection, preprocessing, sentiment analysis, and machine learning to understand customer satisfaction patterns.

## Project Structure
The project follows a clean, modular architecture:

```
src/customer_analytics/
├── __init__.py
├── config/                 # Configuration
│   ├── __init__.py
│   └── settings.py         # Centralized settings
├── visualisation/          # Plotting and graphs
│   ├── __init__.py
│   └── plotter.py          # Visualization utilities
├── analysis/               # Analysis logic
│   ├── __init__.py
│   └── eda.py              # Exploratory data analysis
├── utils/                  # Helper modules
│   ├── __init__.py
│   ├── scraper.py          # Data collection (Google Play Store)
│   ├── preprocessor.py     # Data cleaning and preprocessing
│   ├── data_loader.py      # Database interactions
│   ├── data_cleaning.py    # General cleaning utilities
│   └── alignment.py        # Data alignment functions
└── pipeline/               # NLP pipeline (planned)
    ├── __init__.py
    ├── train.py            # Model training (planned)
    ├── predict.py          # Predictions (planned)
    └── evaluate.py         # Evaluation (planned)
```

## Setup

### Prerequisites
- Python 3.8+
- PostgreSQL (optional, for data storage)

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   poetry install
   # or
   pip install -r requirements.txt
   ```

### Configuration
Create a `.env` file with:
```
CBE_APP_ID=com.combanketh.mobilebanking
AWASHPAY_APP_ID=com.sc.awashpay
AMHARABANK_APP_ID=com.amharabank.Aba_mobile_banking
REVIEWS_PER_BANK=400
MAX_RETRIES=3
```

## Usage

### Task 1: Data Collection and Analysis

#### 1. Scrape Reviews
```python
from customer_analytics.utils import PlayStoreScraper

scraper = PlayStoreScraper()
df = scraper.scrape_all_banks()
```

#### 2. Preprocess Data
```python
from customer_analytics.utils import ReviewPreprocessor

preprocessor = ReviewPreprocessor()
preprocessor.process()
```

#### 3. Exploratory Data Analysis
```python
from customer_analytics.analysis import EDA

eda = EDA()
eda.load_data('data/processed/reviews_processed.csv')
print(eda.summary_report())
```

#### 4. Visualize Data
```python
from customer_analytics.visualisation import Plotter

plotter = Plotter()
plotter.plot_histogram(df, 'rating', title='Rating Distribution')
```

### Database Operations
```python
from customer_analytics.utils import DatabaseLoader

loader = DatabaseLoader()
if loader.connect():
    loader.create_tables()
    # loader.insert_data(restaurants_df, reviews_df)
    loader.close()
```

## Development

### Code Standards
- Follow PEP8 conventions
- Use type hints where applicable
- Write docstrings for all classes and functions
- Keep modules focused and single-purpose

### Testing
```bash
pytest tests/
```

## Contributing
Please follow the coding standards and submit pull requests for review.
