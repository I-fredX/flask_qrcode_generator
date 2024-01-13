from flask import Flask, render_template, request, send_file, jsonify
import helper
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello World!"})

@app.route("/qr_code", methods=["POST"])
def qr_code():
    try:
        json_data = request.get_json()
        if "data" in json_data:
            data = json_data["data"]
            name = data["name"]
            employee_id = data["employee_id"]
            filename = helper.generate_qr_code(helper.generate_uuid(name, employee_id))
            return "QR code generated successfully at {}".format(filename)
            
        else:
            return jsonify({"message": "No data provided"})
    except Exception as e:
        print(e)
        return jsonify({"message": "Invalid data provided"})





if __name__ == "__main__":
    app.run(debug=True)