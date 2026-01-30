def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).upper()

    t_count = combined_names.count("T")
    r_count = combined_names.count("R")
    u_count = combined_names.count("U")
    e_count = combined_names.count("E")
    true_total = t_count + r_count + u_count + e_count

    l_count = combined_names.count("L")
    o_count = combined_names.count("O")
    v_count = combined_names.count("V")
    e2_count = combined_names.count("E")
    love_total = l_count + o_count + v_count + e2_count

    score = str(true_total) + str(love_total)
    print(score)

calculate_love_score("Angela Yu", "Jack Bauer")