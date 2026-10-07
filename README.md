# Python Calculator — GitHub Actions CI/CD

A small Flask calculator app used to demonstrate **CI/CD with GitHub Actions** deploying to **Azure App Service (Linux)**.

## Contents

| Path | Purpose |
|---|---|
| `python_calc.py` | Flask web calculator application |
| `src/calc.py` | Calculator library (`safe_divide`) |
| `tests/test_calc.py` | Unit tests (pytest) |
| `requirements.txt` | Python dependencies |
| `infra/webapp.bicep` | Bicep template that provisions a Linux Python Web App |
| `.github/workflows/python-calc-ci.yml` | CI workflow — build & test on push/PR |
| `.github/workflows/python-calc-cd.yml` | CD workflow — provision infra & deploy on successful CI |

## How CI/CD flows

1. A push to `main` triggers **python-calc-ci**, which installs dependencies, runs the
   tests, and publishes a `Web.zip` artifact.
2. On a successful CI run, **python-calc-cd** logs in to Azure using the
   `AZURE_CREDENTIALS` repository secret, provisions the Web App with `infra/webapp.bicep`,
   and deploys the application.

> **Note:** Update `AZURE_RESOURCE_GROUP` / `AZURE_LOCATION` in `python-calc-cd.yml` (and the
> Bicep parameters if needed) to values your lab subscription permits.

## Run locally

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pytest tests/test_calc.py
python python_calc.py   # serves on http://localhost:80
```
