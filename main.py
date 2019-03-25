def main():
    import spacy
    from spacy import displacy
    from IPython.display import display, HTML, Javascript

    colors = {'CURR_PAIRS': 'linear-gradient(90deg, #aa9cfc, #fc9ce7)',
              'VALUE': 'linear-gradient(180deg, #f920eb, #4957ed)',
              'RATES_UP': 'linear-gradient(90deg, #72db4c, #17ecef)',
              'RATES_DOWN': 'linear-gradient(45deg, #0050ff, #fff600)'}
    options = {'ents': ['CURR_PAIRS', 'CURRENCY', 'RATES_UP', 'RATES_DOWN', 'VALUE'], 'colors': colors}

    nlp = spacy.load('curr_ner')

    articles = [
        'If the mood among investors deteriorates, cyclical currencies come under pressure. We expect that EUR / USD will now rise again towards 1, 19 - 1, 20.',
        'EUR/USD leaps to daily highs near 1.1320 on upbeat IFO.',
        'EUR/USD Technical Analysis: Rising odds for another visit to YTD lows near 1.1180.',
        'EUR/USD is trading above 1.1300 in the wake of the new week, slightly higher.',
        'With Brexit uncertainty weighing, the GBP/USD is expected to test the cyclical low of 1.2200.',
        'he greenback is the overall winner this year, with the AUD/USD pair top at 0.8135 in January.',
        'A stock market crash in February triggered a significant risk-off sentiment that was well reflected in USD/JPY falling below 105']

    for article in articles:
        doc = nlp(article)


        up_key = False
        down_key = False
        rates_up = ['highs', 'rise', 'rising', 'higher', 'top']
        rates_down = ['low', 'falling']
        for i in rates_up:
            if article.find(i) != -1:
                up_key = True
                break
        for i in rates_down:
            if article.find(i) != -1:
                down_key = True
                break

        s = ''
        for i in doc.ents:
            if i.label_ == 'CURR_PAIRS':
                s += i.text.replace(' ', '') + '  '

        for i in doc.ents:
            if i.label_ == 'VALUE':
                s += i.text.replace(' ', '') + '  '

        if up_key:
            s += '↑'
        elif down_key:
            s += '↓'
        else:
            s += '--'

        displacy.render(doc, style='ent', jupyter=True, options=options)
        display(HTML("<span style='background-color: red;'>" + s + '</span><br><br>'))


