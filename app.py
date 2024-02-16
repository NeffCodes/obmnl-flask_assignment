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
@app.route('/edit/<int:transaction_id>', methods=['GET','POST'])
def edit_transaction(transaction_id):
  if request.method == 'GET':
    for transaction in default_transactions:
      if transaction['id'] == transaction_id:
        return render_template('edit.html', transaction)
  if request.method == 'POST':
    date = request.form['date']
    amount = float(request.form['amount'])

    for transaction in default_transactions:
      if transaction['id'] == transaction_id:
        transaction['date'] = date
        transaction['amount'] = amount
        break
      
    return redirct(url_for('get_transactions'))  

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
  for transaction in default_transactions:
    if transaction['id'] == transaction_id:
      default_transactions.remove(transaction)
      break
    
  return redirct(url_for("get_transactions"))

# run flask app
if __name__ == "__main__":
  app.run(debug=True)

# Run the Flask app
    