function startLoop(x) {
	x.play();
	x.nextElementSibling.style.display = "block";
}
function pauseLoop(x) {
	x.pause();
	x.nextElementSibling.style.display = "none";
}