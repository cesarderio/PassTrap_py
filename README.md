# PassTrap

PassTrap is a user-friendly password manager application built using Python and Tkinter. It provides a secure solution for storing and managing passwords for various websites and services.

## Key Features

- User-friendly graphical interface using Tkinter.

- Requires user authentication to access the password manager.

- Strong password encryption using industry-standard algorithms.

- Intuitive controls for adding, updating, and deleting password entries.

- Securely store and manage website, username, and password combinations.

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

(*Currently in development:*

- *You can run main.py file for login with username/password authentication*

  - *Demo username: cesar | password: pass | pin: 0000*

- *Or you can run Pass_Trap.py for minimal version with only pincode verification to show password.*)

1. Download and Install: Clone the PassTrap repository or download the source code to your local machine.

2. Install Dependencies: Install the necessary dependencies by running

        pip install -r requirements.txt

3. Run PassTrap: Launch PassTrap by executing the

        main.py file

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

1. Install **pyinstaller** package:

        pip install pyinstaller

2. Generate the executable:

        - Open a command prompt or terminal window and navigate to the PassTrap project directory.

        - Run the following command:

                pyinstaller --onefile main.py

        - This command will create a standalone executable file named main.exe (or main on Linux/Mac) in the dist directory.

3. Locate and Run the Executable:

        - The generated executable file can be found in the dist directory.

        - Double-click the main.exe (or main on Linux/Mac) file to run PassTrap without the need for Python installation.

***Note: The executable file may trigger antivirus software due to the nature of its packaging. You may need to whitelist or allow the file to run.***

- *Windows Defender settings*:

- *Open the Windows Defender Security Center:*

        - Click on the Start menu, search for "Windows Security," and open the Windows Security app.

- *Go to Virus & Threat Protection:*

        - In the Windows Security app, click on "Virus & Threat Protection" in the left-hand navigation pane.

- *Exclusion Settings:*

        - Under the "Virus & Threat Protection settings" section, click on "Manage settings."

- *Add an Exclusion:*

        - Scroll down to the "Exclusions" section and click on the "Add or remove exclusions" link.

- *Add an Exclusion for a File:*

        - Click on the "Add an exclusion" button and select "File" from the dropdown menu.

- *Browse and Select the Executable:*

        - Navigate to the directory where your executable file is located and select it. Click on "Open" to add the file as an exclusion.

## Security

PassTrap prioritizes the security and confidentiality of your passwords. It employs industry-standard encryption algorithms to protect your data from unauthorized access. However, it is crucial to maintain the security of your master password and take necessary precautions to secure your device and encryption key file.

## Requirements

- [***Python***](https://www.python.org/) 3.x
- [***Tkinter***](https://docs.python.org/3/library/tkinter.html) module
- [***Fernet***](https://cryptography.io/en/latest/fernet/) cryptography module

## Installation

1. Clone the repository or download the source code.

2. Install Python 3.x if it is not already installed. You can download Python from the official website: [Python](https://www.python.org/downloads/)

3. Install the required dependencies:

        pip install -r requirements.txt

***Dependencies can be installed independently:***

- ### Install Tkinter module

  - For Windows users: Tkinter is typically included with Python installation. You can check if it is installed by running the following command in the command prompt:

        python -m tkinter

    - If Tkinter is not installed, you can install it using the following command:

          pip install tk

  - For Linux users:

    - Tkinter is often included with the default Python installation. You can install it using the package manager specific to your distribution. For example, on Ubuntu, you can use the following command:

            sudo apt-get install python3-tk

  - For macOS users: Tkinter is included with the standard Python installation.

- ### Install the cryptography module

        pip install cryptography

        - This module is used for encrypting and decrypting passwords in PassTrap.

## Usage 1

***(Full version with sign authentication functionality and pincode verification to show passwords)***

1. Run the main.py file:

        python3 main.py

2. The Sign In window will appear. Set up your username and password or sign in if you have already set them up.

3. Once signed in, the Passwords window will open, allowing you to manage your passwords.

4. Use the "***Change PIN***" button to update or change the pin code to display saved passwords.

5. Use the "***Randomizer***" button to generate a new random password.

6. Use the "***Add***" button to add a new password entry with the website, username, and password.

7. Use the "***Update***" button to modify an existing password entry.

8. Use the "***Delete***" button to remove a password entry.

## Usage 2 *(Minimal (less secure) version without sign in authentication. Keeps pincode verification to make passwords visible.)*

1. Run the Pass_Trap.py file:

        python3 Pass_Trap.py

2. The Passwords manager window will open, allowing you to manage your passwords.

3. Use the "Change PIN" button to update or change the pin code to display saved passwords.

4. Use the "Randomizer" button to generate a new random password.

5. Use the "Add" button to add a new password entry with the website, username, and password.

6. Use the "Update" button to modify an existing password entry.

7. Use the "Delete" button to remove a password entry.

## Screenshots

![Login Window](./assets/loginWindowLinuxDark.png)

![Login Window](./assets/loginWindowLinuxLightV2.png)

![Password Manager](./assets/passwordKeeperWindowLinuxDark.png)

![Password Manager](./assets/passwordKeeperWindowLinuxLight.png)

![Password Manager](./assets/passwordKeeperWindowpswdsLinuxDark.png)

![Pin unlock to make password visible](./assets/pinWindowLinuxDark.png)

![Pin unlock to make password visible](./assets/pinWindowLinuxLight.png)

![Password Manager](./assets/passwordKeeperWindowLinuxDarkpswdsShown.png)

## License

This project is licensed under the MIT License. See the LICENSE file for more information.# PassTrap
