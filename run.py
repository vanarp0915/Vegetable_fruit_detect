
import os
while True:
    print("Do you want to start detection")
    run = int(input("Press 1 if yes "))
    if run == 1:

        os.system('python test_model.py')
    else: 
        break


