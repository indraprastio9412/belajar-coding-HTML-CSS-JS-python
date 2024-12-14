tahun = new Date().getFullYear();
sepuluh_tahun_lagi = tahun + 4;
tahun = 2018;
kabisat = tahun % 4 == 0 ? "Tahun Kabisat" : "Bukan Tahun Kabisat";

tahun = [2001, 2002, 2003];

tahun2003 = tahun[1];

mahasiswa = { nama: "Budi", nim: 59201010, prodi: "Ilkom", umur: 23 };

prodiMahasisa = mahasiswa.prodi;

status = mahasiswa.umur > 18 ? "Sudah Dewasa" : "Belum Dewasa";

keterangan =
  mahasiswa.nama +
  " dengan nim " +
  mahasiswa.nim +
  " prodi " +
  mahasiswa.prodi +
  " umur " +
  mahasiswa.umur +
  " " +
  status;

//output
//Budi dengan nim 59201010 prodi Ilkom umur 17 sudah belum dewasa

//desawa adalah >18
