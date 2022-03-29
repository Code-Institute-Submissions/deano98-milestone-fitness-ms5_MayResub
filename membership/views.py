from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Member
import stripe

# Create your views here.

def membership(request):
    ''' View to return the index page '''
    return render(request, 'membership/membership.html')

stripe.api_key = "sk_test_51KPpqoJAp5w3wtxOBWUnJsxJqEb3uaoG7AK0cbFTyHv5uYJsSYeLm5hb2e4CQ2HCO2sPKxaaNPBwuD9KK6KHqm5H0022pEx4RX"

def checkout(request):
    try:
        if request.user.member.membership:
            return redirect('settings')
    except Member.DoesNotExist:
        pass

    membership = ""
    price = 0
    if request.method == 'POST':
        pass
    else:
        if request.GET['membership'] == "premium":
            membership = "Premium"
            price = 32
            price_id = "price_1KdwmcJAp5w3wtxO5BfJBzvv"
        else:
            membership = "Basic"
            price = 20
            price_id = "price_1Kdfs8JAp5w3wtxO6l24lzML"

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=request.user.email,
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url='http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:8000/cancel',
        )

        return render(request, 'membership/checkout.html', {
            'session_id': session.id,
            'membership': membership,
            'price': price,
            })