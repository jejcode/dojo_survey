from flask import Flask, render_template, redirect, request, session # import Flask and other tools

app = Flask(__name__) # create an instance of Flask
app.secret_key = "my secret key"
@app.route('/')
def survey():
    session.clear()
    return render_template('survey.html')

@app.route('/process', methods=['POST']) # route to save form data into session and pass it on to /result
def process_form():
    session['data'] = request.form # saves all form data in session
    snacks = []
    for n in range(1,5): # check to see if any snacks were selected
        key = 'snack' + str(n)
        if key in request.form:
            snacks.append(session['data'][key]) # add snack to snack list
    if len(snacks) > 0:
        session['snacks'] = snacks # if there is a snack list, add it to session for results route
    return redirect('/result') # redirect to avoid repeated inputs

@app.route('/result')
def display_result():
    print(session['data'])
    return render_template('results.html')
    
if __name__ == '__main__':
    app.run(debug = True, port = 8000) # port 5000 us used on a Mac