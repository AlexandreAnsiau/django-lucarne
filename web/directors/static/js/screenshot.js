function showGalery() {
	document.getElementsByClassName('grid-screenshot')[0].style.display = 'grid';
	document.getElementById('galery').style.display = 'none';
	document.getElementById('closeGalery').style.display = 'flex';
};

function closeGalery() {
	document.getElementsByClassName('grid-screenshot')[0].style.display = 'none';
	document.getElementById('galery').style.display = 'flex';
	document.getElementById('closeGalery').style.display = 'none';
};