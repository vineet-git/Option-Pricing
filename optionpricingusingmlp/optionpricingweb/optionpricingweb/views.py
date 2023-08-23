from django.shortcuts import render
def home(request):    
    return render(request, 'index.html')

def getPredictions(Strike_Price,Expiration,Adj_Close,Price,volatility):
    from keras.models import model_from_json
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("mlpmodel.h5")
    prediction=loaded_model.predict(Strike_Price,Expiration,Adj_Close,Price,volatility)
    return prediction

def result(request):
    Strike_Price = float(request.GET['Strike Price'])
    Expiration = int(request.GET['Expiration'])
    Adj_Close = float(request.GET['Adj_Close'])
    Price= int(request.GET['Price'])
    volatility = float(request.GET['volatility'])

    result = getPredictions(Strike_Price,Expiration,Adj_Close,Price,volatility)
    return render(request, 'result.html', {'result':result})
