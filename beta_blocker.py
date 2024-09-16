def simulate_beta_blockers():
    import random

    # 38% of patients are given the beta-blocker pill
    p_pill = 0.38

    # 84% of patients who get the medication have high blood pressure after
    p_high_if_pill = 0.84

    # 13% of patients who don't get the medication have high blood pressure
    p_high_if_no_pill = 0.13

    # At baseline, 30% of patients improve
    improve_rate = 0.3

    # Absolute 20% fewer patients improve if their blood pressure is high
    improve_rate_if_high = -0.2

    # Absolute 20% more patients improve if their blood pressure is low
    improve_rate_if_low = 0.2

    # Absolute 40% more patients improve with the medication
    improve_rate_if_pill = 0.4

    # Absolute 20% more patients improve without the medication
    improve_rate_if_no_pill = 0.2

    # This is the baseline improvement probability. It will go up or down below.
    p_improve = improve_rate

    # TASK: Simulate whether the patient gets the beta-blocker pill
    if random.uniform(0, 1) < p_pill:
        intervention = 'pill'
        # TASK: Simulate whether the patient has high or low blood pressure
        if random.uniform(0, 1) < p_high_if_pill:
            blood_pressure = 'high'
        else:
            blood_pressure = 'low'
    else:
        intervention = 'no_pill'
        # TASK: Simulate whether the patient has high or low blood pressure
        if random.uniform(0, 1) < p_high_if_no_pill:
            blood_pressure = 'high'
        else:
            blood_pressure = 'low'

    # TASK: Update the patient's probability of improvement based on their blood pressure
    if blood_pressure == 'high':
        p_improve += improve_rate_if_high
    else:
        p_improve += improve_rate_if_low

    # TASK: Update the patient's probability of improvement based on the treatment
    if intervention == 'pill':
        p_improve += improve_rate_if_pill
    else:
        p_improve += improve_rate_if_no_pill

    # Determine whether the patient improved
    if random.uniform(0, 1) < p_improve:
        improved = 'yes'
    else:
        improved = 'no'

    return (blood_pressure, intervention, improved)


# Run the simulation and record the results
patients = 10000
results = [simulate_beta_blockers() for i in range(patients)]

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

    for blood_pressure, intervention, improved in results:
        if blood_pressure == 'high':
            group_x_a_total += 1
            if improved == 'yes':
                group_x_a += 1
        else:
            group_y_a_total += 1
            if improved == 'yes':
                group_y_a += 1

        if intervention == 'pill':
            group_x_b_total += 1
            if improved == 'yes':
                group_x_b += 1
        else:
            group_y_b_total += 1
            if improved == 'yes':
                group_y_b += 1

    print(f"GROUP X - Treatment A (no pill): {group_x_a}/{group_x_a_total} improved")
    print(f"GROUP Y - Treatment A (no pill): {group_y_a}/{group_y_a_total} improved")
    print(f"GROUP X - Treatment B (pill): {group_x_b}/{group_x_b_total} improved")
    print(f"GROUP Y - Treatment B (pill): {group_y_b}/{group_y_b_total} improved")

summarize_results(results)
