import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.user import User
from models.offer import Offer
from models.reservation import Reservation
from models.rating import Rating


# import session object
from app import ecv

# add three users
u1 = User(username='Sem')
u2 = User(username='Cham')
u3 = User(username='Jafeth')
ecv.session.add(u1)
ecv.session.add(u2)
ecv.session.add(u3)

# add an offering by Sem
hours = 6
time_ready = datetime.datetime.utcnow() + datetime.timedelta(hours=hours)
o1 = Offer(host=u1, portions=2, price=3.50, info="spaghetti gambanero, non-vegetarian", time_ready=time_ready)
ecv.session.add(o1)

# add reservations for Cham and Jafeth
res1 = Reservation(user=u2, offer=o1, portions=1)
res2 = Reservation(user=u3, offer=o1, portions=1)
ecv.session.add(res1)
ecv.session.add(res2)

# add ratings from Cham en Jafeth about Sem
rat1 = Rating(user=u2, host=u1, stars=2, comment="I liked the sauce, but the company was terrible! I think his father was drunk...")
rat2 = Rating(user=u3, host=u1, stars=5, comment="had a good time =) his dad is a fun guy")
ecv.session.add(rat1)
ecv.session.add(rat2)
# commit changes
ecv.session.commit()

u = ecv.session.query(User).all()
u1 = u[0]
u2 = u[1]
u3 = u[2]


# check if everything is added and accessable
allPersons = ecv.session.query(User).all()
for person in allPersons:
	print(person.username)

# list all offers (or just the first in this case)
offering = ecv.session.query(Offer).first()
print (offering.host.username+" offered "+str(offering.portions)+" portions EUR "+str(offering.price)+"per portion. \""+offering.info)

# list all reservations
allReservations = ecv.session.query(Reservation).all()
for reserv in allReservations:
	print(reserv.user.username + " has reserved "+str( reserv.portions)+" portions from " + reserv.offer.host.username +"s offering" )

# check sems ratings
for rating in u1.rateds:
	print(u1.username+" was rated "+str(rating.stars)+" stars by "+rating.user.username+ " saying \""+rating.comment+"\"")

# todo: write functions that can add users, offers, reservations, ratings
# 			to the database, with constraint checking
# then the client needs to be build in a webapp ???
# or should we "simulate" clients ? 



