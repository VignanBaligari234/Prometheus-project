from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask

app = Flask(__name__)
metrics = PrometheusMetrics.for_app_factory()
metrics.init_app(app)

@app.route('/')
def root():
    return 'Hello from root!'

@app.route('/home')
def home():
    return 'Hello from home!'

@app.route('/contact')
def contact():
    return 'Contact us!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)