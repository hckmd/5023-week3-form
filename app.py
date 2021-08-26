from flask import Flask, render_template, request

# create the Flask app
app = Flask(__name__)

# home page
@app.route("/")
def home():
    # show form to get student marks
    return render_template('enter_marks.html')

# called in the form-action in enter_marks.html, when user has entered the marks
@app.route('/submit-marks', methods = ["POST"])
def submit_marks():

    print(request.form)

    student_record = {}
    if request.method == "POST":
        student_record["name"] = request.form.get('student_name')
        student_record["english_mark"] = request.form.get('english_mark')
        student_record["maths_mark"] = request.form.get('maths_mark')
        student_record["science_mark"] = request.form.get('science_mark')
        student_record["does_homework"] = request.form.get('does_homework') == 'on'
        student_record["brings_equipment"] = request.form.get('brings_equipment') == 'on'
        student_record["works_well"] = request.form.get('works_well') == 'on'

        student_record["followup"] = request.form.get('followup')

        return render_template('data_received.html', student_record = student_record)


 