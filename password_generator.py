import random
import string
import os

def genera_password(lunghezza, include_lettere=True, include_numeri=True, include_speciali=True):
    caratteri = ''
    
    if include_lettere:
        caratteri += string.ascii_letters
    if include_numeri:
        caratteri += string.digits
    if include_speciali:
        caratteri += string.punctuation

    if not caratteri:
        print("Error: You must include at least one font.")
        return None

    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
    return password

def salva_password_su_file(password, filename='password.txt'):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, filename)
    
    with open(file_path, 'a') as file:
        file.write(f'~~~>    {password}\n\n\n')

def main():
    lunghezza_password = int(input("Enter the password length: "))
    include_lettere = input("Include letters? (y/n): ").lower() == 'y'
    include_numeri = input("Include numbers? (y/n): ").lower() == 'y'
    include_speciali = input("Include special characters? (y/n): ").lower() == 'y'

    nuova_password = genera_password(lunghezza_password, include_lettere, include_numeri, include_speciali)

    if nuova_password:
        print("New password generated:", nuova_password)
        salva_password_su_file(nuova_password)

if __name__ == "__main__":
    main()
