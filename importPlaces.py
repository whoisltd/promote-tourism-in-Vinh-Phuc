import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://jxjsmnnorqvphr:d72266739d8fa38e2d4d814a9ea062d558710148b55a8a0cd037cf5fb57a04e4@ec2-18-210-95-55.compute-1.amazonaws.com:5432/d8gc0s3lfimj2g")
db = scoped_session(sessionmaker(bind=engine))



def main():
    f = open("places.csv")
    reader = csv.reader(f)
    image= "a"
    for id, title, description, id_tourist_area in reader:
        db.execute("insert into place (id, title, description, image, id_tourist_area) values(:id, :title, :description, :image, :id_tourist_area)",
        {"id":id, "title": title, "description": description, "image":image, "id_tourist_area":id_tourist_area})
        print(f"done")
    db.commit()



if __name__ == '__main__':
    main()