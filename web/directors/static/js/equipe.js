const initial = document.getElementsByClassName('initial')[0];
const mAppear = document.getElementById('divAppear');
const nCorner = document.getElementById('navCorner');
const nCenter = document.getElementById('navCenter');
const selectNavTag = document.getElementsByTagName('nav');
let screener = document.getElementsByClassName('screener')[0];

function teamMove() {
	
	initial.id = 'divDisappear';
	selectNavTag[0].style.display = 'none';
	nCenter.style.display = 'block';
	screener.style.display = 'block';

	setTimeout( function closeMain () {

		const mDisappear = document.getElementById('divDisappear');

		mDisappear.style.display = 'none';
		nCorner.style.display = 'block';
		nCenter.style.display = 'none';
		nCenter.id = "navBack";
		// return;

	}, 1300);
}


document.addEventListener('click', function teamMoveBack(event) {

	let mDisappear = document.getElementById('divDisappear');

	if (mDisappear) {

	const nCorner = document.getElementById('navCorner');
	const nBack = document.getElementById('navBack');
	const getHeader = document.getElementsByTagName('header')[0].children;
	const getFooter = document.getElementsByTagName('footer')[0].children;
	const initial = document.getElementsByClassName('initial')[0];

	let targetEl = event.target;

	do {
		if (targetEl == selectNavTag[0] || 
			targetEl == getHeader[0] ||
			targetEl == getFooter[0] ||
			targetEl == getFooter[1] ||
			targetEl == initial ||
			targetEl == nCorner) {
			return;
		}

		targetEl = targetEl.parentNode;

	} while (targetEl);

		let mDisappear = document.getElementById('divDisappear');

	  	mDisappear.id = 'divAppear';
	  	
	  	nBack.style.display = 'block';
		nCorner.style.display = 'none';


		let mAppear = document.getElementById('divAppear');
		mAppear.style.display = 'block';
		screener.style.display = 'none';


		setTimeout( function openMain () {
	
		selectNavTag[0].style.display = 'block';
		nBack.style.display = 'none';
		nBack.id = 'navCenter';

	}, 1300);
	};
});