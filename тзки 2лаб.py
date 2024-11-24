import sqlite3
import tkinter as tk
from tkinter import messagebox

# Создание базы данных и таблицы
def create_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Создание таблицы, если она не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        birthdate TEXT,
                        address TEXT)''')
    conn.commit()
    conn.close()

# Вставка данных в базу данных (с сохранением данных как есть)
def insert_student(name, birthdate, address):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Сохраняем данные как есть (без хэширования)
    cursor.execute('''INSERT INTO students (name, birthdate, address) 
                      VALUES (?, ?, ?)''', 
                   (name, birthdate, address))
    conn.commit()
    conn.close()

# Функция для просмотра всех студентов
def get_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    conn.close()
    
    # Возвращаем обычные данные, без изменений
    return rows

# Функция для входа (проверка прав доступа)
def login(username, password):
    # Проверка пользователей: администратор Айлин и пользователь Куки
    if username == "Айлин" and password == "555":
        return "admin"
    elif username == "Куки" and password == "123":
        return "user"
    else:
        return None

# Основной графический интерфейс
def main_app():
    # Окно для входа
    login_window = tk.Tk()
    login_window.title("Login")

    def on_login_button_click():
        username = username_entry.get()
        password = password_entry.get()
        role = login(username, password)
        
        if role == "admin":
            messagebox.showinfo("Login Success", "Welcome Айлин (Admin)!")
            login_window.destroy()
            admin_app()
        elif role == "user":
            messagebox.showinfo("Login Success", "Welcome Куки (User)!")
            login_window.destroy()
            user_app()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    username_label = tk.Label(login_window, text="Username")
    username_label.grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    password_label = tk.Label(login_window, text="Password")
    password_label.grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1)

    login_button = tk.Button(login_window, text="Login", command=on_login_button_click)
    login_button.grid(row=2, columnspan=2)

    login_window.mainloop()

# Окно для администраторов
def admin_app():
    app_window = tk.Tk()
    app_window.title("Admin App")

    def add_student():
        name = name_entry.get()
        birthdate = birthdate_entry.get()
        address = address_entry.get()
        
        if name and birthdate and address:
            insert_student(name, birthdate, address)
            messagebox.showinfo("Success", "Student added successfully!")
            refresh_students()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def refresh_students():
        # Очищаем текстовое поле и отображаем обновленный список студентов
        student_list.delete(1.0, tk.END)
        students = get_students()
        for student in students:
            student_list.insert(tk.END, f"ID: {student[0]}, Name: {student[1]}, Birthdate: {student[2]}, Address: {student[3]}\n")

    def logout():
        app_window.destroy()
        main_app()  # Возвращаемся на экран логина

    name_label = tk.Label(app_window, text="Name")
    name_label.pack()
    name_entry = tk.Entry(app_window)
    name_entry.pack()

    birthdate_label = tk.Label(app_window, text="Birthdate")
    birthdate_label.pack()
    birthdate_entry = tk.Entry(app_window)
    birthdate_entry.pack()

    address_label = tk.Label(app_window, text="Address")
    address_label.pack()
    address_entry = tk.Entry(app_window)
    address_entry.pack()

    add_button = tk.Button(app_window, text="Add Student", command=add_student)
    add_button.pack()

    view_button = tk.Button(app_window, text="View Students", command=refresh_students)
    view_button.pack()

    student_list = tk.Text(app_window, height=10, width=50)
    student_list.pack()

    # Кнопка "Сменить пользователя"
    logout_button = tk.Button(app_window, text="Change User", command=logout)
    logout_button.pack()

    app_window.mainloop()

# Окно для обычных пользователей (только просмотр)
def user_app():
    app_window = tk.Tk()
    app_window.title("User App")

    def view_user_students():
        student_list.delete(1.0, tk.END)
        students = get_students()
        for student in students:
            student_list.insert(tk.END, f"ID: {student[0]}, Name: {student[1]}, Birthdate: {student[2]}, Address: {student[3]}\n")

    def logout():
        app_window.destroy()
        main_app()  # Возвращаемся на экран логина

    student_list = tk.Text(app_window, height=10, width=50)
    student_list.pack()

    view_button = tk.Button(app_window, text="View Students", command=view_user_students)
    view_button.pack()

    # Кнопка "Сменить пользователя"
    logout_button = tk.Button(app_window, text="Change User", command=logout)
    logout_button.pack()

    app_window.mainloop()

if __name__ == '__main__':
    create_database()
    main_app()
