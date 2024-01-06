var getAutoScroll = document.getElementById('autoscroll');
var getFader = document.getElementsByClassName('faderWhite')[0];


window.onload = function verify() {
	let vh = window.innerHeight / 100;
	var ratio = 20 * vh;

	var totalH = getAutoScroll.scrollHeight;
	var viewH = getAutoScroll.offsetHeight;
	var scrollable = totalH - viewH;

	if (scrollable <= ratio) {
		getFader.style.opacity = 0;
	} else {
		getAutoScroll.addEventListener('scroll', function scrollCategory () {	
				
			var scrolled = getAutoScroll.scrollTop;
			var scrollBottom = scrollable - scrolled;
		
			var limit = Math.abs(scrollable - 40 * vh);
			var fader = scrollBottom / limit;
			var rounder = fader.toFixed(1);
		
			if (scrolled > limit) {
				getFader.style.opacity = rounder;
			}
			else {
				getFader.style.opacity = 1; 
			}		
		});
	}
};
