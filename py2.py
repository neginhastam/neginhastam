let y = 123e5;    // 12300000
let z = 123e-5;   // 0.00123 


function sum(x,y){
    return x+y;
}


// Create an object:
const person = {
    firstName: "John",
    lastName : "Doe",
    id     :  5566,
    fullName : function() {
        return this.firstName + " " + this.lastName;
      }
  };
  
  function displayDate() {
    document.getElementById("demo").innerHTML = Date();
  }
//If you access a method without the () parentheses, it will return the function definition:

  // Display some data from the object:
  document.getElementById("demo").innerHTML =
  person.firstName + " " + person["lastName"];                                      

// Create an object:
const car = {type:"Fiat", model:"500", color:"white"};

// Display some data from the object:
document.getElementById("demo").innerHTML = "The car type is " + car.type;

let text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let length = text.length;


let part1 = text.slice(-7,-3);
let part2 = text.slice(7,13);
let part3 = text.slice(7);
let part4 = text.slice(-7);

let str = "Apple, Banana, Kiwi";
let part = str.substr(7, 6);

let partt = str.substr(-4);


let text2 = "Please visit Microsoft and Microsoft!";
let newText = text2.replace("Microsoft", "W3Schools");
