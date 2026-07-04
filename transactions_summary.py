import csv

category_totals = {}

with open("transactions.csv", mode="r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        try:
            category = row["category"]
            amount = int(row["amount"])
            
            if not category.strip():
                raise ValueError("category is missing")
                
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
                
        except(ValueError,TypeError) as e:
            print(f"Skipping invalid row {row} : {e}")
        
        
    sorted_totals = sorted(
        category_totals.items(),
        key = lambda item:item[1],
        reverse = True
        )
    
    for category , totals in sorted_totals:
        print(f"{category} : {totals}")