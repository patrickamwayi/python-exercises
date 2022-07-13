
# 1.
# You have rented some movies for your kids: 
# The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

Price = 3
days = [3, 5, 1]
movies = 3 * sum(days)


total = movies * Price
print(total)





# 2.
# Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350.
#  How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

payment = 400, 380, 350
hours = [6, 4, 10]
Google = 400 * 6
Amazon = 380 * 4
Facebook = 350 * 10

total = ((400*6)+(380*4)+(350*10))
print(total)


# 3.
# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.
class_not_full = True 
class_full = False

if class_full ==True & class_not_full == True:
    enroll = True
    


#4. 
# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.
buy_more_than_2_items = True
offer_not_expired = True
premium_members = False

if buy_more_than_2_items == True & offer_not_expired == True:
    premium_members = False



# Continuation
# the password must be at least 5 characters
my_password = "notastrongpassword"
my_username = "codeup"
password_more_than_or_equal_to_5_characters = len(my_password) >= 5


if password_more_than_or_equal_to_5_characters == True:
    password_less_than_5_characters = False

# the username must be no more than 20 characters

username_not_over_twenty = len(my_username) <= 20
name_pass = my_username != my_password

username_less_than_or_equal_to_20_characters = True

# the password must not be the same as the username
my_password != my_username

