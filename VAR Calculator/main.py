class ValueAtRisk:
    
    def __init__(self, base_curr, hist_len):
        self.base_currency = base_curr
        self.history_length = hist_len
        self.equities = {}
        self.forex = {}

    def asset_import(self, asset, curr, hist):
        self.equities[asset] = {'currency' : curr, 'history': hist}

    def curr_import(self, curr, hist: tuple):
        self.forex[curr] = hist

    def get_shift(self, asset):
        rates = self.equities[asset]['history']
        shifts = [(rates[i] - rates[i-1]) / rates[i-1] for i in range(1, len(rates))]
        return shifts

    def buy(self, asset, amount):
        if asset in self.equities:
            self.equities[asset]['quantity'] = amount
        else:
            print("Asset not found!")

    def sell(self, asset, amount):
        if asset in self.equities:
            if 'quality' in self.equities[asset]:
                self.equities[asset]['quantity'] -= amount
            else:
                print("No holdings for this asset.")
        else:
            print("Asset not found.")

    def get_var(self, asset, risk_class, convidence):
        pass