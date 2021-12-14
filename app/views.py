from django.http.response import JsonResponse,HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.conf import settings
import smtplib,ssl
from email.message import EmailMessage
import random
import datetime
from app.models import User
from recharge.models import *

# Create your views here.

def landing(request):
    if(request.user.is_authenticated):
        return redirect('index')
    return render(request,"landing.html")
    
def send_otp(request):
    if(request.user.is_authenticated):
        return redirect('index')
    form=request.POST.get('form')
    email=request.POST.get('email')
    exist=User.objects.filter(email=email).exists()
    if(( exist and form=='formin') or ( not exist and form=='formup')):
        otp=random.randrange(100000,999999)
        otp_str=str(otp)
        meth=""
        if(form=='formin'):
            meth="SignIn"
        else:
            meth="SignUp"
        EMAIL_ADDRESS=settings.EMAIL_ADDRESS
        EMAIL_PASSWORD=settings.EMAIL_PASSWORD
        msg = EmailMessage()
        msg['Subject'] = 'Registration OTP'
        msg['From'] = EMAIL_ADDRESS 
        msg['To'] = email
        htmlt='''
        <!doctype html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <title>Registration OTP</title>
            <style>
            /* -------------------------------------
                GLOBAL RESETS
            ------------------------------------- */
            
            /*All the styling goes here*/
            
            img {
                border: none;
                -ms-interpolation-mode: bicubic;
                max-width: 100%; 
            }

            body {
                background-color: #f6f6f6;
                font-family: sans-serif;
                -webkit-font-smoothing: antialiased;
                font-size: 14px;
                line-height: 1.4;
                margin: 0;
                padding: 0;
                -ms-text-size-adjust: 100%;
                -webkit-text-size-adjust: 100%; 
            }

            table {
                border-collapse: separate;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                width: 100%; }
                table td {
                font-family: sans-serif;
                font-size: 14px;
                vertical-align: top; 
            }

            /* -------------------------------------
                BODY & CONTAINER
            ------------------------------------- */

            .body {
                background-color: #f6f6f6;
                width: 100%; 
            }

            /* Set .ot max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on .ot phone or something */
            .container {
                display: block;
                margin: 0 auto !important;
                /* makes it centered */
                max-width: 580px;
                padding: 10px;
                width: 580px; 
            }

            /* This should also be .ot block element, so that it will fill 100percent of the .container */
            .content {
                box-sizing: border-box;
                display: block;
                margin: 0 auto;
                max-width: 580px;
                padding: 10px; 
            }

            /* -------------------------------------
                HEADER, FOOTER, MAIN
            ------------------------------------- */
            .main {
                background: #ffffff;
                border-radius: 3px;
                width: 100%; 
            }

            .wrapper {
                box-sizing: border-box;
                padding: 20px; 
            }

            .content-block {
                padding-bottom: 10px;
                padding-top: 10px;
            }

            .footer {
                clear: both;
                margin-top: 10px;
                text-align: center;
                width: 100%; 
            }
                .footer td,
                .footer p,
                .footer span,
                .footer .ot {
                color: #999999;
                font-size: 12px;
                text-align: center; 
            }

            /* -------------------------------------
                TYPOGRAPHY
            ------------------------------------- */
            h1,
            h2,
            h3,
            h4 {
                color: #000000;
                font-family: sans-serif;
                font-weight: 400;
                line-height: 1.4;
                margin: 0;
                margin-bottom: 30px; 
            }

            h1 {
                font-size: 35px;
                font-weight: 300;
                text-align: center;
                text-transform: capitalize; 
            }

            p,
            ul,
            ol {
                font-family: sans-serif;
                font-size: 14px;
                font-weight: normal;
                margin: 0;
                margin-bottom: 15px; 
            }
                p li,
                ul li,
                ol li {
                list-style-position: inside;
                margin-left: 5px; 
            }

            .ot {
                color: #3498db;
                text-decoration: underline; 
            }

            /* -------------------------------------
                BUTTONS
            ------------------------------------- */
            .btn {
                box-sizing: border-box;
                width: 100%; }
                .btn > tbody > tr > td {
                padding-bottom: 15px; }
                .btn table {
                width: auto; 
            }
                .btn table td {
                background-color: #ffffff;
                border-radius: 5px;
                text-align: center; 
            }
                .btn .ot {
                background-color: #ffffff;
                border: solid 1px #3498db;
                border-radius: 5px;
                box-sizing: border-box;
                color: #3498db;
                display: inline-block;
                font-size: 14px;
                font-weight: bold;
                margin: 0;
                padding: 12px 25px;
                text-decoration: none;
                text-transform: capitalize; 
            }

            .btn-primary table td {
                background-color: #3498db; 
            }

            .btn-primary .ot {
                background-color: #3498db;
                border-color: #3498db;
                color: #ffffff; 
            }

            /* -------------------------------------
                OTHER STYLES THAT MIGHT BE USEFUL
            ------------------------------------- */
            .last {
                margin-bottom: 0; 
            }

            .first {
                margin-top: 0; 
            }

            .align-center {
                text-align: center; 
            }

            .align-right {
                text-align: right; 
            }

            .align-left {
                text-align: left; 
            }

            .clear {
                clear: both; 
            }

            .mt0 {
                margin-top: 0; 
            }

            .mb0 {
                margin-bottom: 0; 
            }

            .preheader {
                color: transparent;
                display: none;
                height: 0;
                max-height: 0;
                max-width: 0;
                opacity: 0;
                overflow: hidden;
                mso-hide: all;
                visibility: hidden;
                width: 0; 
            }

            .powered-by .ot {
                text-decoration: none; 
            }

            hr {
                border: 0;
                border-bottom: 1px solid #f6f6f6;
                margin: 20px 0; 
            }

            /* -------------------------------------
                RESPONSIVE AND MOBILE FRIENDLY STYLES
            ------------------------------------- */
            @media only screen and (max-width: 620px) {
                table.body h1 {
                font-size: 28px !important;
                margin-bottom: 10px !important; 
                }
                table.body p,
                table.body ul,
                table.body ol,
                table.body td,
                table.body span,
                table.body .ot {
                font-size: 16px !important; 
                }
                table.body .wrapper,
                table.body .article {
                padding: 10px !important; 
                }
                table.body .content {
                padding: 0 !important; 
                }
                table.body .container {
                padding: 0 !important;
                width: 100% !important; 
                }
                table.body .main {
                border-left-width: 0 !important;
                border-radius: 0 !important;
                border-right-width: 0 !important; 
                }
                table.body .btn table {
                width: 100% !important; 
                }
                table.body .btn .ot {
                width: 100% !important; 
                }
                table.body .img-responsive {
                height: auto !important;
                max-width: 100% !important;
                width: auto !important; 
                }
            }

            /* -------------------------------------
                PRESERVE THESE STYLES IN THE HEAD
            ------------------------------------- */
            @media all {
                .ExternalClass {
                width: 100%; 
                }
                .ExternalClass,
                .ExternalClass p,
                .ExternalClass span,
                .ExternalClass font,
                .ExternalClass td,
                .ExternalClass div {
                line-height: 100%; 
                }
                .apple-link .ot {
                color: inherit !important;
                font-family: inherit !important;
                font-size: inherit !important;
                font-weight: inherit !important;
                line-height: inherit !important;
                text-decoration: none !important; 
                }
                #MessageViewBody .ot {
                color: inherit;
                text-decoration: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: inherit;
                line-height: inherit;
                }
            }

            </style>
        </head>
        <body class="">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body">
            <tr>
                <td>&nbsp;</td>
                <td class="container">
                <div class="content">

                    <!-- START CENTERED WHITE CONTAINER -->
                    <table role="presentation" class="main">

                    <!-- START MAIN CONTENT AREA -->
                    <tr>
                        <td class="wrapper">
                        <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                            <tr>
                            <td>
                                <p>Hi there,</p>
                                <p>Hey Buddy, Use this OTP for '''+meth+'''. This is it.</p>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary">
                                <tbody>
                                    <tr>
                                    <td align="left">
                                        <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                        <tbody>
                                            <tr>
                                            <td> <p class="ot">'''+otp_str+'''</p> </td>
                                            </tr>
                                        </tbody>
                                        </table>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>
                                <p>Good luck! Hope it works.</p>
                            </td>
                            </tr>
                        </table>
                        </td>
                    </tr>

                    <!-- END MAIN CONTENT AREA -->
                    </table>
                    <!-- END CENTERED WHITE CONTAINER -->

                    <!-- START FOOTER -->
                    <div class="footer">
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                        <tr>
                        <td class="content-block">
                            <span class="apple-link">Company Inc</span>
                        </td>
                        </tr>
                        <tr>
                        <td class="content-block powered-by">
                            Powered by Sosio.
                        </td>
                        </tr>
                    </table>
                    </div>
                    <!-- END FOOTER -->

                </div>
                </td>
                <td>&nbsp;</td>
            </tr>
            </table>
        </body>
        </html>
        '''
        msg.set_content(htmlt, subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
            smtp.send_message(msg)
        dic={'otp':otp_str,'flag':True}
        print(dic)
        return JsonResponse(dic)
    else:
        dic={'flag':False}
        return JsonResponse(dic)

def verify_otp(request):
    if(request.user.is_authenticated):
        return redirect('index')

    if(request.method=='POST'):
        flag=(request.POST['otp']==request.POST['otp_con'])        
        dic={'flag':flag}
        return JsonResponse(dic)
    else:
        dic={'flag':False}
        return JsonResponse(dic)
        
def signup(request):
    if(request.user.is_authenticated):
        return redirect('index')
    if(request.method=='POST'):
        if(request.POST['flag']):
            user=User.objects.create_user(first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'],password="12345",mobile=request.POST['phone'])
            user.save()
            return redirect('signin')
    return render(request,"signup.html")

def signin(request):
    if(request.user.is_authenticated):
        return redirect('index')
    if(request.method=='POST'):
        if(request.POST['flag']):
            email=request.POST['email']
            user=auth.authenticate(request,email=email,password=12345)
            if(user):
                user.loggedin_at=datetime.datetime.now()
                user.save()
                auth.login(request, user)
                return redirect('index')
            return redirect('signin')
    return render(request,"signin.html")

def log_out(request):
    if(request.user.is_authenticated):
        auth.logout(request)
    return redirect('/')
    
def index(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    return render(request,"index.html")

def profile(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    user=User.objects.get(email=request.user)
    return render(request,"profile.html",{'user':user})
def user_details(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    user=User.objects.get(email=request.user)
    dic={'credits':user.credits,'name':user.first_name}
    return JsonResponse(dic)
