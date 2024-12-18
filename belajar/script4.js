nilai_mahasiswa = [
  {
    nama: "siti",
    mk: [
      { nama: "agama", nilai: { harian: 80, uts: 60, uas: 70 } },
      { nama: "pemrograman", nilai: { harian: 10, uts: 80, uas: 70 } },
      { nama: "pancasila", nilai: { harian: 10, uts: 60, uas: 70 } },
    ],
  },
  {
    nama: "ali",
    mk: [
      { nama: "agama", nilai: { harian: 90, uts: 50, uas: 20 } },
      { nama: "pemrograman", nilai: { harian: 80, uts: 80, uas: 100 } },
      { nama: "pancasila", nilai: { harian: 60, uts: 90, uas: 80 } },
    ],
  },
  {
    nama: "budi",
    mk: [
      { nama: "agama", nilai: { harian: 100, uts: 80, uas: 70 } },
      { nama: "pemrograman", nilai: { harian: 100, uts: 80, uas: 90 } },
      { nama: "pancasila", nilai: { harian: 100, uts: 70, uas: 80 } },
    ],
  },
];

mk = nilai_mahasiswa[0].mk; //mk agama atas nama  siti
harian = mk[0].nilai.harian * 0.2;
uts = mk[0].nilai.uts * 0.3;
uas = mk[0].nilai.uas * 0.5;
na = harian + uts + uas;
document.write(na);
grade = "E";
if (na >= 80) {
  grade = "A";
} else if (na >= 75) {
  grade = "B+";
} else if (na >= 70) {
  grade = "B";
} else if (na >= 60) {
  grade = "C+";
} else if (na >= 50) {
  grade = "C";
} else if (na >= 30) {
  grade = "D";
}

document.write("<br/>");
document.write(grade);
document.write("<br/>");

mk = nilai_mahasiswa[2].mk; //mk pemrograman an budi
harian = mk[1].nilai.harian * 0.2;
uts = mk[1].nilai.uts * 0.3;
uas = mk[1].nilai.uas * 0.5;
na = harian + uts + uas;
document.write(na);

grade = "E";
if (na >= 80) {
  grade = "A";
} else if (na >= 75) {
  grade = "B+";
} else if (na >= 70) {
  grade = "B";
} else if (na >= 60) {
  grade = "C+";
} else if (na >= 50) {
  grade = "C";
} else if (na >= 30) {
  grade = "D";
}

document.write("<br/>");
document.write(grade);
