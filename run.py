from myapp import create_app, db
from myapp.models import FoodItem
import json

app = create_app()

def populate_db():
    with app.app_context():
        db.drop_all()  # Drops all tables
        db.create_all()  # Recreate them

        # Load the data from JSON file
        with open('out.json') as f:
            data = json.load(f)
            for list in data["list"]:
                for item in list['data']['items']:
                    food_item = FoodItem(
                    id=item['id'],
                    name=item['name'],
                    count=item['count'],
                    point=item['point'],
                    showAlternative=item['showAlternative'],
                    foodType=item['foodType']
                    )

                    db.session.add(food_item)

        db.session.commit()

populate_db()

if __name__ == '__main__':
    app.run(debug=True)
