import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

participants = 18500
num_test = 1000
luck_percentage = 0.5
num_select = 50

mu = 50
sigma = 15

def make_participants():
    participant_list = np.empty((participants, 3), dtype=float)
    for j in range(participants):
        luck = np.random.rand() * 100
        skill = np.random.normal(mu, sigma)
        score = (luck_percentage * luck + (1 - luck_percentage) * skill)
        participant_list[j] = [luck, skill, score]
    return participant_list


def sort_participants(part_list):
    sorted_indices = np.argsort(part_list[:, 2])[::-1]
    picked = part_list[sorted_indices[1:num_select]]
    return picked


def calculate_avg_luck_and_skill():
    selected = []
    avg_luck = np.zeros(num_test)
    avg_skill = np.zeros(num_test)

    for i in tqdm(range(num_test)):
        part_list = make_participants()
        selected.append(sort_participants(part_list))

    for index, sel in enumerate(selected):
        for i in range(len(sel)):
            avg_luck[index] += sel[i, 0]
            avg_skill[index] += sel[i, 1]
        avg_luck[index] /= len(sel)
        avg_skill[index] /= len(sel)

    return avg_luck, avg_skill


num_select = 50
luck_percentages = [0.1, 0.3, 0.5, 0.7, 0.9]
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
for luck_percentage in luck_percentages:
    avg_luck, _ = calculate_avg_luck_and_skill()
    plt.plot(avg_luck, label=f"Luck Importance: {luck_percentage}")

plt.xlabel('Test Index')
plt.ylabel('Average Luck')
plt.title('Average Luck over Tests (varying Luck Importance)')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
for luck_percentage in luck_percentages:
    _, avg_skill = calculate_avg_luck_and_skill()
    plt.plot(avg_skill, label=f"Luck Importance: {luck_percentage}")

plt.xlabel('Test Index')
plt.ylabel('Average Skill')
plt.title('Average Skill over Tests (varying Luck Importance)')
plt.legend()
plt.grid(True)

luck_percentage = 0.5
num_selects = [10, 50, 100, 500, 1000, 5000]

plt.subplot(2, 2, 3)
for num_select in num_selects:
    avg_luck, _ = calculate_avg_luck_and_skill()
    plt.plot(avg_luck, label=f"Num Select: {num_select}")

plt.xlabel('Test Index')
plt.ylabel('Average Luck')
plt.title('Average Luck over Tests (varying Num Select)')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
for num_select in num_selects:
    _, avg_skill = calculate_avg_luck_and_skill()
    plt.plot(avg_skill, label=f"Num Select: {num_select}")

plt.xlabel('Test Index')
plt.ylabel('Average Skill')
plt.title('Average Skill over Tests (varying Num Select)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
