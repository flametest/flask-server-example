init db:

    from app import db
    with app.app_context():
        db.create_all()

one to one relation:

    user <-> user_profile
