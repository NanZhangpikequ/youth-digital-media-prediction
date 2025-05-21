# 📱 Youth Digital Media Prediction Project

This repository contains all files and scripts for an AI-driven predictive system analyzing adolescents' digital media use patterns, emotional reactions, and curriculum recommendation logic.

## 🔍 Project Goals

- Predict high-risk youth who may develop digital overuse habits
- Identify those who use media more due to loneliness
- Estimate emotional feedback post-usage
- Segment users and match curriculum based on behavior clusters

## 📦 Structure

- `data/` - Raw and processed survey data
- `notebooks/` - Jupyter Notebooks for preprocessing & model training
- `src/` - Python modules for training and evaluation
- `outputs/` - Charts and prediction results
- `report/` - PPT and written summary
- `assets/` - Images for README and slide use

## 🧠 Models

| Model | Description |
|-------|-------------|
| M1    | Predict digital media dependence risk (XGBClassifier) |
| M2    | Predict media use driven by loneliness (XGBClassifier) |
| M3    | Predict post-usage emotional relief score (XGBRegressor) |

## 📈 Outputs

- Bar chart: Age group vs digital dependence
- Radar chart: Emotional profile by user group
- Course recommendation map (proportional, not tiered)

## 🔧 Requirements

```bash
pip install -r requirements.txt

