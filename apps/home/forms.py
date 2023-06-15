from django import forms

class FilterForm(forms.Form):
    
    # class Meta:
    #   fields = '__all__'

    filter_candlestick_pattern = forms.BooleanField(
        label="Candlestick Pattern",
        # default=True
        )
    filter_index_trend = forms.BooleanField(
        label="Index Trend",
        # default=True
        )
    filter_index_value = forms.BooleanField(
        label="Index Value",
        # default=True
        )
    filter_strategic_stop = forms.BooleanField(
        label="Strategic Stop",
        # default=True
        )
    filter_buy = forms.BooleanField(
        label="Buy",
        # default=True
        )
    filter_sell = forms.BooleanField(
        label="Sell",
        # default=True
        )
    filter_wait = forms.BooleanField(
        label="Wait",
        # default=True
        )