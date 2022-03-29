from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Member
from .forms import TdeeForm
import stripe

# Create your views here.

def membership(request):
    ''' View to return the membership page '''
    if request.method == 'POST':
        tdee_data = request.POST
        gender = tdee_data.get("gender")
        weight = float(tdee_data.get("weight"))
        height = float(tdee_data.get("height"))
        age = float(tdee_data.get("age"))
        activity = tdee_data.get("activity")
        multiplier = 1

        if gender == "male":
            BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        else:
            BMR = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

        if activity == "sedentary":
            multiplier = 1.2
        elif activity == "light":
            multiplier = 1.375
        elif activity == "moderate":
            multiplier = 1.55
        elif activity == "heavy":
            multiplier = 1.725
        else:
            multiplier = 1.9

        user_tdee = BMR * multiplier
        rounded_tdee = round(user_tdee/100)*100
        current_member = Member.objects.get(user=request.user)
        current_member.tdee = rounded_tdee
        current_member.save()
        current_member.save(update_fields=["tdee_update"]) 

    return render(request, 'membership/membership.html', {
        'tdee_form': TdeeForm(),
    })

stripe.api_key = "sk_test_51KPpqoJAp5w3wtxOBWUnJsxJqEb3uaoG7AK0cbFTyHv5uYJsSYeLm5hb2e4CQ2HCO2sPKxaaNPBwuD9KK6KHqm5H0022pEx4RX"

@login_required
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
            success_url='https://8000-deano98-milestonefitnes-jto732nfenq.ws-eu38.gitpod.io/membership/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://8000-deano98-milestonefitnes-jto732nfenq.ws-eu38.gitpod.io/membership/cancel',
        )

        return render(request, 'membership/checkout.html', {
            'session_id': session.id,
            'membership': membership,
            'price': price,
            })

def success(request):
    if request.method == 'GET' and 'session_id' in request.GET:
        session = stripe.checkout.Session.retrieve(request.GET['session_id'],)
        print(session)
        member = Member()
        member.user = request.user
        member.stripe_id = session.customer
        member.membership = True
        member.cancel_at_end = False
        member.stripe_member_id = session.subscription
        member.save()
    return render(request, 'membership/success.html')


def cancel(request):
    return render(request, 'membership/cancel.html')

@login_required
def settings(request):
    membership = False
    cancel_at_end = False
    if request.method == 'POST':
        subscription = stripe.Subscription.retrieve(request.user.member.stripe_member_id)
        subscription.cancel_at_end = True
        request.user.member.cancel_at_end = True
        cancel_at_end = True
        subscription.save()
        request.user.member.save()
    else:
        try:
            if request.user.member.membership:
                membership = True
            if request.user.member.cancel_at_end:
                cancel_at_end = True
        except Member.DoesNotExist:
            membership = False
    return render(request, 'membership/settings.html', {'membership':membership,
    'cancel_at_end':cancel_at_end})



