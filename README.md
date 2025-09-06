# Contemplative NLP Pipeline

An end-to-end MLOps project built in AWS SageMaker that fine-tunes transformer models for:
- 📊 Sentiment analysis (public datasets)
- 📖 Spiritual text classification (custom dataset)

## Architecture
- **Data Storage**: AWS S3
- **Model Training**: SageMaker + Hugging Face Transformers
- **Orchestration**: AWS Step Functions / Lambda
- **Monitoring**: CloudWatch

## Setup
1. Clone the repo
2. Set up a Python virtual environment
3. Install dependencies: `pip install -r requirements.txt`

## Next Steps
- [ ] Configure AWS CLI
- [ ] Build data preprocessing pipeline
- [ ] Fine-tune DistilBERT on IMDb dataset
- [ ] Deploy model via SageMaker endpoint