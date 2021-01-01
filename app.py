from flask import Flask, render_template, request, redirect
import smtplib
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

SUBJECT = "Congratulations"
TEXT = "You have been succesfully subscribed to my email newsletter"

subscribers = []

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#Initialize the database
db = SQLAlchemy(app)

#Create Database Model
class users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)
# Create a function to return a string when we add something

	def __repr__(self):
		return 'Link< %r>' % self.id

@app.route('/users', methods=['POST', 'GET'])
def Friends():
	title = "Register"

	if request.method == 'POST':
		friend_name = request.form['friend_name']
		new_friend = Friends(name=friend_name)
		# Push to database

		try:
			db.session.add(new_friend)
			db.session.commit()
			return redirect('/users')

		except:
			friends = Friends.query.order_by(Friends.date_created)
			return "There was an error adding your name to our database"


	else:
		return render_template("users.html", title = title, friends=friends)

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
	links = ["Torch: cnkj6nippubgycuj.onion",
	"Kilos: dnmugu4755642434.onion",
	"Ahima.fi: msydqstlz2kzerdg.onion",
	"Haystack: haystakvxad7wbk5.onion" ,
	"Recon: reconponydonugup.onion" ,
	"Tor Buy: http://torbuyxpe6auueywlctu4wz6ur3o5n2meybt6tyi4rmeudtjsysayqyd.onion", 
	"7yipwxdv5cfdjfpjztiz7sv2jlzzjuepmxy4mtlvuaojejwhg3zhliqd.onion/- White House Market" ,
	"http://aoh5yljyr2gawvz6isodr3yp4wfb5ghml4bunjymys24vzxqqw6qhayd.onion/- Empire Market",
	"Marketplace Commercial Services",
	"http//6w6vcyn16dumn67conion/— Tor Market Board — Anonymous Marketplace Forums",
	"http//wvk32thojln4gpp4_onion/— Project Evil",
	"http//5mvm7cg6bgklmp_onion/—Discounted electronics goods",
	"http//lw4ipk5choakk5zeonion/raw/evbLewgkDSVkifrv8zAo/ Unfriendtysolution — Legit hitman Services",
	"httphtuu66yxvmn30f71_onion/- UK Guns and Ammo",
	"http//nr6juudpp4as4gjgonion/torguns_htm — Used Tor Guns",
	"http//ucx7bkbi2dtia36ronion/—Amazon Business",
	"http//nr6juudpp4as4gjgonion/tor_html — Tor Technology",
	"http//hbetshipq5yhhrsd_onion/—Hidden BetCoin",
	"http//cstoreav7i44h21r_onion/—CStore Carded Store",
	"http:htft'di3izigxllureonion/— Apples 4 Bitcoin",
	"http//e2qizoerj4d61dif_onion/— Carded Store",
	"http//jvrnuue4bvbftiby_onion/— Data-Bay",
	"http//bgkitnugq5ef2cpi.onion — Hackintosh",
	"http//vlp4uw5ui221jlg7.onionJ EuroArms",
	"http//b4vqxw2j36wf2bqa.onion/—Advantage Products",
	"http//ybp40ezfhk24hxmb_onion/—Hitman Network",
	"http//mts7hqqqeogujc5e_onion/—Marianic Technology Services",
	"http//mobi17rab6nuf7vx_onion/—Mobile Store",
	"http//54flq67kqr5wvjqfonion/ MSR Shop",
	"http//yth5q7zdmqlycbcz_onion/— Old Man Fixer's Fixing Services",
	"http//matrixtxri745dft'_onion/neo/uploadsJMATRlXtxri745dfwONlON 1308272313361PA_pcpng",
	"http//storegsq305mbdz_onion/—Samsung StorE",
	"http//sheep5u64fi457awoniom' — Sheep Marketplace",
	"http//nr6juudpp4as4gjgonionIbetcoin.htm — Tor BetCoin",
	"http//qizriixqwmeq4p5b_onion/—Tor Web Developer",
	"http/Mqnd6mieccqyitonion/— UK Passports",
	"http//en35tuzqmn410fbk.onion/— US Fake ID Store",
	"http//xfnwyig701ypdq5r_onion/— USA Citizenship",
	"http//uybu3melulmoljnd_onion/—iLike Help Guy",
	"http//dbmv53j45pcv534x_onion/— Network Consultü-tg and Software Development",
	"http//nr6juudpp4as4gjgonion/tynermsr.htm — Tyner MSR Store"]
	return render_template("links.html", links = links, title = title)

@app.route('/subscribe')
def subscribe():
	title = "Subscribe for updates on new links"
	return render_template("subscribe.html", title = title)

@app.route('/form', methods=["POST"])
def form():
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	email = request.form.get("email")

	subject = "Congratulations"
	message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
	#message = "You have been succesfully subscribed to my email newsletter"
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("darkweblinkspvtltd@gmail.com", "AdminisBoss")
	server.sendmail("DarkWebLinks", email, message)

	if not first_name or not last_name or not email:
		error_statement = "All fields of the form are required..."
		return render_template("fail.html", error_statement=error_statement)
		first_name=first_name, 
		last_name=last_name, 
		email=email

	subscribers.append(f"{first_name} {last_name} | {email}")
	title = "Thank You for Subscribing"
	return render_template("form.html", title = title, subscribers=subscribers)
