from flask import  Flask, render_template, request, send_file
import os
from crypto_utils import encrypt_file, decrypt_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted"
DECRYPTED_FOLDER = "decrypted"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    if request.method == "POST":
        file = request.files["file"]

        if file:
            input_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(input_path)

            encrypted_filename = file.filename + ".enc"
            key_filename = file.filename + ".key"

            encrypted_path = os.path.join(ENCRYPTED_FOLDER, encrypted_filename)
            key_path = os.path.join(ENCRYPTED_FOLDER, key_filename)

            encrypt_file(input_path, encrypted_path, key_path)

            return f"""
            <h2>🔐 File Encrypted Successfully!</h2>
            <p>Download your encrypted file and key:</p>
            <a href="/download/encrypted/{encrypted_filename}">⬇ Download Encrypted File</a><br><br>
            <a href="/download/encrypted/{key_filename}">🔑 Download Key File</a><br><br>
            <a href="/">🏠 Back to Home</a>
            """

    return render_template("encrypt.html")


# 🔓 DECRYPT ROUTE (WITH DOWNLOAD)
@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    if request.method == "POST":
        enc_file = request.files["enc_file"]
        key_file = request.files["key_file"]

        if enc_file and key_file:
            enc_path = os.path.join(ENCRYPTED_FOLDER, enc_file.filename)
            key_path = os.path.join(ENCRYPTED_FOLDER, key_file.filename)

            enc_file.save(enc_path)
            key_file.save(key_path)

            output_filename = "decrypted_" + enc_file.filename.replace(".enc", "")
            output_path = os.path.join(DECRYPTED_FOLDER, output_filename)

            decrypt_file(enc_path, output_path, key_path)

            return f"""
            <h2>🔓 File Decrypted Successfully!</h2>
            <a href="/download/decrypted/{output_filename}">⬇ Download Decrypted File</a><br><br>
            <a href="/">🏠 Back to Home</a>
            """

    return render_template("decrypt.html")


from flask import send_file
@app.route("/download/encrypted/<filename>")
def download_encrypted(filename):
    path = os.path.join(ENCRYPTED_FOLDER, filename)
    return send_file(
        path,
        as_attachment=True,
        download_name=filename,
        mimetype="application/octet-stream"
    )


# 📥 DOWNLOAD DECRYPTED FILE (ORIGINAL NAME)
@app.route("/download/decrypted/<filename>")
def download_decrypted(filename):
    path = os.path.join(DECRYPTED_FOLDER, filename)
    return send_file(
        path,
        as_attachment=True,
        download_name=filename,
        mimetype="application/octet-stream"
    )

if __name__ == "__main__":
    app.run(debug=True)