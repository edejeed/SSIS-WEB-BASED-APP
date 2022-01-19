from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

class Uploader(FlaskForm):
    profile = FileField(validators=[FileAllowed(['png', 'jpg', 'jpeg'])])