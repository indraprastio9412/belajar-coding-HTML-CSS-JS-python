const motor = document.getElementById('motor');
const gameArea = document.getElementById('gameArea');
let motorPosition = 175; // posisi awal motor

document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft' && motorPosition > 0) {
        motorPosition -= 10; // bergerak ke kiri
    } else if (event.key === 'ArrowRight' && motorPosition < 350) {
        motorPosition += 10; // bergerak ke kanan
    }
    motor.style.left = motorPosition + 'px';
});
