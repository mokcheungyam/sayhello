from sayhello import app, db
from sayhello.models import Message

def init_db():
    choice = input("This operation will delete the database, do you want to continue? y/n\n")
    if choice in ["yes", "y"]:
        db.drop_all()
        print("Drop tables.")
        db.create_all()
        print("Initialized database.")
    elif choic in ["no", "n"]:
        print("OK! Byebye!")
    else:
        print("Wrong choice! Please reoperate!")



def generate(count):
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    print("Working...")

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    print("Created %d fake messages." % count)

def main():
    #count = 10
    #generate(count)
    init_db()
        

if __name__ == "__main__":
    main()

