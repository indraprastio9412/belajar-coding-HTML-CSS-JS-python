nama = "Andi";
umur = 10;

status = "";
if (umur >= 41) {
  status = "Orang tua";
} else if (umur > 21) {
  status = "Dewasa";
} else if (umur > 12) {
  status = "Remaja";
} else if (umur > 5) {
  status = "Anak-Anak";
} else {
  status = "Balita";
}

document.write(nama);
document.write("<br/>");
document.write(status);

// 0-5 balita
// 6-12 anak-anak
//13-21 remaja
// 22-40 dewasa
// >=41 orang tua
