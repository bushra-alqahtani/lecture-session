from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.


def index(request):
     #value counter will incrementing when user access the page (so its value assigned to context)
    if "counter" in request.session: #if the counter exist in our dictionary 
        counter =request.session["counter"]#if it does just read it from the session 
    else:
        counter=0 #if it doesn't the counter set as 0
        request.session["counter"]=0
    #value counter will incrementing when user access the page (so its value assigned to context)
    if "card" in request.session: #if the counter exist in our dictionary 
        card =request.session["card"]#if it does just read it from the session 
    else:
        card=[] #if it doesn't the card as list 
        request.session["card"]=[]
    shopping_items=[
        {"productName":"wa1","productText":"tray that", "img":"https://www.apple.com/mideast/apple-watch-series-7/d/images/overview/connect/en/connect_hw__cryw5lqu4ryq_large.jpg"},
        {"productName":"wa2","productText":"tray that","img":"2wCEAAoHCBYWFRgWFRUZGRgaGhoaGBoYGBocGhwaGhwaGh4hGhocIS4lHB4rIRoYJjgmKy8xNTU1GiQ7QDs0Py40NTEBDAwMEA8QHhISGjQhISE0NDQ0NDQ0NDQ0MTQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0MTQ0NDQ0NDQ0NP"},
        {"productName":"wa3","productText":"tray that","img":"https://cdn.vox-cdn.com/thumbor/eTQhbaxDs6MYk3P1i5uMICW_iuM=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/22908906/vpavic_211006_4796_0061.jpg"}
    ]

    #print how many times this page is accessed
    request.session["counter"]= counter +1 #add one for each refresh page or access page in general 
    context={
       "counter":counter,
       "card":card,
       "shopping_items":shopping_items
    }
    return render(request,"index1.html",context=context)

def add_to_card(request):
    product_name=request.POST["product_name"] #ti access it
    request.session["card"].append(product_name)#append it to card
    request.session.save()
    return redirect('/')#then redirect me to page