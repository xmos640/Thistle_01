from django.shortcuts import render,redirect
from .models import Product,prod_images,Review,CouponCode,Orders,announcement
from django.contrib.auth.models import User
from django.contrib.auth  import logout
import requests
from datetime import date,datetime,timedelta
import json

# Create your views here.
try:
    announcement1 = announcement.objects.values()[0]
except:
    announcement1 = False
print(announcement)


def index(request):
    allProds = Product.objects.values()
    
    
    
    params = {'allProds':allProds,'announcement':announcement1}
    return render(request, 'index.html', params)



#==================================== accept feedback ====================================================================================
 






def productview(request,myid):
    if request.method == "GET":
        try:
            name = request.GET.get('name','')
            email = request.GET.get('email','')
            comment = request.GET.get('review','')
            rating = request.GET.get('rating','')
            user_review = str(myid) + email
            product_name = request.GET.get('product_name','')
            feedback=Review(name=name,email=email,comment=comment,rate=rating,product=myid ,product_name=product_name,user_review=user_review)
            feedback.save()
        except Exception as e:
            print(e)
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
        'announcement':announcement1
    })







def cart(request):
    params={'announcement':announcement1}
    return render(request,'cart.html',params)


def checkout(request):
    coupons = CouponCode.objects.values()
    try:
        used = CouponCode.objects.filter(used_by = request.user).values()
    except:
        used = []

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
    
    return render(request,'checkout.html',{'coup':coupons,'announcement':announcement1})

def get_user_email(access_token):
    r = requests.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            params={'access_token': 'https://oauth2.googleapis.com/token'})
    return r.json()
def handelLogout(request):
    logout(request)
    
    return redirect('/')

def orders(request):
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name','')
        amount = request.POST.get('amount','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        postal_code = request.POST.get('postal_code','')
        phone = request.POST.get('phone','')
        payment_ref = request.POST.get('utr','')
        instructions = request.POST.get('instructions','')
        coupon_used = request.POST.get('coupon','') 
       
        items = (json.loads(itemsJson)).values()
        cart = []
        number_of_items = 0
        for i in items:
            item_details = [i[1],i[0]]
            number_of_items +=i[0]
            cart.append(item_details)

            
        try:
            this_coupon = CouponCode.objects.filter(coupon = coupon_used)[0]
        except:
            pass
        today = datetime.today()
        delivery_date = today + timedelta(days=7)
        
        order=Orders(items_json=itemsJson,
                     cart=cart,
                     number_of_items=number_of_items,
                     name=name,
                     email=email,
                     phone_number=phone,
                     Address=address,
                     city=city,
                     
                     postal_code=postal_code,
                     amount=int(float(amount)),
                     coupon_used = coupon_used+".",
                     instructions = instructions+".",
                     payment_conf = 0,
                     payment_ref=payment_ref,
                     delivered = 0,
                     dispatched = 0,
                     link = "0",
                     declined=0,
                     delivery_date=delivery_date,
                     )
        order.save()
        try:
            this_coupon.used_by.add(request.user)
        except:
            pass
    
    
    this_user = 0
    try:
        this_user = request.user.email
        orders = Orders.objects.filter(email = this_user).values()

        allOrders= [order for order in orders]
        allOrders=allOrders[::-1]
        print(allOrders,1)
        for i in allOrders:
            items = (json.loads(i['items_json']))
            i['items_json']=items.values()
            
            
        count = len(allOrders)
        
    except Exception as e:
        allOrders = False
        count = False
        
    
    params = {'allOrders':allOrders,'count':count,'announcement':announcement1}
    return render(request, 'orders.html', params)


def orderview(request,myid):
    print(myid)
    order = Orders.objects.filter(payment_ref=str(myid)).values()[0]
    items = (json.loads(order['items_json']))
    order['items_json']=items.values()
    order['dispatched']=int(order['dispatched'])
    order['delivered']=int(order['delivered'])
    order['declined']=int(order['declined'])
    order['payment_conf']=int(order['payment_conf'])

    params = {'order':order,'announcement':announcement1}
    return render(request, 'orderview.html', params)
    

