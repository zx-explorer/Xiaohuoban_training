
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号


def score_to_grade(score):
    if score == 100:
        grade = "A+"
    elif score >= 95:
        grade = "A"
    elif score >= 90:
        grade = "A-"
    elif score >= 85:
        grade = "B+"
    elif score >= 80:
        grade = "B"
    elif score >= 77:
        grade = "B-"
    elif score >= 73:
        grade = "C+"
    elif score >= 70:
        grade = "C"
    elif score >= 67:
        grade = "C-"
    elif score >= 63:
        grade = "D+"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


grade_to_GPA = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 4.0,
    "B+": 3.6,
    "B": 3.3,
    "B-": 3.0,
    "C+": 2.6,
    "C": 2.3,
    "C-": 2.0,
    "D+": 1.6,
    "D": 1.3,
    "F": 0,
}
score_quantization = {
    "A+": 100,
    "A": 98,
    "A-": 92,
    "B+": 87,
    "B": 82,
    "B-": 78,
    "C+": 75,
    "C": 71,
    "C-": 68,
    "D+": 65,
    "D": 61,
    "F": 0,
}


def plot_curve():
    score_list = []
    score_q_list = []

    for score in range(60, 101):
        grade = score_to_grade(score)
        score_q = score_quantization[grade]

        score_list.append(score)
        score_q_list.append(score_q)

    fig = plt.figure(figsize=(8, 6), dpi=100)
    plt.plot(score_list, score_q_list)
    plt.plot(score_list, score_list)
    plt.style.use("ggplot")

    plt.title("GPA量化曲线")
    plt.xlabel("原始分")
    plt.ylabel("对等百分制成绩")
    plt.savefig("GPA量化曲线.png")
    plt.close()


if __name__ == "__main__":
    write_txt("测试.txt")
    plot_curve()
