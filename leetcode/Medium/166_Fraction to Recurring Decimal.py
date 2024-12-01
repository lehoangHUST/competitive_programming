class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)

        # Tính phần nguyên
        integer_part = numerator // denominator
        numerator %= denominator
        if numerator == 0:
            return sign + str(integer_part)

        # Xử lý phần thập phân
        result = [sign + str(integer_part) + "."]
        remainder_map = {}  # Lưu vị trí của mỗi phần dư để tìm chu kỳ
        fraction_part = []

        while numerator != 0:
            if numerator in remainder_map:
                # Phát hiện chu kỳ
                cycle_start = remainder_map[numerator]
                fraction_part.insert(cycle_start, "(")
                fraction_part.append(")")
                break

            # Lưu phần dư hiện tại cùng vị trí
            remainder_map[numerator] = len(fraction_part)
            numerator *= 10
            fraction_part.append(str(numerator // denominator))
            numerator %= denominator

        result.append("".join(fraction_part))
        return "".join(result)