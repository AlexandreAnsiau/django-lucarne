var getAutoScroll = document.getElementById('autoscroll');

// let getHeader = document.getElementsByTagName('header')[0].children;
// let getFooter = document.getElementsByTagName('footer')[0].children;

// var vh = window.innerHeight / 100;

var totalH = getAutoScroll.scrollHeight;
var viewH = getAutoScroll.offsetHeight;
var scrolled = getAutoScroll.scrollTop;
var scrollable = totalH - viewH;
var scrollBottom = scrollable - scrolled;

getAutoScroll.addEventListener('scroll', function scrollPosition () {
	console.log(totalH + "; " + viewH + "; " + scrolled  + "; " + scrollable + "; " + scrollBottom);
});