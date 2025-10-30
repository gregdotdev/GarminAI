import garminconnect
from garth.exc import GarthException, GarthHTTPError
from datetime import datetime, timedelta
import google.generativeai as genai


GEMINI_API_KEY = ''
genai.configure(api_key=GEMINI_API_KEY)

email = ""
password = ""

def get_week_calories():
    # Login to Garmin Connect
    garmin = garminconnect.Garmin(email, password)
    garmin.login()

    # Calculate the start of last week (last Monday)
    today = datetime.now()
    last_monday = today - timedelta(days=today.weekday() + 7)
    num_days = (today - last_monday).days + 1

    # Initialize calories sum
    total_calories = 0
    daily_data = []

    # Iterate from last Monday until today
    for i in range(num_days):
        date_value = last_monday + timedelta(days=i)
        date_str = date_value.strftime('%Y-%m-%d')

        # Get daily summary
        summary = garmin.get_user_summary(date_str)
        day_calories = summary.get('totalKilocalories') or 0  # Treat None as 0

        print(f"{date_str}: {day_calories} kcal")
        total_calories += day_calories
        daily_data.append((date_str, day_calories))

    return total_calories, daily_data

def ai_analysis(total_calories, daily_data):
    # Calculate daily average
    daily_average = total_calories / len(daily_data) if daily_data else 0

    prompt = f"""Analyze the following calorie expenditure information:
Total weekly calories: {total_calories} kcal
Daily average calories: {daily_average:.0f} kcal

Return a diet recommendation I can follow next week to lose 1 kg per week.
Consider an approximate 1000 kcal daily deficit to lose about 1 kg per week.
Provide a practical and balanced meal plan."""

    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    print("\n" + "="*60)
    print("ANALYSIS AND RECOMMENDED DIET")
    print("="*60)
    print(response.text)

# Run
total_calories, daily_data = get_week_calories()
print(f"\nTotal calories (last week up to today): {total_calories} kcal")

# AI analysis
ai_analysis(total_calories, daily_data)