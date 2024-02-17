from django.shortcuts import render
from .models import Board
from rest_framework import viewsets
from .serializers import BoardSerializer

def board_list(request):
    board_list = Board.objects.all()
    return render(
        request, 
        'board/board_list.html', 
        {
            'board_list': board_list
        }
    )
    

def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(
        request, 
        'board/board_detail.html', 
        {
            'board': board
        }
    )
    
    
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer