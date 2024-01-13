import qrcode
"""Generates a UUID for an employee and creates a QR code encoding their name, 
employee ID, and generated UUID.

The generate_uuid function generates a random UUID for the given employee name and ID.

The generate_qr_code function takes a dict with employee name, ID, and UUID, and creates a QR code 
encoding that data. The QR code is saved to a PNG file named after the employee. The filename is returned.
"""
import uuid0

# data = name, employee id
#generate_uuid
def generate_uuid(name:str, employee_id:str):
    return {"name": name, "uuid": str(uuid0.generate()),"employee_id": employee_id}

def generate_qr_code(data: dict) -> str:
    "This function creates and save our qrcode information"
    # unid = generate_id()
    img = qrcode.make(str({"name":data["name"],"employee_id": data["employee_id"], "unid": data["uuid"] }))
    filename = "{}_{}.png".format( data["name"], data["uuid"]) 
    img.save(filename)

    # save user information to the db

    return filename
