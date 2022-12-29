import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))




#http://127.0.0.1:5000/




def jokes_post_process(caption, jokes, name):
    if name == "test":
        return "test"
    else:
        return None


    '''
    else:
        return None
    return joke

# domain = "dogs.jpg"
# domain = "rock-band.jpg"
domain = "test"
test = jokes_post_process("hello", "Check", domain)
print(test)
