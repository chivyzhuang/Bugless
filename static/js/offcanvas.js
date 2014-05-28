function initial(){
	$('[data-toggle=popover]').popover();

	$('[data-toggle=offcanvas]').click(function () {
		$('.row-offcanvas').toggleClass('active');
	});
}

$(document).ready(initial);