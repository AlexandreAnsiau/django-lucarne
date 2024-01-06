function delayTransition(x) {

	event.preventDefault();
	
	var link = x.getAttribute('href');
	
	document.getElementsByTagName('main')[0].id = 'mainDisappear';
	
	setTimeout(function fadeMain() {
	
		location.assign(link);
	
	}, 700)
};

window.addEventListener('unload', () => {
	document.getElementsByTagName('main')[0].id = 'mainAppear';
})