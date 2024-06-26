
"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
from flask import Flask, render_template, request, jsonify, url_for, redirect, session, flash
import google.generativeai as genai
app = Flask(__name__)
# Add Your API Key from http://makersuite.google.com
genai.configure(api_key="REPLACE_WITH_YOUR_API_KEY_HERE")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hi"]
  },
  {
    "role": "model",
    "parts": ["Hello there! Welcome to Career Compass, your personalized guide to navigating the exciting world of career choices. I'm here to assist you in discovering potential career paths that align with your unique skills and aptitudes. Let's embark on this journey together! \nTo start, could you please share your scores from your aptitude test? This will provide valuable insights into your strengths and preferences, allowing me to offer tailored career recommendations."]
  },
])






app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/loginregpage')
def login():
    return render_template('login.html')



@app.route('/chatbotpage')
def chatbotpage():
    # Retrieve user information from session
    # user = session.get('user', None)

    # Check if user is logged in
    # if user:
        # Pass the username to the template
    return render_template('chatbot.html')
    # else:
    #     # Redirect to login page if not logged in
    #     flash('Please log in first', 'error')
    #     return redirect(url_for('loginregpage'))
@app.route('/ask', methods=['POST'])
def ask():
    # Retrieve user input from the POST request
    user_input = request.form.get('user_message')

    # Send user input to the generative model
    convo.send_message(user_input)

    # Get the model's response
    bot_response = convo.last.text

    # Return the response in JSON format
    return jsonify({'bot_response': bot_response, 'user_input': user_input})

@app.route('/edu')
def edu():
    return render_template('demo.html')

@app.route('/ten')
def ten():
    return render_template('tenth.html')
@app.route('/twe')
def twe():
    return render_template('twelth.html')
@app.route('/high')
def high():
    return render_template('proof.html')

@app.route('/numten')
def numten():
    return render_template('num10.html')

@app.route('/numtwe')
def numtwe():
    return render_template('num12.html')

@app.route('/quant')
def quant():
    return render_template('quant.html')

@app.route('/arten')
def arten():
    return render_template('ar10.html')

@app.route('/artwe')
def artwe():
    return render_template('ar12.html')

@app.route('/abstr')
def abstr():
    return render_template('abstr.html')

@app.route('/verbten')
def verbten():
    return render_template('verb10.html')

@app.route('/verbtwe')
def verbtwe():
    return render_template('verb12.html')

@app.route('/verbal')
def verbal():
    return render_template('verbal.html')

@app.route('/spten')
def spten():
    return render_template('sp10.html')

@app.route('/sptwe')
def sptwe():
    return render_template('sp12.html')

@app.route('/spat')
def spat():
    return render_template('spat.html')

@app.route('/mechten')
def mechten():
    return render_template('mech10.html')

@app.route('/mechtwe')
def mechtwe():
    return render_template('mech12.html')

@app.route('/mech')
def mech():
    return render_template('mech.html')

@app.route('/perten')
def perten():
    return render_template('per10.html')

@app.route('/pertwe')
def pertwe():
    return render_template('per12.html')

@app.route('/peracc')
def peracc():
    return render_template('peracc.html')

@app.route('/langten')
def langten():
    return render_template('lang10.html')

@app.route('/langtwe')
def langtwe():
    return render_template('lang12.html')

@app.route('/lang')
def lang():
    return render_template('lang.html')

@app.route('/result')
def result():
    return render_template('results.html')

@app.route('/appoint')
def appoint():
    return render_template('appointment.html')
@app.route('/manage')
def manage():
    return render_template('manage-appointment.html')

@app.route('/book')
def book():
    return render_template('index2.html')
@app.route('/admin')
def admin():
    return render_template('admin-login.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')




if __name__ == '__main__':
    app.run(debug=True)