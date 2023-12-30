
import kelompok4 as np

def input_matrix(order):
    print(f"Masukkan matriks {order}x{order}:")
    matrix = []
    for i in range(order):
        row = []
        for j in range(order):
            value = float(input(f"Masukkan nilai a({i + 1},{j + 1}): "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix):
    print("Matriks hasil:")
    print(matrix)

def matrix_addition():
    print("\nPenjumlahan Matriks")
    order = int(input("Masukkan order matriks (misal, untuk matriks 2x2, masukkan 2): "))
    matrix_a = input_matrix(order)
    matrix_b = input_matrix(order)
    result_matrix = matrix_a + matrix_b
    display_matrix(result_matrix)

def matrix_subtraction():
    print("\nPengurangan Matriks")
    order = int(input("Masukkan order matriks (misal, untuk matriks 2x2, masukkan 2): "))
    matrix_a = input_matrix(order)
    matrix_b = input_matrix(order)
    result_matrix = matrix_a - matrix_b
    display_matrix(result_matrix)

def matrix_transpose(order):
    print("\nMatriks Transpose")
    matrix_a = input_matrix(order)
    result_matrix = np.transpose(matrix_a)
    display_matrix(result_matrix)

def matrix_inverse(order):
    print("\nMatriks Balikan")
    matrix_a = input_matrix(order)
    determinant = np.linalg.det(matrix_a)
    if determinant == 0:
        print("Matriks tidak memiliki balikan karena determinannya nol.")
    else:
        inverse_matrix = np.linalg.inv(matrix_a)
        display_matrix(inverse_matrix)

def matrix_determinant(order):
    print("\nDeterminan Matriks")
    matrix_a = input_matrix(order)
    determinant = np.linalg.det(matrix_a)
    print(f"Determinan matriks adalah: {determinant}")

def linear_system_solution(order):
    print("\nSistem Persamaan Linier")
    print("Contoh SPL: Ax = B")
    matrix_a = input_matrix(order)
    vector_b = np.array([float(input(f"Masukkan nilai b({i + 1}): ")) for i in range(order)])
    solution = np.linalg.solve(matrix_a, vector_b)
    print("Solusi dari SPL:")
    print(solution)

def main():
    while True:
        print("\nMENU")
        print("1. Penjumlahan dan Pengurangan Matriks")
        print("2. Matriks Transpose")
        print("3. Matriks Balikan")
        print("4. Determinan Matriks")
        print("5. Sistem Persamaan Linier")
        print("6. Keluar")

        choice = int(input("Masukkan pilihan menu: "))

        if choice == 1:
            print("\nSub-menu Penjumlahan dan Pengurangan Matriks")
            print("1. Penjumlahan Matriks")
            print("2. Pengurangan Matriks")
            sub_choice = int(input("Masukkan pilihan sub-menu: "))
            if sub_choice == 1:
                matrix_addition()
            elif sub_choice == 2:
                matrix_subtraction()
            else:
                print("Pilihan sub-menu tidak valid.")
        elif choice == 2:
            print("\nSub-menu Matriks Transpose")
            print("1. Matriks 2x2")
            print("2. Matriks 3x3")
            sub_choice = int(input("Masukkan pilihan sub-menu: "))
            if sub_choice == 1:
                matrix_transpose(2)
            elif sub_choice == 2:
                matrix_transpose(3)
            else:
                print("Pilihan sub-menu tidak valid.")
        elif choice == 3:
            print("\nSub-menu Matriks Balikan")
            print("1. Matriks 2x2")
            print("2. Matriks 3x3")
            sub_choice = int(input("Masukkan pilihan sub-menu: "))
            if sub_choice == 1:
                matrix_inverse(2)
            elif sub_choice == 2:
                matrix_inverse(3)
            else:
                print("Pilihan sub-menu tidak valid.")
        elif choice == 4:
            print("\nSub-menu Determinan Matriks")
            print("1. Matriks 2x2")
            print("2. Matriks 3x3")
            sub_choice = int(input("Masukkan pilihan sub-menu: "))
            if sub_choice == 1:
                matrix_determinant(2)
            elif sub_choice == 2:
                matrix_determinant(3)
            else:
                print("Pilihan sub-menu tidak valid.")
        elif choice == 5:
            print("\nSub-menu Sistem Persamaan Linier")
            print("1. Matriks 2x2")
            print("2. Matriks 3x3")
            sub_choice = int(input("Masukkan pilihan sub-menu: "))
            if sub_choice == 1:
                linear_system_solution(2)
            elif sub_choice == 2:
                linear_system_solution(3)
            else:
                print("Pilihan sub-menu tidak valid.")
        elif choice == 6:
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan menu tidak valid.")
main()