$('.datepicker').addClass('date')
let myD = new Date($('.datepicker').val())
var d = new Date()
// var bool = (d.toDateString() === myD.toDateString());
console.log(d)
console.log(myD)
checkDate();
function checkDate() {
    if (d < myD) {
        $('.datepicker').removeClass('date')
        console.log("yes")
    }
}