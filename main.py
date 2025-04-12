from ufc_data_scraper import ufc_scraper
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "UFC Scraper API draait!"

@app.route("/event", methods=["GET"])
def get_event():
    event_url = request.args.get("url")
    if not event_url:
        return jsonify({"error": "Geef een geldige UFC event URL mee als queryparam ?url=..."}), 400

    try:
        event = ufc_scraper.scrape_event_url(event_url)
        return jsonify({
            "event_name": event.name,
            "status": event.status,
            "date": str(event.date),
            "location": event.location.venue,
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)