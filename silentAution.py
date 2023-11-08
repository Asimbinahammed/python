import os
auctionList={}
def newUser():
    userName=input("Enter your name: ")
    userBid=int(input("Whats your bid: "))
    if not auctionList:
        auctionList[userName]=userBid
        print(auctionList)
        print(auctionList.keys())
        print(auctionList.values())
    else:
        print(userBid)
        print(auctionList.keys())
        print(auctionList.values())
        if userBid > max(auctionList.values()):
            auctionList[userName]=userBid
    question=input("Is there any other bid? Type 'yes/no': ")
    return(question)

# question=newUser()
# if(question.lower()=="yes"):
#     os.system('clear')
#     newUser()
# else:
#     print(f"The highest bid is from {auctionList.key()} worth Rs {auctionList.value()}")


while True:
    os.system('clear')
    question = newUser()
    if question == "no":
        highest_bidder = max(auctionList, key=auctionList.get)
        highest_bid = auctionList[highest_bidder]
        print(f"The highest bid is from {highest_bidder} worth Rs {highest_bid}")
        break