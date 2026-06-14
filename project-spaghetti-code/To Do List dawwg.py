import random as rd
Menu = """1. Tambah tugas
2. Lihat semua tugas
3. Tandai tugas selesai
4. Hapus tugas
5. Keluar"""

tugas = {0:{}}
nomor_tugas = 0
kategori = ["Tinggi","Sedang","Rendah"]
error_message1 = "[Masukkan Angka Yang Valid]"
error_message2 = "[Masukkan Angka]"
exit_message = "[Anda Keluar dari menu]"
while True:
    print(Menu)
    try:
        Choose_menu = int(input("Masukkan nomor menu >> "))
        if Choose_menu == 1:
            while True:
                nama_tugas = input("Masukkan nama tugas >> ").title()
                if len(nama_tugas)<2 or  nama_tugas == "":
                    print("[Tugas Tidak Bisa Kosong / Coba Lagi]")
                    continue
                else:
                    while True:
                        prioritas_tugas = input("Masukkan prioritas Tugas (Tinggi/Sedang/Rendah) >> ").capitalize()
                        if prioritas_tugas in kategori:
                            random_nomor = rd.randint(1,100000)
                            tugas.update({nomor_tugas:{"Nama Tugas":nama_tugas, "Prioritas":prioritas_tugas, "Status":"belum"}})
                            nomor_tugas += random_nomor
                            print("[Tugas Berhasil Ditambahkan]")
                            
                            break
                        else:
                            print("[Masukkan prioritas tugas berdasarkan kategori yang tersedia]")
                            print("[Maaf Anda Harus Mengulanginya]") #Saya menggunakan 2 loop walaupun kurang rapi hahaha
                            continue
                confirm = input("Tekan 'q' untuk keluar atau tekan apapun untuk lanjut menambah >> ".title())
                if confirm == "q":
                    print(exit_message)
                    break
                else:
                    continue
        elif Choose_menu == 2:
            while True:
                try:
                    if len(tugas) == 0:
                        print("[Tugas Kosong]")
                        confirm4 = input("Tekan 'q' untuk keluar >> ").lower()
                        if confirm4 == "q":
                            print(exit_message)
                            break
                        else:
                            break
                    else:
                        for number,value in tugas.items():
                            print(f"[{number}] {value["Nama Tugas"]} | Prioritas : {value["Prioritas"]} | Status : {value["Status"]}") # sedikit saya ubah untuk menu 2 karena menggunakan nested dictionary
                except KeyError:
                    print("[Tugas kosong]")
                confirm1 = input("Tekan 'q' untuk keluar >> ")
                if confirm1 == "q":
                    print(exit_message)
                    break
        elif Choose_menu == 3:
                while True:
                    try:
                        for key_dict,value_dict in tugas.items():
                            print(f"Nomor : {key_dict} | Tugas : {value_dict["Nama Tugas"]} | Status : {value_dict["Status"]}")
                        try:
                            if len(tugas) == 0:
                                print("[Tugas Kosong]")
                                confirm4 = input("Tekan 'q' untuk keluar >> ").lower()
                                if confirm4 == "q":
                                    print(exit_message)
                                    break
                                else:
                                    break
                            else:
                                tugas_selesai = int(input("Masukkan ID tugas yang ingin ditandai >> "))
                                if tugas_selesai in tugas:
                                    tugas[tugas_selesai].update({"Status":"selesai"})
                                    print("[Tugas Telah Ditandai Selesai Dan Tidak Perlu Ditandai Lagi]")
                                else:
                                    print(error_message1)
                                    continue
                                confirm3 = input("Tekan 'q' untuk keluar atau tekan apapun untuk lanjut menandai >> ").lower()
                                if confirm3 == "q":
                                    print(exit_message)
                                    break
                                else:
                                    continue
                        except ValueError:
                            print(error_message2)
                    except KeyError:
                        print("[Tugas Kosong]")
                        confirm4 = input("Tekan 'q' untuk keluar >> ").lower()
                        if confirm4 == "q":
                            print(exit_message)
                            break
                        else:
                            break
        elif Choose_menu == 4:
            while True:
                try:
                    for key_dict1,value_dict1 in tugas.items():
                        print(f"Nomor : {key_dict1} | Tugas : {value_dict1["Nama Tugas"]} | Status : {value_dict1["Status"]}")
                    try:
                        if len(tugas) == 0:
                            print("[Tugas Kosong]")
                            confirm4 = input("Tekan 'q' untuk keluar >> ").lower()
                            if confirm4 == "q":
                                print(exit_message)
                                break
                            else:
                                break
                        else:
                            tugas_hapus = int(input("Masukkan nomor tugas yang ingin dihapus >> "))
                            if tugas_hapus in tugas:
                                tugas.pop(tugas_hapus)
                                print("[Tugas Berhasil dihapus]")
                            else:
                                print(error_message1)
                                continue
                            confirm4 = input("Tekan 'q' untuk keluar atau tekan apapun untuk lanjut menghapus >> ").lower()
                            if confirm4 == "q":
                                print(exit_message)
                                break
                            elif confirm4 == "":
                                # if tugas 
                                continue
                    except ValueError:
                        print(error_message2)
                except KeyError:
                    print("[Tugas Kosong]")
                    confirm4 = input("Tekan 'q' untuk keluar >> ").lower()
                    if confirm4 == "q":
                        print(exit_message)
                        break
                    else:
                        break
                
        elif Choose_menu == 5:
            while True:
                confirm_exit = input("Anda Yakin Ingin Keluar (y/n) >> ").lower()
                if confirm_exit == "y":
                    print("="*10,"[Terima Kasih]","="*10)
                    raise SystemExit
                else:
                    print("[Anda Melanjutkan Program]")
                    break
        else:
            print(error_message1)
    except ValueError:
        print(error_message2)

