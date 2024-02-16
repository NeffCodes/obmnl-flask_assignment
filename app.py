from flask import Flask, request, render_template, redirct, url_for

app = Flask(__name__)

# Sample data
default_transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/')
def get_transactions(transactions):
  return render_template('transactions.html',transactions=default_transactions)
  
# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
  if request.method == 'GET':
    return render_template('form.html')
  if request.method == 'POST':
    # Create a new transaction object using form field values
    transaction = {
      'id': len(default_transactions)+1,
      'date': request.form['date'],
      'amount': float(request.form['amount'])
    }

    default_transactions.append(transaction)

    return redirct(url_for('get_transactions'))
  
# Update operation

# Delete operation

# Run the Flask app
    