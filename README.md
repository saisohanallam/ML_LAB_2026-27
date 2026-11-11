# Customer Segmentation Studio

A Flask + scikit-learn mini-project that groups customers and visualises the result.

## Methods
1. **K-Means**: partitions customers into clusters.
2. **Gaussian Mixture Model (GMM)**: probabilistic clustering.
3. **PCA**: dimensionality reduction and the 2D customer map.
4. **Factor Analysis**: latent-factor representation.

PCA and Factor Analysis are dimensionality-reduction methods, not clustering algorithms. If your course needs four distinct clustering algorithms, check with your instructor whether this combination is acceptable.

## Project layout
```
customer-segmentation/
├── app.py                 # Flask routes (/, /health)
├── requirements.txt
├── data/
│   ├── sample_customers.csv   # synthetic demo data (200 rows)
│   ├── generate_data.py       # regenerates the sample
│   └── README.md
├── src/
│   └── segmentation.py    # preprocessing + K-Means, GMM, PCA, Factor Analysis
└── templates/
    └── index.html         # upload form, metrics, PCA plot, cluster profiles
```

## Run locally
Python 3.10 to 3.12 recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Use your own data
Upload a CSV with at least 5 rows. Numeric columns are median-imputed and scaled; categorical columns are imputed and one-hot encoded. Columns named `CustomerID`, `customer_id`, `id` or `name` are dropped automatically.

## Deploy on Render
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

## Limitations
- The sample data is synthetic and for demonstration only.
- Cluster numbers are arbitrary labels, not quality rankings.
- Silhouette score is a clustering diagnostic, not prediction accuracy.
- K-Means and GMM may assign customers differently.
