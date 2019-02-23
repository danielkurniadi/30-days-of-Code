class Solution:
    def intToRoman(num):
        basic_roman = {1: 'I', 2: 'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9: 'IX'}
        tens_roman = {1: 'X', 2: 'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9: 'XC'}
        hundred_roman = {1: 'C', 2: 'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9: 'CM'}
        one_thousand = 'M'
        
        roman = ""
        while(num):
            if num >= 1000:
                d = num//1000
                num = num%1000
                roman += one_thousand*d
            elif num >= 100:
                d = num//100
                num = num%100
                roman += hundred_roman[d]
            elif num >= 10:
                d = num // 10
                num = num%10
                roman += tens_roman[d]
            else:
                roman += basic_roman[num]
                break
        return roman