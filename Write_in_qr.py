import qrcode

#car_number=input("Enter the car number: ")
wheel_number=input("Enter the wheel number: ")
registration_number=input("Enter the registration number: ")
model_number=input("Enter the model number: ")
average_weight=input("Enter the average weight: ")
average_weight=float(average_weight)


data = {"registration_number":registration_number,"model_number":model_number,"average_weight":average_weight,"wheel_number":wheel_number}


img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode1.png')