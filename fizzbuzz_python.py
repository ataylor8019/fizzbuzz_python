
    # Fizzbuzz solution:
    # Common problem statement is to test all numbers from 1 to 100, and if the
    # number is a multiple of 3, to print the word "fizz", and if the number is
    # a multiple of 5, to print the word "buzz". If the number is a multiple of
    # both, then the program should print the word "fizzbuzz". Otherwise, print
    # out the number.

    # Allan Taylor
    # 09/06/2021



for i in range(1,101):

    # i mod 3 AND i mod 5 having a nonzero value means this number is not
    # a multiple of either, therefore print the number. Note that this
    # calculation is the same as c: a nonzero value suffices as truth
    if ((i%3) and (i%5)):    # Most common scenario, is placed first.
        print(str(i))    # No need to test more factors, go to the next iteration of the loop.
        continue

    fizzbuzz=str()    # As python's print prints entire lines, making a temp string variable
                      # to collect fizz/buzz output strings

    # Inverting i mod 3's output results in "true" for factors of 3
    # (i mod 3 for factors of 3 equals 0).
    if (not(i%3)): fizzbuzz="fizz"    #Second most common scenario, is placed second.

    # The previous logic applies to the output of i mod 5 as well.
    if (not(i%5)): fizzbuzz+="buzz"    # Third most common scenario, is placed last.

    print(fizzbuzz)

    
    # If a number is a factor of 3 and 5, the execution will fall 
    # through both of the if statements starting at line 25. The variable
    # fizzbuzz is always declared as an empty string at this point in the script.
    # As the test for being a factor of 3 is always done before the
    # test for being a factor of 5, the resulting output is "fizzbuzz".

    # If a number is only a factor of 3 or only a factor of 5, the
    # respective word will be stored in the fizzbuzz variable, and the 
    # alternate if case ignored. When divisibility by 3 and 5 have been tested,
    # the fizzbuzz variable (and all strings in it) is printed using python's 
    # print function.
