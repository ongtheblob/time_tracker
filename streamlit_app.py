import streamlit as st

st.title("⚽ Time Penalty Calculator")

st.write("Enter the raw time and the number of errors/bonuses below:")

# Inputs
raw_time = st.number_input("Raw Time (s)", min_value=0.0, step=0.1)
misses_bench = st.number_input("Misses Bench (5s each)", min_value=0, step=1)
misses_target = st.number_input("Misses Target Area (3s each)", min_value=0, step=1)
handling_errors = st.number_input("Handling Errors (3s each)", min_value=0, step=1)
outside_passes = st.number_input("Outside Passes (2s each)", min_value=0, step=1)
cone_touches = st.number_input("Cone Touches (2s each)", min_value=0, step=1)
bonus_hits = st.number_input("Bonus Hits (–1s each)", min_value=0, step=1)

# Calculate
if st.button("Calculate Final Time"):
    penalties = (misses_bench * 5 +
                 misses_target * 3 +
                 handling_errors * 3 +
                 outside_passes * 2 +
                 cone_touches * 2)

    # Overtime penalty (1s per extra second beyond 43s)
    overtime_penalty = max(0, raw_time - 43)

    bonus = bonus_hits * 1
    
    final_time = raw_time + penalties + overtime_penalty - bonus
    
    st.success(f"✅ Final Adjusted Time: **{final_time:.2f} seconds**")
