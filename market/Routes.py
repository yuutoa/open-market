from market import app
from flask import render_template, redirect, url_for, flash, request
from market.Models import Item, User
from market.forms import (
    RegisterForm,
    LoginForm,
    PurchaseItemForm,
    SellItemForm,
    AddItemForm,
)
from market import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market", methods=["GET", "POST"])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method == "POST":
        # Purchase Item Logic
        purchased_item = request.form.get("purchased_item")
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(
                    f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$",
                    category="success",
                )
            else:
                flash(
                    f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!",
                    category="danger",
                )
        return redirect(url_for("market_page"))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None).all()
        return render_template("market.html", items=items, purchase_form=purchase_form)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if email is already registered
        existing_user = User.query.filter_by(
            email_address=form.email_address.data
        ).first()
        if existing_user:
            flash(
                "An account with this email address already exists. Please log in or use a different email.",
                category="danger",
            )
            return render_template("register.html", form=form)

        # Create and save the new user
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data,
        )
        try:
            db.session.add(user_to_create)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash(
                "An unexpected error occurred while creating your account. Please try again later.",
                category="danger",
            )
            return render_template("register.html", form=form)

        # Log in the new user
        login_user(user_to_create)
        flash(
            f"Your account has been created successfully! Welcome, {user_to_create.username}!",
            category="success",
        )
        return redirect(url_for("market_page"))

    # Handle form errors
    if form.errors:
        flashed_messages = set()
        if "username" in form.errors:
            flash(
                "The username is already taken. Please try a different one.",
                category="danger",
            )
        if "email_address" in form.errors:
            flash(
                "The email address you entered is invalid. Please provide a valid email.",
                category="danger",
            )
        if "password1" in form.errors or "password2" in form.errors:
            flash(
                "Passwords must match and meet complexity requirements. Please try again.",
                category="danger",
            )

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f"Welcome back! You have logged in successfully.", category="success")
            return redirect(url_for("market_page"))
        else:
            flash("Invalid username or password. Please try again.", category="danger")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logged out. See you next time!", category="info")
    return redirect(url_for("home_page"))


@app.route("/account", methods=["GET", "POST"])
@login_required
def account_page():
    selling_form = SellItemForm()
    add_item_form = AddItemForm()

    if request.method == "POST":
        # Handle selling items
        if selling_form.validate_on_submit() and "sold_item" in request.form:
            sold_item_name = request.form.get("sold_item")
            s_item_object = Item.query.filter_by(
                name=sold_item_name, owner=current_user.id
            ).first()
            if s_item_object:
                s_item_object.sell(current_user)
                flash(
                    f"Successfully sold {s_item_object.name} back to the market!",
                    category="success",
                )
            else:
                flash(
                    "Error: Could not sell the item. Please try again.",
                    category="danger",
                )

        # Handle adding new items
        if add_item_form.validate_on_submit():
            new_item = Item(
                name=add_item_form.name.data,
                price=add_item_form.price.data,
                description=add_item_form.description.data,
                owner=current_user.id,
                added_by_user=current_user.username,
            )
            try:
                db.session.add(new_item)
                db.session.commit()
                flash(f"Item '{new_item.name}' added successfully!", category="success")
            except Exception as e:
                db.session.rollback()
                flash(
                    "An error occurred while adding the item. Please try again.",
                    category="danger",
                )

        return redirect(url_for("account_page"))

    # Fetch items for the account page
    owned_items = Item.query.filter_by(owner=current_user.id).all()
    return render_template(
        "account.html",
        owned_items=owned_items,
        add_item_form=add_item_form,
        selling_form=selling_form,
    )


@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response
