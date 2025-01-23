from flask import Flask, render_template, request
from python import bitcoin_wallet as btc
from forms import forms

app = Flask(__name__)

# Variable to keep track of the user selected currency, with GBP as the default
global currency
currency = "GBP"


@app.route("/", methods=['GET', 'POST'])
def homepage():
    # If the search form is used
    search = forms.WalletSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template("index.html", form=search, title="Hashboard Search")


@app.route('/results', methods=['GET', 'POST'])
def search_results(search):
    global currency  # Get prefered currency to display results in
    search_string = search.data['search']
    wallet = btc.Wallet(search_string)
    search = forms.WalletSearchForm(request.form)
    if wallet.get_exists():
        return render_template('results.html', results=search_string, wallet=wallet, form=search, currency=currency, wallet_value=wallet.get_current_balance_fiat(currency), title="Hashboard Search")
    else:
        return render_template('results_not_found.html', form=search, title="Hashboard Search")


@app.route('/settings', methods=['GET', 'POST'])
def settings_page():
    message = ""
    # If the update button is pressed
    if request.method == 'POST':
        global currency
        currency = request.form['currency']
        message = "Settings Updated."

    return render_template("settings.html", title="Settings", currency=currency, message=message)


if __name__ == "__main__":
    app.run(debug=True)
