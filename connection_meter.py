def love_meter(name1, name2):
    combined_names=(name1+name2).lower()
    total=0
    for char in combined_names:
        if char.isalpha():
            total+=ord(char)
    precentage=total% 101
    return precentage
def show_meter(percentage):
    filled=percentage//10
    empty=10-filled
    meter="🩷"*filled + "🤍"*empty
    print(f"\nLove Meter: [{meter}]")
    print(f"Love percentage: {percentage}%\n")
    if percentage>80:
        print("You are a perfect match! 💖")
    elif percentage>60:
        print("There's a strong connection! 💕")
    elif percentage>40:
        print("There's potential for love! 💞")
    elif percentage>20:
        print("Yyeyyy friends forever😏")
    else:
        print("Better luck next time! or try again💔") 
print("Hello lovebirds! welcome to the love connection meter")
name1=input("Enter her name:")
name2=input("Enter his name:")
love_percentage=love_meter(name1, name2)
show_meter(love_percentage)