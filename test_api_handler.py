from   datetime  import datetime
import pandas    as pd
import requests
import json

df = pd.read_csv('dataset/cardio_train.csv', sep=';')
df = df.sample(5)

json_df = json.dumps(df.to_dict(orient = 'records'))

def predict(data):
    # API Call

    # Web URL
    # url =  'https://healthinsurance-webapp-api.onrender.com/healthinsurance/predict'  

    # Local URL
    url = 'https://dc36-54-172-217-41.ngrok-free.app/cardio'

    header = {'Content-type': 'application/json' }
    data = data
    r = requests.post( url, data = data, headers = header )
    print( 'Status Code {}'.format( r.status_code ) )
    d1 = pd.DataFrame(r.json(), columns = r.json()[0].keys())
    d1.sort_values('predictions', ascending = False)
    return d1['predictions']

predictions = predict(json_df)
print(predictions)

# Export data
predictions.to_csv('dataset/predictions/predictions2.csv', index = False)