crypto_likes = {"bitcoin": 98,
    "ethereum": 84,
    "ripple": 72,
    }

# 'crypto_likess["bitcoin"]' gets the value of the key 'bitcoin'
bitcoin_likes = crypto_likes["bitcoin"]
ethereum_likes = crypto_likes["ethereum"]
ripple_likes = crypto_likes["ripple"]

bitcoin_message = f"bitcoin has {bitcoin_likes} likes"
ethereum_message = f"ethereum has {ethereum_likes} likes"
ripple_message = f"ripple has {ripple_likes} likes"

print(bitcoin_message)
print(ethereum_message)
print(ripple_message)

# notes
    # you can use a dictionary to store one kind of information about many objects