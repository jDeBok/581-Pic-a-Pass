import sys
import csv
import time
from generatepassword import PasswordGenerator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont
from password_strength import p_strength #password strength function
class EditPasswordProfile(QWidget):
    def __init__(self, super_window, super_object, label, password_profile_window, hash, cipher):
        super().__init__()
        self.hash = hash
        self.cipher = cipher
        self.initUI( super_window, super_object, label, password_profile_window )

    def initUI( self, super_window, super_object, label, password_profile_window ):
        self.setWindowTitle("Edit Password Profile")
        self.resize(900, 600)
        
        # Display label in new window
        self.layout = QVBoxLayout()
        #website
        self.label_website = QLabel( "Website" )
        self.label_website.setStyleSheet("""
            QLabel {
                font-family: Arial;
                font-size: 24px;
            }
             """)
        self.layout.addWidget( self.label_website )
        self.label_websiteReal = QLineEdit( label[ 0 ] ) #set label as website name
        self.label_websiteReal.setStyleSheet("""
            QLineEdit {
                font-family: Arial;
                font-size: 20px;
                border: 1px solid black;
                background-color: white;
            }
             """)
        self.label_websiteReal.setReadOnly( True )
        self.layout.addWidget( self.label_websiteReal )
        #Username
        self.label_uname = QLabel( "Username" )
        self.label_uname.setStyleSheet("""
            QLabel {
                font-family: Arial;
                font-size: 24px;
            }
             """)
        self.layout.addWidget( self.label_uname )
        self.label_unameReal = QLineEdit( label[ 1 ] ) #set label as user name
        self.label_unameReal.setStyleSheet("""
            QLineEdit {
                font-family: Arial;
                font-size: 20px;
                border: 1px solid black;
                background-color: white;
            }
             """)
        self.layout.addWidget( self.label_unameReal )
        #Password
        self.label_pw = QLabel( "Password" )
        self.label_pw.setStyleSheet("""
            QLabel {
                font-family: Arial;
                font-size: 24px;
            }
             """)
        self.layout.addWidget( self.label_pw )
        password = label[ 2 ]
        nonce = label[ 5 ]
        auth_data = label[ 1 ].encode('utf-8') # Use the username of the password as the authentication data
        self.label_pwReal = QLineEdit( password ) # Set label as password
        self.label_pwReal.setStyleSheet("""
            QLineEdit {
                font-family: Arial;
                font-size: 20px;
                border: 1px solid black;
                background-color: white;
            }
             """)
        self.layout.addWidget( self.label_pwReal )
        #show password strength
        self.strength_label = QLabel( "Password strength: Waiting..." )
        self.strength_label.setFont(QFont("Arial", 14))
        self.layout.addWidget( self.strength_label )
        self.label_pwReal.textChanged.connect(self.check_password_strength)
        self.check_password_strength() #sets original colors
        #Notes
        self.label_note = QLabel( "Username" )
        self.label_note.setStyleSheet("""
            QLabel {
                font-family: Arial;
                font-size: 24px;
            }
             """)
        self.layout.addWidget( self.label_note )
        self.label_noteReal = QLineEdit( label[ 3 ] ) #set label as user name
        self.label_noteReal.setStyleSheet("""
            QLineEdit {
                font-family: Arial;
                font-size: 20px;
                border: 1px solid black;
                background-color: white;
            }
             """)
        self.layout.addWidget( self.label_noteReal )
        #Add "Edit Password Profile" button to the bottom
        # Generate button
        generate_button = QPushButton("Generate Password")
        generate_button.clicked.connect( self.generate_pw )
        self.layout.addWidget( generate_button )
        # Save button
        save_button = QPushButton("Save to CSV")
        save_button.clicked.connect(self.save_to_csv)
        save_button.clicked.connect( super_window.close )
        #refresh the main page
        save_button.clicked.connect( super_object.refresh )
        save_button.clicked.connect( password_profile_window.close ) #close password profile menu to get back to list
        self.layout.addWidget(save_button)
        
        self.setLayout( self.layout)
        #self.show()

    def save_to_csv(self):
        # Get values from input fields
        auth_data = self.label_unameReal.text().encode('utf-8')
        ciphertext, nonce = self.cipher.encrypt(self.label_pwReal.text(), auth_data)
        data = [
            self.label_websiteReal.text(),
            self.label_unameReal.text(),
            ciphertext.decode('utf-8'),
            self.label_noteReal.text(),
            time.time(),
            nonce.decode('utf-8')
        ]

        
        # Open file dialog to choose where to save the CSV
        file_path = "passwords.csv"
        
        #save info from csv file except for my edit one
        lines_to_keep = []
    
        with open(file_path, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            
            # Iterate over each row in the CSV
            for row in reader:
                # If the value in the specified column does not match, keep the line
                if len(row) > 0:
                    if row[ 0 ] != self.label_websiteReal.text():
                        lines_to_keep.append(row)

        lines_to_keep.append( data ) #save new info
        # Write the lines back to the CSV file
        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(lines_to_keep)
    def generate_pw( self ):
        pw = PasswordGenerator()
        self.label_pwReal.setText( pw.generate_password() )
    def check_password_strength( self ):
        if self.label_pwReal.text() == "":
            #do nothing, prevents crashing
            a = 1
        elif p_strength( self.label_pwReal.text() ) == 0:
            #weak
            self.strength_label.setText("Password strength: Weak")
            self.strength_label.setStyleSheet("color: red;")
        elif p_strength( self.label_pwReal.text() ) == 1:
            self.strength_label.setText("Password strength: Medium")
            self.strength_label.setStyleSheet("color: orange;")
        else:
            #strong
            self.strength_label.setText("Password strength: Strong")
            self.strength_label.setStyleSheet("color: green;")
