from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

 
app = Flask(__name__)
 
@app.route("/wa")
def wa_hello():
    return "Hello, World!"
 
@app.route("/wasms", methods=['POST'])
def wa_sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    
    msg = request.form.get('Body').lower() # Reading the message from the whatsapp
 
    print("msg-->",msg)
    resp = MessagingResponse()
    reply=resp.message()
    # Create reply
    if msg == "hi" or msg=="hola":
         reply.body("hello!")
    
    elif msg=="1": 
        reply.body(''' 
नमस्ते 🔔 Please Choose Your Service:
A:Flex Printing 📰
B:Digital Printing  🧧
C:Screen Printing 📄
D:3D Printing 📋
E:LED UV 📮
                  ''')

    elif msg=="a"or msg=="b" or msg=="c" or msg=="d" or msg=="e":
        reply.body('''
Select Size For Your Print   ☑🎯
s1:8.5" x 11" (Letter-Size) ..🔤
s2:11" x 17" (Bulletin Posters) 🔤
s3:12" x 18" (Mini Posters) ...🔤
s4:16" x 20" ...🔤
s5:18" x 24" (Medium Posters) ...🔤
s6:19" x 27" ...🔤
s7:20" x 30"🔤
                ''')

    elif msg=="s1"or msg=="s2" or msg=="s3" or msg=="s4" or msg=="s5" or msg=="s6" or msg=="s7":
        reply.body("🎫🎟☑☑🎯🎯Order Confirmed! Our Team Will Reach you within 24 Hours ")
   
    elif msg=="complaint" or msg=="2":
         reply.body('''
Please Feel Free To Contact Us For Furthur Queries
"Our Team Will Reach You WithIn 24 Hours"
📧 EMAIL US:SupportINDIA@gmail.com📨
📧 EMAIL US:SupportUSA@gmail.com📨
📧 EMAIL US:SupportGermany@gmail.com📨
📲Call Us On Our Toll Free Numbers:
📲USA:+12064512559 
📲INDIA:+91 9000555941
📲GERMANY:+49 211 5684962
                 ''')
    
    elif msg=="About Us" or msg=="About" or msg=="aboutus" or msg=="about" or msg=="3":
        reply.media('http://www.africau.edu/images/default/sample.pdf')

    
    elif msg=="payments" or msg=="4":
         reply.body('''
💰💰💰💰💰Please Choose A Payment Method💸💸💸💸💸💸
gg:GooglePay🏦
pp:PhonePay📲
ib:Internet Banking 💸💸
cc:cash 💷💶💶
        ''')
        

    else:
        reply.body('''
 Welcome! 🙏  Please choose an option to use our services 
1.Printing Services 📜
2.Customer Support 📞
3.About Us 🎢
4.Payments 💰
 ''')
    
    return str(resp)

if __name__ == "__main__":	
    app.run(debug=True)