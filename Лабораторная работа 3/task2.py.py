def find_common_participants(group1, group2, delimiter=','):
    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)
    common = set(list1).intersection(set(list2))
    return sorted(list(common))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# С разделителем точка с запятой
group_a = "Иванов;Петров;Сидоров"
group_b = "Петров;Смирнов;Сидоров"
print("Тест (;):", find_common_participants(group_a, group_b, delimiter=';'))