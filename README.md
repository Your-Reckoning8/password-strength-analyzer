# Password Strength Analyzer
Built a Python application using object-oriented programming to evaluate password strength. The PasswordAnalyzer class checks length, character variety (uppercase, lowercase, numbers, special characters), and returns a strength score with detailed feedback. Includes file I/O to log results for review.
The log file path is for my own personal path. change this pathway to better fit where you want the log file to be saved!
<img width="1918" height="1015" alt="Screenshot 2026-06-14 113541" src="https://github.com/user-attachments/assets/13b76b37-dd28-411f-96ce-95a931aa54ca" />
<img width="1906" height="1040" alt="Screenshot 2026-06-14 113713" src="https://github.com/user-attachments/assets/32406dbb-81ab-4eab-a05b-7be086f07f5f" />
<img width="1918" height="1011" alt="Screenshot 2026-06-14 113631" src="https://github.com/user-attachments/assets/d9ff47af-2e30-417f-a559-af6b9b6aef69" />
How it works:
A PasswordAnalyzer class holds the password and runs each check as a separate method, building up a score and feedback list. After all checks run, get_strength() converts the score into a a WEAK/MEDIUM/STRONG rating. The results are also logged to a text file using Python's file I/O, so past analyses can be reviewd later.
