function hitungGrade(na) {
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
  return grade;
}

function hitungNA(harian, uts, uas) {
  harian = harian * 0.2;
  uts = uts * 0.3;
  uas = uas * 0.5;
  na = harian + uts + uas;
  return na;
}

na = 90;
grade = hitungGrade(na);
console.log(grade);
na = 70;
grade = hitungGrade(na);
console.log(grade);

na = 75;
grade = hitungGrade(na);
console.log(grade);

na = 40;
grade = hitungGrade(na);
console.log(grade);

na = 30;
grade = hitungGrade(na);
console.log(grade);

na = hitungNA(10, 70, 100);
console.log(na);

na = hitungNA(100, 70, 10);
console.log(na);

harian = 100;
uts = 100;
uas = 100;

grade = hitungGrade(hitungNA(harian, uts, uas));

function hitungNilai(harian, uts, uas) {
  na = hitungNA(harian, uts, uas);
  grade = hitungGrade(na);
  return {
    harian: harian,
    uts: uts,
    uas: uas,
    na: na,
    grade: grade,
  };
}

nilai_budi = hitungNilai(10, 20, 30);
console.log(nilai_budi);

nilai_ali = hitungNilai(100, 20, 100);
console.log(nilai_ali);
