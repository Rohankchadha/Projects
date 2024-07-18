import requests

url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
headers = {'Content-Type':'application/json', 'x-app-id':'cf603149', 'x-app-key':'cbbd0d41f6db22ef430c149072faa50a'}
def get_data(q):
    try:
        data={
        "query":q,
        "timezone": "US/Eastern"
        }

        res=requests.post(url, headers=headers, json=data)
        print(res.status_code)
        n_data=[]
        for i in range(len(res.json()['foods'])):
            name=("Name-"+str(res.json()['foods'][i]['food_name']))
            qty=("Quantity-"+str(res.json()['foods'][i]['serving_qty']))
            serv=("Serving-"+str(res.json()['foods'][i]['serving_unit']))
            weight=("Weight-"+str(res.json()['foods'][i]['serving_weight_grams']))
            cal=("Calories-"+str(res.json()['foods'][i]['nf_calories']))
            fat=("Fats-"+str(res.json()['foods'][i]['nf_total_fat']))
            cho=("Cholesterol-"+str(res.json()['foods'][i]['nf_cholesterol']))
            carbs=("Carbs-"+str(res.json()['foods'][i]['nf_total_carbohydrate']))
            fiber=("Fiber-"+str(res.json()['foods'][i]['nf_dietary_fiber']))
            sugars=("Sugars-"+str(res.json()['foods'][i]['nf_sugars']))
            protein=("Protein-"+str(res.json()['foods'][i]['nf_protein']))
            n_data.append([name,qty,serv,weight,cal,fat,cho,carbs,fiber,sugars,protein])
        return True,n_data
    except:
        return False, None
# print(res.json())
# units - 
# carbs, protein, fats, weight, sugars, fibers = g
# cholesterol, potassium, sodium = mg
got_data=get_data('couple of drumsticks and a coke')
