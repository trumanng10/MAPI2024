from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model for votes
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Vote option={self.option}, count={self.count}>"

# Initialize the database
def create_tables():
    with app.app_context():
        db.create_all()

# Route to get the current vote counts
@app.route('/votes', methods=['GET'])
def get_votes():
    votes = Vote.query.all()
    return jsonify({vote.option: vote.count for vote in votes})

# Route to vote for an option
@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    option = data.get('option')

    if not option:
        return jsonify({"error": "Option is required"}), 400

    vote = Vote.query.filter_by(option=option).first()

    if vote:
        vote.count += 1
    else:
        new_vote = Vote(option=option, count=1)
        db.session.add(new_vote)

    db.session.commit()
    return jsonify({"message": f"Vote for {option} recorded successfully"}), 200

# Route to reset votes
@app.route('/reset', methods=['POST'])
def reset_votes():
    Vote.query.delete()
    db.session.commit()
    return jsonify({"message": "Votes have been reset"}), 200

# Run the app
if __name__ == '__main__':
    create_tables()  # Make sure tables are created before running the app
    app.run(debug=True, host="0.0.0.0", port=5000)
