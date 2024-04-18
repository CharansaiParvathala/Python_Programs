def function(n_arg, d_arg1 = "Hi", d_arg2 = "how are you ?"):
	print(d_arg1, n_arg)
	print(d_arg2)

function("Charan") #call function without passing default arguments

print()

function("Charan","Hello","What are you doing ?") #call function by passing default arguments
