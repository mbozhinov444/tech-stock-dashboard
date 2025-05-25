# 📈 Tableau de bord Tech Stocks – Projet Applied Data Science in Finance

## 👤 Auteur  
Marko Bozhinov  
M1 PSME – Université Paris 1 Panthéon-Sorbonne

---

## 🎯 Objectif  
Ce projet présente un tableau de bord interactif pour analyser les principales actions technologiques à l’aide de Python, Streamlit et SQLite.  
Il a été développé dans le cadre du cours *Applied Data Science in Finance*.

### Objectifs pédagogiques :
- Appliquer un pipeline ETL (Extract–Transform–Load) à des données financières issues de Yahoo Finance  
- Mettre en œuvre une structure de code modulaire avec des fonctions réutilisables  
- Créer des visualisations interactives avec Streamlit et Plotly  
- Combiner plusieurs ensembles de données avec des jointures SQL  
- Extraire des informations en temps réel via le web scraping

---

## 🧰 Technologies
- Python 3  
- yfinance  
- pandas  
- SQLAlchemy  
- Streamlit  
- Plotly  
- matplotlib (utilisé partiellement)  
- PyYAML  
- scikit-learn  
- requests  
- BeautifulSoup4

---

## 📁 Structure du projet

```
tech_stock_project/
├── config.yaml                  # Fichier de configuration (tickers, chemins, etc.)
├── data/
│   └── stocks.db                # Base de données SQLite contenant les données historiques
├── etl/
│   └── load_data.py            # Script ETL : téléchargement et enregistrement des données
├── utils/
│   └── helpers.py              # Fonctions utilitaires pour la gestion des données
├── app/
│   └── streamlit_app.py        # Tableau de bord Streamlit
├── requirements.txt            # Packages Python nécessaires
└── README.md                   # Documentation du projet
```

---

## 🚀 Lancer le tableau de bord

1. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

2. **Charger les données**
```bash
python etl/load_data.py
```

3. **Lancer l’application**
```bash
streamlit run app/streamlit_app.py
```

Puis ouvrir : [http://localhost:8501](http://localhost:8501)

---

## 📊 Fonctionnalités
- Sélection de l’action via un menu déroulant  
- Filtre de date avec curseur  
- Statistiques résumées  
- **Graphique Plotly des prix avec régression linéaire**  
- **Histogramme Plotly des rendements quotidiens**  
- Affichage de la pente et du R²  
- Volatilité et ratio de Sharpe  
- Bouton de téléchargement CSV  
- Extraction d’un titre d’actualité depuis Yahoo Finance  
- Métadonnées des entreprises et des secteurs  
- Agrégation des rendements par secteur

---

## 📚 Références
- https://github.com/ranaroussi/yfinance  
- https://docs.streamlit.io  
- https://plotly.com/python  
- https://www.crummy.com/software/BeautifulSoup/  
- https://scikit-learn.org/stable/modules/linear_model.html

---

## 📌 Remarques  
Ce projet a été développé à des fins académiques dans le cadre du cours *Applied Data Science in Finance*.
Remarque : Plotly a été utilisé à la place de matplotlib pour améliorer l’interactivité et la qualité des visualisations.


# 📈 Tech Stock Dashboard – Applied Data Science in Finance Project

## 👤 Author  
Marko Bozhinov  
M1 PSME – Université Paris 1 Panthéon-Sorbonne

---

## 🎯 Objective  
This project presents an interactive dashboard for analyzing major tech stocks using Python, Streamlit, and SQLite.  
It is developed as part of the *Applied Data Science in Finance* course.

### Key learning goals:
- Apply ETL (Extract–Transform–Load) to financial data using Yahoo Finance  
- Implement modular code structure and reusable functions  
- Build interactive visualizations with Streamlit  
- Combine multiple datasets with SQL joins  
- Extract real-time information using web scraping

---

## 🧰 Technologies
- Python 3  
- yfinance  
- pandas  
- SQLAlchemy  
- Streamlit  
- matplotlib 
- plotly for interactive charts 
- PyYAML  
- scikit-learn  
- requests  
- BeautifulSoup4

---

## 📁 Project Structure

```
tech_stock_project/
├── config.yaml                  # Configuration settings (tickers, paths, etc.)
├── data/
│   └── stocks.db                # SQLite database with historical stock data
├── etl/
│   └── load_data.py            # ETL script: downloads and saves data
├── utils/
│   └── helpers.py              # Reusable functions for data handling
├── app/
│   └── streamlit_app.py        # Streamlit dashboard
├── requirements.txt            # Required Python packages
└── README.md                   # Project documentation
```

---

## 🚀 How to Run the Dashboard

1. **Install the dependencies**
```bash
pip install -r requirements.txt
```

2. **Load the data**
```bash
python etl/load_data.py
```

3. **Launch the app**
```bash
streamlit run app/streamlit_app.py
```

Then go to: [http://localhost:8501](http://localhost:8501)

---

## 📊 Features
- Interactive Plotly line chart with regression trend
- Interactive Plotly histogram of daily returns
- Sector and company-level metadata
- Volatility, Sharpe ratio, and regression metrics
- CSV export functionality
- Live headline scraping from Yahoo Finance


---

## 📚 References
- [yfinance](https://github.com/ranaroussi/yfinance)  
- [Streamlit documentation](https://docs.streamlit.io)  
- [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/)  
- [scikit-learn Linear Regression](https://scikit-learn.org/stable/modules/linear_model.html)

---

## 📌 Notes  
This project was developed for academic purposes under the *Applied Data Science in Finance* course.
Note: Plotly was used instead of matplotlib to improve interactivity and visualization quality.
