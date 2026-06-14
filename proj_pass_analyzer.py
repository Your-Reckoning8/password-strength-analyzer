import os
from datetime import datetime

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.feedback = []

    def check_length(self):
        if len(self.password) < 8:
            self.feedback.append("Password is too short. Consider using at least 8 characters.")
        elif len(self.password) >= 12:
            self.score += 2
            self.feedback.append("Good length. Consider using 12 or more characters for better security.")
        else:
            self.score += 1
            self.feedback.append("Decent length. Consider using more than 12 characters for better security.")
    def check_uppercase(self):
        if any(char.isupper() for char in self.password):
            self.score += 1
            self.feedback.append("Good job including uppercase letters.")
        else:
            self.feedback.append("Consider adding uppercase letters to increase password strength.")

    def check_lowercase(self):
        if any(char.islower() for char in self.password):
            self.score += 1
            self.feedback.append("Good job including lowercase letters.")
        else:
            self.feedback.append("Consider adding lowercase letters to increase password strength.")

    def check_numbers(self):
        if any(char.isdigit() for char in self.password):
            self.score += 1
            self.feedback.append("Good Job including numbers")
        else:
            self.feedback.append("Consider adding numbers to increase password strength")

    def check_special_characters(self):
        special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
        if any(char in special_characters for char in self.password):
            self.score += 1
            self.feedback.append("Good job including special characters.")
        else:
            self.feedback.append("Consider adding special characters to increase password strength.")
    
    def get_strength(self):
            if self.score <= 1:
                return "WEAK"
            elif self.score <= 3:
                return "MEDIUM"
            else:
                return "STRONG"
            
    def analyze(self):
        self.check_length()
        self.check_uppercase()
        self.check_lowercase()
        self.check_numbers()
        self.check_special_characters()

# Add in loop if the password is WEAK or MEDIUM
while True:
    password = input("Enter a password to analyze: ")
    analyzer = PasswordAnalyzer(password)
    analyzer.analyze()

    print("\n--- Password Analysis ---")
    print(f"Password: {password}")
    print(f"Strength: {analyzer.get_strength()}")
    print(f"Score: {analyzer.score}/6")
    print("\nFeedback: ")
    for item in analyzer.feedback:
        print(item)

    if analyzer.get_strength() =="STRONG":
        print("\nGreat password! You're good to go!")

# Save to Log File
        desktop = os.path.join(os.path.expanduser("~"), "OneDrive" "Desktop")
        log_path = os.path.join(desktop, "Logs", "password_log.txt")
        log =  open(log_path, "a")
        log.write(f"\n--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log.write(f"Password: {password}\n")
        log.write(f"Strength: {analyzer.get_strength()}\n")
        log.write(f"Score: {analyzer.score}/6\n")
        log.close()
        print("Results saved to Logs/password_log.txt")

        break
    else:
        print("\nPlease try a stronger password!\n")