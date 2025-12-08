from database import db
from datetime import datetime


class Problem(db.Model):
    __tablename__ = "problems"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    method_type = db.Column(db.String(50), nullable=False)  # 'CG', 'SOR', 'ROOTS', 'INTERPOLATION'
    input_data = db.Column(db.Text, nullable=False)  # JSON string con los parámetros de entrada
    result_data = db.Column(db.Text, nullable=False)  # JSON string con los resultados
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    title = db.Column(db.String(200), nullable=True)  # Título descriptivo del problema

    # Relación con User
    user = db.relationship('User', backref=db.backref('problems', lazy=True))

    def __init__(self, user_id, method_type, input_data, result_data, title=None):
        self.user_id = user_id
        self.method_type = method_type
        self.input_data = input_data
        self.result_data = result_data
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Problem.query.all()

    @staticmethod
    def get_by_id(id):
        return Problem.query.get(id)

    @staticmethod
    def get_by_user(user_id):
        return Problem.query.filter_by(user_id=user_id).order_by(Problem.created_at.desc()).all()

    @staticmethod
    def get_by_method(method_type):
        return Problem.query.filter_by(method_type=method_type).order_by(Problem.created_at.desc()).all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
