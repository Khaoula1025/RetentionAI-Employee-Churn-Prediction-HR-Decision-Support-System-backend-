# RetentionAI - Backend API

## 📋 Vue d'ensemble

Backend API REST pour RetentionAI, un système intelligent de prédiction et de rétention des employés basé sur le Machine Learning et l'IA générative.

Cette API fournit :
- 🔐 Authentification sécurisée avec JWT
- 🤖 Prédiction du risque de départ via Machine Learning
- 💡 Génération automatique de plans de rétention personnalisés
- 📊 Traçabilité complète des prédictions en base de données

## 🏗️ Architecture

```
retention-ai-backend/

├── app/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │       |   ├── __init__.py
│   │       |   ├── auth.py              # /register, /login
│   │       |   ├── predictions.py       # /predict
│   │       |   └── retention.py         # /generate-retention-plan
│   │       |
|   |       └── deps.py                  # Dependencies (get_current_user, get_db)
|   |
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── security.py                  # JWT, password hashing functions
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── session.py                   # Database session management
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py                      # User SQLAlchemy model
│   │   ├── employe.py                    # Employe SQLAlchemy model
│   │   └── prediction_history.py         # PredictionHistory SQLAlchemy model
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py                      # Token, TokenData schemas
│   │   ├── prediction.py                # PredictionRequest, PredictionResponse
│   │   └── retention.py                 # RetentionPlanRequest, RetentionPlanResponse
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_service.py               # Call Hugging Face/Gemini API
│   │   └── retention_service.py         # Business logic for retention plans
│   │
│   └── main.py                          # FastAPI app initialization
│
├── ml/
│   ├── __init__.py
│   ├── notebooks/
│   │   ├── 01_eda.ipynb                 # Exploratory Data Analysis
│   │   ├── 02_preprocessing.ipynb       # Data preprocessing
│   │   └── 03_model_training.ipynb      # Model training & evaluation
│   │
│   ├── data/
│   │   └──data.csv       # dataset
│   │
│   ├── models/
│   │   └── proModel.pkl                  # Trained model (Random Forest/Logistic Regression)
│
├── tests/
│   ├── __init__.py
│   ├── test_predictions.py              # Test prediction endpoint
│   └── test_ml_service.py               # Test ML model loading and prediction
|
├── .env                                 # Environment variables (not in git)
├── .gitignore                           # Git ignore file
├── .dockerignore                        # Docker ignore file
├── Dockerfile                           # Docker configuration for backend
├── docker-compose.yml                   # Docker Compose (backend + postgres)
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

## 🚀 Technologies

- **FastAPI** - Framework web moderne et performant
- **PostgreSQL** - Base de données relationnelle
- **SQLAlchemy** - ORM Python
- **Pydantic** - Validation des données
- **JWT (python-jose)** - Authentification
- **Bcrypt (passlib)** - Hashing sécurisé
- **Scikit-learn** - Machine Learning
- **Pandas & NumPy** - Manipulation de données
- **Pytest** - Tests unitaires
- **Docker** - Conteneurisation
- **Uvicorn** - Serveur ASGI

### IA Générative
- **Google AI (Gemini)**

## 📦 Installation

### Prérequis
- Python 3.10+
- PostgreSQL 14+
- Docker & Docker Compose (recommandé)

### Option 1 : Docker (Recommandé)

1. **Cloner le repository**
```bash
git clone https://github.com/Khaoula1025/RetentionAI-Employee-Churn-Prediction-HR-Decision-Support-System-backend-.git
```

2. **Configurer les variables d'environnement**
```bash
cp .env.example .env
# Éditer .env avec vos configurations
```

3. **Lancer avec Docker Compose**
```bash
docker-compose up --build
```

L'API sera accessible sur `http://localhost:8000`

### Option 2 : Installation locale

1. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Configurer PostgreSQL**
```bash
# Créer la base de données
createdb retention_db
```

4. **Configurer les variables d'environnement**
```bash
cp .env.example .env
# Éditer .env
```

5. **Lancer l'application**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
## 📡 API Endpoints

### Documentation Interactive
- Swagger UI : `http://localhost:8000/docs`
- ReDoc : `http://localhost:8000/redoc`

### Authentification

#### POST `/register`
Créer un nouveau compte utilisateur RH

**Request:**
```json
{
  "username": "hr_manager",
  "password": "SecureP@ssw0rd"
}
```

**Response:**
```json
{
  "id": 1,
  "username": "hr_manager",
  "created_at": "2025-12-19T10:30:00"
}
```

#### POST `/login`
Se connecter et obtenir un token JWT

**Request:**
```json
{
  "username": "hr_manager",
  "password": "SecureP@ssw0rd"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Prédiction (🔒 Protégé par JWT)

#### POST `/predict`
Prédire le risque de départ d'un employé

**Headers:**
```
Authorization: Bearer <your_jwt_token>
```

**Request:**
```json
{
  "age": 35,
  "department": "Sales",
  "job_role": "Sales Executive",
  "monthly_income": 5000,
  "years_at_company": 5,
  "job_satisfaction": 2,
  "work_life_balance": 3,
  "performance_rating": 4,
  "distance_from_home": 10,
  "business_travel": "Travel_Frequently"
}
```

**Response:**
```json
{
  "employee_id": "EMP001",
  "churn_probability": 0.78,
  "risk_level": "high",
  "prediction_id": 123,
  "timestamp": "2025-12-19T10:35:00"
}
```

### Plan de Rétention (🔒 Protégé par JWT)

#### POST `/retention`
Générer un plan de rétention personnalisé

**Headers:**
```
Authorization: Bearer <your_jwt_token>
```

**Request:**
```json
{
  "employee_data": {
    "age": 35,
    "department": "Sales",
    "job_role": "Sales Executive",
    "job_satisfaction": 2,
    "work_life_balance": 3,
    "performance_rating": 4
  },
  "churn_probability": 0.78
}
```

**Response:**
```json
{
  "retention_plan": [
    "Proposer 2 jours de télétravail par semaine pour améliorer l'équilibre vie professionnelle/personnelle",
    "Réévaluer la charge de déplacements professionnels et proposer des alternatives (visioconférence)",
    "Mettre en place un plan de développement de carrière avec formation en management"
  ],
  "risk_level": "high",
  "generated_at": "2025-12-19T10:36:00"
}
```

## 🗄️ Schéma Base de Données

### Table `users`
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Table `predictions_history`
```sql
CREATE TABLE predictions_history (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER REFERENCES users(id),
    employee_id VARCHAR(50),
    age INTEGER,
    department VARCHAR(50),
    job_role VARCHAR(100),
    churn_probability FLOAT,
    risk_level VARCHAR(20),
    metadata JSONB
);
```

## 🤖 Machine Learning

### Modèle
- **Algorithme principal** : Random Forest Classifier
- **Comparaison avec** : Logistic Regression
- **Optimisation** : GridSearchCV

### Pipeline de Preprocessing
1. Suppression des colonnes non pertinentes (ID, etc.)
2. Encodage des variables catégorielles (OneHotEncoder)
3. Normalisation/Standardisation (StandardScaler)
4. Gestion des valeurs manquantes

### Métriques de Performance
- Accuracy : ~85%
- Precision : ~82%
- Recall : ~80%
- F1-Score : ~81%
- ROC-AUC : ~88%

### Entraînement du Modèle
```bash
# Ouvrir le notebook Jupyter
jupyter notebook notebooks/preprocessing&model_training.ipynb

# Le modèle entraîné sera sauvegardé dans app/ml/
```

## 🧪 Tests

### Lancer tous les tests
```bash
pytest tests/ -v
```

### Tests avec coverage
```bash
pytest tests/ -v --cov=app --cov-report=html
```
## 🐳 Docker

### Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose
```yaml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    ports:
      - "5432:5432"
    # volumes:
    #   - postgres_data:/var/lib/postgresql/data
  
  backend:
    build: .
    ports: 
      - "8000:8000"
    environment:
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_HOST: db
      DB_PORT: 5432
      DB_NAME: ${DB_NAME}
      secret: ${SECRET}
      GEMINI_API_KEY: ${GEMINI_API_KEY}
    depends_on:
      - db
  
  frontend:
    build: ../retentionai-frontend
    ports:
      - "3000:3000"
    environment:
      # For Next.js rewrites (server-side proxy)
      API_URL: http://backend:8000
    depends_on:
      - backend
```

## 🔒 Sécurité

- ✅ Hashing des mots de passe avec bcrypt (salt rounds: 12)
- ✅ Authentification JWT avec expiration
- ✅ Protection CORS configurée
- ✅ Validation des entrées avec Pydantic
- ✅ Protection contre les injections SQL (SQLAlchemy ORM)
- ✅ Variables sensibles dans .env (jamais commitées)

## 🚀 Déploiement

### Variables d'environnement Production
```env
DEBUG=False
DATABASE_URL=postgresql://user:password@prod-db:5432/retention_db
SECRET_KEY=<générer-une-clé-forte>
```

## 🤝 Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Projet pédagogique - Tous droits réservés

## 📞 Support

Pour toute question :
- Ouvrir une issue sur GitHub
- Consulter la documentation API : `/docs`

## 🔗 Liens Utiles

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [JWT.io](https://jwt.io/)

---
