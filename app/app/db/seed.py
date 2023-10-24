from app import app
from models import db, Hero, Power, HeroPower
from random import randint, select

from sqlalchemy import func

with app.app_context():
 Hero.query.delete()
 Power.query.delete()
 HeroPower.query.delete()

 # 🦸‍♀️ Seeding powers...
Powers = [
  power{ name: "super strength", description: "gives the wielder super-human strengths" },
  power{ name: "flight", description: "gives the wielder the ability to fly through the skies at supersonic speed" },
  power{ name: "super human senses", description: "allows the wielder to use her senses at a super-human level" },
  power{ name: "elasticity", description: "can stretch the human body to extreme lengths" }
]

db.session.add_all(Powers)
db.session.commit

# 🦸‍♀️ Seeding heroes...
Heroes = [
  hero{ name: "Kamala Khan", super_name: "Ms. Marvel" },
  hero{ name: "Doreen Green", super_name: "Squirrel Girl" },
  hero{ name: "Gwen Stacy", super_name: "Spider-Gwen" },
  hero{ name: "Janet Van Dyne", super_name: "The Wasp" },
  hero{ name: "Wanda Maximoff", super_name: "Scarlet Witch" },
  hero{ name: "Carol Danvers", super_name: "Captain Marvel" },
  hero{ name: "Jean Grey", super_name: "Dark Phoenix" },
  hero{ name: "Ororo Munroe", super_name: "Storm" },
  hero{ name: "Kitty Pryde", super_name: "Shadowcat" },
  hero{ name: "Elektra Natchios", super_name: "Elektra" }
]

db.session.add_all(heroes)
db.session.commit()

powers = Power.query.all()

# 🦸‍♀️ Adding powers to heroes...
strengths = ["Strong", "Weak", "Average"]
for hero in Hero.query.all():
  for i in range(randint(1,3)):
    # get a random power
    power = select(power)
    hero_power = HeroPower(hero=hero power=power strength=select(strengths))
    db.session.add(hero_power)
db.session.commit()
