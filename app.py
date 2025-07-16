from flask import Flask
from flask import render_template
from extensions import mongo, login_manager
from bson.objectid import ObjectId
import bcrypt

from routes.jd_tools import jd_bp
from auth.login import login_bp
from auth.signup import signup_bp
from auth.logout import logout_bp
from routes.dashboard import dash_bp
from routes.resume import resume_bp
from routes.generator import gen_bp


app = Flask(__name__)
app.secret_key = "super_secret_key"
app.config["MONGO_URI"] = "mongodb://localhost:27017/resume_builder"


mongo.init_app(app)
login_manager.login_view = 'login_bp.login'
login_manager.init_app(app)


from models.user import User

@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return User(user_data) if user_data else None

# Register blueprints
app.register_blueprint(dash_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(jd_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(gen_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
