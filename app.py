from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json.get('user_choice')
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = get_game_result(user_choice, computer_choice)
    return jsonify({"result": result, "computer_choice": computer_choice})

def get_game_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "We Tied!"
    elif (user_choice == 'Rock' and computer_choice == 'Paper') or\
         (user_choice == 'Paper' and computer_choice == 'Scissors') or\
         (user_choice == 'Scissors' and computer_choice == 'Rock'):
        return "Looks like you lost"
    else:
        return "You win!"

if __name__ == '__main__':
    app.run(debug=True)


