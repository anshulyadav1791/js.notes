# Our 1st JS Code
Console.log is used to (print) a message to the console

console.log("anshuprogrammer");


# Varibles in JS
Varibles are containers for data

memory1 = [data...], memory2 = [data...], memory3 = [data...] ...

## Varible Rules
* Varible name are case secitive; "a" & "A" is different.
* Only letters, digits, underscore(_) and $ is allowed. (not even space)
* Only a letters, underscore(_) or $ should be 1st character.
* Resrved words cannot be variable names.

## let, var & const
 * let: Varible cannot be re-declared but be updated. A block scope variable.
 * var: Varible cannot be re-declared & updated. A globle scope variable.
 * const: varible cannot be re-declared or updated. A block scope variable.   

## Data Types in JS
  Number, String, Boolean, Uudefined, Null, BigInt, Syambol 

## Operator in JS
   Used to perform some operation on data

   Arithmetic Operators
     +  -  *  /
             
    modulus, Exponention, Increment Decrement

   Assignment Operators
      =  +=  -=  *=  %=  **=

  ## Comparison Operators
   Equal to ==   Equal to ===   Not equal to !=    not equal to type !==
    >, >=, <, <=


# Conditinal Statements
   To implements some condition in the code
 ## If Statement
      let color;
      if(mode === "dark-mode") {
        color = "black";
      } 
## if-else Statement
      let color;
      if(mode === "dark-mode") {
        color = "black";
      } else {
        color = "white";
      }
    
## Operators in js
  * Ternary Operators
   * condition ? True Output:false output

Ex. age > 18 ? "adult" : "not adult";
# Loops in JS
Loops are used to execute a piece of code again & again
## for Loop
    for (let i = i; i <= 5; i++) {
       console.log("anshu")
    }
    
## Infinite Loop in JS: A Loop that never ends
    for (let i = 1; i >= 0; i++) {
       console.log(i);
       }
## While Loop
    let i = 1
    while(i <= 10){
        console.log(i);
        i++;
       }
## do-while Loop
    let i = 1
    do { 
       console.log("anshu", i);
       i++;
       } while (i <= 10);
## for-of loop
     let str = "anshuprogrammer";
     for ( let i of str) {
        console.log(i);    
      }
## for- in Loop       
    let student = {
       name: "anshu",
       age: 20,
       cgpa: 7.5,
       isPass: true
    };
    for (let key in student) {
    console.log(key, student[key])
    }
    
## let's Practice
  Q.. Print all even numbers form 0 to 100.
  
  Q.. Create a game where you start with any random game number. Ask the user to keep guessing the game number until the user enters correct value.

# String in JS
   String is a sequence of characters used to represent test 
   
   ####  Create String  <br>
      let str = "string.."; 
   #### String Length   <br>
      str.length  
   #### String Indices   <br>
      str[0], str[1], str[2] 
      
## Template Literals in JS
A way to have embedded expession in strings

      `this is a template literal`

### String Interpolation 
 To create strings by doing substitution of placeholders
 
     `string text ${expression} string text`

## String  Methods in JS
  These bare built-in functions to mainpulate a string
  #### str.toUpprCase()
    let str = "anshu";
    str = str.toUpperCase();
    console.log(str)
  #### str.toLowerCase)()
    let str = "Anshu";
    str = str.toLowerCase();
    console.log(str)
  #### Str.trim()  //remove whitespaces
    let str = "  anshu    ";
    str = str.trim();
    console.log(str)

  #### str.slice(start,end?)  //returns parts of string
    let str = "hello";
    console.log(str.slice(1));
  #### str1.concat(srt1)  //joins str2 with str1
    let str1 = "anshu";
    let str2 = "anshu";
    let add = str2.concat(str1);
    console.log(add);
  #### str.replace(searchVal, newVal) 
    let str = "hellololo";
    console.log(str.replaceAll("lo", "p"));
  #### str.charAt(idx)
    let str = "hello";
    console.log(str.charAt(2));
## Let's Practice
Q.. Prompt the user to enter their full name. Generale a ussername for them based on the input. Start username with @, followed by their full name and ending with the length.  <br>
    eg: username = "_____", useremail = "______"

# Arrays in JS
  Collections of items in Array   <br>
    `let heroes = ["ironman", "hulk", "thor", "batman"];` <br>
    `let marks = [96, 79, 95, 43, 44];` <br>
    `let info = ["rahul, 89, "Delhi"];`

  ### Array Indices
  arr[0], arr[1], arr[2]...    <br>
  `hello`  `anshu`  `yadav`
  
### Looping aver an Array
    let marks = ["anshu", "anshu1", "anshu2", "anshu4","anshu5"];

    for(let ans = 0; ans < marks.length; ans++) {
    console.log(marks[ans])
    }

## Let's Practice 
Q.. For a given array with marks of students -> [98, 83, 83, 35, 43]  <br>
    Find the averge marks of the entie class.

Q.. For a given array with prices of 5 items -> [98, 83, 83, 35, 43]  <br>
    All items have an offer 10% OFF on them. Change the array to store fimal price price after applying offer.

## Array Methods 
    .push()  //add to end
    .pop()  //delete from end & return
    .toString()  //converts array to string
    .concat()  //joins multiple arrays & returns result 
    .shift()   //delete from start & return
    .slice()  //returns a piece of the array
    .splice()  //change original array (add,remove, replace)

 ## Lets Practice
 ### Q.. Create an array to store compaines -> "Blooberg", "Microsoft", "Uber"
* Remove to first company form the array
* Remove Uber & add Ola in its place
* add Amazon at the end
  
 #  Function in JS
  Block of code the performes a specific task, can be invoked whenver needed
  ### Function Definition
      function functionName() {
          // do some work
          }
### Function Call
      functionName();
      
  ### Function        
    function sum( x, y) {
     sum = x + y;
     return sum;
    }
    let val = sum(4, 4);
    console.log(val);

 ## Arrow Functions 
### Compact way of writing a funcation
    const funcationName = (param1, param2...) => {
           // do some work
    }
    lfyuf
  
## Let's Practice 
Q.. Create a function using the "function" keyword that takes a String as an argument & returns the number of vowels in string.

Q.. Create an arrow function to perform the same task.

## forEach Loop in Arrays
arr.forEach(callBackFunction)
### CallbackFuncation: Here, it is a function to execute for each element in the array
* A callback is a function passed as an argument to another function.
     ##
      let arr = [33, 44]
      arr.forEach((val) => {
      console.log(val);
      });
      
## Map
Create a new array with the result of same operation. The value its callback returns are used to form new array
### arr.map(callbackFnx(value,index,array))
     let nums = [33, 44];
     let newArr = nums.map((val) => {
     return val * 2;
     })
     console.log(newArr);
## Filter 
 ### Creates a new array of elements that give truve for a condition/filter.
  #### Eg: all enen elements
     let arr = [1,2,3,4,5]
     let evenArr = arr.filter((val) => {
      return val % 2 ===0;
     })
     console.log(evenArr)
 
## Reduce 
### Performs some operations & reduce the array to a single value. It returns that single value.
    let arr = [1,2,3,4,5,6,7,8,9,10]
    const output = arr.reduce((res, curr) => {
    return res + curr;
    })
    console.log(output)
## Lets Pratice
### Q.. We ate given array of marks of students. Filter out of the marks of students that scored 90+.
### Q.. Take a numver n as input from user. Create an array of numbers form 1 to n.
* Use the reduce method to calculate sum of all numbers in the array.
* Use the reduce method to calculate product of all numbers in the array.

# What is DOM?
 ### When a wob page is loaded, the borwser create a Document Object Model (DOM) of the page.

 ## `window `----> `document` ----> `HTML` ----> `body` ----> `script`
 ## `html` ----> `head` ----> `meta, title, link`
 ## `script` <---- `body` ----> `img, h1, p, div` 
 
 ### DOM Mainpulation
 ### `Selecting with id`
  * document.getElementById("myId")
 ###  `Selectiog with class`
  * document.getElementsByClassName("myClass")
### `Selecting with tag`
* document.getElementsByTagName("p")

## Query Selector
  document.querySelector("myId/myclass/tag")  <br>
  //returns frist element
  document.querySelectorAll("myId/myClass/tag") <br>
  //returns a NodeList

  ### Propertes
  * `tagName:`  returns tage for element nodes
  * `innerText:`  returns the text content of the element and all its children
  * `innerHTML:`  returns the plains text or HTML contents in the element
  * `textContent:`  returns textual content even for hidden elenments
   
### Attributes
* getAttribute(attr)  //to get the attribute value
* setAttribute(attr.value)  //to set the attribute value
### Style
* node.style
### insert Elements 
let el = document.createElement("div")
* node.append(el) //adds at the end of node (inside)
* node.perpend(el) //adds at the start of node (inside)
* node.before(el) //adds before the node (outside)
* node.after(el) //adds ofter the node (outside)
## Delete Elenoent 
* node.remove() //removes the node
