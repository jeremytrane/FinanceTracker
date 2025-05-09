# Finance Tracker

A Flask-based web application for tracking and managing your subscriptions and recurring payments. Keep track of your monthly and yearly expenses with an easy-to-use interface.

## Features

- **Subscription Management**
  - Add, edit, and delete subscriptions
  - Categorize subscriptions (Entertainment, Software, Utilities, etc.)
  - Track billing cycles (monthly/yearly)
  - Set next billing dates
  - Add descriptions for each subscription

- **Payment History**
  - Record payment history for each subscription
  - View payment details including date, amount, and notes
  - Track payment patterns over time

- **Financial Overview**
  - View total monthly and yearly expenses
  - See category-wise expense breakdown
  - Track costs in euros (€)
  - Monitor upcoming billing dates

## Technology Stack

- **Backend**: Python with Flask framework
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, Bootstrap 5
- **Features**: 
  - Flask-SQLAlchemy for database management
  - Flask templates for dynamic content
  - Bootstrap for responsive design

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/FinanceTracker.git
cd FinanceTracker
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. **Adding Subscriptions**
   - Click "Add New Subscription"
   - Fill in the subscription details
   - Select a category
   - Set the billing cycle and next billing date

2. **Managing Payments**
   - Click "Payments" on any subscription
   - View payment history
   - Record new payments with notes

3. **Editing Subscriptions**
   - Click "Edit" on any subscription
   - Update details as needed
   - Save changes

4. **Viewing Expenses**
   - See total monthly and yearly costs
   - View category-wise breakdown
   - Monitor upcoming payments

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask framework and its extensions
- Bootstrap for the UI components
- SQLAlchemy for database management 