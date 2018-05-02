from flask import Flask
from flask import request
node = Flask(__name__)

# Store the transactions that
# this node has in a list
this_nodes_transactions = []

@node.route('/txion', methods=['POST'])
def transaction():
  if request.method == 'POST':
    # On each new POST request,
    # we extract the transaction data
    new_txion = request.get_json()
    # Then we add the transaction to our list
    this_nodes_transactions.append(new_txion)
    # Because the transaction was successfully
    # submitted, we log it to our console
    print 'New transaction'
    print 'FROM: {}'.format(new_txion['from'])
    print 'TO: {}'.format(new_txion['to'])
    print 'AMOUNT: {}\n'.format(new_txion['amount'])
    # Then we let the client know it worked out
    return 'Transaction submission successful\n'

node.run()
