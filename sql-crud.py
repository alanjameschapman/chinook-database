from sqlalchemy import (
    create_engine, Column, Integer, String,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
# class Programmer(base):
#     __tablename__ = "Programmer"

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous_for = Column(String)

# create a class-based model for the favourite games table
class FaveGames(base):
    __tablename__ = "FavouriteGames"

    id = Column(Integer, primary_key=True)
    game = Column(String)
    number_of_players = Column(Integer)
    difficulty = Column(String)
    length_of_game = Column(Integer)

# instead of connecting to the database directly, we will use a session
# create a new instance of sessionmaker and point it to our database
Session = sessionmaker(db)
# opens an actual session by calling the Session() sub-class we just created
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on the "FaveGames" table
game1 = FaveGames(
    id=1,
    game="Catan",
    number_of_players=4,
    difficulty="Medium",
    length_of_game=60
)

game2 = FaveGames(
    id=2,
    game="Ticket to Ride",
    number_of_players=4,
    difficulty="Easy",
    length_of_game=45
)

game3 = FaveGames(
    id=3,
    game="Pandemic",
    number_of_players=4,
    difficulty="Hard",
    length_of_game=60
)

game4 = FaveGames(
    id=4,
    game="Carcassonne",
    number_of_players=4,
    difficulty="Easy",
    length_of_game=45
)

# creating records on the "Programmer" table
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Programmer"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL Language"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous_for="Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous_for="World Wide Web"
# )

# alan_chapman = Programmer(
#     first_name="Alan",
#     last_name="Chapman",
#     gender="M",
#     nationality="British",
#     famous_for="Being a great teacher!"
# )

# updating a single record on the "Programmer" table
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Being awesome!"

# updating a single record on the "FaveGames" table
# game = session.query(FaveGames).filter_by(id=1).first()
# game.difficulty = "Hard"

# updating multiple records on the "Programmer" table
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print('Gender not specified!')
#     session.commit()

# add each instance of the "Programmer" class to the session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(alan_chapman)
# session.add(game1)
# session.add(game2)
# session.add(game3)
# session.add(game4)

# commit the session to the database
session.commit()

# delete a single record on the "Programmer" table
# fname = input("Input first name: ")
# lname = input("Input last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Found programmer:", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted!")
#     else:
#         print("Programmer not deleted!")
# else:
#     print("No records found!")

# delete records with id 13 and 14 on the "FaveGames" table
# game = session.query(FaveGames).filter_by(id=13).first()
# session.delete(game)
# game = session.query(FaveGames).filter_by(id=14).first()
# session.delete(game)
# session.commit()


# query the database for all programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(programmer.id,
#           programmer.first_name + " " + programmer.last_name,
#           programmer.gender,
#           programmer.nationality,
#           programmer.famous_for,
#           sep=" | ")

# query the database for all games
games = session.query(FaveGames)
for game in games:
    print(game.id,
          game.game,
          game.number_of_players,
          game.difficulty,
          game.length_of_game,
          sep=" | ")
