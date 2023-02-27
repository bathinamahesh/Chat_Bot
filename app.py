from flask import Flask, request,jsonify
import requests


app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def index():
    try:
        data = request.get_json()
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']
        print("\n", source_currency, "  ", amount, " ->", target_currency)
        url = "https://api.apilayer.com/currency_data/convert?to=" +str(target_currency)+"&from="+str(source_currency)+"&amount="+str(amount)
        payload = {}
        headers = {
            "apikey": "1P9lFkdPAwRl2O8hPduIrCOBXpP1RENh"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
        index=result.find("result")
        print("\n\n", result[index+8:len(result)-2:], "\n")
        response={
            'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,result[index+8:len(result)-2:],target_currency)
            }
        return jsonify(response)
    except Exception as e:
        print("No Data Still ;;--", e, "\n\n")
    return "<h1>Welcome To Flask APi</h1>"


if __name__ == "__main__":
    app.run(port=5002, debug=True)
