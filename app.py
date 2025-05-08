from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
db = SQLAlchemy(app)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    billing_cycle = db.Column(db.String(20), nullable=False)  # 'monthly' or 'yearly'
    next_billing_date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False, default='Other')  # New field
    description = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    subscriptions = Subscription.query.all()
    total_monthly = sum(sub.cost if sub.billing_cycle == 'monthly' else sub.cost/12 for sub in subscriptions)
    total_yearly = sum(sub.cost if sub.billing_cycle == 'yearly' else sub.cost*12 for sub in subscriptions)
    
    # Group subscriptions by category
    categories = {}
    for sub in subscriptions:
        if sub.category not in categories:
            categories[sub.category] = {
                'subscriptions': [],
                'monthly_total': 0,
                'yearly_total': 0
            }
        categories[sub.category]['subscriptions'].append(sub)
        categories[sub.category]['monthly_total'] += sub.cost if sub.billing_cycle == 'monthly' else sub.cost/12
        categories[sub.category]['yearly_total'] += sub.cost if sub.billing_cycle == 'yearly' else sub.cost*12

    return render_template('index.html', 
                         categories=categories,
                         subscriptions=subscriptions,
                         total_monthly=total_monthly,
                         total_yearly=total_yearly)

@app.route('/add', methods=['GET', 'POST'])
def add_subscription():
    if request.method == 'POST':
        name = request.form['name']
        cost = float(request.form['cost'])
        billing_cycle = request.form['billing_cycle']
        next_billing_date = datetime.strptime(request.form['next_billing_date'], '%Y-%m-%d').date()
        category = request.form['category']
        description = request.form['description']

        subscription = Subscription(
            name=name,
            cost=cost,
            billing_cycle=billing_cycle,
            next_billing_date=next_billing_date,
            category=category,
            description=description
        )

        db.session.add(subscription)
        db.session.commit()
        flash('Subscription added successfully!')
        return redirect(url_for('index'))

    # Predefined categories
    categories = ['Entertainment', 'Software', 'Utilities', 'Shopping', 'Health', 'Other']
    return render_template('add.html', categories=categories)

@app.route('/delete/<int:id>')
def delete_subscription(id):
    subscription = Subscription.query.get_or_404(id)
    db.session.delete(subscription)
    db.session.commit()
    flash('Subscription deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 