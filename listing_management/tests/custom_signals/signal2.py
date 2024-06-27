from listing_management.signals import CustomSignal

signal2 = CustomSignal()

def single2_handler(sender, **kwargs):
    print(sender)

signal2.connect(single2_handler)