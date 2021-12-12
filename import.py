import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("")
db = scoped_session(sessionmaker(bind=engine))



def main():
    f = open("posts.csv")
    reader = csv.reader(f)
    image = "a"
    for id, title, content, id_tourist_area,id_place in reader:
        db.execute("insert into posts (id, title, content,image, id_tourist_area,id_place) values(:id, :title, :content, :image, :id_tourist_area, :id_place)",
        {"id":id, "title": title, "content": content,"image": image, "id_tourist_area": id_tourist_area, "id_place":id_place})
        print(f"oke")
    db.commit()



if __name__ == '__main__':
    main()