from sys import argv

script,user_name,work=argv
prompt='->>'

print(f"Hi {user_name}{work},I'm the {script} script.")
print("I'd like to ask you  a few questions.")
print(f"Do you like me {user_name}{work}?")
likes= input(prompt)

print(f"Where do you live {user_name}{work}?")
lives= input(prompt)

print("What kind of computer do you have?")
computer=input(prompt)

print(f"""
Alright,so you said {likes} about liking me.
You live in {lives}. Not sure where it is.
And you have a {computer} computer.Nice!
""")
#当你登陆游戏输入你的角色名后   NPC与你的对话。。。。。。 虽然我也很不想回答@_@/