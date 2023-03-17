from django.shortcuts import render,redirect
from .models import Product,prod_images,Review
from django.contrib.auth.models import User
from django.contrib.auth  import logout
import requests

# Create your views here.
def index(request):
    allProds = Product.objects.values()
    
        
    
        
    params = {'allProds':allProds}
    return render(request, 'index.html', params)

def productview(request,myid):

    # fetch details
    product = Product.objects.filter(product_id=myid).values()
    photos = prod_images.objects.filter(prod=myid)
    this_reviews = Review.objects.filter(product=myid).values()

    # check user feedback
    emails = []
    for i in this_reviews:
        
        emails.append(i['email'])
    if request.user.email in emails:
        done=True
    else:
        done =False


    # accept feedback
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        comment = request.POST.get('review','')
        rating = request.POST.get('rating','')
        feedback=Review(name=name,email=email,comment=comment,rate=rating,product=myid)
        feedback.save()
    


    # calculate reviews
    total = 0
    ratings=0
    for review in this_reviews:
        total+=1
        ratings+=review['rate']
    def myround(x, base=1):
        return base * round(float(x) / base)
    star_count= myround(ratings/total)
    print(ratings/total)
    stars = [ 1  if i<=star_count else 0 for i in range(5) ]
    print(stars)
    return render(request,'prodview.html',{
        'product':product[0],
        'product_id':myid,
        'photos':photos,
        'reviews':this_reviews,
        'done':done,
        'stars':stars
    })


def get_user_email(access_token):
    r = requests.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            params={'access_token': 'https://oauth2.googleapis.com/token'})
    return r.json()
def handelLogout(request):
    logout(request)
    
    return redirect('/')

