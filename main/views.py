from django.shortcuts import render,redirect
from .models import Product,prod_images,Review,CouponCode,Orders
from django.contrib.auth.models import User
from django.contrib.auth  import logout
import requests
from datetime import date

# Create your views here.


def index(request):
    allProds = Product.objects.values()
    print(allProds)
    
    
    params = {'allProds':allProds}
    return render(request, 'index.html', params)



#==================================== accept feedback ====================================================================================
#  if request.method == "GET":
#         try:
#             name = request.GET.get('name','')
#             email = request.GET.get('email','')
#             comment = request.GET.get('review','')
#             rating = request.GET.get('rating','')
#             user_review = str(myid) + email
#             product_name = request.GET.get('product_name','')
#             feedback=Review(name=name,email=email,comment=comment,rate=rating,product=myid ,product_name=product_name,user_review=user_review)
#             feedback.save()
#         except Exception as e:
#             print(e)






def productview(request,myid):

    # fetch details
    product = Product.objects.filter(product_id=myid).values()
    photos = prod_images.objects.filter(prod=myid)
    
    this_reviews = Review.objects.filter(product=myid).values()

    
    # check user feedback
    emails = [i['email'] for i in this_reviews]
    

    try:

        if request.user.email in emails:
            done=True
            user_review = this_reviews.filter(email= request.user.email)[0]
        else:
        
            done =False
            user_review = False
        logged_in =True
    except Exception as e:
        print(e)
        logged_in = False
        done=False
        user_review=False

    # calculate reviews
    total = 0
    ratings= 0
    for review in this_reviews:
        total+=1
        ratings+=review['rate']
    def myround(x, base=1):
        return base * round(float(x) / base)
    if total!=0:
        star_count= myround(ratings/total)
    else:
        star_count = 0
    
    stars = [ 1  if i<star_count else 0 for i in range(5) ]
    
    this_reviews=this_reviews[::-1]
    return render(request,'prodview.html',{
        'product':product[0],
        'product_id':myid,
        'photos':photos,
        'reviews':this_reviews,
        'done':done,
        'stars':stars,
        'logged_in':logged_in,
        'user_review':user_review,
    })







def cart(request):
    return render(request,'cart.html')


def checkout(request):
    coupons = CouponCode.objects.values()
    used = CouponCode.objects.filter(used_by = request.user).values()

    for i in coupons:
        
        if i in used:
            i['not_used']=False
        else:
            i['not_used'] =True

        if i['validity'].date() >date.today():
            i['valid'] = True
        else:
            i['valid'] =False
        i['can_be_used'] = i['not_used'] and i['valid'] 
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name','')
        amount = request.POST.get('amount','')
        email = request.POST.get('email','')
        address = request.POST.get('address','') + "  "+request.POST.get('address2','')
        city = request.POST.get('city','')
        postal_code = request.POST.get('postal_code','')
        phone = request.POST.get('phone','')
        payment_ref = request.POST.get('utr','')
        instructions = request.POST.get('instructions','')
        coupon_used = request.POST.get('coupon','') 
        this_coupon = CouponCode.objects.filter(coupon = this_coupon)
        this_coupon.used_by.add(request.user)
        order=Orders(items_json=itemsJson,
                     name=name,
                     email=email,
                     phone_number=phone,
                     address=address,
                     city=city,
                     
                     postal_code=postal_code,
                     amount=amount,
                     coupon_used = coupon_used,
                     instructions = instructions,
                     payment_conf = 0,
                     payment_ref=payment_ref,
                     delivered = 0,
                     dispatched = 0,
                     link = "0",
                     declined=0)
        order.save()
    return render(request,'checkout.html',{'coup':coupons})

def get_user_email(access_token):
    r = requests.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            params={'access_token': 'https://oauth2.googleapis.com/token'})
    return r.json()
def handelLogout(request):
    logout(request)
    
    return redirect('/')

