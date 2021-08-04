from datetime import date

from my_db.model.base import Session, engine, Base
from my_db.model.Actor import Actor
from my_db.model.ContactDetails import ContactDetails
from my_db.model.Movie import Movie
from my_db.model.Stuntman import Stuntman


def addInfo():
    #Generate database schema
    Base.metadata.create_all(engine)

    #Create a new session
    session = Session()

    #Create movies
    bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
    furious_7 = Movie("Furious 7", date(2015, 4, 2))
    pain_and_gain = Movie("Pain & Gain", date(2013, 8, 23))

    #Create actors
    matt_damon = Actor("Matt Damon",date(1970, 10, 8))
    dwayne_johnson = Actor("Dwayne Johnson", date(1972, 5, 2))
    mark_wahlberg = Actor("Mark Wahlberg", date(1971, 6, 5))

    #Add actors to movies
    bourne_identity.actors = [matt_damon]
    furious_7.actors = [dwayne_johnson]
    pain_and_gain.actors = [dwayne_johnson, mark_wahlberg]

    #Add contact details to actors
    matt_contact = ContactDetails("415 555 2671", "Burbank, CA", matt_damon)
    dwayne_contact = ContactDetails("423 555 5623", "Glendale, CA", dwayne_johnson)
    dwayne_contact_2 = ContactDetails("421 444 2323", "West Hollywood, CA", dwayne_johnson)
    mark_contact = ContactDetails("421 333 9428", "Glendale, CA", mark_wahlberg)

    #Create stuntman
    matt_stuntman = Stuntman("John Doe", True, matt_damon)
    dwayne_stuntman = Stuntman("John Roe", True, dwayne_johnson)
    mark_stuntman = Stuntman("Richard Roe", True, mark_wahlberg)

    #Persists data
    session.add(bourne_identity)
    session.add(furious_7)
    session.add(pain_and_gain)

    session.add(matt_contact)
    session.add(dwayne_contact)
    session.add(dwayne_contact_2)
    session.add(mark_contact)

    session.add(matt_stuntman)
    session.add(dwayne_stuntman)
    session.add(mark_stuntman)

    #Commit and close session
    session.commit()
    session.close()



if __name__ == "__main__":
    addInfo()



