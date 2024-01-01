// <!DOCTYPE html>
// <html>
// <body>

// <h2>JavaScript Comparisons</h2>

// <p>Input your age and click the button:</p>

// <input id="age" value="18" />

// <button onclick="myFunction()">Try it</button>

// <p id="demo"></p>

// <script>
// function myFunction() {
//   let voteable;
//   let age = Number(document.getElementById("age").value);
//   if (isNaN(age)) {
//     voteable = "Input is not a number";
//   } else {
//     voteable = (age < 18) ? "Too young" : "Old enough";
//   }
//   document.getElementById("demo").innerHTML = voteable + " to vote";
// }
// </script>

// </body>
// </html>



//string methods

let text = "Please locate where 'locate' occurs!";
let index = text.lastIndexOf("locate");
document.getElementById("demo").innerHTML = index; 

let indexf = text.indexOfndexOf("locate");
document.getElementById("demo").innerHTML = indexf; 

//oth indexOf(), and lastIndexOf() return -1 if the text is not found:
//Both methods accept a second parameter as the starting position for the search:


let index3 = text.search(/locate/);
document.getElementById("demo").innerHTML = index3;


// The search() method cannot take a second start position argument.
// The indexOf() method cannot take powerful search values (regular expressions).





let text2 = "The rain in SPAIN stays mainly in the plain"; 
const myArr = text2.match(/ain/gi);
// const myArr = text2.match(/ain/g);
// const myArr = text2.match(/ain/);
// const myArr = text2.match("ain");
document.getElementById("demo").innerHTML = myArr.length + " " + myArr;
// //The match() method returns an array containing the results of matching a string against a string (or a regular expression).




let text3 = "I love cats. Cats are very easy to love. Cats are very popular."
const iterator = text3.matchAll(/Cats/gi);

document.getElementById("demo").innerHTML = Array.from(iterator);

//The matchAll() method returns an iterator containing the results of matching a string against a string (or a regular expression).



let text4 = "Hello world, welcome to the universe.";
document.getElementById("demo").innerHTML = text4.includes("world",20);
// document.getElementById("demo").innerHTML = text4.includes("world");
//includes() is case sensitive.

let text5 = "Hello world, welcome to the universe.";
document.getElementById("demo").innerHTML = text5.startsWith("world",6);
document.getElementById("demo").innerHTML = text5.endsWith("world");









//Template literals allows multiline strings:

let myName="negin";
let myFamily = "taheri";
document.getElementById('demo').innerHTML = `i am ${myName} ${myFamily}`;



let price = 10;
let VAT = 0.25;
let total = `Total: ${(price * (1 + VAT)).toFixed(3)}`;
//toFixed تعداد رقم بعد از اعشار را مشخص میکند


//for each

let temp=`coffe`;
const arr = [`milk`, `shuger`]
//It is a common practice to declare arrays with the const keyword.
let html=`<h2> ${temp} </h2><ul>`;
for (const i of arr){
    html+= `<li>${i}</li>`
}

html+=`</ul>`


// const fruits = ["Banana", "Orange", "Apple", "Mango"];

// let text=`<ul>`
// for (const i of fruits){
// 	text+=`<li>${i}<li>`;
//     }
// text+=`</ul>`

// const fruits = ["Banana", "Orange", "Apple", "Mango"];

// let text = "<ul>";
// fruits.forEach(myFunction);
// text += "</ul>";

// document.getElementById("demo").innerHTML = text;

// function myFunction(value) {
//   text += "<li>" + value + "</li>";
// } 








//number

// let x = 123e5;    // 12300000
// let y = 123e-5;   // 0.00123 

//Integers (numbers without a period or exponent notation) are accurate up to 15 digits

let x = 0.2 + 0.1;
document.getElementById("demo1").innerHTML = "0.2 + 0.1 = " + x;
let y = (0.2*10 + 0.1*10) / 10;
document.getElementById("demo2").innerHTML = "0.2 + 0.1 = " + y;
//NaN is a number: typeof NaN returns number:

//Infinity and -Infinity is a number: typeof Infinity returns number.

// //create a big inteer type
//let x = 9999999999999999n;
//let y = BigInt("9999999999999999");

// With BigInt the total number of supported data types in JavaScript is 8:

// 1. String
// 2. Number
// 3. Bigint
// 4. Boolean
// 5. Undefined
// 6. Null
// 7. Symbol
// 8. Object 

// numeric methods

//let x = Number.MAX_SAFE_INTEGER;
// let x = Number.MIN_SAFE_INTEGER;
// Number.isSafeInteger(12345678901234567890);
// Number.isInteger(123456789012);

// let x = 9.656;
// document.getElementById("demo").innerHTML =
//   x.toFixed(0) + "<br>" +
//   x.toFixed(2) + "<br>" +
//   x.toFixed(4) + "<br>" +
//   x.toFixed(6);


// let x = 9.656;
//   x.toPrecision();
//   x.toPrecision(2);
//   x.toPrecision(4);
//   x.toPrecision(6); 


// let x = new Date("1970-01-02");
// document.getElementById("demo").innerHTML = Number(x); 
// parseFloat() and parseInt()
//document.getElementById("demo").innerHTML = Number.MAX_VALUE;






//array

//The easiest way to add a new element to an array is using the push() method:

//You should use objects when you want the element names to be strings (text).
//You should use arrays when you want the element names to be numbers.

const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.at(2);
let f= fruits.toString()
fruits.length;
document.getElementById("demo").innerHTML = fruits.join(" * ");
// join is lik sostring but w can use seprator
fruits.pop();
// pop othe last element
fruits.shift()
//The shift() method removes the first element of an array (and "shifts" the other elements to the left):
fruits.unshift('ri')
//The unshift() method adds a new element to an array (at the beginning), and "unshifts" older elements:    

// Using delete() leaves undefined holes in the array.

// Use pop() or shift() instead

const arr1 = ["Cecilie", "Lone"];
const arr2 = ["Emil", "Tobias", "Linus"];
const arr3 = ["Robin", "Morgan"];
const myChildren = arr1.concat(arr2, arr3);
//The concat() method does not change the existing arrays. It always returns a new array.
//The concat() method can also take strings as arguments:

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.splice(2, 0, "Lemon", "Kiwi");
// // The first parameter (2) defines the position where new elements should be added (spliced in).

// // The second parameter (0) defines how many elements should be removed.

// // The rest of the parameters ("Lemon" , "Kiwi") define the new elements to be added.

//The difference between the new toSpliced() method and the old splice() method is that the new method creates a new array, keeping the original array unchanged, while the old method altered the original array.



// The slice() method creates a new array.

// The slice() method does not remove any elements from the source array.

let position = fruits.indexOf("Apple") + 1;
fruits.includes("Mango");

const numbers = [4, 9, 16, 25, 29];
let first = numbers.find(myFunction);

function myFunction(value, index, array) {
  return value > 18;
} 


const temp = [27, 28, 30, 40, 42, 35, 30];
let high = temp.findLast(x => x > 40);
// ?






// Creating Date Objects

// Date objects are created with the new Date() constructor.

// There are 9 ways to create a new date object:
new Date()
new Date('date string')

new Date(year,month)
new Date(year,month,day)
new Date(year,month,day,hours)
new Date(year,month,day,hours,minutes)
new Date(year,month,day,hours,minutes,seconds)
new Date(year,month,day,hours,minutes,seconds,ms)

new Date(milliseconds)


// JavaScript counts months from 0 to 11:

// January = 0.

// December = 11.



const date = new Date();
Document.getElementById('demo').innerHTML=date.toUTCString();
Document.getElementById('demo').innerHTML=date.toISOString();
Document.getElementById('demo').innerHTML=date.toString();

//Date.now() returns the number of milliseconds since January 1, 1970.


date.getTimezoneOffset();
//Date.now() returns the number of milliseconds since January 1, 1970.


let text1;
const today = new Date();
const someday = new Date();
someday.setFullYear(2100, 0, 14);

if (someday > today) {
  text1 = "Today is before January 14, 2100.";
} else {
  text1 = "Today is after January 14, 2100.";
}

document.getElementById("demo").innerHTML = text1;



Math.ceil(3.2)
Math.trunc(3.2)
Math.round(3.5)
Math.floor(3.6)

// Math.sin(x) returns the sine (a value between -1 and 1) of the angle x (given in radians).

// If you want to use degrees instead of radians, you have to convert degrees to radians:

// Angle in radians = Angle in degrees x PI / 180.





//Math.random() always returns a number lower than 1.

Math.floor(Math.random()*100)
// between 0 and 99

function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min) ) + min;
}

function getRndInteger2(min, max) {
  return Math.floor(Math.random() * (max - min + 1 ) ) + min;
} 


//the 0 value is false other numric are true

//Comparing two JavaScript objects always return false.

//  !== 	not equal value or not equal type


let yy;
if ( 2 > 12){
  yy='no'
}else{
  yy='y'
}


// Switch cases use strict comparison (===).

// The values must be of the same type to match.



let xx='3'
switch (xx){
  case '3':
    xx=true
    break
  case 3:
    xx=false;
    break;
  default:
    xx=3
}

// if default come first remmeber to ass a break line




// // for loops

// JavaScript supports different kinds of loops:

//     for - loops through a block of code a number of times
//     for/in - loops through the properties of an object
//     for/of - loops through the values of an iterable object
//     while - loops through a block of code while a specified condition is true
//     do/while - also loops through a block of code while a specified condition is true
let res;
const mydic = {nam:'negin',famil:'taheri',age:24}
for ( const i in mydic){
  res+= mydic[i]
}



const namess=['negin','mohsen','negar']
namess.forEach(callme)
function callme(value,index,array){
   res+= value + '  '
}
//the function also can get just the value. its ok

// value is item in array.  index is shomarande array is namess that do the call

for ( let x of namess){
  res+= x;
}

for ( let x of 'negin'){
  res+= x + '<br>';
}
//The JavaScript for of statement loops through the values of an iterable object.

//It lets you loop over iterable data structures such as Arrays, Strings, Maps, NodeLists, and more:





//do-while loop is execue once then check the condition  but while loop first check the conditon then execute

do{
  res+='e'
}
while(res!='eee')
