import sys
import csv
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
class create(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the form layout
        self.setWindowTitle("Form to CSV")
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
        form_layout.addRow("Notes:", self.input4)
        #timetamp is automatic
        layout.addLayout(form_layout)
        
        # Save button
        save_button = QPushButton("Save to CSV")
        save_button.clicked.connect(self.save_to_csv)
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
            with open(file_path, mode="a", newline="\n") as file:
                writer = csv.writer(file)
                writer.writerow(data)
            QMessageBox.information(self, "Success", "Data saved to CSV file successfully!")
            
            # Clear the input fields
            self.input1.clear()
            self.input2.clear()
            self.input3.clear()
            self.input4.clear()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save data: {e}")