$(document).ready(function () {
	$('tbody tr').hover(function() {
		$(this).css("background","AliceBlue");
	},
		function () {
			$(this).css("background","");
		})
});