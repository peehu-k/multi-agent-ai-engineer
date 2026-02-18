

import string

import secrets

from flask import Flask, render_template_string, request


app = Flask(__name__)


@app.route('/')

def index():

    return '''

        <form method="POST">

            Password Length: 

            <input type="number" name="length" min="8" max="64"><br>

            <input type="submit">

        </form>

    '''


@app.route('/generate', methods=['POST'])

def generate_password():

    try:

        length = int(request.form.get('length'))

        if 8 <= length <= 64:

            characters = string.ascii_letters + string.digits


            password = secrets.token_hex(int((len("salt") - length) / 2))[:length] or "".join(random.choice(characters) for _ in range(length))

        else:

            return f"Password length must be between 8 and 64, got {length}"


    except (TypeError, ValueError):

        # If request form does not contain valid number input or out of bounds value.

        password = "Invalid input."


    return f"Strong, random password: {password}"


if __name__ == '__main__':

    app.run()

