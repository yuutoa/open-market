from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import (
    Length,
    EqualTo,
    Email,
    DataRequired,
    ValidationError,
    InputRequired,
    NumberRange,
)
from market.Models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                "Username already exists! Please choose another username."
            )

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data
        ).first()
        if email_address:
            raise ValidationError("Email address already exists! ")

    username = StringField(
        label="Username", validators=[Length(min=3, max=25), DataRequired()]
    )
    email_address = StringField(label="Email", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password", validators=[Length(min=6, max=100)])
    password2 = PasswordField(
        label="Confirm Password", validators=[EqualTo("password1"), DataRequired()]
    )
    submit = SubmitField(label="Register")


class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item!")


class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item!")


class AddItemForm(FlaskForm):
    name = StringField(
        label="Item Name", validators=[InputRequired(), Length(min=3, max=50)]
    )
    price = IntegerField(
        label="Price ($)", validators=[InputRequired(), NumberRange(min=1, max=99999)]
    )
    description = TextAreaField(
        label="Description", validators=[InputRequired(), Length(max=500)]
    )
    submit = SubmitField(label="Add Item to Market")
