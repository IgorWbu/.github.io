from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Define a list of dictionaries containing movie and event information
movie_events = [
    {"movie": "The Social Network", "year": 2010, "event": "Launch of Instagram", "event_year": 2010},
    {"movie": "Inception", "year": 2010, "event": "Deepwater Horizon oil spill", "event_year": 2010},
    {"movie": "The Dark Knight", "year": 2008, "event": "Beijing Olympics", "event_year": 2008},
    {"movie": "Avatar", "year": 2009, "event": "Barack Obama's inauguration as President of the United States", "event_year": 2009},
    {"movie": "Iron Man", "year": 2008, "event": "Lehman Brothers bankruptcy", "event_year": 2008},
    {"movie": "The Lord of the Rings: The Return of the King", "year": 2003, "event": "Space Shuttle Columbia disaster", "event_year": 2003},
    {"movie": "The Matrix", "year": 1999, "event": "Euro currency introduced", "event_year": 1999},
    {"movie": "Forrest Gump", "year": 1994, "event": "Nelson Mandela elected President of South Africa", "event_year": 1994},
    {"movie": "Jurassic Park", "year": 1993, "event": "World Wide Web goes public", "event_year": 1993},
    {"movie": "Terminator 2: Judgment Day", "year": 1991, "event": "Dissolution of the Soviet Union", "event_year": 1991},
    {"movie": "The Silence of the Lambs", "year": 1991, "event": "World Wide Web goes public", "event_year": 1993},
    {"movie": "Die Hard", "year": 1988, "event": "Chernobyl disaster", "event_year": 1986},
    {"movie": "Back to the Future", "year": 1985, "event": "Chernobyl disaster", "event_year": 1986},
    {"movie": "E.T. the Extra-Terrestrial", "year": 1982, "event": "Chernobyl disaster", "event_year": 1986},
    {"movie": "Raiders of the Lost Ark", "year": 1981, "event": "Chernobyl disaster", "event_year": 1986},
    {"movie": "The Empire Strikes Back", "year": 1980, "event": "Chernobyl disaster", "event_year": 1986},
    {"movie": "Star Wars", "year": 1977, "event": "Chernobyl disaster", "event_year": 1986},
    {"movie": "Jaws", "year": 1975, "event": "Chernobyl disaster", "event_year": 1986},
    {"movie": "The Godfather", "year": 1972, "event": "Chernobyl disaster", "event_year": 1986},
    {"movie": "The Godfather: Part II", "year": 1974, "event": "Chernobyl disaster", "event_year": 1986},
]

# Function to generate a random question
def generate_question():
    # Choose a random movie-event pair
    movie_event = random.choice(movie_events)
    # Generate the question string
    question = f"Was the movie '{movie_event['movie']}' released before or after the {movie_event['event']}?"
    # Determine the correct answer
    if movie_event['year'] < movie_event['event_year']:
        answer = "before"
    else:
        answer = "after"
    return question, answer

# Function to check if the user's answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

# Route to serve the game HTML page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    # Generate a random question
    question, answer = generate_question()
    return render_template("game.html", question=question)


# Route to handle the user's answer
@app.route('/check_answer', methods=['POST'])
def check_user_answer():
    # Get the user's choice from the request
    user_choice = request.json.get('choice')

    # Determine if the user's answer is correct
    correct_answer = request.json.get('correct_answer')
    is_correct = check_answer(user_choice, correct_answer)

    # Prepare the response
    response = {'is_correct': is_correct}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
