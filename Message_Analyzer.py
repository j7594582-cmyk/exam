#Joshua
message = "coding is fun!"
input("gimmie a message: ").strip()

print(f"""
{message}
length: {message.count("c")+message.count("o")+message.count("d")+message.count("i")+message.count("n")+message.count("g")+message.count("s")+message.count("f")+message.count("!")+message.count(" ")}
last: {message[-1:]}
first: {message[0:1]}
first 3: {message[0:3]}
last 3: {message[-3:]}
every second character: {message[0::2]}
reversed: {message[::-1]}
""")