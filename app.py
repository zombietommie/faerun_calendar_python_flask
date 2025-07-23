from flask import Flask, render_template
import calendar_logic # import the calendar logic

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
@app.route("/year/<int:year>")
def index(year=1491):
    all_months = calendar_logic.MONTHS
    return render_template(
        'index.html',
        months=all_months,
        year=year,
    )

@app.route("/month/<month_name>")
def month_view(month_name):
    # Find the month's number (index + 1)
    try:
        month_number = calendar_logic.MONTHS.index(month_name) + 1
    except ValueError:
        # If the month name isn't valid, return a 404 error
        return "Month no found!", 404

    # Check for a holiday after the previous month
    holiday_before = calendar_logic.get_holiday_after_month(month_number - 1)

    # check for holiday after the current month
    holiday_after = calendar_logic.get_holiday_after_month(month_number)

    return render_template(
        "month_view.html",
        name=month_name,
        holiday_before=holiday_before,
        holiday_after=holiday_after
    )