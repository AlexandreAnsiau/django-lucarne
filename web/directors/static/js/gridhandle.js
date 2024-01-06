const video = document.getElementsByClassName('mini-video');
const grid = document.getElementsByClassName('grid-container')[0];
let videoNbr = video.length;
let windWidth = window.innerWidth;

function resizeGrid () {
	if (windWidth >= 1280 && grid) {

		if (videoNbr < 9 && videoNbr >= 4 ) {
			grid.style.gridTemplateColumns = '1fr 1fr';
		} 
		else if (videoNbr < 4) {
			grid.style.gridTemplateColumns = '1fr';
		} 
		else {
		};
	};
	if (windWidth > 720 && windWidth < 1280 && grid) {

		if (videoNbr < 6) {
			grid.style.gridTemplateColumns = '1fr';
		} 
		else {
		};
	};
};

window.addEventListener('load', resizeGrid ());
window.addEventListener('resize', resizeGrid ());