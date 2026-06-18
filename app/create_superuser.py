from database import SessionLocal
from user.models import User

db = SessionLocal()

user = User(
    name = "Super Admin",
    admin = "admin@travel.com",
    role="superuser"

)

db.add(user)
db.commit()
print("Superuser created successfully!")
