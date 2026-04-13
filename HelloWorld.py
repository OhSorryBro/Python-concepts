# First variable and printout.
message = "Hello World"
print(message)

# Does variable works similar to C#?
message = "Hello Python Crash Course"
print(message)
message = "hello python crash course"

# Method chain.
print(message.title())
print(message.upper())
print(message.lower())

# Multiple variables used to print string + transformation via method.
message_p1 = "Hello"
message_p2 = "python"
message_p3 = "crash"
message_p4 = "course"
print(f"{message_p1} {message_p2} {message_p3} {message_p4}".title())

# White spaces
print(f"{message_p1} \t {message_p2}")
print(f"{message_p1} \n {message_p2}")
print(f"{message_p1} \n\t {message_p2} \n\t {message_p3} \n\t {message_p4} \n\t random_text ")

# Stripping white spaces.
message_to_strip = "   Hello Python Crash Course   "
print(message_to_strip.rstrip())
print(message_to_strip.lstrip())
message_to_strip = message_to_strip.strip()
print(message_to_strip)

# Prefix removal.
message_to_strip_no_prefix = message_to_strip.removeprefix("hello")
print(message_to_strip_no_prefix)
message_to_strip_no_prefix = message_to_strip.removeprefix("Hello")
print(message_to_strip_no_prefix)
message_to_strip_no_prefix = message_to_strip.removeprefix(" ")
print(message_to_strip_no_prefix)