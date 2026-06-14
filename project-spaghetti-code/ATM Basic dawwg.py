tr =  0
Saldo = 1000000
riwayat = []
while True:
    try:
        pin_secret = int(input("Enter your secret pin: "))
        if tr == 3:
            print("Coba lagi nanti")
            break
        if pin_secret != 1234:
            tr += 1
            print("Pin salah")
            print(f"Anda memiliki percobaan {tr}/3")
        else:
            print(f"""
    Pin benar
    {"="*10} SELAMAT DATANG {"="*10}
    Silahkan pilih menu:
    1.Cek saldo
    2.Setor Tunai
    3.Tarik Tunai
    4.keluar
    """)
            menu = [1,2,3,4]
            while True:
                try:
                    menu_input = int(input("Masukkan pilihan : "))
                
                    if menu_input in menu:
                        if menu_input == 1:
                            print(f"Saldo anda sekarang : {Saldo:,}")
                            riwayat.append("Anda mengecek saldo anda")
                        elif menu_input == 2:
                            try:
                                setor = int(input("Masukkan nilai yang ingin disetor : "))
                                Saldo += setor
                                print(f"saldo anda menjadi : {Saldo:,}")
                                riwayat.append(f"Anda menyetor saldo, nilai : Rp.{setor:,}")
                            except ValueError:
                                print("Masukkan nilai yang benar")
                        elif menu_input == 3:
                            try:
                                tarik = int(input("Masukkan nilai yang ingin ditarik : "))
                                Saldo -= tarik
                            except ValueError:
                                print("Masukkan nilai yang benar")
                            while tarik > Saldo:
                                if tarik > Saldo:
                                    print("Saldo tidak mencukupi")
                                    print("coba lagi ")
                                    try:
                                        tarik = int(input("Masukkan nilai yang ingin ditarik : "))
                                    except ValueError:
                                        print("Masukkan nilai yang benar")
                                else:
                                    print(f"Saldo anda menjadi : Rp.{Saldo:,} ")
                                    riwayat.append(f"Anda menarik saldo, nilai : Rp.{tarik:,}")
                            print(f"Saldo anda menjadi {Saldo:,}")
                            riwayat.append(f"Anda menarik saldo, nilai : Rp.{tarik:,}")
                        elif menu_input == 4:
                            leave_user = input("Anda yakin ingin keluar? (y/n)").upper()
                            while True:
                                if leave_user == "Y":
                                    print("Terima kasih telah menggunakan layanan kami")
                                    for i in riwayat:
                                        print(i)
                                    raise SystemExit
                                else:
                                    print("Masukkan jawaban yang benar")
                                    leave_user = input("Anda yakin ingin keluar? (y/n)").upper()
                    else:
                        print("Masukkan angka yang ada di menu")
                except ValueError:
                    print("Pilihan harus angka")
    except ValueError:
        print("Masukkan angka")
