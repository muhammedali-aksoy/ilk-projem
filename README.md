# İlk Projem  

Bu benim Python ile yaptığım **ilk projem** 🎉  
Program basit bir hesap makinesi gibi çalışıyor: toplama, çıkarma, çarpma ve bölme işlemleri yapabiliyor.  

## 📌 Nasıl Çalıştırılır?  
1. Bu depoyu bilgisayarına ya da telefonuna indir.  
2. Dosyanın içinde `my first project.py` adlı Python dosyasını aç.  
3. Pydroid 3 (Android) veya Python 3 yüklü bir bilgisayarda çalıştır.  
4. Sayıları gir ve sonucu gör!  

## 🧑‍💻 Öğrendiklerim  
- `print()` fonksiyonu ile ekrana yazı yazdırmayı  
- `input()` ile kullanıcıdan veri almayı  
- Temel matematik işlemlerini kodlamayı  

## 📅 Tarih  
16.08.2025 – Benim yazılım dünyasına attığım ilk adım 🚀
## 💻 Hesap Makinesi Kodu
```python
# Get numbers from user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Ask which operation to perform
operation = input("Choose an operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2
else:
    result = "Invalid operation!"

# Show the result
print("Result:", result)
```
