document.addEventListener('click', function goPreviousPage(event) {

	const videoWindow = document.getElementsByClassName('contentFrame');
	const close = document.getElementsByClassName('close');
	let getHeader = document.getElementsByTagName('header')[0].children;
	let getFooter = document.getElementsByTagName('footer')[0].children;
	let screener = document.getElementsByClassName('screener')[0];
	const nCenter = document.getElementById('navCenter');

	let targetEl = event.target;

	do {
		if (targetEl == videoWindow[0] ||
			targetEl == getHeader[0] ||
			targetEl == getHeader[1] ||
			targetEl == getFooter[0] ||
			targetEl == getFooter[1] ||
			targetEl == screener ||
			targetEl == nCenter) {
			return;
		}
		targetEl = targetEl.parentNode;
	} while (targetEl);
	
	document.getElementsByClassName('initial')[0].id = 'mainDisappear';

	setTimeout(function delayPrevious() {
		// history.back();
		previousPage = document.referrer;
		window.location.assign(previousPage);

	}, 1500);
});

