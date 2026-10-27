# CSC325 Module 8 – First CI/CD Pipeline

**Author:** Sinan Sevindik — CSC325 Software Engineering, Farmingdale State College

A small Django + Django REST Framework backend with a four-stage GitHub Actions pipeline
(**Setup → Dependencies → Test → Deploy**) that deploys to Render.

**Live app:** https://csc325-cicd-sinan.onrender.com/  *(update if your Render URL differs)*

## Endpoints

| Method | Path | Returns |
|---|---|---|
| GET | `/` | Project name and list of endpoints |
| GET | `/api/hello/` | `{"message": "Hello from CSC325!"}` |
| GET | `/api/health/` | `{"status": "ok", "commit": "<deployed commit sha>"}` |

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py test -v 2
python manage.py runserver
```

## Pipeline

Workflow file: [`.github/workflows/csc325_ci_cd.yml`](.github/workflows/csc325_ci_cd.yml)

| Stage | What it does |
|---|---|
| Setup | Checks out the code and installs Python 3.12 |
| Dependencies | Installs packages from `requirements.txt` |
| Test | Runs `python manage.py test`; any failing test fails the pipeline |
| Deploy | `needs: test` — triggers the Render deploy hook, then waits until `/api/health/` reports the new commit |

`main` is protected by a ruleset: changes go through a feature branch and a pull request.
