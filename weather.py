import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    # To ensure the temp is in string format,this covers an  input edge case
    temp = str(temp)
    # A variable defined using unicode of degree celsius 
    # Reference :https://www.google.com/search?q=how+to+define+temperature+degree+%3Dcelscius+symbols+in+python&rlz=1C5CHFA_enAU856AU856&oq=how+to+define+temperature+degree+%3Dcelscius+symbols+in+python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTIwMjEyajBqOagCALACAA&sourceid=chrome&ie=UTF-8#ip=1&kpvalbx=_qQM-ZbfCFfidseMPxM6RsQs_36
    DEGREE_SYBMOL= f'\u00b0C' 
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    # refer to testcases for an iso_string input and expected output
    # date = "2021-07-05T07:00:00+08:00"
    # expected_result = "Monday 05 July 2021"
    
    import datetime

    # slice the iso_string for date only
    sliced_iso_string = iso_string[:10]

    # converting iso_string to a date object
    # Reference : https://note.nkmk.me/en/python-datetime-isoformat-fromisoformat/#convert-an-isoformat-string-to-a-date-object
    sliced_iso_string_dateobject = datetime.date.fromisoformat(sliced_iso_string)

    # formatting the dateobject to a human readable format
    # Reference: https://strftime.org/
    iso_string_2_human_readable_format = sliced_iso_string_dateobject.strftime('%A %d %B %Y')
    
    return iso_string_2_human_readable_format
    

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

    # refer to testcases for a temp_in_farenheit input and expected output
    # temp_in_f = 90
    # expected_result = 32.2
    
    # understand formula to convert given fahrenheit to celsius
    # Reference: https://www.calculatorsoup.com/calculators/conversions/fahrenheit-to-celsius.php

    # double casting of input string to float to address edge test cases
    temp_in_farenheit = float(str(temp_in_farenheit))

    celsius = (temp_in_farenheit - 32) / (9/5)
    temp_in_celsius = round(celsius,1)

    return temp_in_celsius


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # mean = sum_list/len(list)

    # Helper functions:
    def is_positive(n):
        """validates if a given number is positive or negative.

        Args:
            n: a number.
        Returns:
            A boolean value ex: positive integer : True, Negative integer : False.
        """
        # if the number is positive
        if n >= 0:
            print(True) 
        # if the number is negative
        else:
            print(False)

    def cal_mean(list):
        """Calculates the mean value from a list of numbers.

        Args:
            list: a list of numbers.
        Returns:
            A float representing the mean value.
        """
        return sum(list)/len(list) # Mean = add up all the given values, then divide by how many values there are.
    
    def string_2_number(string_list):
        """converts a string number to a numbers dtype.

        Args:
            string_list: a list of string numbers.
        Returns:
            A list of numbers.
        """
        empty_list = []
        for i in string_list:
            empty_list.append(int(i))
        return empty_list
    
    # understanding the input datatype using isinstance method:
    # Reference: https://www.w3schools.com/python/ref_func_isinstance.asp

    if isinstance(weather_data[0], int): # if integer
        return cal_mean(weather_data) # return mean 
    
    elif isinstance(weather_data[0], float): # if float
        return round(float(cal_mean(weather_data)),5) # return float with 5d
    
    elif isinstance(weather_data[0], str): # if string
        return cal_mean(string_2_number(weather_data)) # return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    # CSV File Reading and Writing
    # Reference : https://docs.python.org/3/library/csv.html
    # DictReader().. This function returns a DictReader object from the underlying CSV file.
    empty_list = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            empty_list.append([row['date'],int(row['min']),int(row['max'])])
            # Remove empty List from List
            # Reference : https://www.geeksforgeeks.org/python-remove-empty-list-from-list/
            # using list comprehension using if condition:
            non_empty_list = [element for element in empty_list if element != []]
    return non_empty_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)

    """
    # By using the min, float and round methods: 
    # print(round(float(min(weather_data)),1)), print(weather_data.index(min(weather_data)))

    # By problem solving approach:
    # Reference : https://www.geeksforgeeks.org/python-maximum-minimum-elements-position-list/
    
    # Casting each element in the weather to a float using list comprehension 
    
    # If input is empty list then retun empty tuple
    if len(weather_data) == 0:
        return ()
    else:
        weather_data = [float(item) for item in weather_data]
    
        # Initialise min_element in the list with the first list value
        # Initialise min_index in the list with 0
        min_element = weather_data[0]
        min_index = 0

        for i in range(1, len(weather_data)):
        # iterate through the list and check if each element is less than and equal to the initialised value
        # Incase of two same values, we need to pick the later index and value, so using  <= instead <
        # using float and round methods to present the result in required format
            if weather_data[i] <= min_element:
                min_element = weather_data[i]
                min_index = i
        return (round(float(min_element),1), min_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # By using the max, float and round methods: 
    # print(round(float(max(weather_data)),1)), print(weather_data.index(min(weather_data)))

    # By problem solving approach:
    # Reference : https://www.geeksforgeeks.org/python-maximum-minimum-elements-position-list/
    
    # Casting each element in the weather to a float using list comprehension 
    
    # If input is empty list then retun empty tuple
    if len(weather_data) == 0:
        return ()
    else:
        weather_data = [float(item) for item in weather_data]
    
        # Initialise max_element in the list with the first list value
        # Initialise max_index in the list with 0
        max_element = weather_data[0]
        max_index = 0

        for i in range(1, len(weather_data)):
        # iterate through the list and check if each element is greather than and equal to the initialised value
        # Incase of two same values, we need to pick the later index and value, so using  >= instead >
        # using float and round methods to present the result in required format
            if weather_data[i] >= max_element:
                max_element = weather_data[i]
                max_index = i
        return (round(float(max_element),1), max_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # Helper functions:
    def format_temperature(temp):
        """Takes a temperature and returns it in string format with the degrees
            and celcius symbols.

        Args:
            temp: A string representing a temperature.
        Returns:
            A string contain the temperature and "degrees celcius."
        """
        # To ensure the temp is in string format,this covers an  input edge case
        temp = str(temp)
        # A variable defined using unicode of degree celsius 
        # Reference :https://www.google.com/search?q=how+to+define+temperature+degree+%3Dcelscius+symbols+in+python&rlz=1C5CHFA_enAU856AU856&oq=how+to+define+temperature+degree+%3Dcelscius+symbols+in+python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTIwMjEyajBqOagCALACAA&sourceid=chrome&ie=UTF-8#ip=1&kpvalbx=_qQM-ZbfCFfidseMPxM6RsQs_36
        DEGREE_SYBMOL= f'\u00b0C' 
        return f"{temp}{DEGREE_SYBMOL}"

    def convert_date(iso_string):
        """Converts and ISO formatted date into a human readable format.

        Args:
            iso_string: An ISO date string..
        Returns:
            A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
        """

        # refer to testcases for an iso_string input and expected output
        # date = "2021-07-05T07:00:00+08:00"
        # expected_result = "Monday 05 July 2021"
        
        import datetime

        # slice the iso_string for date only
        sliced_iso_string = iso_string[:10]

        # converting iso_string to a date object
        # Reference : https://note.nkmk.me/en/python-datetime-isoformat-fromisoformat/#convert-an-isoformat-string-to-a-date-object
        sliced_iso_string_dateobject = datetime.date.fromisoformat(sliced_iso_string)

        # formatting the dateobject to a human readable format
        # Reference: https://strftime.org/
        iso_string_2_human_readable_format = sliced_iso_string_dateobject.strftime('%A %d %B %Y')
        
        return iso_string_2_human_readable_format

    def convert_f_to_c(temp_in_farenheit):
        """Converts an temperature from farenheit to celcius.

        Args:
            temp_in_farenheit: float representing a temperature.
        Returns:
            A float representing a temperature in degrees celcius, rounded to 1dp.
        """

        # refer to testcases for a temp_in_farenheit input and expected output
        # temp_in_f = 90
        # expected_result = 32.2
        
        # understand formula to convert given fahrenheit to celsius
        # Reference: https://www.calculatorsoup.com/calculators/conversions/fahrenheit-to-celsius.php

        # double casting of input string to float to address edge test cases
        temp_in_farenheit = float(str(temp_in_farenheit))

        celsius = (temp_in_farenheit - 32) / (9/5)
        temp_in_celsius = round(celsius,1)

        return temp_in_celsius

    def cal_mean(list):
        """Calculates the mean value from a list of numbers.

        Args:
            list: a list of numbers.
        Returns:
            A float representing the mean value.
        """
        return round(sum(list)/len(list),1) # Mean = add up all the given values, then divide by how many values there are.

    def find_min(weather_data):
        """Calculates the minimum value in a list of numbers.

        Args:
            weather_data: A list of numbers.
        Returns:
            The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)

        """
        # By using the min, float and round methods: 
        # print(round(float(min(weather_data)),1)), print(weather_data.index(min(weather_data)))

        # By problem solving approach:
        # Reference : https://www.geeksforgeeks.org/python-maximum-minimum-elements-position-list/
        
        # Casting each element in the weather to a float using list comprehension 
        
        # If input is empty list then retun empty tuple
        if len(weather_data) == 0:
            return ()
        else:
            weather_data = [float(item) for item in weather_data]
        
            # Initialise min_element in the list with the first list value
            # Initialise min_index in the list with 0
            min_element = weather_data[0]
            min_index = 0

            for i in range(1, len(weather_data)):
            # iterate through the list and check if each element is less than and equal to the initialised value
            # Incase of two same values, we need to pick the later index and value, so using  <= instead <
            # using float and round methods to present the result in required format
                if weather_data[i] <= min_element:
                    min_element = weather_data[i]
                    min_index = i
            return (round(float(min_element),1), min_index)

    def find_max(weather_data):
        """Calculates the maximum value in a list of numbers.

        Args:
            weather_data: A list of numbers.
        Returns:
            The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
        """
        # By using the max, float and round methods: 
        # print(round(float(max(weather_data)),1)), print(weather_data.index(min(weather_data)))

        # By problem solving approach:
        # Reference : https://www.geeksforgeeks.org/python-maximum-minimum-elements-position-list/
        
        # Casting each element in the weather to a float using list comprehension 
        
        # If input is empty list then retun empty tuple
        if len(weather_data) == 0:
            return ()
        else:
            weather_data = [float(item) for item in weather_data]
        
            # Initialise max_element in the list with the first list value
            # Initialise max_index in the list with 0
            max_element = weather_data[0]
            max_index = 0

            for i in range(1, len(weather_data)):
            # iterate through the list and check if each element is greather than and equal to the initialised value
            # Incase of two same values, we need to pick the later index and value, so using  >= instead >
            # using float and round methods to present the result in required format
                if weather_data[i] >= max_element:
                    max_element = weather_data[i]
                    max_index = i
            return (round(float(max_element),1), max_index)

    iso_dates = [convert_date(row[0]) for row in weather_data]
    min_temp = [convert_f_to_c(row[1]) for row in weather_data]
    max_temp = [convert_f_to_c(row[2]) for row in weather_data]

    avg_min = format_temperature(cal_mean(min_temp))
    avg_max = format_temperature(cal_mean(max_temp))

    # Finding minimum temp by recalling the helper function:
    mintemp, minindex = find_min(min_temp)
    maxtemp, maxindex = find_max(max_temp)

    mintemp = format_temperature(mintemp)
    maxtemp = format_temperature(maxtemp)

    min_date = iso_dates[minindex]
    max_date = iso_dates[maxindex]

    generate_summary = (
        f'{len(weather_data)} Day Overview\n'
        f'  The lowest temperature will be {mintemp}, and will occur on {min_date}.\n'
        f'  The highest temperature will be {maxtemp}, and will occur on {max_date}.\n'
        f'  The average low this week is {avg_min}.\n'
        f'  The average high this week is {avg_max}.'
        )
    return generate_summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # Helper functions:
    def format_temperature(temp):
        """Takes a temperature and returns it in string format with the degrees
            and celcius symbols.

        Args:
            temp: A string representing a temperature.
        Returns:
            A string contain the temperature and "degrees celcius."
        """
        # To ensure the temp is in string format,this covers an  input edge case
        temp = str(temp)
        # A variable defined using unicode of degree celsius 
        # Reference :https://www.google.com/search?q=how+to+define+temperature+degree+%3Dcelscius+symbols+in+python&rlz=1C5CHFA_enAU856AU856&oq=how+to+define+temperature+degree+%3Dcelscius+symbols+in+python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTIwMjEyajBqOagCALACAA&sourceid=chrome&ie=UTF-8#ip=1&kpvalbx=_qQM-ZbfCFfidseMPxM6RsQs_36
        DEGREE_SYBMOL= f'\u00b0C' 
        return f"{temp}{DEGREE_SYBMOL}"
    
    def convert_date(iso_string):
        """Converts and ISO formatted date into a human readable format.

        Args:
            iso_string: An ISO date string..
        Returns:
            A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
        """

        # refer to testcases for an iso_string input and expected output
        # date = "2021-07-05T07:00:00+08:00"
        # expected_result = "Monday 05 July 2021"
        
        import datetime

        # slice the iso_string for date only
        sliced_iso_string = iso_string[:10]

        # converting iso_string to a date object
        # Reference : https://note.nkmk.me/en/python-datetime-isoformat-fromisoformat/#convert-an-isoformat-string-to-a-date-object
        sliced_iso_string_dateobject = datetime.date.fromisoformat(sliced_iso_string)

        # formatting the dateobject to a human readable format
        # Reference: https://strftime.org/
        iso_string_2_human_readable_format = sliced_iso_string_dateobject.strftime('%A %d %B %Y')
        
        return iso_string_2_human_readable_format
        

    def convert_f_to_c(temp_in_farenheit):
        """Converts an temperature from farenheit to celcius.

        Args:
            temp_in_farenheit: float representing a temperature.
        Returns:
            A float representing a temperature in degrees celcius, rounded to 1dp.
        """

        # refer to testcases for a temp_in_farenheit input and expected output
        # temp_in_f = 90
        # expected_result = 32.2
        
        # understand formula to convert given fahrenheit to celsius
        # Reference: https://www.calculatorsoup.com/calculators/conversions/fahrenheit-to-celsius.php

        # double casting of input string to float to address edge test cases
        temp_in_farenheit = float(str(temp_in_farenheit))

        celsius = (temp_in_farenheit - 32) / (9/5)
        temp_in_celsius = round(celsius,1)

        return temp_in_celsius  
    
    generate_daily_summary  =''
    
    for row in weather_data:

        '''
        # Finding min and max temps (advised not to  by mentor):
        if row[1]<row[2]:
            Minimum_temperature = row[1]
            Maximum_temperature = row[2]
        else:
            Minimum_temperature = row[2]
            Maximum_temperature = row[1]
        '''
        formatted_date = convert_date(row[0])
        Minimum_temperature = row[1]
        Maximum_temperature = row[2]

        # converting temps from farenheit to celcius:
        Minimum_temperature =  convert_f_to_c(float(Minimum_temperature))
        # formatting temp to a human readble format:
        Minimum_temperature =  format_temperature(str(Minimum_temperature))

        # converting temps from farenheit to celcius:
        Maximum_temperature =  convert_f_to_c(float(Maximum_temperature))
        # formatting temp to a human readble format:
        Maximum_temperature =  format_temperature(str(Maximum_temperature))

        # How to format in a f string:
        # Reference: https://stackoverflow.com/questions/49416042/how-to-write-an-f-string-on-multiple-lines-without-introducing-unintended-whites
        # After a lot of try and error realised a newline in f string works well for print rather return 
        
        part_summary = (
            f'---- {formatted_date} ----\n'
            f'  Minimum Temperature: {Minimum_temperature}\n'
            f'  Maximum Temperature: {Maximum_temperature}\n\n'
            )
        generate_daily_summary += part_summary
    #summary = '\n'.join(summary.splitlines()[:-1])
    return generate_daily_summary
