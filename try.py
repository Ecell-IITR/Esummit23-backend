import os
import razorpay
RAZOR_KEY_ID = os.getenv('RAZORPAY_KEY_ID',"rzp_live_U0W39W3I1yR00g")
RAZOR_KEY_SECRET = os.getenv('RAZORPAY_SECRET_KEY', "RndrTeCVPTxYTJxVt10S7KET")
# Creating Razorpay Client instance.
razorpay_client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))
z=razorpay_client.order.all()
for i in z:
    print(i)