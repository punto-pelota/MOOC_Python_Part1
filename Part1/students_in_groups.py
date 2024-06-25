students_on_the_course = int(input("How many students on the course?"))
number_of_groups = int(input("Desired group size?"))

groups_formed = students_on_the_course // number_of_groups

if (students_on_the_course - groups_formed*number_of_groups) > 0:
    groups_formed = groups_formed + 1

print(f"Number of groups formed: {groups_formed}")


