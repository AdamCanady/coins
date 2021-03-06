import coinbase.wallet.client

import config

NAME = 'Coinbase'


def get_balances():
  client = coinbase.wallet.client.Client(
      config.COINBASE_KEY, config.COINBASE_SECRET)
  accounts = client.get_accounts().data
  balances = {account['currency']: float(account['balance']['amount'])
              for account in accounts}
  return balances


if __name__ == '__main__':
  balances = get_balances()
  for symbol, balance in balances.iteritems():
    if balance > 0:
      print '%6s %.3f' % (symbol, balance)
