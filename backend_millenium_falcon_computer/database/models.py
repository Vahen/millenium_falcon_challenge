from flask import jsonify
from sqlalchemy import Column, Integer, String
from backend_millenium_falcon_computer.database import Base


# We should not need to put everything with primary keys, but since we have no ID or unique things,
# SQL alchemy wants a primary key and it
#
class Routes(Base):
    __tablename__ = "routes"
    origin = Column(String(128), primary_key=True)
    destination = Column(String(128), primary_key=True)
    travel_time = Column(Integer, primary_key=True)

    # ORIGIN (TEXT): Name of the origin planet. Cannot be null or empty.
    # DESTINATION (TEXT): Name of the destination planet. Cannot be null or empty.
    # TRAVEL_TIME (INTEGER): Number days needed to travel from one planet to the other. Must be strictly positive.

    #
    def __repr__(self):
        return '{\norigin: \"'+self.origin+'\",\n' + \
               'destination: \"'+self.destination+'\",\n' + \
               'travel_time: '+str(self.travel_time)+'\n}\n'

    #
    def to_json(self):
        return {"origin": self.origin,
                'destination': self.destination,
                'travel_time': self.travel_time,
                }
