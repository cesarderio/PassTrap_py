# PassTrap

PassTrap is a user-friendly password manager application built using Python and Tkinter. It provides a secure solution for storing and managing passwords for various websites and services.

## Key Features

- User-friendly graphical interface using Tkinter.
- Strong password encryption using industry-standard algorithms.
- Intuitive controls for adding, updating, and deleting password entries.
- Securely store and manage website, username, and password combinations.
<!-- - Requires user authentication to access the password manager. -->
## How PassTrap Works

PassTrap ensures that your passwords are stored securely and easily accessible when needed. Here's how it works:

1. Store Passwords: Enter the website, username, and password details into PassTrap's password manager.
2. Secure Encryption: PassTrap employs robust encryption algorithms to encrypt and safeguard your passwords, ensuring they remain confidential and protected.
3. Easy Access: Retrieve your stored passwords whenever required, providing convenience and eliminating the need to remember multiple passwords.
4. Password Management: Update or delete password entries as needed to keep your records up to date.
5. User-Friendly Interface: PassTrap's intuitive and visually appealing interface makes it easy to navigate and manage your passwords efficiently.

## Why Use PassTrap?

PassTrap offers several advantages that make it an excellent choice for password management:

- Convenient Access: Access your passwords with ease whenever you need them, allowing for a seamless login experience without the hassle of manual password retrieval.
- Enhanced Security: By storing your passwords in PassTrap, you reduce the risk of using weak or easily guessable passwords, improving overall security for your online accounts.
- User-Friendly Design: PassTrap's intuitive and visually appealing interface ensures a smooth user experience, even for individuals without technical expertise.
- Simplified Password Management: PassTrap eliminates the need to remember multiple passwords for various websites or services, making your password management more efficient.

## Getting Started

To get started with PassTrap, follow these simple steps:
(Currently in development - You can run main.py file for login with username/password authentication or you can run Pass_Trap.py for minimal version with pincode verification to show password.)

1. Download and Install: Clone the PassTrap repository or download the source code to your local machine.
2. Install Dependencies: Install the necessary dependencies by running
        ***pip install -r requirements.txt.***
3. Run PassTrap: Launch PassTrap by executing the
        ***main.py file***.
4. Store and Manage Passwords: Add your website, username, and password details to the password manager. Update or delete entries as needed.
5. Retrieve Passwords: Access your stored passwords whenever required to simplify the login process.

## Customization and Further Development

PassTrap can be customized and extended to meet your specific requirements. Consider the following possibilities:

- Implement password strength validation.
- Improve error handling and user feedback.
- Add a feature to generate secure passwords.
- Add additional fields to the password entry form (e.g., email, notes).
- Enhance the user interface with themes, icons, or personalized branding.
- Integrate with cloud storage or sync functionality for cross-device password access.
- Implement additional features such as password strength assessment, password generation, or category-based organization of password entries.
- Expand PassTrap's security features, such as two-factor authentication or biometric login options.

## Creating an Executable File

PassTrap can be converted into an executable file for easy distribution and usage on systems without Python installed. Follow these steps to create an executable file:

1. Install **pyinstaller** package: Run ***pip install pyinstaller*** to install the **pyinstaller** package, which will be used to create the executable file.
2. Generate the executable: Open a command prompt or terminal window and navigate to the PassTrap project directory. Run the following command:
        ***pyinstaller --onefile main.py***
        *This command will create a standalone executable file named main.exe (or main on Linux/Mac) in the dist directory.*
3. Locate and Run the Executable: The generated executable file can be found in the dist directory. Double-click the ***main.exe*** (or ***main*** on Linux/Mac) file to run PassTrap without the need for Python installation.
***Note**: The executable file may trigger antivirus software due to the nature of its packaging. You may need to whitelist or allow the file to run.*

## Security

PassTrap prioritizes the security and confidentiality of your passwords. It employs industry-standard encryption algorithms to protect your data from unauthorized access. However, it is crucial to maintain the security of your master password and take necessary precautions to secure your device and encryption key file.

## Requirements

- ***Python*** 3.x
- ***Tkinter*** module
- ***Fernet*** cryptography module

## Installation

1. Clone the repository or download the source code.

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

## Usage

1. Run the main.py file:

        python3 main.py

2. The Sign In window will appear. Set up your username and password or sign in if you have already set them up.

3. Once signed in, the Passwords window will open, allowing you to manage your passwords.

4. Use the "Change PIN" button to update or change the pin code to display saved passwords.

5. Use the "Randomizer" button to generate a new random password.

6. Use the "Add" button to add a new password entry with the website, username, and password.

7. Use the "Update" button to modify an existing password entry.

8. Use the "Delete" button to remove a password entry.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.# PassTrap
