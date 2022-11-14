from app import db, app

with app.app_context():
    db.session.execute("TRUNCATE TABLE tb_data")