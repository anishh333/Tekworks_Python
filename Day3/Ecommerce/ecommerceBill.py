def discount1(t:int,discount:int)->int:
    return t-t*(discount/100)
def addGST(t:int)->int:
    return t+t*0.18
def invoice(cart:dict,discount:int,gst:int):
    print("----------------InVoice----------------------")
    t=0
    for key,value in cart.items():
        print(f"{key}  ${value}")
        t+=value
    print("---------------------------------------------")
    print(f"SubTotal {t}")
    print(f"After {discount}% discount : ${discount1(t,discount)}")
    print(f"After 18% GST : ${addGST(t)}")
    print("---------------------------------------------")
    print("Thank You for shopping with us!")