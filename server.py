import base64
import json
from flask import Flask, render_template, request
from worker import speech_to_text, text_to_speech, openai_process_message
from flask_cors import CORS
import os

# Itinitalise Flask
app = Flask(__name__)

# Set CORS policy. 
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# A CORS policy is used to allow or prevent web pages from making 
# requests to different domains than the one that served the web page. 
# Currently, it is set to * to allow any request.



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')# Frontend interface


@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print("processing speech-to-text")
    audio_binary = request.data # Get the user's speech from their request
    text = speech_to_text(audio_binary) # Call speech_to_text function to transcribe the speech

    # Return the response back to the user in JSON format
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    if 'results' in response and response['results']:
        text = response['results'][0]['alternatives'][0]['transcript']
        print('recognised text: ', text)
        print(response)
        print(response.data)
        return text
    else:
        return 'No speech detected'



@app.route('/process-message', methods=['POST'])
def process_message_route():
    try:
        user_message = request.json['userMessage']  # Get user's message from their request
        print('user_message', user_message)

        voice = request.json.get('voice', '')  # Get user's preferred voice from their request, default to empty string
        print('voice', voice)

        # Call openai_process_message function to process the user's message and get a response back
        openai_response_text = openai_process_message(user_message)

        # Clean the response to remove any empty lines
        openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])

        # Call our text_to_speech function to convert OpenAI API's response to speech
        openai_response_speech = text_to_speech(openai_response_text, voice)

        # Convert openai_response_speech to base64 string so it can be sent back in the JSON response
        openai_response_speech = base64.b64encode(openai_response_speech).decode('utf-8')

        # Send a JSON response back to the user containing their message's response both in text and speech formats
        response = app.response_class(
            response=json.dumps({"openaiResponseText": openai_response_text, "openaiResponseSpeech": openai_response_speech}),
            status=200,
            mimetype='application/json'
        )

        print(response)
        return response

    except KeyError as e:
        error_message = f"Missing expected key in JSON request: {str(e)}"
        print(error_message)
        return app.response_class(
            response=json.dumps({"error": error_message}),
            status=400,
            mimetype='application/json'
        )
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        return app.response_class(
            response=json.dumps({"error": error_message}),
            status=500,
            mimetype='application/json'
        )

if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0') # localhost
