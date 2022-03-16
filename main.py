hair_styles = ['High Fade' , 'Low Fade' , 'Mid Fade' , 'Clean Shave' , 'Spunk']
High_Fade = 10
print("""Weekly Report
                             Carlys  Hair & Salon
                         Your hair deserves the best!!""")

print('')
print('')
while True:
  print('Only authorized users can access the weekly report.')
  password = input('Please enter the code: ')
  if password == '9750':
    print('')
    print('This is the report.')
    break
  else:
    print('You are not authorized.')

print ('')
prices = [15 , 20 , 15  , 30 , 40]
print('Old prices: ' + '$' + str(prices) )
total_price = 0
last_week = [2 , 5 , 1 , 5, 3]
total_price += sum(prices)
print('')
print("Total price for all the haircuts: " + "$" + str(total_price ) + "$")

average_price = sum(prices) / len(prices)
print('Average price: ' + '$' + str(average_price))

print('')
print('These are the new prices, we care for your hair more than you!!')
new_prices = [prices -5 for prices in prices]
print('New Prices: ' + '$' + str(new_prices))
print('')

total_revenue = 0
for i in range(len(hair_styles)):
  total_revenue = prices[i] * last_week[i]
print('')
print('Total revenue: ' + '$' + str(total_revenue) )
print('')
average_daily_revenue = int(total_revenue) / 7 
print('Average daily revenue: '  + '$' + str(average_daily_revenue))
print ('')
cuts_under_30 = [new_prices[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
print('These are the haircuts under $30: ' + str(cuts_under_30))
