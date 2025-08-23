# Our 1st JS Code
Console.log is used to (print) a message to the console

console.log("anshuprogrammer");


## Varibles in JS
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

  * Arithmetic Operators
   * +  -  *  /
    modulus, Exponention, Increment Decrement

  * Assignment Operators
   * =  +=  -=  *=  %=  **=

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
    
# let's Practice
  Q.. Print all even numbers form 0 to 100.
  
  Q.. Create a game where you start with any random game number. Ask the user to keep guessing the game number until the user enters correct value.



