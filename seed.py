from models import Pet, db
from app import app
import datetime
# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add Base Pets
whiskey = Pet(name='Whiskey', species='Cat', photo_url='https://images.unsplash.com/photo-1593483316242-efb5420596ca?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80', age=4, notes="What a fine kitty. He will make a great friend one day!" )
bowser = Pet(name='Bowser', species='Dog', photo_url='https://images.unsplash.com/photo-1612958037591-db2a095230da?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80', age=3, notes="What a fine doggy. She will make a great friend one day!" )
spike = Pet(name='Spike', species='Porcupine', photo_url='https://images.unsplash.com/photo-1604962052822-eb6259a4c10a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1471&q=80', age=2, notes="What a fine porcupine. She will make a great friend one day!" )

## Add Base Dummy Post

#dummy_post = Post(title="It's a Dummy", content="I'm a post, and I'm a dummy!", user_id=1)
#dummy_post2 = Post(title="It's a Dummy", content="I'm a post, and I'm a dummy!", user_id=2)
#dummy_post3 = Post(title="It's a Dummy", content="I'm a post, and I'm a dummy!", user_id=3)

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# Commit--otherwise, this never gets saved!
db.session.commit()

## create / commit post after users are created so that the user_id of 1 is valid upon post creation
#db.session.add(dummy_post)
#db.session.add(dummy_post2)
#db.session.add(dummy_post3)
#db.session.commit()
