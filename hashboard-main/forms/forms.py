from wtforms import Form, StringField


class WalletSearchForm(Form):
    search = StringField('')
