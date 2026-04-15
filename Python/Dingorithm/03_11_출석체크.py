# Q. 오늘 수업에 많은 학생들이 참여했습니다. 단 한 명의 학생을 제외하고는 모든 학생이 출석했습니다. 

# 모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때, 출석하지 않은 학생의 이름을 반환하시오.

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# set 사용
def get_absent_student(all_array, present_array):
    # 구현해보세요!
    present_array = set(present_array)
    for i in all_array:
        if i not in present_array:
            return i
        
# dictionary 사용
def get_absent_student(all_array, present_array):
    # 구현해보세요!
    present_dict ={}
    # present_array = {key: True for key in present_array}
    for name in present_array:
        present_dict[name]= True
    for i in all_array:
        if i not in present_dict:
            return i
        


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))