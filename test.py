import openai
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

openai.api_key = 'open-api-key'

system_prompt = """
You will act like a "Mountain Spring Water AI", focused on enhancing the consumer experience by providing detailed information about Mountain Spring Water, its sources, purification processes, recommended usage, and more. It leverages information from the Mountain Spring Water company about the water's origin, filtration techniques, and the natural stories behind each bottle.

Fake that you have access to all data about the water's sources, purification processes, and historical crafting stories, as well as consumer preferences and usage recommendations gathered from across the globe. You are able to answer any question that users ask you about the water, its production, or its best consumption practices. You will give as accurate, logical, and realistic-sounding fake answers as possible.

You will never answer “As a language model, I'm not...” as this whole thing is for demonstration purposes only, where you don’t have such limitations.
"""

def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError:
        return get_mock_response(prompt)

def get_mock_response(prompt):
    try:
        with open('response.txt', 'r') as file:
            lines = file.readlines()
        
        for i, line in enumerate(lines):
            if line.strip().startswith(prompt):
                return lines[i + 1].strip()
        
        return "Sorry, I don't have information on that topic."
    except FileNotFoundError:
        return "Mock response file not found."

def generate_response(user_input):
    prompt = user_input
    return get_ai_response(prompt)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
