const { ready, noConflict } = require("jquery");

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


fadeIn(2000) // use to fade in a hidden element              value is optional
fadeOut()  //use to fade out  a visible element
fadeToggle()  //between fade in and out
fadeTo()
$(selector).fadeTo(speed,opacity,callback); //opacity is between 0 and 1 . callback is optional and is a function we want to execue after fad in 

slideDown()
slideUp()
// use to sliding 
$(document).ready(function(){
  $("#flip").click(function(){
    $("#panel").slideToggle("slow");
  });
});

// animating
//all property names must be camel-cased when used with the animate() method: You will need to write paddingLeft instead of padding-left, marginRight instead of margin-right, and so on. 

$("button").click(function(){
  $("div").animate({
    left: '250px',
    height: '+=150px',
    width: '+=150px'
  });
});  

//we can use show or hide or toggle for value like height

$("button").click(function(){
  var div = $("div");
  div.animate({height: '300px', opacity: '0.4'}, "slow");
  div.animate({width: '300px', opacity: '0.8'}, "slow");
  div.animate({height: '100px', opacity: '0.4'}, "slow");
  div.animate({width: '100px', opacity: '0.8'}, "slow");
  div.animate({fontSize: '3em'}, "slow");
});  



// stop
stop()
// this method works for all jquey effect methods
$("#stop").click(function(){
  $("#panel").stop();
}); 

// The optional stopAll parameter specifies whether also the animation queue should be cleared or not. Default is false, which means that only the active animation will be stopped, allowing any queued animations to be performed afterwards.

// The optional goToEnd parameter specifies whether or not to complete the current animation immediately. Default is false.

// So, by default, the stop() method kills the current animation being performed on the selected element.

// The following example demonstrates the stop() method, with no parameters:







//why w use callback function ? 
// to avoid errors



//chaninig
// we can chain he effects to be faster this way we sont have to search an element more than one time.
// simply ue "."
$(document).ready(function(){
  $("button").click(function(){
    $("#p1").css("color", "red").slideUp(2000).slideDown(2000);
  });
});
// to avoid being long we can aplit it lik this
$(document).ready(function(){
  $("button").click(function(){
    $("#p1").css("color", "red")
      .slideUp(2000)
      .slideDown(2000);
  });
});








// jQuery HTML
// have selector before themselves
//get :
  text()
  html()
  vall()
  attr()
  $("#btn1").click(function(){
    alert("Text: " + $("#test").text());
  });
//set
  // the same 3 methods abov with valu so the set thing
  $(document).ready(function(){
    $('#id').attr("href","www.darsman.ir")
  })
  //or
  $("button").click(function(){
    $("#w3s").attr({
      "href": "https://www.w3schools.com/jquery/",
      "title":"darsman"
    });
      });

//add
  append()    //the end of element
  prepend()      //the bigenig of element ( if its a <li> its change all of the numbers i like it)
  // it posible to add a single text or add more than one. 
  // here its 3 way to create 1 thing
  function appendText() {
    var txt1 = "<p>Text.</p>";               // Create element with HTML 
    var txt2 = $("<p></p>").text("Text.");   // Create with jQuery
    var txt3 = document.createElement("p");  // Create with DOM
    txt3.innerHTML = "Text.";
    $("body").append(txt1, txt2, txt3);      // Append the new elements
  } 
  after()
  before()
  // also work like above

//remove
  remove()       // remove the element and children
  empty()        //jst remove the children
  // these methoda also can get one parametr. and filter the tags that want tham be clear
  $(document).ready(function(){
    $("button").click(function(){
      $("p").remove(".test, .demo");
    });
  });


//css class
  removeClass("class1 class2 class3")          // classes will be seprated with space
  addClass()
  toggleClass()
  // use :
  $("p , h1").removeClass()

//css
  css("backgrond_color")  //et value
  css("backgrond_color","blue")      //set value
  css({"backgrond_color":"blue","font_size":"25px"})        //set values


//dimention
  height()            //just element
  width()         
  innerHeight()       //+padding
  innerWidth()
  outerHeight()       //+border
  outerWidth()
  outerHeight(true)   // +margin
  outerWidth(true)    
  // we can set value with thses too






//jQuery Travesing
  $('span').parent()                      //return direct parent
  $('span').parents()                 //return all parents
  $('span').parentsUntill("div")          // return between span adn div (without div itself)

  $('div').children()                     //direct child
  $('div').children('p.first')
  $('div').children('.first')           //class first
  $('div').find("span")                 //all span chik=ls
  $('div').find("*")                 //all children

  //sibiling
  $('h2').siblings()
  $('h2').siblings('p')          // all sibiling that are p
  $('h2').next()          // return all elements after all h2 (after each one)
  $('h2').nextAll()
  $('h2').nextUntil('h6')              // all bitween 2 , 6 withouth 2 , 6
  $('h6').prev()
  $('h6').prevAll()
  $('h6').prevUntil('h2')

  //filtering
  $('p').first()
  $('p').last()
  $('p').eq(0)       //get a number from 0 its the index      0 return the first p tag    1 return scend one
  $('p').filter(".neg")           //      ==   $('p.neg')
  $('p').not('.neg')          //its the opposite of filter






// jQuery ajax
// first and powerfull method
load('url')   //load(url,data,callback)
//It is also possible to add a jQuery selector to the URL parameter. 
// like #p1 that spesify text whit id p1

$get('url')

$post('url',date,callback)
$("button").click(function(){
  $.post("demo_test_post.asp",
  {
    name: "Donald Duck",
    city: "Duckburg"
  },
  function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
  });
}); 






$.noConflict()
// we can use the javaScript name insed of $ when we also use angular and etc.
javaScript.ready()

var js=$.noConflict()
// or use on other name that we want
js.ready()


// what is asp
// asp is a thecnology on server side its like php for executing script
// asp is a program that run in the server and its microsoft technology 
// stand for active server program
// <%
// response.write("My first ASP script!")
// %>

// why asp
// its easy to learn and its fast. its securit (beacuse it can not  view in browser) 
// we can change and edit the file get reques and have response

// How Does it Work?

// When a browser requests a normal HTML file, the server just returns the file.

// When a browser requests an ASP file, the server passes the request to the ASP engine which reads the ASP file and executes the server scripts in the file.

// Finally the ASP file is returned to the browser as plain HTML.
