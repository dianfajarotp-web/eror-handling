class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print("The", self.brand, self.model, "is driving.")


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        
        # PERBAIKAN: cek jumlah pintu tidak boleh <= 0
        if doors <= 0:
            raise ValueError("Jumlah pintu tidak boleh nol atau negatif.")
        
        self.doors = doors

    def honk(self):
        print("Beep! Beep!")


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)

        # PERBAIKAN: kapasitas tidak boleh <= 0
        if load_capacity <= 0:
            raise ValueError("Kapasitas harus lebih dari 0.")
        
        self.load_capacity = load_capacity

    def load(self, weight):
        # PERBAIKAN: cek overload
        if weight > self.load_capacity:
            print("Error: Muatan melebihi kapasitas!")   # lebih sederhana
        else:
            print("Loaded", weight, "kg.")


def main():
    try:  # PERBAIKAN: tambahkan error handling
        my_car = Car("Toyota", "Corolla", 4)
        my_truck = Truck("Ford", "F-150", 1200)

        my_car.drive()
        my_car.honk()

        my_truck.drive()
        my_truck.load(40000)  # sekarang akan muncul pesan error

    except ValueError as e:
        print("Terjadi kesalahan:", e)


if __name__ == "__main__":
    main()