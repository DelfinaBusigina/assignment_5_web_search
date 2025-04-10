from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    df1, df2, merged = None, None, None

    if request.method == 'POST':
        file1 = request.files.get('file1')
        file2 = request.files.get('file2')
        join_type = request.form.get('joins')
        join_on_col = request.form.get('on_col')

        if file1 and file2:
            df1 = pd.read_csv(file1)
            df2 = pd.read_csv(file2)
            merged = pd.merge(df1, df2, how=join_type, on=join_on_col)  # adjust 'how' as needed

    return render_template('index.html',
                           tables=[df1.to_html(classes='data') if df1 is not None else '',
                                   df2.to_html(classes='data') if df2 is not None else '',
                                   merged.to_html(classes='data') if merged is not None else ''])

if __name__ == '__main__':
    app.run(debug=True)