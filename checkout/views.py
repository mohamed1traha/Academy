import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from academy_app.models import Course
from django.contrib.auth.models import User
stripe.api_key = settings.STRIPE_SECRET_KEY
# تهيئة Stripe باستخدام مفتاح الـ Secret من الإعدادات
from academy_app.models import UserCourse  # استيراد الموديل الجديد

def create_checkout_session(request, course_id):
    course = Course.objects.get(id=course_id)
    
    # تخزين معلومات الدورة في الـ session
    request.session['course_id'] = course.id

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': course.title,
                },
                'unit_amount': int(course.price * 100),  # تحويل السعر إلى سنتات
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/checkout/success/'),
        cancel_url=request.build_absolute_uri('/checkout/cancel/'),
    )

    return redirect(checkout_session.url, code=303)


def success(request):
    # استرجاع بيانات الدورة من الـ session
    course_id = request.session.get('course_id')

    if course_id:
        try:
            course = Course.objects.get(id=course_id)

            # إضافة العلاقة بين المستخدم والدورة
            user = request.user
            user_course = UserCourse.objects.create(user=user, course=course)

            return render(request, 'success.html', {'course': course})
        except Course.DoesNotExist:
            return HttpResponse("الدورة غير موجودة.")
    else:
        return HttpResponse("لم يتم العثور على الدورة.")

def cancel(request):
    return render(request, 'cancel.html')
