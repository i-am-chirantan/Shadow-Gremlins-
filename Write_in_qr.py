import qrcode

car_number=input("Enter the car number: ")
model_number=input("Enter the model number: ")
average_weight=input("Enter the average weight: ")

data = {"car_number":car_number, "model_number":model_number, "average_weight":average_weight}


img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode1.png')