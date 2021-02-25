$(document).ready(function () {
    $('.sidenav').sidenav({edge: 'right'});
    $('.collapsible').collapsible();
    $('.datepicker').datepicker({
        showClearBtn: true
    });
    $('select').formSelect();
});