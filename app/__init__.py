from flask import Flask, render_template, request, flash, redirect
from flask_mail import Message, Mail
from config_file import Config
from pathlib import Path
from app.static.img.content.works import *
from app.forms import ContactForm

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():

    site_title = 'Personal Portfolio'
    copyright_info = "Copyright."
    logo_img = '/static/img/logo/logo.png'
    favicon = '/static/img/logo/favicon.ico'
    project_title = 'Projects'
    services_dict = {
        'title': 'Services',
        'icon_left':'/static/img/icons/portfolio.svg',
        'icon_right':'/static/img/icons/monitor.svg',
        'services_left' : ['Line 1','Line 2','Line 3'],
        'services_right' : ['Line 1','Line 2','Line 3', 'Line 4', 'Line 5', 'Line 6']
    }
    social = {
        'linkedin':'https://www.linkedin.com',
        'instagram': 'https://www.instagram.com',
    }
    nav_bar = {
        'home': 'Home',
        'portfolio': 'Projects',
        'contact': 'Contact',
        'services': 'Services',
    }
    jumbo = {
        'title': "",
        'description': "",
        'image' : '/static/img/jumbotron/jumbo.jpg',
        'image2' : '/static/img/jumbotron/jumbo.jpg',
    }
    form = ContactForm()

    if request.method == 'GET':
        return render_template(
            'index.html',
            logo_img=logo_img,
            nav_bar=nav_bar, 
            jumbo=jumbo, 
            social=social,
            services_dict=services_dict,
            work_list=work_list, 
            site_title=site_title, 
            copyright_info=copyright_info,
            project_title=project_title,
            form=form,
            )    
    
    elif request.method == 'POST':
        # Form not filled properly.
        if form.validate() == False:
            flash("Please, don't leave any empty field")
            return redirect("/#contact-me")
        # Email generation.
        else:
            msg = Message(form.subject.data, sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[app.config['MAIL_RECEIVER']])
            msg.body = """
            From: %s <%s>
            Message:
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            # Send email.
            try:
                mail.send(msg)
            # Email credentials failed.
            except:
                flash('Email delivery failed. Please, try again.')
                return redirect("/#contact-me") 
            # Email succesfully sent.    
            flash('Email sent!')
            return redirect("/#contact-me")