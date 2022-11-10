// Numbers Only Checking Start

function validateFloatKeyPress(el, evt) {
    var charCode = (evt.which) ? evt.which : event.keyCode;
    var number = el.value.split('.');
    if (charCode != 46 && charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    //just one dot
    if(number.length>1 && charCode == 46){
         return false;
    }
    //get the carat position
    var caratPos = getSelectionStart(el);
    var dotPos = el.value.indexOf(".");
    if( caratPos > dotPos && dotPos>-1 && (number[1].length > 1)){
        return false;
    }
    return true;
}

function getSelectionStart(o) {
    if (o.createTextRange) {
        var r = document.selection.createRange().duplicate()
        r.moveEnd('character', o.value.length)
        if (r.text == '') return o.value.length
        return o.value.lastIndexOf(r.text)
    } else return o.selectionStart
}

jQuery('.plan_eff').keyup(function () {     
    this.value = this.value.replace(/[^0-9]/g,'');
  });

  $(".noZero").keyup(function(){
    var value = $(this).val();
    value = value.replace(/^(0*)/,"");
    $(this).val(value);
});

$(".empty_Zero").keyup(function () {
    var incomeval = $(this).val();
    
    $(this).val(incomeval);
    if (incomeval == ".") {
        incomeval = "0";
        $(this).val(incomeval);
    }

});


// Numbers Only Checking end


// Scroll from Bottom

// var scrollBottom = document.getElementById("previous_reports");
// scrollBottom.scrollTop = scrollBottom.scrollHeight;




// window.addEventListener('load', () => {
//     let scrollElement = document.querySelector('#previous_reports');
//     scrollElement.scrollLeft =  (scrollElement.scrollWidth - scrollElement.clientWidth ) / 2;
//   });

