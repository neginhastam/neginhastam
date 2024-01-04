const { ready } = require("jquery");

$(document).ready(function(){
    $("p").click(function(){
      $(this).hide();
    });
  });

  // jwury refrense ahou ne in <head><script></script></head>

  // $ is a sign to acces/efine jquery 
  //a selector define with $(   )
  // in selector  we can use these :
    // (this)
    // (".class")
    // ("#id")
    // ("tag")       ("p")           ...
    // $("*")       select all elements
    // $ ("[href]")    all elements with this attribute
    // $('a[target="_blank"]')  all <a> with target att and blank value
    // $("ul li:first") 	Selects the first <li> element of the first <ul> 	
    // $("ul li:first-child") 	Selects the first <li> element of every <ul>
    // $(:button)            	Selects all <button> elements and <input> elements of type="button"
    //$("tr : even")            Selects all even <tr> elements
    //$("tr : odd")             Selects all odd <tr> elements
$(document).ready(function(){

})
// the above line is use to avoid runnig jqury code before page is finished loading


//event in jQry

click
dblclick
mouseleave
mouseenter
hover  // both of mouseenter & mouseleave
focus 
blur  // تبرعکس بالایی




//effects in jquery
hide(1000)
hide()
show()
show(2000)
toggle()  //btween hide and show
// The optional speed parameter can take the following values: "slow", "fast", or milliseconds.

// The optional callback parameter is a function to be executed after toggle() completes.
