from django.shortcuts import render


ITEMS = [
    {"name": "Burger", "category": "food", "price": 50, "available": True},
    {"name": "Pizza", "category": "food", "price": 80, "available": True},
    {"name": "Pasta", "category": "food", "price": 60, "available": False},
    {"name": "Cola", "category": "drink", "price": 15, "available": True},
    {"name": "Orange Juice", "category": "drink", "price": 25, "available": True},
    {"name": "Coffee", "category": "drink", "price": 20, "available": False},
]

def search_items(request):
    query = request.GET.get('q', '').lower()
    category = request.GET.get('category', '').lower()
    
    filtered_items = ITEMS
    
    if category:
        filtered_items = [item for item in filtered_items  if item["category"] == category]
    
    if query:
        filtered_items = [item for item in filtered_items if query in item["name"].lower()]
    return render(request, 'base.html', {"items": filtered_items})