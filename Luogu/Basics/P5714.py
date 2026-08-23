import math

# 格式化数值，保留 n 位有效数字，去掉末尾的 0
def format_sigfigs(value, n=6):
    if value == 0:
        return "0"
    
    return f"{value:.{n}g}"
    # `value`表示要格式化的变量，`:`是格式说明符的起始符号
    # `.{n}`表示要保留的有效位数，`g`指自动选择 f 或 e，并去掉多余的 0

m, h = map(float, input().split())
bmi = m / (h * h)

if bmi < 18.5:
    print("Underweight")
elif bmi < 24:  
    print("Normal")
else:  
    print(format_sigfigs(bmi, 6))
    print("Overweight")