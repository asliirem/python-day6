class Student:
    def __init(self, number, name):
        self.number = number
        self.name =name

    def __str__(self):
        return f"{self.number} - {self.name}"
    
class StudentManager:
    def __init__(self):
        self.stuents = []

    def add_student(self, number, name):
        student = Student(number, name)
        self.students.append(student)
        print("Öğrenci eklendi.")

    def remove_student(self, number):
        for student in self.students:
            self.students.remove(student)
            print("Öğrenci silindi.")
            return
        print("Öğrenci bulunamadı.")

    def list_students(self):
        if not self.students:
            print("Kayıtlı Öğrenci Yok")
            return
        for student in self.students:
            print(student)

    def save_to_file(self):
        with open("students.txt", "w", encoding="utf-8") as file:
            for student in self.students:
                file.write(f"{student.number},{student.name}\n")
        print("Dosyaya kaydedildi.")
manager = StudentManager()

while True:
    print("\n--- Öğrenci Yönetim Sistemi ---")
    print("1- Öğrenci Ekle")
    print("2- Öğrenci Sil")
    print("3- Listele")
    print("4- Kaydet")
    print("5- Çıkış")

    choice = input("Seçim: ")

    if choice == "1":
        num = input("Öğrenci numarası: ")
        name = input("Öğrenci adı: ")
        manager.add_student(num, name)

    elif choice == "2":
        num = input("Silinecek öğrenci numarası: ")
        manager.remove_student(num)

    elif choice == "3":
        manager.list_students()

    elif choice == "4":
        manager.save_to_file()

    elif choice == "5":
        print("Çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")
                    