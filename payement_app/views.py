import uuid

from django.conf import settings
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import razorpay
import json

from rest_framework.response import Response
from rest_framework import viewsets, status

from payement_app.models import Payment
from payement_app.serializers import PaymentSerializers


# @csrf_exempt
# def initiate_payment(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         amount = int(data.get('amount')) * 100  # Razorpay accepts amount in paise
#         client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
#         payment_data = {
#             'amount': amount,
#             'currency': 'INR',
#             'receipt': 'receipt_1',
#             'notes': {},
#         }
#         try:
#             order = client.order.create(data=payment_data)
#             return JsonResponse(order)
#         except Exception as e:
#             return JsonResponse({'error': str(e)})


# @csrf_exempt
# def initiate_payment(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         amount = int(data.get('amount')) * 100  # Razorpay accepts amount in paise
#         client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
#         payment_data = {
#             'amount': amount,
#             'currency': 'INR',
#             'receipt': 'receipt_1',
#             'notes': {},
#         }
#         try:
#             order = client.order.create(data=payment_data)
#
#             # Save payment details in the database
#             payment = Payment.objects.create(
#                 amount=amount,
#                 currency=data.get('currency'),
#                 receipt=order.reciept,
#                 status=order.status,
#                 customer_id=data.get('customer_id'),
#                 customer_name=data.get('customer_name'),
#                 description=data.get('description')
#             )
#             payment.save()
#             return JsonResponse(order)
#         except Exception as e:
#             return JsonResponse({'error': str(e)})


# class PaymentView(View):
#     @csrf_exempt
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def get(self, request):
#         if request.GET['id']:
#             response = Payment.objects.filter(id=request.GET['id'])
#             return JsonResponse({'response': response})
#         else:
#             response = Payment.objects.all()
#             return JsonResponse({'response': response})
#
#     def post(self, request):
#         data = json.loads(request.body)
#         amount = int(data.get('amount')) * 100  # Razorpay accepts amount in paise
#         client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
#         receipt = str(uuid.uuid4())
#         payment_data = {
#             'amount': amount,
#             'currency': 'INR',
#             'receipt': receipt,
#             'notes': {},
#         }
#         try:
#             # order = client.order.create(data=payment_data)
#
#             payment = Payment.objects.create(
#                 amount=amount,
#                 currency=data.get('currency'),
#                 receipt=receipt,
#                 status="DONE",
#                 customer_id=data.get('customer_id'),
#                 customer_name=data.get('customer_name'),
#                 description=data.get('description')
#             )
#             payment.save()
#
#             return JsonResponse(payment)
#         except Exception as e:
#             return JsonResponse({'error': str(e)})


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body)
        amount = int(data.get('amount')) * 100  # Razorpay accepts amount in paise
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
        receipt = str(uuid.uuid4())
        payment_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': receipt,
            'notes': {},
        }
        try:
            order = client.order.create(data=payment_data)

            payment = Payment.objects.create(
                amount=amount,
                currency=data.get('currency'),
                receipt=receipt,
                status="DONE",
                customer_id=data.get('customer_id'),
                customer_name=data.get('customer_name'),
                description=data.get('description')
            )

            serializer = self.get_serializer(payment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
