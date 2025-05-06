# Subscription Tracker

A simple web application to track your monthly and yearly subscriptions, with total cost calculations.

## Features

- Add, view, and delete subscriptions
- Track monthly and yearly billing cycles
- Calculate total monthly and yearly costs
- Modern, responsive UI using Tailwind CSS
- SQLite database for data persistence

## Setup

1. Install Python 3.8 or higher
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`

## Deployment

### Raspberry Pi Deployment

1. Install Python and pip on your Raspberry Pi
2. Clone this repository
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. To run the application in the background:
   ```bash
   nohup python app.py &
   ```

### AWS Deployment

1. Create an EC2 instance (t2.micro is sufficient)
2. Install Python and pip
3. Clone this repository
4. Install dependencies
5. Run the application using a process manager like PM2 or Supervisor
6. Configure your security group to allow traffic on port 5000

## Security Notes

- Change the `SECRET_KEY` in `app.py` before deploying to production
- Consider adding authentication for production use
- Use HTTPS in production

## License

MIT 