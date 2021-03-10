from flask import Flask, render_template, request, redirect
import smtplib
from werkzeug.utils import import_string
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

subscribers = []

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#Initialize the database
#db = SQLAlchemy(app)

#Create Database Model
'''class Friends(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)
# Create a function to return a string when we add something'''

	#def __repr__(self):
	#	return '<Name< %r>' % self.id

'''@app.route('/register', methods=['GET','POST'])
def register():
	#title = "Register"
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        user = User.Query(filter_by=username)
        if user.count() == 0:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()

            flash('You have registered the username {0}. Please login'.format(username))
            return redirect(url_for('login'))
        else:
            flash('The username {0} is already in use.  Please try a new username.'.format(username))
            return redirect(url_for('register'))
    else:
        abort(405)'''

@app.route('/howto')
def howto():
	title = "How to visit the DarkWeb in the safest way"
	return render_template("web.html", title = title)


@app.route('/contact')
def contact():
	title = "Contact Us"
	return render_template("contact.html", title = title)

@app.route('/')
def index():
	title = "Home"
	return render_template("index.html", title = title)

@app.route('/disclaimer')
def warning():
	title = "Disclaimer"
	return render_template("disclaimer.html", title=title)

@app.route('/about')
def about():
	title = "About"
	return render_template("about.html", title = title)

@app.route('/links', methods=['POST', 'GET'])
def links():
	title = "DarkWebLinks"
	links = ["cnkj6nippubgycuj.onion /— Torch",
	"http://bv42i2sn3p2nzxmhoqmmjaxf66onm6p7wpmtiuctnbus76ilxugx7wyd.onion/doku.php /— The Hidden Wiki",
	"http://vlbva4lmlqkjuqrgmtiryofla7lrqc3wg6gagubehsqvoxxdvzyrdjad.onion /— Imperial Market",
	"http://22pptkhbo775q4pc.onion /— The PayPal Plaza",
	"dnmugu4755642434.onion /— Kilos",
	"msydqstlz2kzerdg.onion /— Ahima.fi",
	"haystakvxad7wbk5.onion /— Haystack" ,
	"reconponydonugup.onion /— Recon" ,
	"http://torbuyxpe6auueywlctu4wz6ur3o5n2meybt6tyi4rmeudtjsysayqyd.onion /— Tor Buy", 
	"7yipwxdv5cfdjfpjztiz7sv2jlzzjuepmxy4mtlvuaojejwhg3zhliqd.onion /— White House Market" ,
	"http://aoh5yljyr2gawvz6isodr3yp4wfb5ghml4bunjymys24vzxqqw6qhayd.onion /— Empire Market",
	"Marketplace Commercial Services",
	"http//6w6vcyn16dumn67conion/ Tor Market Board  /— Anonymous Marketplace Forums",
	"http//wvk32thojln4gpp4.onion /— Project Evil",
	"http//5mvm7cg6bgklmp.onion /— Discounted electronics goods",
	"http//lw4ipk5choakk5ze.onionraw/evbLewgkDSVkifrv8zAo /— Unfriendtysolution — Legit hitman Services",
	"httphtuu66yxvmn30f71.onion /— UK Guns and Ammo",
	"http//nr6juudpp4as4gjg.onion /— torguns_htm — Used Tor Guns",
	" http://torbrokerge7zxgq.onion/ - TorBroker - Trade securities anonymously with bitcoin, currently supports nearly 1000 stocks and ETFs",
	"http//ucx7bkbi2dtia36r.onion /— Amazon Business",
	"http//nr6juudpp4as4gjg.onion/tor_html /— Tor Technology",
	"http//hbetshipq5yhhrsd.onion /— Hidden BetCoin",
	"http://kpvz7ki2v5agwt35.onion - The Hidden Wiki",
	"http//cstoreav7i44h21r.onion /— CStore Carded Store",
	"http:htft'di3izigxllure.onion /— Apples 4 Bitcoin",
	"http//e2qizoerj4d61dif.onion /— Carded Store",
	"http//jvrnuue4bvbftiby.onion /— Data-Bay",
	"http//bgkitnugq5ef2cpi.onion /— Hackintosh",
	"http//vlp4uw5ui221jlg7.onionJ /— EuroArms",
	"http//b4vqxw2j36wf2bqa.onion /— Advantage Products",
	"http//ybp40ezfhk24hxmb.onion /— Hitman Network",
	"http//mts7hqqqeogujc5e.onion /— Marianic Technology Services",
	"http//mobi17rab6nuf7vx.onion /— Mobile Store",
	"http//54flq67kqr5wvjqf.onion /— MSR Shop",
	"http//yth5q7zdmqlycbcz.onion /— Old Man Fixer's Fixing Services",
	"http//matrixtxri745dft.onion /— neo/uploadsJMATRlXtxri745dfwONlON 1308272313361PA_pcpng",
	"http//storegsq305mbdz.onion /— Samsung StorE",
	"http//sheep5u64fi457aw.oniom' /— Sheep Marketplace",
	"http//nr6juudpp4as4gjg.onion/Ibetcoin.html /— Tor BetCoin",
	"http//qizriixqwmeq4p5b.onion /— Tor Web Developer",
	"http/Mqnd6mieccqyit.onion /— UK Passports",
	"http//en35tuzqmn410fbk.onion /— US Fake ID Store",
	"http//xfnwyig701ypdq5r.onion /— USA Citizenship",
	"http//uybu3melulmoljnd.onion /—iLike Help Guy",
	"http//dbmv53j45pcv534x.onion /— Network Consultü-tg and Software Development",
	"http://matrixtxri745dfw.onion/ - Image Uploader",
	"http//nr6juudpp4as4gjg.onion/tynermsr.html /— Tyner MSR Store"]
	return render_template("links.html", links = links, title = title)

@app.route('/subscribe')
def subscribe():
	title = "Subscribe for updates on new links"
	return render_template("subscribe.html", title = title)

@app.route('/form', methods=["POST"])
def form():
	SUBJECT = "Congratulations"
	TEXT = "You have been succesfully subscribed to my email newsletter"
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	email = request.form.get("email")
	message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("darkweb101pvtltd@gmail.com", "AdminisBoss")
	server.sendmail("DarkWebLinks", email, message)

	if not first_name or not last_name or not email:
		error_statement = "All fields of the form are required..."
		return render_template("fail.html", error_statement=error_statement,first_name=first_name, last_name=last_name,
		email=email)
		

	subscribers.append(f"{first_name} {last_name} | {email}")
	title = "Thank You for Subscribing"
	return render_template("form.html", title = title, subscribers=subscribers)
	