#docstring
#docstring dimulai dan ditutup dengan tanda """ (triple double quote) 
#dan harus berada tepat di bawah header fungsi.

def my_print(jlh, kata):
    """
    Fungsi untuk memprint kata dengan jumlah tertentu.

    Parameters:
    jlh (integer) : kata akan di print sebanyak jlh kali
    kata (string) : kata yang akan diprintkan
    """
    print("Kita akan print sebanyak", jlh, "kali")
    print("-"*30)
    """
    ini bukan docstring
    namun tetap tidak dianggap sebagai kode yang harus dieksekusi
    """
    for i in range(jlh):
        print("cok", kata)
    print("-"*30)

#memanggil docstring
print(my_print.__doc__)
help(my_print)
