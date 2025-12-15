# RetentionAI Backend

Backend API for employee retention prediction and personalized retention plan generation.

## Features

- 🔐 JWT Authentication
- 🤖 Machine Learning prediction (Random Forest/Logistic Regression)
- 🧠 LLM-powered retention plan generation
- 📊 PostgreSQL database with tracking
- 🐳 Docker containerization
- ✅ Comprehensive testing

## Setup

### Local Development

1. Clone the repository:
```bash
git clone <your-repo-url>
cd retention-ai-backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run database migrations:
```bash
alembic upgrade head
```

6. Start the server:
```bash
uvicorn app.main:app --reload
```

### Docker Deployment

```bash
docker-compose up --build
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
retention-ai-backend/
├── app/              # FastAPI application
├── ml/               # Machine Learning pipeline
├── tests/            # Test suite
└── alembic/          # Database migrations
```

## Testing

```bash
pytest
```

With coverage:
```bash
pytest --cov=app tests/
```

## ML Model Training

See notebooks in `ml/notebooks/` for the complete ML pipeline:
1. `01_eda.ipynb` - Exploratory Data Analysis
2. `02_preprocessing.ipynb` - Data preprocessing
3. `03_model_training.ipynb` - Model training & evaluation

## License

MIT
