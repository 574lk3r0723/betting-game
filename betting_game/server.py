from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for demonstration purposes
games = {}
users = {
    'user1': {'name': 'User 1', 'balance': 100},
    'user2': {'name': 'User 2', 'balance': 50},
    # Add more users as needed
}

# API endpoint for creating a new game
@app.route('/games', methods=['POST'])
def create_game():
    # Parse request data
    data = request.json
    user_id = data['user_id']
    numbers = data['numbers']

    # Deduct bet amount from user's balance
    bet_amount = len(numbers) * 5  # Assuming $5 per number
    if users[user_id]['balance'] < bet_amount:
        return jsonify({'error': 'Insufficient balance'}), 400

    users[user_id]['balance'] -= bet_amount

    # Generate game ID and store game data
    game_id = len(games) + 1
    games[game_id] = {'user_id': user_id, 'numbers': numbers, 'winners': []}

    return jsonify({'game_id': game_id}), 201

# API endpoint for processing game results and drink transactions
@app.route('/games/<int:game_id>/results', methods=['POST'])
def process_results(game_id):
    # Parse request data
    data = request.json
    winners = data['winners']

    # Update game data with winners
    games[game_id]['winners'] = winners

    # Handle drink transactions
    for winner in winners:
        loser_id = winner['loser_id']
        drink_amount = winner['drink_amount']

        # Deduct drink amount from winner's balance
        users[winner['winner_id']]['balance'] -= drink_amount

        # Add drink amount to loser's balance
        users[loser_id]['balance'] += drink_amount

    return jsonify({'message': 'Results processed successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
