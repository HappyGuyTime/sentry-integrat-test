import sentry_sdk, logging
from flask import Flask, request
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_sdk.init(
    dsn="https://2a1ddee8bf3af190463a6091c8c7f0d0@o4505386053140480.ingest.us.sentry.io/4506919706492928",
    integrations=[FlaskIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


@app.route('/test_type')
def test_type():
    user_id = request.args.get('user_id')
    user_id = float(user_id)


@app.route('/test')
def ll():
    raise IndexError


@app.route('/test_logging')
def test_logging():
    logging.error("error to log")


if __name__ == '__main__':
    app.run()