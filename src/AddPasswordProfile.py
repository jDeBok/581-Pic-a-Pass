import sys
import csv
import time
from generatepassword import PasswordGenerator
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox, QLabel
from password_strength import p_strength #password strength function
class AddPasswordProfile(QWidget):
    def __init__(self, super_window, super_object ):
        super().__init__()
        self.initUI( super_window, super_object )

    def initUI( self, super_window, super_object ):
        # Set up the form layout
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        # Input fields
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.input3 = QLineEdit()
        self.input4 = QLineEdit()
        
        # Add input fields to the form layout with labels
        form_layout.addRow("Web URL:", self.input1)
        form_layout.addRow("Username:", self.input2)
        form_layout.addRow("Password:", self.input3)
        #show password strength
        self.strength_label = QLabel( "Password strength: Waiting..." )
        self.strength_label.setFont(QFont("Arial", 14))
        form_layout.addWidget( self.strength_label )
        self.input3.textChanged.connect(self.check_password_strength)
        form_layout.addRow("Notes:", self.input4)
        #timetamp is automatic
        layout.addLayout(form_layout)
        # Generate button
        generate_button = QPushButton("Generate Password")
        generate_button.clicked.connect( self.generate_pw )
        layout.addWidget( generate_button )
        # Save button
        save_button = QPushButton("Save to CSV")
        save_button.clicked.connect(self.save_to_csv)
        save_button.clicked.connect( super_window.close )
        #refresh the main page
        save_button.clicked.connect( super_object.refresh )
        layout.addWidget(save_button)
        
        self.setLayout(layout)

    def save_to_csv(self):
        # Get values from input fields
        data = [
            self.input1.text(),
            self.input2.text(),
            self.input3.text(),
            self.input4.text(),
            time.time()
        ]
        
        # Open file dialog to choose where to save the CSV
        file_path = "passwords.csv"
        
        # Save data to CSV file
        try:
            with open(file_path, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)
            #QMessageBox.information(self, "Success", "Data saved to CSV file successfully!")
            #Don't bring up success box
            # Clear the input fields
            self.input1.clear()
            self.input2.clear()
            self.input3.clear()
            self.input4.clear()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save data: {e}")
    def generate_pw( self ):
        pw = PasswordGenerator()
        self.input3.setText( pw.generate_password() )
    def check_password_strength( self ):
        if self.input3.text() == "":
            #do nothing, prevents crashing
            a = 1
        elif p_strength( self.input3.text() ) == 0:
            #weak
            self.strength_label.setText("Password strength: Weak")
            self.strength_label.setStyleSheet("color: red;")
        elif p_strength( self.input3.text() ) == 1:
            self.strength_label.setText("Password strength: Medium")
            self.strength_label.setStyleSheet("color: orange;")
        else:
            #strong
            self.strength_label.setText("Password strength: Strong")
            self.strength_label.setStyleSheet("color: green;")
