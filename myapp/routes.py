from flask import Blueprint, render_template, request, jsonify
from .models import FoodItem
import json

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('query')
        food_items = FoodItem.query.filter(FoodItem.name.contains(name)).all()
        res = {'food_items': [food_item.to_dict() for food_item in food_items]}
        # Converting the SQLAlchemy objects to dictionaries
        food_items = [food_item.to_dict() for food_item in food_items]
        #return jsonify(food_items)
        return jsonify({'foodItems': food_items})   
    return render_template('index.html')
