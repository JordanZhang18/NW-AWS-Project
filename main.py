from flask import Flask, request, render_template
import numpy as np                                
import pandas as pd                               
import matplotlib.pyplot as plt    
import matplotlib
from io import BytesIO
import s3fs
import base64

bucket='msds-capstone-project'
data_key = '2015cleaned.csv'
data_location = 's3://{}/{}'.format(bucket, data_key)

new_data=pd.read_csv(data_location)

app = Flask(__name__)

matplotlib.use('Agg')

def histogram_plot (Major, Column):
    try:
        img = BytesIO()

        subset1=new_data[['Education.Major',Column]]
        metric=subset1.loc[subset1['Education.Major'] ==Major][Column]
        s = subset1[Column]
        p = s.plot(kind='hist', bins=20, color='orange')

        bar_value_to_label = np.array(metric)[0]
        min_distance = 100 # initialize min_distance with infinity
        index_of_bar_to_label = 0
        for i, rectangle in enumerate(p.patches):  # iterate over every bar
            tmp = abs(  # tmp = distance from middle of the bar to bar_value_to_label
                (rectangle.get_x() +
                    (rectangle.get_width() * (1 / 2))) - bar_value_to_label)
            if tmp < min_distance:  # we are searching for the bar with x cordinate
                                    # closest to bar_value_to_label
                min_distance = tmp
                index_of_bar_to_label = i
        p.patches[index_of_bar_to_label].set_color('b')
        plt.title(Column +' Distribution with '+Major+' Major highlighted')
        plt.savefig(img, format='png',bbox_inches='tight')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        return plot_url
    except:
        return 'Sorry, error!'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def DrawPost():
    Major1=request.form['Major']
    Column1=request.form['Metric']
    plot_url = histogram_plot (Major1, Column1)
    
    return render_template("histograms.html",plot_url=plot_url)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)