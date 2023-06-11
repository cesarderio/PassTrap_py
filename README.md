# PassTrap

PassTrap is a password manager application built using Python and Tkinter. It allows you to securely store and manage your passwords for different websites or services.

## Features

- Securely store website, username, and password combinations.
- Add, update, and delete password entries.
- Encrypts passwords using the Fernet encryption algorithm.
- Requires user authentication to access the password manager.
- Simple and user-friendly graphical interface using Tkinter.

## Requirements

- Python 3.x
- Tkinter module
- cryptography module

## Installation

1. Clone the repository or download the source code.

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

## Usage

1. Run the main.py file:

        python Pass_Trap.py

2. Use the "pin" button to add a new pin.

3. Use the "randomizer" button to generate a new random password.

4. Use the "Add" button to add a new password entry with the website, username, and password.

5. Use the "Update" button to modify an existing password entry.

6. Use the "Delete" button to remove a password entry.

<!--  The Sign In window will appear. Set up your username and password or sign in if you have already set them up. -->

<!--  Once signed in, the Passwords window will open, allowing you to manage your passwords. -->
## Customization

You can customize the behavior and appearance of the application by modifying the source code. Here are a few possible enhancements:

- Add additional fields to the password entry form (e.g., email, notes).
- Implement password strength validation.
- Improve error handling and user feedback.
- Add a feature to generate secure passwords.

## Security

PassTrap uses the Fernet encryption algorithm from the cryptography module to encrypt and decrypt passwords. It is important to keep your master password secure and ensure the confidentiality of the encryption key file (.key). Additionally, use strong and unique passwords for your accounts.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
