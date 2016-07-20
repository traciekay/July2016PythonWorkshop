

print("Please use small caps...for now :-)")


first = input("Hello? Are you a math geek?")
if first == 'yes' or 'Yes' or 'sure' or 'Sure':
	print("Okay let's start")
	print("Here we go...")

	ans1 = input("Do you think '+' and 'x' are related?")
	if ans1 == 'yes':
		ans1E = input("Hmm...interesting, why?")
		print("Well, I don't know!..you're the geek!")

		ans2 = input("WHat about '-' and '/'?")
		if ans2 == 'yes':
			print("Okay you're good :-) Officially a math geek **Certified")
		elif ans2 == 'no':
			print("Gerrarrahia!!!")
			ans2E = input("Explain further...'half-one'")
			print("EEEK! NO!...Gerrarrahia!!")


	elif ans1 == 'no':
		ans3 = input("wait what??...you skipped math didn't you?")
		if ans3 == 'yes':
			print("No wonder...")

		elif ans3 == 'no':
			print("Team usingizi huh??")

		else:
			print("Gerrarrahia!!!")
			

else:
	print("Mummy...take me home")		

	





