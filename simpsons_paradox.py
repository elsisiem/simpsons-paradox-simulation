def simulate_kidney_stone():
    import random

    # 40% of patients present with large kidney stones (60% with small)
    p_large = 0.4

    # 80% of large kidney stone patients are assigned to surgery (20% to medication)
    p_surgery_if_large = 0.8

    # 10% of small kidney stone patients are assigned to surgery (90% to medication)
    p_surgery_if_small = 0.1

    # At baseline, 30% of patients improve
    improve_rate = 0.3

    # Absolute 20% fewer patients improve if the stone is large
    improve_rate_if_large = -0.2

    # Absolute 20% more patients improve if the stone is small
    improve_rate_if_small = 0.2

    # Absolute 40% more patients improve with surgery
    improve_rate_if_surgery = 0.4

    # Absolute 20% more patients improve with medication
    improve_rate_if_medication = 0.2

    # This is the baseline improvement probability. It will go up or down below.
    p_improve = improve_rate

    # TASK: Simulate whether it is a large or a small stone
    if random.uniform(0, 1) < p_large:
        stone_size = 'large'
        # TASK: Simulate which treatment the patient gets
        if random.uniform(0, 1) < p_surgery_if_large:
            intervention = 'surgery'
        else:
            intervention = 'medication'
    else:
        stone_size = 'small'
        # TASK: Simulate which treatment the patient gets
        if random.uniform(0, 1) < p_surgery_if_small:
            intervention = 'surgery'
        else:
            intervention = 'medication'

    # TASK: Update the patient's probability of improvement based on the size
    # of the kidney stone
    if stone_size == 'large':
        p_improve += improve_rate_if_large
    else:
        p_improve += improve_rate_if_small

    # TASK: Update the patient's probability of improvement based on the type
    # of treatment they got.
    if intervention == 'surgery':
        p_improve += improve_rate_if_surgery
    else:
        p_improve += improve_rate_if_medication

    # Determine whether the patient improved
    if random.uniform(0, 1) < p_improve:
        improved = 'yes'
    else:
        improved = 'no'

    return (stone_size, intervention, improved)


# Run the simulation and record the results
patients = 10000
results = [simulate_kidney_stone() for i in range(patients)]

# Summarize the results
def summarize_results(results):
    group_x_a = 0
    group_x_b = 0
    group_x_a_total = 0
    group_x_b_total = 0

    group_y_a = 0
    group_y_b = 0
    group_y_a_total = 0
    group_y_b_total = 0

    for stone_size, intervention, improved in results:
        if stone_size == 'large':
            group_x_a_total += 1
            if improved == 'yes':
                group_x_a += 1
        else:
            group_y_a_total += 1
            if improved == 'yes':
                group_y_a += 1

        if intervention == 'surgery':
            group_x_b_total += 1
            if improved == 'yes':
                group_x_b += 1
        else:
            group_y_b_total += 1
            if improved == 'yes':
                group_y_b += 1

    print(f"GROUP X - Treatment A: {group_x_a}/{group_x_a_total} improved")
    print(f"GROUP Y - Treatment A: {group_y_a}/{group_y_a_total} improved")
    print(f"GROUP X - Treatment B: {group_x_b}/{group_x_b_total} improved")
    print(f"GROUP Y - Treatment B: {group_y_b}/{group_y_b_total} improved")

summarize_results(results)
