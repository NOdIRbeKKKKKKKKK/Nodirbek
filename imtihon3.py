class Worker:
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary
    
    def increase_salary(self):
        self.salary *= 1.15
    
    def display_info(self):
        print("Ishchi Familiyasi:", self.surname)
        print("Lavozimi:", self.position)
        print("Oyligi:", self.salary)

ishchilar_soni = int(input("Ishchilar soni: "))

ishchilar = []
for i in range(ishchilar_soni):
    print(f"\nIshchi #{i + 1} ma'lumotlari:")
    surname = input("Ishchi Familiyasi: ")
    position = input("Lavozimi: ")
    salary = float(input("Oyligi: "))
    
    worker = Worker(surname, position, salary)
    ishchilar.append(worker)

for worker in ishchilar:
    if worker.salary > 0:
        worker.increase_salary()

for worker in ishchilar:
    if worker.surname.startswith("Abdulla"):
        worker.position = "injener"
for i, worker in enumerate(ishchilar):
    print(f"\nIshchi #{i + 1} ma'lumotlari:")
    worker.display_info()
