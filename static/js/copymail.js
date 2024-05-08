function copyMail(x) {
	event.preventDefault()

	let mail = x.getAttribute('href');

	navigator.clipboard.writeText(mail);

	popup = document.getElementsByClassName('mailPopup')[0];

	popup.style.display = 'block';

	setTimeout(function popupNone() {
		popup.style.display = 'none';
	}, 3000)
}