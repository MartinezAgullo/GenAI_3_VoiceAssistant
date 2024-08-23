# Voice Assistant
 Voice Assistant with Open AI's GPT-3 and IBM Watson embedebale AI. 

  - GPT-3: Enables the assistant to undertand and respond to user input: Using "gpt-3.5-turbo"
  - Watson AI
    - Watosn Speech To Text (STT): Allowsthe  assistant to hear to user's response.
    - Watson Text To Speech (TTS): Allows the assistant to read the answers back to the user.

<img src="https://github.com/MartinezAgullo/GenAI_3_VoiceAssistant/tree/main/tmp/Voice-lightmode.png" alt="css result" width="600"/>





## Composition

  - Backend: Python and Flask
  - Iterface: HTML, CSS, an JavaScript
  - Functionality to understand voice input: [STT](https://www.ibm.com/products/speech-to-text#:~:text=IBM%20Watson%C2%AE%20Speech%20to,agent%20assistance%20and%20speech%20analytics.)
  - Intelligence: [GPT-3](https://openai.com/index/gpt-3-apps/)
  - Functionality for spoken responses: [TTS](https://www.ibm.com/products/text-to-speech)

## Ussage

<!-- > pip install -r requirements.txt -->

Using the Docker image to simplify the deployement process. I'm doing this on [Skills Network](https://skills.network/) lab.
> cp /usr/local/share/ca-certificates/rootCA.crt /home/project/chatapp-with-voice-and-openai/certs/
> docker build . -t voice-chatapp-powered-by-openai
> docker run -p 8000:8000 voice-chatapp-powered-by-openai


Check a of languahes it can recognize and available voices with:
> curl https://sn-watson-stt.labs.skills.network/speech-to-text/api/v1/models
> curl https://sn-watson-tts.labs.skills.network/text-to-speech/api/v1/voices


## Credits
This repository contains solutions and work done for the thrid module of the course[Building Generative AI-Powered Applications with Python](https://www.coursera.org/learn/building-gen-ai-powered-applications). All rights and credits go to the course creators and instructors. This work is shared for personal use and academic purposes only.

The original scripts can be foudn in [chatapp-with-voice-and-openai-outline](https://github.com/arora-r/chatapp-with-voice-and-openai-outline.git). Download them with

> git clone https://github.com/arora-r/chatapp-with-voice-and-openai-outline.git