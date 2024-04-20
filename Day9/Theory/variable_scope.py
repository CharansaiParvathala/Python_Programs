
 Variable Scope in Python 🌐

🔸 Local Scope (Function Scope):
   - Variables defined inside a function have local scope.
   - They can only be accessed within that function.

🔸 Global Scope:
   - Variables defined outside of any function have global scope.
   - They can be accessed from anywhere in the code.

🔸 Enclosed Scope (Nonlocal Variables):
   - Enclosed scope refers to the scope of nested functions (functions defined inside other functions).
   - Nonlocal variables are used to access and modify variables from the outer (enclosing) function's scope.

🔸 Built-in Variables/Functions:
   - Python provides several built-in variables (like e in math module) and built-in functions (like `print()`, `len()`, etc.) that are globally available.

🔸 Using `global` Keyword:
   - Inside a function, the `global` keyword is used to modify a global variable.
   - It allows you to assign a value to a global variable from within a function's local scope.
   - like we use it previously in day8 in banking program

the 🔸scope and 🔸revolution are in inverse relationship

Happy coding! 💻✨
