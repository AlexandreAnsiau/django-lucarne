var timer = null;

var elem = document.getElementById('autoscroll')

elem.addEventListener('mouseover', handleMouseOver, false);

function handleMouseOver(event) {


		var coor = event.clientY;
		var y = document.body.clientHeight;
		var eh = elem.clientHeight;
		var ep = coor - y*(15/100);

		var zoneTop = ( ep < eh*(1/3) && ep > 0);
		var zoneBottom = (ep > eh*(2/3) && ep < eh)

		if ( ! ( zoneTop || zoneBottom ) ) {

		clearTimeout( timer );
		return;

	}

		(function checkForWindowScroll () {
			clearTimeout( timer );
			if ( adjustWindowScroll() ) {
				timer = setTimeout( checkForWindowScroll(), 30 );
				}
			}) ();

		if (zoneTop) {
		elem.scrollBy(0, -50);
		return( true );
		}

		else if (zoneBottom) {
		elem.scrollBy(0, 50);
		return( true );
		}

		else {
			return( false );
		}
	};