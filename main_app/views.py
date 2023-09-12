from django.shortcuts import render

# Create your views here.
finches = [
    {'species': 'House Finch', 'habitat': 'generalist', 'population trend': 'increasing'},
    {'species': 'Lawrence Goldfinch', 'habitat': 'chaparral', 'population trend': 'decreasing'}
]

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })