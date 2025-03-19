def sort_emotions(arr, order):
    # If array is empty
    if len(arr) == 0:
        return arr
    
    emotions = [":D", ":)", ":|", ":(", "T_T"]
    # enumerate of this list will give me order
    
    for emotion in emotions:
        if emotion not in arr:
            emotions.remove(emotion)
    
    for index, emotion in enumerate(emotions):
            arr[index] = emotion
            
    if not order:
        arr.reverse()
    
    return arr
        

#if order:

print(sort_emotions([], False))