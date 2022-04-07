his_visit_list = ["vietnam", "argentina", "georgia", "china"]
his_visit_list.append("japan")

# 'his_visit_list[:1]' slices the first item in the list
his_visit_first = his_visit_list[:1]

# 'his_visit_list[1:]' slices the last item in the list
his_visit_last = his_visit_list[-1:]

# 'his_visit_list[:]' copies the the list saving it to a new variable
her_visit_list = his_visit_list[:]
her_visit_list.append("south korea")
her_visit_first = her_visit_list[:1]
her_visit_last = her_visit_list[-1:]

print(f"he wants to visit {his_visit_first} first and {his_visit_last} last")
print(f"she wants to visit {her_visit_first} first and {her_visit_last} last")

# notes
    # 'his_visit_list[0:2]' is an alternative to slide from index zero to two