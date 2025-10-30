# GarminAI

A small Python script that logs into Garmin Connect, aggregates total calorie expenditure from last Monday up to today, and asks Google's Gemini to generate a practical, balanced diet recommendation targeting about 1 kg weight loss per week (assuming ~1000 kcal daily deficit).

## Features
- Fetches daily summaries from Garmin Connect
- Sums total weekly calories and computes daily average
- Sends context to Gemini (Generative AI) to generate a diet recommendation
- Simple console output

## Prerequisites
- Python 3.9+
- Garmin account with activity data
- Google Gemini API key

## Installation
1. Clone or download this repository.
2. (Recommended) Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install garminconnect garth google-generativeai
```

Note: Some environments may require additional setup for `garminconnect`/`garth` depending on platform and authentication method.

## Configuration
Open `main.py` and set the following variables:
- `GEMINI_API_KEY`: your Google Gemini API key
- `email` and `password`: your Garmin account credentials

Example:
```python
GEMINI_API_KEY = "your_gemini_api_key_here"
email = "your_email@example.com"
password = "your_password"
```

Security tip: Prefer using environment variables or a local `.env`/secret manager in production. Avoid committing credentials to version control.

## Usage
Run the script:

```bash
python main.py
```

It will:
- Log into Garmin Connect
- Print daily calories from last Monday up to today
- Print total calories and invoke Gemini
- Display the AI-generated recommendation

## Troubleshooting
- Authentication errors: ensure your Garmin credentials are correct. If your account uses MFA, you may need additional handling per `garminconnect` docs.
- Empty or low data: if there are no activities recorded for the period, totals may be zero.
- Gemini errors: verify `GEMINI_API_KEY` and that your project has access to the specified model (`gemini-2.5-flash`).

## Disclaimer
The generated diet recommendations are for informational purposes only and are not a substitute for professional medical or nutritional advice. Consult a qualified professional before making significant dietary changes.
