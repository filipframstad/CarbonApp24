from flask import render_template, Blueprint
carbon_app=Blueprint('carbon_app',__name__)

@carbon_app.route('/carbon_app')
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

@carbon_app.route('/carbon_app/new_entry')
def new_entry_home():
    return render_template('new_entry.html', title='new_entry')

@carbon_app.route('/carbon_app/your_data')
def your_data_home():
    return render_template('your_data.html', title='your_data')
