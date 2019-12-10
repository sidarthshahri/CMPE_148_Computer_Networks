def is_prime(input_num):
    """
    Checks if an input number is prime and returns a boolean value

    :param input_num: Input number to check
    :return: True if prime, False if not prime
    """

    # Flag to keep track if a number is prime
    prime_flag = True

    # If number is under 2, it's not prime
    if input_num < 2:
        prime_flag = False

    # Simple algorithm to multiply numbers together to check if they equal the input numbers (NOT AN ELEGANT SOLUTION)
    for i in range(2, input_num):
        for j in range(2, input_num):
            if (i * j) == input_num:
                prime_flag = False

    return prime_flag