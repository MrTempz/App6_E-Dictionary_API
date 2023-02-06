from flask import Flask, render_template
import pandas as pd
from os import path

app = Flask(__name__)

data_file = path.join('data', 'dictionary.csv')
df = pd.read_csv(data_file)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/api/v1/<word>")
def about(word: str):
    
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    print(definition)
    return {'word': word,
            'definition': definition
            }
if __name__ == '__main__':
     app.run(debug=True, port=5001)