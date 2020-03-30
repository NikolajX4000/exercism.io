class Luhn:
    def __init__(self, card_num):
        self.nums = card_num

    def valid(self):
        nums = ''
        for char in self.nums:
            if ord('0') <= ord(char) <= ord('9'):
                nums += char
            elif char == ' ':
                continue
            else:
                return False
        if len(nums) <= 1:
            return False

        temp_list = [int(c) for c in nums]
        list1 = temp_list[-2::-2]
        list2 = temp_list[::-2]
        total_sum = sum(list2)
        for num in list1:
            num *= 2
            while num:
                num, rem = divmod(num, 10)
                total_sum += rem
        return total_sum % 10 == 0
